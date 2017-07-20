# pySkroutz
[![PyPI](https://img.shields.io/pypi/v/pySkroutz.svg)](https://pypi.python.org/pypi/pySkroutz/) [![Codacy grade](https://img.shields.io/codacy/grade/e27821fb6289410b8f58338c7e0bc686.svg)](https://www.codacy.com/app/sp1thas/pySkroutz/dashboard) [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.python.org/pypi/pySkroutz)

This client library is designed to support the Skroutz API. You can read more about the Skroutz API by accessing its [official documentation](https://developer.skroutz.gr/api/v3/).


## Install
via PyPI:
```bash
pip install pySkroutz
```

## Usage

```python
>>> from pySkroutz import Skroutz
>>> client_id = 'your client id'
>>> client_secret = 'your client secret'
>>> skrtz = Skroutz(client_id=client_id, client_secret=client_secret)
>>> skrtz.search('xiaomi redmi note 4')
```

## License
This project is licensed under the GNU General Public License version 3
