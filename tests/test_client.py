import pytest
from requests.exceptions import RequestException

import pyskroutz


def test_failed_init():
    with pytest.raises(RequestException):
        pyskroutz.client("invalid", "invalid")
