from pyskroutz import SkroutzClient
from pyskroutz.exceptions import SkroutzApiError
import pytest


def test_failed_init():
    with pytest.raises(SkroutzApiError):
        client = SkroutzClient("invalid", "invalid")
