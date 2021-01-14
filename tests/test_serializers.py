import pytest
import json


@pytest.fixture
def load_response(path):
    """Load json file"""
    with open(path) as f:
        return json.load(f)


class TestCategories:
    @pytest.mark.parametrize('load_response', [('categories_list', )], indirect=["load_response"])
    def test_tc1(self, response, model):
       pass
