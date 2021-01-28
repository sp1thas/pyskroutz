import os
from typing import Type

import pytest
from pydantic import BaseModel

from . import load_response, fixtures_list


@pytest.mark.parametrize("fixture_file,model,method,url", fixtures_list)
def test_models(fixture_file, model: Type[BaseModel], method: str, url: str):
    response = load_response(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
        )
    )
    model(**response)
