# pySkroutz

![](https://raw.githubusercontent.com/sp1thas/pySkroutz/master/logo.png)

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
