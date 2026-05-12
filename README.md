# EPL Package Registry

Official package index for the **English Programming Language (EPL)**.

[![Packages](https://img.shields.io/badge/packages-16-orange?style=flat-square)](https://abneeshsingh21.github.io/epl-packages-index/)
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
| **epl-http** | 1.0.0 | HTTP client — GET/POST/PUT/DELETE, auth, file transfers, webhooks |
| **epl-auth** | 1.0.0 | Authentication — JWT, bcrypt, API keys, sessions, OAuth2, rate limiting |
| **epl-collections** | 1.0.0 | Data structures — Stack, Queue, PriorityQueue, LinkedList, HashMap, BST, Graph, Set |
| **epl-crypto** | 1.0.0 | Cryptography — AES-256, RSA, digital signatures, file encryption, key derivation |
| **epl-email** | 1.0.0 | Email — SMTP, HTML emails, attachments, templates, bulk sending |
| **epl-cache** | 1.0.0 | Caching — LRU cache, TTL expiry, memoization, atomic counters |
| **epl-validator** | 1.0.0 | Validation — schema rules, type checking, sanitization, pattern matching |
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

```
https://abneeshsingh21.github.io/epl-packages-index/index.json
```

## How It Works

```
Author: epl publish --repo user/pkg → CI validates → Auto-registers
User:   epl install pkg-name → Fetches from author's GitHub Release
```

Packages live on **authors' own repos**. This index is just the discovery layer.

## License

Apache 2.0 — Copyright (c) 2024-2026 Abneesh Singh
