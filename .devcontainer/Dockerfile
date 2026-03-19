# [Choice] Python version: 3, 3.13, 3.12, 3.11, 3.10, 3.9, 3.8
ARG VARIANT="3.13-bookworm"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Install Node.js 20 (includes npm).
# Also disable broken Yarn apt source if present to avoid apt update failures.
RUN set -eux; \
    if [ -f /etc/apt/sources.list.d/yarn.list ]; then \
    sed -i 's/^deb /# deb /' /etc/apt/sources.list.d/yarn.list; \
    fi; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates curl gnupg; \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -; \
    apt-get install -y --no-install-recommends nodejs; \
    node -v; \
    npm -v; \
    rm -rf /var/lib/apt/lists/*
