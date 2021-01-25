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
        ("skus_category_list", skus.SkuList),
        ("skus_category_metainclude_list", skus.SkuList),
        ("skus_category_q_filter_list", skus.SkuList),
        ("skus_category_manufactures_filter_list", skus.SkuList),
        ("skus_category_filters_filter_list", skus.SkuList),
        ("skus_retrieve", skus.SkuRetrieve),
        ("skus_similar_retrieve", skus.SkuList),
        ("sku_reviews_include_aggr", skus.ReviewList),
        ("sku_reviews_include_breakdown", skus.ReviewList),
        ("skus_reviews_retrieve", skus.ReviewList),
        ("skus_reviews_vote_retrieve", skus.VoteRetrieve),
        ("skus_reviews_flag_retrieve", skus.FlagItem),
        ("skus_review_form_retrieve", skus.ReviewFormRetrieve),
    ],
)
def test_models(fixture_file, model: Type[BaseModel]):
    response = load_response(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
        )
    )
    model(**response)
