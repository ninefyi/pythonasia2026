# [Choice] Python version: 3, 3.13, 3.12, 3.11, 3.10, 3.9, 3.8
ARG VARIANT="3.13-bookworm"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# [Optional] Install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Install uv for package management
RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

# Install marp-cli for slides
RUN su vscode -c "npm install -g @marp-team/marp-cli"
