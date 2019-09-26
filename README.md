# DEPRECATED
This project is discontinued due to the fact that Skroutz API does not accept requests anymore.

# pySkroutz
[![PyPI](https://img.shields.io/pypi/v/pySkroutz.svg)](https://pypi.python.org/pypi/pySkroutz/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d4cfa2124f94e1c823de6dec50268bb)](https://www.codacy.com/app/sp1thas/pySkroutz?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sp1thas/pySkroutz&amp;utm_campaign=Badge_Grade)[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.python.org/pypi/pySkroutz) [![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/sp1thas/pySkroutz/master/LICENSE)

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
