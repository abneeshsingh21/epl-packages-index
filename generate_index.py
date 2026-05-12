"""Generate the EPL package registry index from official packages."""

import json
import os
import time

OFFICIAL_PACKAGES_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'EPL(programming language)', 'epl', 'official_packages'
)
OUTPUT_DIR = os.path.dirname(__file__)


def parse_toml_simple(path):
    """Minimal TOML parser for epl.toml manifests."""
    result = {}
    current_section = None
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                if current_section not in result:
                    result[current_section] = {}
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if val.startswith('[') and val.endswith(']'):
                    val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',') if v.strip()]
                if current_section:
                    result[current_section][key] = val
                else:
                    result[key] = val
    return result


def generate():
    packages_dir = os.path.join(OUTPUT_DIR, 'packages')
    os.makedirs(packages_dir, exist_ok=True)

    all_packages = {}
    now = time.time()

    for pkg_name in sorted(os.listdir(OFFICIAL_PACKAGES_DIR)):
        pkg_path = os.path.join(OFFICIAL_PACKAGES_DIR, pkg_name)
        manifest_path = os.path.join(pkg_path, 'epl.toml')
        if not os.path.isfile(manifest_path):
            continue

        manifest = parse_toml_simple(manifest_path)
        project = manifest.get('project', {})
        deps = manifest.get('dependencies', {})
        python_deps = manifest.get('python', {})

        name = project.get('name', pkg_name)
        version = project.get('version', '1.0.0')
        description = project.get('description', '')
        author = project.get('author', 'EPL Community')
        license_name = project.get('license', 'MIT')
        keywords = project.get('keywords', [])
        entry = project.get('entry', 'src/main.epl')

        metadata = {
            'name': name,
            'description': description,
            'author': author,
            'license': license_name,
            'repository': f'https://github.com/abneeshsingh21/EPL/tree/main/epl/official_packages/{pkg_name}',
            'homepage': 'https://github.com/abneeshsingh21/EPL',
            'keywords': keywords if isinstance(keywords, list) else [keywords],
            'created_at': now,
            'updated_at': now,
        }

        version_entry = {
            'version': version,
            'checksum': '',
            'download_url': f'https://github.com/abneeshsingh21/EPL/releases/download/v{version}/{name}-{version}.zip',
            'published_at': now,
            'yanked': False,
            'dependencies': deps,
            'python_requires': python_deps.get('requires', []),
            'epl_version': '>=7.5.0',
            'size': 0,
            'entry': entry,
        }

        # Write per-package files
        pkg_dir = os.path.join(packages_dir, name)
        os.makedirs(pkg_dir, exist_ok=True)

        with open(os.path.join(pkg_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

        with open(os.path.join(pkg_dir, 'versions.json'), 'w', encoding='utf-8') as f:
            json.dump({'versions': [version_entry]}, f, indent=2)

        all_packages[name] = {
            'metadata': metadata,
            'versions': [version_entry],
            'latest': version,
        }

    # Write full index
    index = {
        'packages': all_packages,
        'updated_at': now,
        'total_packages': len(all_packages),
        'registry': 'https://abneeshsingh21.github.io/epl-packages-index',
    }

    with open(os.path.join(OUTPUT_DIR, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)

    print(f'Generated index with {len(all_packages)} packages')
    for name in sorted(all_packages):
        print(f'  - {name} v{all_packages[name]["latest"]}')


if __name__ == '__main__':
    generate()
