# AtlasGuard

AtlasGuard is a Python 3.12 FastAPI service. This repository currently contains
only the service foundation; data storage, AI, authentication, and lineage
features are intentionally out of scope.

## Local setup

Create a virtual environment and install the development dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

The service is available at `http://127.0.0.1:8000`. Check `/health` or
`/api/v1/health`.

## Configuration

Settings are read from environment variables with the `ATLASGUARD_` prefix.
For example, `ATLASGUARD_ENVIRONMENT=staging` sets the runtime environment.
An optional `.env` file is also supported.

## Quality checks

```bash
pytest
ruff check .
mypy app
```
