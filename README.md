# EPL Package Registry

Official package index for the **English Programming Language (EPL)**.

[![Packages](https://img.shields.io/badge/packages-9-orange?style=flat-square)](https://abneeshsingh21.github.io/epl-packages-index/)
[![Browse](https://img.shields.io/badge/browse-registry-blue?style=flat-square)](https://abneeshsingh21.github.io/epl-packages-index/)

## Install Packages

```bash
pip install eplang              # Install EPL first
epl install epl-array           # Install by name
epl install github:user/repo    # Install from any GitHub repo
epl search array                # Search packages
```

## Publish Your Own Package

**It takes 3 commands:**

```bash
# 1. Login (one time)
epl login

# 2. Push your package to GitHub (must have epl.toml)
git push origin main

# 3. Publish — auto-registers to this index
epl publish --repo yourname/my-package
```

Your package is **automatically validated and registered** — no PRs, no approval wait.

### Quality Gates (Automatic)

Your package must pass these checks to be accepted:

- Valid package name (no reserved names, no duplicates from other authors)
- Valid semantic version (e.g., `1.0.0`)
- Description at least 10 characters
- Author and license specified
- Entry point file exists
- HTTPS download URL

### Package Structure

```
my-package/
├── epl.toml          # Required manifest
├── src/
│   └── main.epl     # Entry point
├── README.md         # Recommended
└── LICENSE           # Recommended
```

### Manifest (`epl.toml`)

```toml
[project]
name = "my-package"
version = "1.0.0"
description = "A useful utility library for EPL"
author = "Your Name"
license = "MIT"
entry = "src/main.epl"
keywords = ["utils", "helpers"]

[dependencies]
```

## Available Packages

| Package | Version | Description |
|---------|---------|-------------|
| epl-array | 1.0.0 | NumPy-like array operations |
| epl-cloud | 1.0.0 | AWS S3, Lambda, SQS integration |
| epl-dataframe | 1.0.0 | Pandas-like DataFrames |
| epl-db | 7.0.1 | Database ORM utilities |
| epl-learn | 1.0.0 | Machine learning |
| epl-plot | 1.0.0 | Plotting and visualization |
| epl-science | 1.0.0 | Scientific computing |
| epl-test | 7.0.1 | Testing utilities |
| epl-web | 7.0.1 | Web framework extras |

## API

The index is served via GitHub Pages:

```
https://abneeshsingh21.github.io/epl-packages-index/index.json
```

Per-package metadata:
```
https://raw.githubusercontent.com/abneeshsingh21/epl-packages-index/main/packages/<name>/metadata.json
https://raw.githubusercontent.com/abneeshsingh21/epl-packages-index/main/packages/<name>/versions.json
```

## How It Works

```
Author: epl publish --repo user/pkg
         ↓
    Creates GitHub Release (on author's repo)
         ↓
    Sends repository_dispatch to this repo
         ↓
    CI validates (quality gates)
         ↓
    Auto-registers in index.json
         ↓
User: epl install pkg-name
         ↓
    Fetches from author's GitHub Release
```

Packages live on **authors' own repos**. This index is just the discovery layer.

## License

Apache 2.0 — Copyright (c) 2024-2026 Abneesh Singh
