#!/bin/bash
# Setup script for PythonAsia 2026 Workshop using uv

# Check if uv is installed
if ! command -v uv &> /dev/null
then
    echo "uv could not be found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

echo "Creating virtual environment..."
uv venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
uv pip install -r django_app/requirements.txt

echo "Setup complete! Activate the environment with 'source .venv/bin/activate'"
