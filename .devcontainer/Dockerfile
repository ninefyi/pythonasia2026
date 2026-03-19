# [Choice] Python version: 3, 3.13, 3.12, 3.11, 3.10, 3.9, 3.8
ARG VARIANT="3.13-bookworm"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# [Optional] Install additional OS packages.
RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn.sources
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Install Node.js 20 for Marp
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs
