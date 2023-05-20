from typing import Optional

from pyskroutz.models import books
from pyskroutz.resources import PaginationParams
from pyskroutz.resources.base import ApiResource
from pyskroutz.utils import fluent


class Books(ApiResource):
    """This Class holds the group of Books related endpoints.
    More details in [category](https://developer.skroutz.gr/api/v3/category/) section.
    """

    ENDPOINT_PATH: str = "books"

    @fluent
    def get(self, _id: int) -> None:
        """Retrieve a single Book

        Args:
            _id: Book identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}",
            method="GET",
            model=books.BooksRetrieve,
        )

    @fluent
    def get_details(self, _id: int) -> None:
        """Retrieve Book details

        Args:
            _id: Book identifier.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}/details",
            method="GET",
            model=books.BookDetailsRetrieve,
        )

    @fluent
    def get_author(self, _id: int) -> None:
        """Retrieve Book Author

        Args:
            _id: author identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{_id}",
            model=books.BookAuthorRetrieve,
        )

    @fluent
    def get_author_books(self, _id: int, **pag_params: PaginationParams) -> None:
        """Retrieve Author Books

        Args:
            _id: author identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{_id}/books",
            model=books.BooksList,
            params=pag_params,
        )

    @fluent
    def get_similar_by_author(self, _id: int, **pag_params: PaginationParams) -> None:
        """Retrieve similar Books by Author

        Args:
            _id: author identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}/similar_by_author",
            model=books.BooksList,
            params=pag_params,
        )

    @fluent
    def get_publisher(self, _id: int) -> None:
        """Retrieve Book Publisher

        Args:
            _id: publisher identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{_id}", model=books.PublisherRetrieve
        )

    @fluent
    def get_publisher_books(self, _id: int, **pag_params: PaginationParams) -> None:
        """Retrieve Publisher Books

        Args:
            _id: publisher identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{_id}/books",
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
    def get_category(self, _id: int) -> None:
        """Retrieve Book Category

        Args:
            _id: book identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{_id}",
            model=books.BookCategoryRetrieve,
        )

    @fluent
    def get_category_books(
        self, _id: int, order_by: Optional[str] = None, order_dir: Optional[str] = None
    ) -> None:
        """Retrieve Book Category's Books

        Args:
            _id: category identifier
            order_by: order by
            order_dir: order dir
        """
        if order_by or order_dir:
            raise NotImplemented
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{_id}/books", model=books.BooksList
        )
