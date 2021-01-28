import json
from pyskroutz.models import categories, skus, books


def load_response(path):
    """Load json file"""
    with open(path) as f:
        return json.load(f)


fixtures_list = [
    # Category
    ("categories", categories.CategoryList, "GET", "categories.list"),
    ("categories__", categories.CategoryRetrieve, "GET", ""),
    ("categories__children", categories.CategoryList, "GET", ""),
    ("categories__parent", categories.CategoryRetrieve, "GET", ""),
    ("categories__root", categories.CategoryRetrieve, "GET", ""),
    (
        "categories__specifications__include_group",
        categories.SpecificationList,
        "GET",
        "",
    ),
    ("categories__specifications", categories.SpecificationList, "GET", ""),
    # SKU
    ("skus_category_list", skus.SkuList, "GET", ""),
    ("skus_category_metainclude_list", skus.SkuList, "GET", ""),
    ("skus_category_q_filter_list", skus.SkuList, "GET", ""),
    ("skus_category_manufactures_filter_list", skus.SkuList, "GET", ""),
    ("skus_category_filters_filter_list", skus.SkuList, "GET", ""),
    ("skus_retrieve", skus.SkuRetrieve, "GET", ""),
    ("skus_similar_retrieve", skus.SkuList, "GET", ""),
    ("sku_reviews_include_aggr", skus.ReviewList, "GET", ""),
    ("sku_reviews_include_breakdown", skus.ReviewList, "GET", ""),
    ("skus_reviews_retrieve", skus.ReviewList, "GET", ""),
    ("skus_reviews_vote_retrieve", skus.VoteRetrieve, "POST", ""),
    ("skus_reviews_flag_retrieve", skus.FlagItem, "POST", ""),
    ("skus_review_form_retrieve", skus.ReviewFormRetrieve, "GET", ""),
    # Book
    ("author__", books.BookAuthorRetrieve, "GET", ""),
    ("author__books", books.BooksList, "GET", ""),
    ("book_categories__", books.BookCategoryRetrieve, "GET", ""),
    ("book_categories__books", books.BooksList, "GET", ""),
    ("book_categories__filters", books.BookCategoriesList, "GET", ""),
    ("books", books.BooksRetrieve, "GET", ""),
    ("books__details", books.BookDetailsRetrieve, "GET", ""),
    ("books__search", books.BooksList, "GET", ""),
    ("books__similar_by_author", books.BooksList, "GET", ""),
    ("books_categories", books.BookCategoriesList, "GET", ""),
    ("publisher__", books.PublisherRetrieve, "GET", ""),
    ("publisher__books", books.BooksList, "GET", ""),
]
