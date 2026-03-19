from pathlib import Path
import importlib
import os
import sys

def load_env_file(env_path: Path) -> None:
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


def load_environment() -> None:
    root_dir = Path(__file__).resolve().parent
    load_env_file(root_dir / ".env")
    load_env_file(root_dir / "django_app" / ".env")


def get_api_key() -> str:
    api_key = os.getenv("VOYAGE_API_KEY", "").strip()
    if api_key:
        return api_key

    print(
        "VOYAGE_API_KEY is not set. Add it to .env or django_app/.env before running this script.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def prompt_for_text() -> str:
    text = input("Enter a sentence to embed: ").strip()
    if text:
        return text

    print("Please enter a non-empty sentence.", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    load_environment()
    api_key = get_api_key()
    text = prompt_for_text()

    try:
        voyageai = importlib.import_module("voyageai")
    except ModuleNotFoundError as exc:
        print(
            "VoyageAI is not installed. Run ./.venv/bin/pip install -r django_app/requirements.txt first.",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc

    try:
        client = voyageai.Client(api_key=api_key)
        result = client.embed([text], model="voyage-4-large")
        vector = result.embeddings[0]
    except Exception as exc:
        print(f"VoyageAI request failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"Embedding dimensions: {len(vector)}")
    print("First 5 values:")
    for index, value in enumerate(vector[:5], start=1):
        print(f"{index}: {value:.6f}")


if __name__ == "__main__":
    main()