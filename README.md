<div align="center">
    <h1>pyskroutz</h1>
    <p>A Python client for <a href="https://developer.skroutz.gr/api/v3/">Skroutz API</a>.</p>
    <img src="https://github.com/sp1thas/pyskroutz/workflows/testing/badge.svg" alt="testing badge">
    <img src="https://github.com/sp1thas/pyskroutz/workflows/build/badge.svg" alt="build badge">
    <img src="https://readthedocs.org/projects/pyskroutz/badge/?version=latest" alt="docs badge">
    <a href="https://pypi.python.org/pypi/pyskroutz/">
        <img src="https://img.shields.io/pypi/v/pyskroutz.svg" alt="pypi badge" />
    </a>
    <a href="https://codecov.io/gh/sp1thas/pyskroutz">
        <img alt="code coverage badge" src="https://codecov.io/gh/sp1thas/pyskroutz/branch/master/graph/badge.svg?token=WTYZU0ENYX" />
    </a>
    <img src="https://img.shields.io/badge/code%20style-black-black">
</div>
<hr>


## Installation
```bash
pip install pyskroutz
```

## Usage

```python
import pyskroutz
client = pyskroutz.client('<client-id>', '<client-secret>')
first_category = pyskroutz.categories(client).get(per=1).execute()
```

## Supported resources:

 - Categories
 - SKUs
 - Books
 - Products
 - Manufacturers
 - Flags


### Note
This project is under a major refactoring and heavy development. Most endpoint of Skroutz API will be implemented asap.

## How to contribute

If you wish to contribute, read [CONTRIBUTING.md](docs/contributing.md) guide for further details.
