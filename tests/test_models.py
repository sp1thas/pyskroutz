import json
import os
from typing import Type

import pyskroutz
import pytest
from pydantic import BaseModel


def load_response(path):
    """Load json file"""
    with open(path) as f:
        return json.load(f)


fixtures_list = [
    # Category
    ("categories", pyskroutz.models.categories.CategoryList),
    ("categories__", pyskroutz.models.categories.CategoryRetrieve),
    ("categories__children", pyskroutz.models.categories.CategoryList),
    ("categories__parent", pyskroutz.models.categories.CategoryRetrieve),
    ("categories__root", pyskroutz.models.categories.CategoryRetrieve),
    (
        "categories__specifications__include_group",
        pyskroutz.models.categories.SpecificationList,
    ),
    ("categories__specifications", pyskroutz.models.categories.SpecificationList),
    # SKU
    ("skus_category_list", pyskroutz.models.skus.SkuList),
    ("skus_category_metainclude_list", pyskroutz.models.skus.SkuList),
    ("skus_category_q_filter_list", pyskroutz.models.skus.SkuList),
    ("skus_category_manufactures_filter_list", pyskroutz.models.skus.SkuList),
    ("skus_category_filters_filter_list", pyskroutz.models.skus.SkuList),
    ("skus_retrieve", pyskroutz.models.skus.SkuRetrieve),
    ("skus_similar_retrieve", pyskroutz.models.skus.SkuList),
    ("sku_reviews_include_aggr", pyskroutz.models.skus.ReviewList),
    ("sku_reviews_include_breakdown", pyskroutz.models.skus.ReviewList),
    ("skus_reviews_retrieve", pyskroutz.models.skus.ReviewList),
    ("skus_reviews_vote_retrieve", pyskroutz.models.skus.VoteRetrieve),
    ("skus_reviews_flag_retrieve", pyskroutz.models.flags.FlagItem),
    ("skus_review_form_retrieve", pyskroutz.models.skus.ReviewFormRetrieve),
    # Book
    ("author__", pyskroutz.models.books.BookAuthorRetrieve),
    ("author__books", pyskroutz.models.books.BooksList),
    ("book_categories__", pyskroutz.models.books.BookCategoryRetrieve),
    ("book_categories__books", pyskroutz.models.books.BooksList),
    ("book_categories__filters", pyskroutz.models.books.BookCategoriesList),
    ("books", pyskroutz.models.books.BooksRetrieve),
    ("books__details", pyskroutz.models.books.BookDetailsRetrieve),
    ("books__search", pyskroutz.models.books.BooksList),
    ("books__similar_by_author", pyskroutz.models.books.BooksList),
    ("books_categories", pyskroutz.models.books.BookCategoriesList),
    ("publisher__", pyskroutz.models.books.PublisherRetrieve),
    ("publisher__books", pyskroutz.models.books.BooksList),
    # Products
    ("products__", pyskroutz.models.products.ProductRetrieve),
    ("skus__products", pyskroutz.models.products.ProductsList),
    ("skus__product_cards", pyskroutz.models.products.CardsList),
    ("personalization", pyskroutz.models.products.PersonalizationRetrieve),
    ("personalization_put", pyskroutz.models.products.PersonalizationRetrieve),
    ("shops__products__search", pyskroutz.models.products.ProductsList),
    # Manufacturers
    ("manufacturers", pyskroutz.models.manufacturers.ManufacturersList),
    ("manufacturers__", pyskroutz.models.manufacturers.ManufacturerRetrieve),
    ("manufacturers__skus", pyskroutz.models.skus.SkuList),
    ("manufacturers__categories", pyskroutz.models.categories.CategoryList),
    # Flags
    ("flags", pyskroutz.models.flags.FlagList),
    # User Profile
    ("user", pyskroutz.models.users.UserRetrieve),
    ("user__avatars", pyskroutz.models.users.AvatarList),
    ("user__addresses", pyskroutz.models.users.AddressList),
    ("user__addresses__new", pyskroutz.models.users.AddressFormRetrieve),
    ("user__saved_orders", pyskroutz.models.users.SavedOdersList),
    # User Favorites
    ("favorite_lists", pyskroutz.models.favorites.FavoriteListsRetrieve),
    ("favorite_lists__post", pyskroutz.models.favorites.FavoriteListRetrieve),
    ("favorites", pyskroutz.models.favorites.FavoriteList),
    ("favorite_lists__favorites", pyskroutz.models.favorites.FavoriteList),
    ("favorites__", pyskroutz.models.favorites.FavoriteRetrieve),
    ("favorites__post", pyskroutz.models.favorites.FavoriteRetrieve),
    ("favorites__put", pyskroutz.models.favorites.FavoriteRetrieve),
    # Search
    ("search__no_results", pyskroutz.models.search.SearchResultsList),
    ("search__results_in_another_language", pyskroutz.models.search.SearchResultsList),
    ("search__misspelled", pyskroutz.models.search.SearchResultsList),
    ("search__many_categories", pyskroutz.models.search.SearchResultsList),
    ("search__strong_category_hint", pyskroutz.models.search.SearchResultsList),
    ("search__strong_manufacturer_hint", pyskroutz.models.search.SearchResultsList),
    ("search__strong_sku_hint", pyskroutz.models.search.SearchResultsList),
    ("search__ommitted_query", pyskroutz.models.search.SearchResultsList),
    ("autocomplete", pyskroutz.models.search.AutocompleteList),
    # Notifications
    ("notifications", pyskroutz.models.notifications.NotificationList),
    ("notifications__", pyskroutz.models.notifications.NotificationRetrieve),
    # Shops
    ("shops__", pyskroutz.models.shops.ShopRetrieve),
    ("shops__reviews", pyskroutz.models.skus.ReviewList),
    ("shops__locations", pyskroutz.models.shops.LocationList),
    ("shops__locations__embed_address", pyskroutz.models.shops.LocationList),
    ("shops__locations__", pyskroutz.models.shops.LocationRetrieve),
    ("shops__locations__signle_embed_address", pyskroutz.models.shops.LocationRetrieve),
    ("locations__find", pyskroutz.models.shops.ShopList),
    # Filter Groups
    ("categories__filter_groups", pyskroutz.models.filters.FilterGroupsList),
]


@pytest.mark.parametrize("fixture_file,model", fixtures_list)
def test_models(fixture_file, model: Type[BaseModel]):
    response = load_response(
        os.path.join(
            os.path.dirname(__file__), f"fixtures/responses/{fixture_file}.json"
        )
    )
    model(**response)
