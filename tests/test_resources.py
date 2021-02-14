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
    args: Union[None, tuple],
    kwargs: Union[None, dict],
    req_attr_: dict,
):
    args = args if args is not None else tuple()
    kwargs = kwargs if kwargs is not None else {}
    obj = resource(client_)
    getattr(obj, method)(*args, **kwargs)
    for k, v in req_attr_.items():
        assert rgetattr(obj, f"_prepared_request.{k}") == v


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/categories/88",
                "method": "GET",
            },
            (88,),
            {},
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/categories",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "get_parent",
            {
                "url": "https://api.skroutz.gr/categories/88/parent",
                "method": "GET",
            },
            (88,),
            {},
        ),
        (
            "get_root",
            {
                "url": "https://api.skroutz.gr/categories/root",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "list_children",
            {
                "url": "https://api.skroutz.gr/categories/88/children",
                "method": "GET",
            },
            (88,),
            {},
        ),
        (
            "get_specifications",
            {
                "url": "https://api.skroutz.gr/categories/88/specifications",
                "method": "GET",
            },
            (88,),
            {},
        ),
        (
            "get_manufacturers",
            {
                "url": "https://api.skroutz.gr/categories/88/manufacturers",
                "method": "GET",
            },
            (88,),
            {},
        ),
        (
            "get_favorites",
            {
                "url": "https://api.skroutz.gr/categories/88/favorites",
                "method": "GET",
            },
            (88,),
            {},
        ),
    ],
)
def test_categories(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.categories, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/books/242327",
                "method": "GET",
            },
            (242327,),
            {},
        ),
        (
            "get_details",
            {
                "url": "https://api.skroutz.gr/books/242327/details",
                "method": "GET",
            },
            (242327,),
            {},
        ),
        (
            "get_author",
            {
                "url": "https://api.skroutz.gr/author/385",
                "method": "GET",
            },
            (385,),
            {},
        ),
        (
            "get_author_books",
            {
                "url": "https://api.skroutz.gr/author/385/books",
                "method": "GET",
            },
            (385,),
            {},
        ),
        (
            "get_similar_by_author",
            {
                "url": "https://api.skroutz.gr/books/242327/similar_by_author",
                "method": "GET",
            },
            (242327,),
            {},
        ),
        (
            "get_publisher",
            {
                "url": "https://api.skroutz.gr/publisher/78",
                "method": "GET",
            },
            (78,),
            {},
        ),
        (
            "get_publisher_books",
            {
                "url": "https://api.skroutz.gr/publisher/78/books",
                "method": "GET",
            },
            (78,),
            {},
        ),
        (
            "get_book_categories",
            {
                "url": "https://api.skroutz.gr/book_categories",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "get_category",
            {
                "url": "https://api.skroutz.gr/book_categories/1857",
                "method": "GET",
            },
            (1857,),
            {},
        ),
        (
            "get_category_books",
            {
                "url": "https://api.skroutz.gr/book_categories/1857/books",
                "method": "GET",
            },
            (1857,),
            {},
        ),
    ],
)
def test_books(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.books, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/manufacturers/12907",
                "method": "GET",
            },
            (12907,),
            {},
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/manufacturers",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "get_manufacturer_categories",
            {
                "url": "https://api.skroutz.gr/manufacturers/12907/categories",
                "method": "GET",
            },
            (12907,),
            {},
        ),
    ],
)
def test_manufacturers(method, req_attr, args, kwargs):
    util_test_endpoint(
        client, manufacturers.Manufacturers, method, args, kwargs, req_attr
    )


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/products/242327",
                "method": "GET",
            },
            (242327,),
            {},
        ),
        (
            "get_sku_products",
            {
                "url": "https://api.skroutz.gr/skus/242327/products",
                "method": "GET",
            },
            (242327,),
            {},
        ),
        (
            "get_sku_products_grouped_cards",
            {
                "url": "https://api.skroutz.gr/skus/3783654/product_cards",
                "method": "GET",
            },
            (3783654,),
            {},
        ),
        (
            "get_personalization",
            {
                "url": "https://api.skroutz.gr/personalization",
                "method": "GET",
            },
            None,
            {},
        ),
    ],
)
def test_products(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.products, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "list",
            {
                "url": "https://api.skroutz.gr/categories/40/skus",
                "method": "GET",
            },
            (40,),
            {},
        ),
        (
            "get",
            {
                "url": "https://api.skroutz.gr/skus/3443837",
                "method": "GET",
            },
            (3443837,),
            {},
        ),
        (
            "get_similar",
            {
                "url": "https://api.skroutz.gr/skus/3034682/similar",
                "method": "GET",
            },
            (3034682,),
            {},
        ),
        (
            "get_reviews",
            {
                "url": "https://api.skroutz.gr/skus/3783654/reviews",
                "method": "GET",
            },
            (3783654,),
            {},
        ),
        (
            "vote_review",
            {
                "url": "https://api.skroutz.gr/skus/3982592/reviews/21943/votes",
                "method": "POST",
                "body": b'{"vote": {"helpful": true}}',
            },
            (3982592, 21943, True),
            {},
        ),
        (
            "flag_review",
            {
                "url": "https://api.skroutz.gr/skus/9783213/reviews/240896/flags",
                "method": "POST",
                "body": b'{"vote": {"reason": "spam"}}',
            },
            (9783213, 240896, "spam"),
            {},
        ),
        (
            "get_review_form",
            {
                "url": "https://api.skroutz.gr/skus/3783654/reviews/new",
                "method": "GET",
            },
            (3783654,),
            {},
        ),
    ],
)
def test_skus(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.skus, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/flags",
                "method": "GET",
            },
            None,
            {},
        ),
    ],
)
def test_flags(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.flags, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get",
            {
                "url": "https://api.skroutz.gr/user",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "update",
            {
                "url": "https://api.skroutz.gr/user",
                "method": "PATCH",
                "body": b'{"sex": "male", "birthyear": 1980}',
            },
            None,
            {"sex": "male", "birthyear": 1980},
        ),
        (
            "get_avatars",
            {"url": "https://api.skroutz.gr/user/avatars", "method": "GET"},
            None,
            {},
        ),
        (
            "get_addresses",
            {"url": "https://api.skroutz.gr/user/addresses", "method": "GET"},
            None,
            {},
        ),
        (
            "get_address_form",
            {"url": "https://api.skroutz.gr/user/addresses/new", "method": "GET"},
            None,
            {},
        ),
        (
            "new_address_form",
            {
                "url": "https://api.skroutz.gr/user/addresses",
                "method": "POST",
                "body": b'{"label": "home", "first_name": "bill", "last_name": "Testopoulos", "street_name": "Panagouli", "street_number": "61", "city": "Nea Ionia", "zip": 14123, "region_id": 5}',
            },
            None,
            {
                "label": "home",
                "first_name": "bill",
                "last_name": "Testopoulos",
                "street_name": "Panagouli",
                "street_number": "61",
                "city": "Nea Ionia",
                "zip": 14123,
                "region_id": 5,
            },
        ),
        (
            "update_address",
            {
                "url": "https://api.skroutz.gr/user/addresses/48937",
                "method": "POST",
                "body": b'{"street_number": "62"}',
            },
            (48937,),
            {"street_number": "62"},
        ),
        (
            "delete_address",
            {
                "url": "https://api.skroutz.gr/user/addresses/48937",
                "method": "DELETE",
            },
            (48937,),
            {},
        ),
        (
            "saved_orders",
            {
                "url": "https://api.skroutz.gr/user/saved_orders",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "logout",
            {
                "url": "https://api.skroutz.gr/user/logout",
                "method": "DELETE",
            },
            None,
            {},
        ),
    ],
)
def test_user(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.user, method, args, kwargs, req_attr)


@pytest.mark.parametrize(
    "method,req_attr,args,kwargs",
    [
        (
            "get_lists",
            {
                "url": "https://api.skroutz.gr/favorite_lists",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "create_list",
            {
                "url": "https://api.skroutz.gr/favorite_lists",
                "method": "POST",
                "body": b'{"favorite_list": {"name": "test name"}}',
            },
            None,
            {"name": "test name"},
        ),
        (
            "destroy_list",
            {
                "url": "https://api.skroutz.gr/favorite_lists/973812",
                "method": "DELETE",
            },
            (973812,),
            {},
        ),
        (
            "list_favorites",
            {
                "url": "https://api.skroutz.gr/favorites",
                "method": "GET",
            },
            None,
            {},
        ),
        (
            "list_favorites",
            {
                "url": "https://api.skroutz.gr/favorite_lists/861839/favorites",
                "method": "GET",
            },
            (861839,),
            {},
        ),
        (
            "get_favorite",
            {
                "url": "https://api.skroutz.gr/favorites/5896665",
                "method": "GET",
            },
            (5896665,),
            {},
        ),
        (
            "create_favorite",
            {
                "url": "https://api.skroutz.gr/favorites",
                "method": "POST",
                "body": b'{"favorite": {"sku_id": 7957675}}',
            },
            (7957675,),
            {},
        ),
        (
            "destroy_favorite",
            {
                "url": "https://api.skroutz.gr/favorites/5896665",
                "method": "DELETE",
            },
            (5896665,),
            {},
        ),
    ],
)
def test_favorites(method, req_attr, args, kwargs):
    util_test_endpoint(client, pyskroutz.favorites, method, args, kwargs, req_attr)
