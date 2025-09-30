# How-to

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

```bash
# how to create a project
uvx copier copy https://github.com/gregunz/gentle-monorepo
# how to update a project
uvx copier update
```

## This is a gentle Python monorepo template
Inspired by [The Gentle Monorepo](https://pretalx.com/pydata-amsterdam-2025/talk/XYZ) talk at PyData Amsterdam 2025, based of this [template](https://github.com/davidvujic/python-polylith-example-uv).

## What's this? 🤔
This is a monorepo template for Python projects.
It follows the **Polylith Architecture** and focuses on:
- Reusing components across multiple products
- Fast, reproducible dependency management
- Trust-based, lightweight collaboration

## Tooling 🛠
- **Polylith** → structure & modularity
- **uv** → dependency management

## Why?
To iterate faster, share more, and avoid the pain of managing internal packages in separate repos.
