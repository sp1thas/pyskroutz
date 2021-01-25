import json
import os
from typing import Type

import pytest
from pydantic import BaseModel
from pyskroutz.models import categories, skus


def load_response(path):
    """Load json file"""
    with open(path) as f:
        return json.load(f)


@pytest.mark.parametrize(
    "fixture_file,model",
    [
        ("categories_list", categories.CategoryList),
        ("categories_retrieve", categories.CategoryRetrieve),
        ("categories_children_list", categories.CategoryList),
        ("categories_parent_retrieve", categories.CategoryRetrieve),
        ("categories_root_retrieve", categories.CategoryRetrieve),
        ("categories_specifications_group_list", categories.SpecificationList),
        ("categories_specifications_list", categories.SpecificationList),
        ("skus_category_list", skus.SkuListResponseModel),
        ("skus_retrieve", skus.SkuRetrieveResponseModel),
        ("skus_similar_retrieve", skus.SkuListResponseModel),
        ("skus_reviews_retrieve", skus.ReviewListResponseModel),
        ("skus_reviews_vote_retrieve", skus.SkuReviewVoteRetrieveResponseBody),
        ("skus_reviews_flag_retrieve", skus.SkuReviewFlagResponseModel),
        ("skus_review_form_retrieve", skus.SkuReviewFormRetrieveResponseModel),
    ],
)
def test_models(fixture_file, model: Type[BaseModel]):
    response = load_response(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
        )
    )
    model(**response)
