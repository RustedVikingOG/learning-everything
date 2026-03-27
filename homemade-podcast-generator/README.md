# Homemade Podcast Generator

AI-powered podcast generation using Hugging Face transformers.

## Package Management with `uv`

This project uses [`uv`](https://github.com/astral-sh/uv) for fast, reliable Python dependency management.

### Quick Commands

```bash
# Add a new package
uv add <package-name>

# Add a dev dependency (testing, linting, etc)
uv add --dev <package-name>

# Install dependencies from pyproject.toml
uv sync

# Run a script in the virtual environment
uv run python script.py

# Activate the virtual environment manually
source .venv/bin/activate

# Remove a package
uv remove <package-name>

# Update all dependencies
uv sync --upgrade

# Show installed packages
uv pip list
```

### Why `uv`?

- **Fast**: 10-100x faster than pip for installs
- **Deterministic**: `uv.lock` ensures reproducible environments
- **Python version management**: Automatically uses the configured Python version (3.12)
- **Virtual environment**: Automatically created and managed in `.venv`

### Project Dependencies

- **transformers** — Hugging Face model inference & fine-tuning
- **datasets** — Load and process datasets from Hugging Face Hub
- **huggingface-hub** — Client for downloading/uploading models and datasets
- **tokenizers** — Fast Rust-backed tokenization
- **torch** — PyTorch backend for model inference (required for transformers)

### Virtual Environment

The project automatically uses the `.venv` virtual environment. When you run `uv run`, it activates this environment automatically. To manually activate it:

```bash
source .venv/bin/activate
```

### Python Version

This project requires Python 3.12+. The version is locked in `.python-version` and `pyproject.toml`. `uv` automatically uses the specified version.
