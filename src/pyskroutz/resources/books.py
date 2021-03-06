from typing import Optional

from .base import ApiResource
from ..models import books
from ..utils import fluent
from ..resources import PaginationParams


class Books(ApiResource):
    """This Class holds the group of Books related endpoints.
    More details in [category](https://developer.skroutz.gr/api/v3/category/) section.
    """

    ENDPOINT_PATH: str = "books"

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single Book

        Args:
            id: Book identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            method="GET",
            model=books.BooksRetrieve,
        )

    @fluent
    def get_details(self, id: int) -> None:
        """Retrieve Book details

        Args:
            id: Book identifier.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/details",
            method="GET",
            model=books.BookDetailsRetrieve,
        )

    @fluent
    def get_author(self, id: int) -> None:
        """Retrieve Book Author

        Args:
            id: author identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}",
            model=books.BookAuthorRetrieve,
        )

    @fluent
    def get_author_books(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve Author Books

        Args:
            id: author identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}/books",
            model=books.BooksList,
            params=pag_params,
        )

    @fluent
    def get_similar_by_author(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve similar Books by Author

        Args:
            id: author identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar_by_author",
            model=books.BooksList,
            params=pag_params,
        )

    @fluent
    def get_publisher(self, id: int) -> None:
        """Retrieve Book Publisher

        Args:
            id: publisher identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}", model=books.PublisherRetrieve
        )

    @fluent
    def get_publisher_books(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve Publisher Books

        Args:
            id: publisher identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}/books",
            model=books.BooksList,
            params=pag_params,
        )

    @fluent
    def get_book_categories(self) -> None:
        """Retrieve Book Categories"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories", model=books.BookCategoriesList
        )

    @fluent
    def get_category(self, id: int) -> None:
        """Retrieve Book Category

        Args:
            id: book identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}",
            model=books.BookCategoryRetrieve,
        )

    @fluent
    def get_category_books(
        self, id: int, order_by: Optional[str] = None, order_dir: Optional[str] = None
    ) -> None:
        """Retrieve Book Category's Books

        Args:
            id: category identifier
        """
        if order_by or order_dir:
            raise NotImplemented
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}/books", model=books.BooksList
        )
