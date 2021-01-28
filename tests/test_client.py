import os
from typing import Type

import pytest
import requests
import responses
from pydantic import BaseModel
from pyskroutz import SkroutzClient
from pyskroutz.exceptions import SkroutzApiError
from pyskroutz.utils import rgetattr

from . import fixtures_list, load_response


def req_wrap():
    return requests.get("https://twitter.com/api/1/foobar")


def test_failed_init():
    with pytest.raises(SkroutzApiError):
        client = SkroutzClient("invalid", "invalid")


client = SkroutzClient("", "", dev=True)
client._access_token = "random"
client._access_token_type = "random"


# @pytest.mark.parametrize("fixture_file,model,method,url", fixtures_list)
# def test_clients(
#         fixture_file,
#         model: Type[BaseModel],
#         method: str,
#         url: str
# ):
#     responses.add(
#         getattr(responses, method),
#         url,
#         json=load_response(
#         os.path.join(
#             os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
#         )
#     )
#     )
#     if url:
#         a = rgetattr(client, url)()
#         print(a)
