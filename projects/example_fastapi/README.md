# Example usage

## Dev

```bash
uv run poe dev
```

Starts the FastAPI app with Uvicorn in reload mode so changes in bases/ or components/ are picked up automatically.

#### Env vars used

* `PROJECT_NAME`
* `IMAGE_NAME`

## Build

```bash
uv run poe build
```

This will:

* Export dependencies to `requirements.txt` (for workspace use without a project lockfile).
* Build a wheel into `./dist`.
* Build a Docker image tagged as `$IMAGE_NAME` (passing `PROJECT_NAME` as a build arg).

#### Env vars used

* `PROJECT_NAME`
* `IMAGE_NAME`

## Run

```bash
uv run poe run
```

Starts the container in interactive mode, removes it on exit, maps `localhost:$APP_PORT → container:8000`, and names it `$CONTAINER_NAME`.

**Env vars used**

* `IMAGE_NAME`
* `CONTAINER_NAME`
* `APP_PORT`

> Need background mode? `uv run poe run-detached`

---

## (Optional) Configure or extend

All defaults and tasks live in `pyproject.toml`:

* Env defaults: `[tool.poe.env]` → `PROJECT_NAME`, `IMAGE_NAME`, `CONTAINER_NAME`, `APP_PORT`
* Tasks: `[tool.poe.tasks]` → adjust commands or add new ones

You can temporarily override envs per call:

```bash
APP_PORT=8081 IMAGE_NAME=my_image uv run poe build-run
```
