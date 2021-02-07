# pyskroutz
A Python client for [Skroutz API](https://developer.skroutz.gr/api/v3/).

![testing](https://github.com/sp1thas/pyskroutz/workflows/testing/badge.svg) ![build](https://github.com/sp1thas/pyskroutz/workflows/build/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyskroutz/badge/?version=latest)](https://pyskroutz.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/v/pyskroutz.svg)](https://pypi.python.org/pypi/pyskroutz/) ![code style](https://img.shields.io/badge/code%20style-black-black) [![codecov](https://codecov.io/gh/sp1thas/pyskroutz/branch/master/graph/badge.svg?token=WTYZU0ENYX)](https://codecov.io/gh/sp1thas/pyskroutz) ![Python versions](https://img.shields.io/pypi/pyversions/pyskroutz.svg)

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


### Note
This project is under a major refactoring and heavy development. Most endpoint of Skroutz API will be implemented asap.

## How to contribute

If you wish to contribute, read [CONTRIBUTING.md](docs/contributing.md) guide for further details.
