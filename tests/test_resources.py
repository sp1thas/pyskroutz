import importlib
import pyskroutz
import pytest
from pyskroutz.utils import rgetattr
from typing import Union

client = pyskroutz.client("123", "123", raise_auth_error=False)


def util_test_endpoint(
    method_ref: str,
    args: Union[None, tuple],
    kwargs: Union[None, dict],
    req_attr_: dict,
):
    args = args if args is not None else tuple()
    kwargs = kwargs if kwargs is not None else {}
    module = ".".join(method_ref.split(".")[:-2])
    mthd = method_ref.split(".")[-1]
    mdl = importlib.import_module(module)
    obj = getattr(mdl, method_ref.split(".")[-2])(client)
    getattr(obj, mthd)(*args, **kwargs)
    for k, v in req_attr_.items():
        assert rgetattr(obj, f"_prepared_request.{k}") == v


fixtures_list = [
    # Categories
    (
        "pyskroutz.categories.get",
        {
            "url": "https://api.skroutz.gr/categories/88",
            "method": "GET",
        },
        (88,),
        {},
    ),
    (
        "pyskroutz.categories.get",
        {
            "url": "https://api.skroutz.gr/categories",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.categories.get_parent",
        {
            "url": "https://api.skroutz.gr/categories/88/parent",
            "method": "GET",
        },
        (88,),
        {},
    ),
    (
        "pyskroutz.categories.get_root",
        {
            "url": "https://api.skroutz.gr/categories/root",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.categories.list_children",
        {
            "url": "https://api.skroutz.gr/categories/88/children",
            "method": "GET",
        },
        (88,),
        {},
    ),
    (
        "pyskroutz.categories.get_specifications",
        {
            "url": "https://api.skroutz.gr/categories/88/specifications",
            "method": "GET",
        },
        (88,),
        {},
    ),
    (
        "pyskroutz.categories.get_manufacturers",
        {
            "url": "https://api.skroutz.gr/categories/88/manufacturers",
            "method": "GET",
        },
        (88,),
        {},
    ),
    (
        "pyskroutz.categories.get_favorites",
        {
            "url": "https://api.skroutz.gr/categories/88/favorites",
            "method": "GET",
        },
        (88,),
        {},
    ),
    # Books
    (
        "pyskroutz.books.get",
        {
            "url": "https://api.skroutz.gr/books/242327",
            "method": "GET",
        },
        (242327,),
        {},
    ),
    (
        "pyskroutz.books.get_details",
        {
            "url": "https://api.skroutz.gr/books/242327/details",
            "method": "GET",
        },
        (242327,),
        {},
    ),
    (
        "pyskroutz.books.get_author",
        {
            "url": "https://api.skroutz.gr/author/385",
            "method": "GET",
        },
        (385,),
        {},
    ),
    (
        "pyskroutz.books.get_author_books",
        {
            "url": "https://api.skroutz.gr/author/385/books",
            "method": "GET",
        },
        (385,),
        {},
    ),
    (
        "pyskroutz.books.get_similar_by_author",
        {
            "url": "https://api.skroutz.gr/books/242327/similar_by_author",
            "method": "GET",
        },
        (242327,),
        {},
    ),
    (
        "pyskroutz.books.get_publisher",
        {
            "url": "https://api.skroutz.gr/publisher/78",
            "method": "GET",
        },
        (78,),
        {},
    ),
    (
        "pyskroutz.books.get_publisher_books",
        {
            "url": "https://api.skroutz.gr/publisher/78/books",
            "method": "GET",
        },
        (78,),
        {},
    ),
    (
        "pyskroutz.books.get_book_categories",
        {
            "url": "https://api.skroutz.gr/book_categories",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.books.get_category",
        {
            "url": "https://api.skroutz.gr/book_categories/1857",
            "method": "GET",
        },
        (1857,),
        {},
    ),
    (
        "pyskroutz.books.get_category_books",
        {
            "url": "https://api.skroutz.gr/book_categories/1857/books",
            "method": "GET",
        },
        (1857,),
        {},
    ),
    # Manufacturers
    (
        "pyskroutz.manufacturers.get",
        {
            "url": "https://api.skroutz.gr/manufacturers/12907",
            "method": "GET",
        },
        (12907,),
        {},
    ),
    (
        "pyskroutz.manufacturers.get",
        {
            "url": "https://api.skroutz.gr/manufacturers",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.manufacturers.get_manufacturer_categories",
        {
            "url": "https://api.skroutz.gr/manufacturers/12907/categories",
            "method": "GET",
        },
        (12907,),
        {},
    ),
    # Products
    (
        "pyskroutz.products.get",
        {
            "url": "https://api.skroutz.gr/products/242327",
            "method": "GET",
        },
        (242327,),
        {},
    ),
    (
        "pyskroutz.products.get_sku_products",
        {
            "url": "https://api.skroutz.gr/skus/242327/products",
            "method": "GET",
        },
        (242327,),
        {},
    ),
    (
        "pyskroutz.products.get_sku_products_grouped_cards",
        {
            "url": "https://api.skroutz.gr/skus/3783654/product_cards",
            "method": "GET",
        },
        (3783654,),
        {},
    ),
    (
        "pyskroutz.products.get_personalization",
        {
            "url": "https://api.skroutz.gr/personalization",
            "method": "GET",
        },
        None,
        {},
    ),
    # SKUs
    (
        "pyskroutz.skus.list",
        {
            "url": "https://api.skroutz.gr/categories/40/skus",
            "method": "GET",
        },
        (40,),
        {},
    ),
    (
        "pyskroutz.skus.get",
        {
            "url": "https://api.skroutz.gr/skus/3443837",
            "method": "GET",
        },
        (3443837,),
        {},
    ),
    (
        "pyskroutz.skus.get_similar",
        {
            "url": "https://api.skroutz.gr/skus/3034682/similar",
            "method": "GET",
        },
        (3034682,),
        {},
    ),
    (
        "pyskroutz.skus.get_reviews",
        {
            "url": "https://api.skroutz.gr/skus/3783654/reviews",
            "method": "GET",
        },
        (3783654,),
        {},
    ),
    (
        "pyskroutz.skus.vote_review",
        {
            "url": "https://api.skroutz.gr/skus/3982592/reviews/21943/votes",
            "method": "POST",
            "body": b'{"vote": {"helpful": true}}',
        },
        (3982592, 21943, True),
        {},
    ),
    (
        "pyskroutz.skus.flag_review",
        {
            "url": "https://api.skroutz.gr/skus/9783213/reviews/240896/flags",
            "method": "POST",
            "body": b'{"vote": {"reason": "spam"}}',
        },
        (9783213, 240896, "spam"),
        {},
    ),
    (
        "pyskroutz.skus.get_review_form",
        {
            "url": "https://api.skroutz.gr/skus/3783654/reviews/new",
            "method": "GET",
        },
        (3783654,),
        {},
    ),
    # Flags
    (
        "pyskroutz.flags.get",
        {
            "url": "https://api.skroutz.gr/flags",
            "method": "GET",
        },
        None,
        {},
    ),
    # User
    (
        "pyskroutz.user.get",
        {
            "url": "https://api.skroutz.gr/user",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.user.update",
        {
            "url": "https://api.skroutz.gr/user",
            "method": "PATCH",
            "body": b'{"sex": "male", "birthyear": 1980}',
        },
        None,
        {"sex": "male", "birthyear": 1980},
    ),
    (
        "pyskroutz.user.get_avatars",
        {"url": "https://api.skroutz.gr/user/avatars", "method": "GET"},
        None,
        {},
    ),
    (
        "pyskroutz.user.get_addresses",
        {"url": "https://api.skroutz.gr/user/addresses", "method": "GET"},
        None,
        {},
    ),
    (
        "pyskroutz.user.get_address_form",
        {"url": "https://api.skroutz.gr/user/addresses/new", "method": "GET"},
        None,
        {},
    ),
    (
        "pyskroutz.user.new_address_form",
        {
            "url": "https://api.skroutz.gr/user/addresses",
            "method": "POST",
            "body": b'{"label": "home", "first_name": "bill", "last_name": "Testopoulos", "street_name": "Panagouli", '
            b'"street_number": "61", "city": "Nea Ionia", "zip": 14123, "region_id": 5}',
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
        "pyskroutz.user.update_address",
        {
            "url": "https://api.skroutz.gr/user/addresses/48937",
            "method": "POST",
            "body": b'{"street_number": "62"}',
        },
        (48937,),
        {"street_number": "62"},
    ),
    (
        "pyskroutz.user.delete_address",
        {
            "url": "https://api.skroutz.gr/user/addresses/48937",
            "method": "DELETE",
        },
        (48937,),
        {},
    ),
    (
        "pyskroutz.user.saved_orders",
        {
            "url": "https://api.skroutz.gr/user/saved_orders",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.user.logout",
        {
            "url": "https://api.skroutz.gr/user/logout",
            "method": "DELETE",
        },
        None,
        {},
    ),
    # User favorites
    (
        "pyskroutz.favorites.get_lists",
        {
            "url": "https://api.skroutz.gr/favorite_lists",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.favorites.create_list",
        {
            "url": "https://api.skroutz.gr/favorite_lists",
            "method": "POST",
            "body": b'{"favorite_list": {"name": "test name"}}',
        },
        None,
        {"name": "test name"},
    ),
    (
        "pyskroutz.favorites.destroy_list",
        {
            "url": "https://api.skroutz.gr/favorite_lists/973812",
            "method": "DELETE",
        },
        (973812,),
        {},
    ),
    (
        "pyskroutz.favorites.list_favorites",
        {
            "url": "https://api.skroutz.gr/favorites",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.favorites.list_favorites",
        {
            "url": "https://api.skroutz.gr/favorite_lists/861839/favorites",
            "method": "GET",
        },
        (861839,),
        {},
    ),
    (
        "pyskroutz.favorites.get_favorite",
        {
            "url": "https://api.skroutz.gr/favorites/5896665",
            "method": "GET",
        },
        (5896665,),
        {},
    ),
    (
        "pyskroutz.favorites.create_favorite",
        {
            "url": "https://api.skroutz.gr/favorites",
            "method": "POST",
            "body": b'{"favorite": {"sku_id": 7957675}}',
        },
        (7957675,),
        {},
    ),
    (
        "pyskroutz.favorites.destroy_favorite",
        {
            "url": "https://api.skroutz.gr/favorites/5896665",
            "method": "DELETE",
        },
        (5896665,),
        {},
    ),
    # Search
    (
        "pyskroutz.search.__call__",
        {
            "url": "https://api.skroutz.gr/search?q=iphone",
            "method": "GET",
        },
        ("iphone",),
        {},
    ),
    (
        "pyskroutz.search.autocomplete",
        {
            "url": "https://api.skroutz.gr/autocomplete?q=iph",
            "method": "GET",
        },
        ("iph",),
        {},
    ),
    # Notifications
    (
        "pyskroutz.notifications.get",
        {
            "url": "https://api.skroutz.gr/notifications",
            "method": "GET",
        },
        None,
        {},
    ),
    (
        "pyskroutz.notifications.get",
        {
            "url": "https://api.skroutz.gr/notifications/314233664",
            "method": "GET",
        },
        (314233664,),
        {},
    ),
    (
        "pyskroutz.notifications.mark_as_viewed",
        {
            "url": "https://api.skroutz.gr/notifications/view",
            "method": "POST",
            "body": b'{"ids": [314233664]}',
        },
        ([314233664],),
        {},
    ),
    # Shops
    (
        "pyskroutz.shops.get",
        {"url": "https://api.skroutz.gr/shops/452", "method": "GET"},
        (452,),
        {},
    ),
    (
        "pyskroutz.shops.get_reviews",
        {"url": "https://api.skroutz.gr/shops/452/reviews", "method": "GET"},
        (452,),
        {},
    ),
    # Filter groups
    (
        "pyskroutz.filters.get",
        {"url": "https://api.skroutz.gr/categories/40/filter_groups", "method": "GET"},
        (40,),
        {},
    ),
]


@pytest.mark.parametrize("method_ref,req_attr,args,kwargs", fixtures_list)
def test_resources(method_ref, req_attr, args, kwargs):
    util_test_endpoint(method_ref, args, kwargs, req_attr)
