import os
from typing import Type

import pytest
from pydantic import BaseModel

from . import load_response, fixtures_list


@pytest.mark.parametrize("fixture_file,model", fixtures_list)
def test_models(fixture_file, model: Type[BaseModel]):
    response = load_response(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
        )
    )
    model(**response)
