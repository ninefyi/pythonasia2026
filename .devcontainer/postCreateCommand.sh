#!/bin/bash

# Install dependencies using uv
# We install globally (in the container) to simplify things for the workshop
uv pip install --system -r django_app/requirements.txt

# Install Jupyter and ipykernel to support notebooks
uv pip install --system jupyter ipykernel

# Setup ipykernel for the container's python
python -m ipykernel install --user --name python3 --display-name "Python 3"

echo "Devcontainer post-create setup complete!"
