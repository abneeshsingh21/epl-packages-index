# EPL Package Registry

Official package index for the **English Programming Language (EPL)**.

## Usage

```bash
# Install a package
epl install epl-array

# Search packages
epl search array

# Sync local index
epl sync-index
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

## Publishing a Package

```bash
epl publish --repo abneeshsingh21/your-package
```

This creates a GitHub Release with your package archive and submits an update to this index.

## Index Format

- `index.json` — Full package listing
- `packages/<name>/metadata.json` — Package metadata
- `packages/<name>/versions.json` — Version history with download URLs

## API

The index is served via GitHub Pages at:

```
https://abneeshsingh21.github.io/epl-packages-index/index.json
```

## License

Apache 2.0 — Copyright (c) 2024-2026 Abneesh Singh
