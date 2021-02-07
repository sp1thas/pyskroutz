from typing import Union, Type

import pyskroutz
import pytest
from pyskroutz.resources import manufacturers, base
from pyskroutz.utils import rgetattr

client = pyskroutz.client("123", "123", raise_auth_error=False)


def util_test_endpoint(
    client_: pyskroutz.client,
    resource: Type[base.ApiResource],
    method: str,
    params: Union[None, tuple],
    req_attr_: dict,
):
    params = params if params is not None else tuple()
    obj = resource(client_)
    getattr(obj, method)(*params)
    for k, v in req_attr_.items():
        assert rgetattr(obj, f"_prepared_request.{k}") == v


@pytest.mark.parametrize(
    "method,req_attr,params",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/categories/88",
                "method": "GET",
            },
            (88,),
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/categories",
                "method": "GET",
            },
            None,
        ),
        (
            "get_parent",
            {
                "url": "https://api.skroutz.gr/categories/88/parent",
                "method": "GET",
            },
            (88,),
        ),
        (
            "get_root",
            {
                "url": "https://api.skroutz.gr/categories/root",
                "method": "GET",
            },
            None,
        ),
        (
            "list_children",
            {
                "url": "https://api.skroutz.gr/categories/88/children",
                "method": "GET",
            },
            (88,),
        ),
        (
            "get_specifications",
            {
                "url": "https://api.skroutz.gr/categories/88/specifications",
                "method": "GET",
            },
            (88,),
        ),
        (
            "get_manufacturers",
            {
                "url": "https://api.skroutz.gr/categories/88/manufacturers",
                "method": "GET",
            },
            (88,),
        ),
        (
            "get_favorites",
            {
                "url": "https://api.skroutz.gr/categories/88/favorites",
                "method": "GET",
            },
            (88,),
        ),
    ],
)
def test_categories(method, req_attr, params):
    util_test_endpoint(client, pyskroutz.categories, method, params, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,params",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/books/242327",
                "method": "GET",
            },
            (242327,),
        ),
        (
            "get_details",
            {
                "url": "https://api.skroutz.gr/books/242327/details",
                "method": "GET",
            },
            (242327,),
        ),
        (
            "get_author",
            {
                "url": "https://api.skroutz.gr/author/385",
                "method": "GET",
            },
            (385,),
        ),
        (
            "get_author_books",
            {
                "url": "https://api.skroutz.gr/author/385/books",
                "method": "GET",
            },
            (385,),
        ),
        (
            "get_similar_by_author",
            {
                "url": "https://api.skroutz.gr/books/242327/similar_by_author",
                "method": "GET",
            },
            (242327,),
        ),
        (
            "get_publisher",
            {
                "url": "https://api.skroutz.gr/publisher/78",
                "method": "GET",
            },
            (78,),
        ),
        (
            "get_publisher_books",
            {
                "url": "https://api.skroutz.gr/publisher/78/books",
                "method": "GET",
            },
            (78,),
        ),
        (
            "get_book_categories",
            {
                "url": "https://api.skroutz.gr/book_categories",
                "method": "GET",
            },
            None,
        ),
        (
            "get_category",
            {
                "url": "https://api.skroutz.gr/book_categories/1857",
                "method": "GET",
            },
            (1857,),
        ),
        (
            "get_category_books",
            {
                "url": "https://api.skroutz.gr/book_categories/1857/books",
                "method": "GET",
            },
            (1857,),
        ),
    ],
)
def test_books(method, req_attr, params):
    util_test_endpoint(client, pyskroutz.books, method, params, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,params",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/manufacturers/12907",
                "method": "GET",
            },
            (12907,),
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/manufacturers",
                "method": "GET",
            },
            None,
        ),
        (
            "get_manufacturer_categories",
            {
                "url": "https://api.skroutz.gr/manufacturers/12907/categories",
                "method": "GET",
            },
            (12907,),
        ),
    ],
)
def test_manufacturers(method, req_attr, params):
    util_test_endpoint(client, manufacturers.Manufacturers, method, params, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,params",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/products/242327",
                "method": "GET",
            },
            (242327,),
        ),
        (
            "get_sku_products",
            {
                "url": "https://api.skroutz.gr/skus/242327/products",
                "method": "GET",
            },
            (242327,),
        ),
        (
            "get_sku_products_grouped_cards",
            {
                "url": "https://api.skroutz.gr/skus/3783654/product_cards",
                "method": "GET",
            },
            (3783654,),
        ),
        (
            "get_personalization",
            {
                "url": "https://api.skroutz.gr/personalization",
                "method": "GET",
            },
            None,
        ),
    ],
)
def test_products(method, req_attr, params):
    util_test_endpoint(client, pyskroutz.products, method, params, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,params",
    [
        (
            "list",
            {
                "url": "https://api.skroutz.gr/categories/40/skus",
                "method": "GET",
            },
            (40,),
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/skus/3443837",
                "method": "GET",
            },
            (3443837,),
        ),
        (
            "get_similar",
            {
                "url": "https://api.skroutz.gr/skus/3034682/similar",
                "method": "GET",
            },
            (3034682,),
        ),
        (
            "get_reviews",
            {
                "url": "https://api.skroutz.gr/skus/3783654/reviews",
                "method": "GET",
            },
            (3783654,),
        ),
        (
            "vote_review",
            {
                "url": "https://api.skroutz.gr/skus/3982592/reviews/21943/votes",
                "method": "POST",
                "body": b'{"vote": {"helpful": true}}',
            },
            (3982592, 21943, True),
        ),
        (
            "flag_review",
            {
                "url": "https://api.skroutz.gr/skus/9783213/reviews/240896/flags",
                "method": "POST",
                "body": b'{"vote": {"reason": "spam"}}',
            },
            (9783213, 240896, "spam"),
        ),
    ],
)
def test_skus(method, req_attr, params):
    util_test_endpoint(client, pyskroutz.skus, method, params, req_attr)
