# pyskroutz
![testing](https://github.com/sp1thas/pyskroutz/workflows/testing/badge.svg) ![build](https://github.com/sp1thas/pyskroutz/workflows/build/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyskroutz/badge/?version=latest)](https://pyskroutz.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/v/pyskroutz.svg)](https://pypi.python.org/pypi/pyskroutz/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d4cfa2124f94e1c823de6dec50268bb)](https://www.codacy.com/app/sp1thas/pySkroutz?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sp1thas/pySkroutz&amp;utm_campaign=Badge_Grade) ![code style](https://img.shields.io/badge/code%20style-black-black) [![codecov](https://codecov.io/gh/sp1thas/pyskroutz/branch/master/graph/badge.svg?token=WTYZU0ENYX)](https://codecov.io/gh/sp1thas/pyskroutz)

A Python client for Skroutz API

## Install
```bash
pip install pyskroutz
```

## Usage

```python
>>> from pyskroutz.client import SkroutzClient
>>> client = SkroutzClient('<client-id>', '<client-secret>')
>>> first_category = client.categories.list(per=1)
>>> first_category.categories
```

### Supported endpoints:

 - Categories

This project is under a major refactoring and heavy development. Most endpoint of Skroutz API will be implemented asap.

## How to contribute

If you wish to contribute, read [CONTRIBUTING.md](docs/contributing.md) guide for further details.
