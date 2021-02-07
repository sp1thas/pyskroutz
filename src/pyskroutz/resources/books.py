from .base import ApiResource
from ..models.books import (
    BookCategoriesList,
    BookCategoryRetrieve,
    PublisherRetrieve,
    BooksRetrieve,
    BooksList,
    BookDetailsRetrieve,
    BookAuthorRetrieve,
)
from typing import Optional
from ..utils import fluent


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

        Examples:

            >>> pyskroutz.books(client).get(242327).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            method="GET",
            model=BooksRetrieve,
        )

    @fluent
    def get_details(self, id: int) -> None:
        """Retrieve Book details

        Args:
            id: Book identifier.

        Examples:

            >>> pyskroutz.books(client).get_details(242327).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/details",
            method="GET",
            model=BookDetailsRetrieve,
        )

    @fluent
    def get_author(self, id: int) -> None:
        """Retrieve Book Author

        Args:
            id: author identifier

        Examples:

            >>> pyskroutz.books(client).get_author(385).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}",
            model=BookAuthorRetrieve,
        )

    @fluent
    def get_author_books(self, id: int) -> None:
        """Retrieve Author Books

        Args:
            id: author identifier

        Examples:

            >>> pyskroutz.books(client).get_author_books(385).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}/books", model=BooksList
        )

    @fluent
    def get_similar_by_author(self, id: int) -> None:
        """Retrieve similar Books by Author

        Args:
            id: author identifier

        Examples:

            >>> pyskroutz.books(client).get_similar_by_author(242327).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar_by_author",
            model=BooksList,
        )

    @fluent
    def get_publisher(self, id: int) -> None:
        """Retrieve Book Publisher

        Args:
            id: publisher identifier

        Examples:

            >>> pyskroutz.books(client).get_publisher(78).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}", model=PublisherRetrieve
        )

    @fluent
    def get_publisher_books(self, id: int) -> None:
        """Retrieve Publisher Books

        Args:
            id: publisher identifier

        Examples:

            >>> pyskroutz.books(client).get_publisher_books(78).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}/books", model=BooksList
        )

    @fluent
    def get_book_categories(self) -> None:
        """Retrieve Book Categories

        Examples:

            >>> pyskroutz.books(client).get_book_categories().execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories", model=BookCategoriesList
        )

    def get_category(self, id: int) -> None:
        """Retrieve Book Category

        Args:
            id: book identifier

        Examples:

            >>> pyskroutz.books(client).get_category(1857).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}", model=BookCategoryRetrieve
        )

    def get_category_books(
        self, id: int, order_by: Optional[str] = None, order_dir: Optional[str] = None
    ) -> None:
        """Retrieve Book Category's Books

        Args:
            id: category identifier

        Examples:

            >>> pyskroutz.books(client).get_category_books(1857).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}/books", model=BooksList
        )
