import pyskroutz
import pytest
from requests.exceptions import RequestException


def test_failed_init():
    with pytest.raises(RequestException):
        pyskroutz.client("invalid", "invalid")
