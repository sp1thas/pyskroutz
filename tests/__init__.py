import json

from pyskroutz.models import (
    categories,
    skus,
    books,
    products,
    manufacturers,
    flags,
    users,
    favorites,
)


def load_response(path):
    """Load json file"""
    with open(path) as f:
        return json.load(f)


fixtures_list = [
    # Category
    ("categories", categories.CategoryList),
    ("categories__", categories.CategoryRetrieve),
    ("categories__children", categories.CategoryList),
    ("categories__parent", categories.CategoryRetrieve),
    ("categories__root", categories.CategoryRetrieve),
    ("categories__specifications__include_group", categories.SpecificationList),
    ("categories__specifications", categories.SpecificationList),
    # SKU
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
    ("skus_reviews_flag_retrieve", flags.FlagItem),
    ("skus_review_form_retrieve", skus.ReviewFormRetrieve),
    # Book
    ("author__", books.BookAuthorRetrieve),
    ("author__books", books.BooksList),
    ("book_categories__", books.BookCategoryRetrieve),
    ("book_categories__books", books.BooksList),
    ("book_categories__filters", books.BookCategoriesList),
    ("books", books.BooksRetrieve),
    ("books__details", books.BookDetailsRetrieve),
    ("books__search", books.BooksList),
    ("books__similar_by_author", books.BooksList),
    ("books_categories", books.BookCategoriesList),
    ("publisher__", books.PublisherRetrieve),
    ("publisher__books", books.BooksList),
    # Products
    ("products__", products.ProductRetrieve),
    ("skus__products", products.ProductsList),
    ("skus__product_cards", products.CardsList),
    ("personalization", products.PersonalizationRetrieve),
    ("personalization_put", products.PersonalizationRetrieve),
    ("shops__products__search", products.ProductsList),
    # Manufacturers
    ("manufacturers", manufacturers.ManufacturersList),
    ("manufacturers__", manufacturers.ManufacturerRetrieve),
    ("manufacturers__skus", skus.SkuList),
    ("manufacturers__categories", categories.CategoryList),
    # Flags
    ("flags", flags.FlagList),
    # User Profile
    ("user", users.UserRetrieve),
    ("user__avatars", users.AvatarList),
    ("user__addresses", users.AddressList),
    ("user__addresses__new", users.AddressFormRetrieve),
    ("user__saved_orders", users.SavedOdersList),
    # User Favorites
    ("favorite_lists", favorites.FavoriteListsRetrieve),
    ("favorite_lists__post", favorites.FavoriteListRetrieve),
    ("favorites", favorites.FavoriteList),
    ("favorite_lists__favorites", favorites.FavoriteList),
    ("favorites__", favorites.FavoriteRetrieve),
    ("favorites__post", favorites.FavoriteRetrieve),
    ("favorites__put", favorites.FavoriteRetrieve),
]
