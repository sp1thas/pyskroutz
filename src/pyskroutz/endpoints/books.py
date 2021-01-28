from ..client.base import _SkroutzClient
from ..models.books import (
    BookCategoriesList,
    BookCategoryRetrieve,
    PublisherRetrieve,
    BooksRetrieve,
    BooksList,
    BookDetailsRetrieve,
    BookAuthorRetrieve,
)
from . import PaginationParams
from typing import Dict, Any, Optional


class Books(_SkroutzClient):
    """This Class holds the group of Books related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/category/) section."""

    ENDPOINT_PATH: str = "books"

    def get(self, id: int) -> BooksRetrieve:
        """Retrieve a single Book

        Examples:

            >>> client.books.get(242327)

        Args:
            id: Book identifier

        Returns:
            Book object.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            "GET",
            BooksRetrieve,
        )

    def get_details(self, id: int) -> BookDetailsRetrieve:
        """Retrieve Book details

        Examples:

            >>> client.get_details(242327)

        Args:
            id: Book identifier.

        Returns:
            Book detals object.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/details",
            "GET",
            BookDetailsRetrieve,
        )

    def get_author(self, id: int) -> BookAuthorRetrieve:
        """Retrieve Book Author

        Examples:

            >>> client.get_author(385)

        Args:
            id: author identifier

        Returns:
            Book's author object
        """
        return self.fetch(
            f"{self.BASE_URL}/author/{id}",
            "GET",
            BookAuthorRetrieve,
        )

    def get_author_books(self, id: int) -> BooksList:
        """Retrieve Author Books

        Examples:

            >>> client.get_author_books(385)

        Args:
            id: author identifier

        Returns:
            list of book objects
        """
        return self.fetch(
            f"{self.BASE_URL}/author/{id}/books",
            "GET",
            BooksList,
        )

    def get_similar_by_author(self, id: int) -> BooksList:
        """Retrieve similar Books by Author

        Examples:

            >>> client.get_similar_by_author(242327)

        Args:
            id: author identifier

        Returns:
            list of book objects
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar_by_author",
            "GET",
            BooksList,
        )

    def get_publisher(self, id: int) -> PublisherRetrieve:
        """Retrieve Book Publisher

        Examples:

            >>> client.get_publisher(78)

        Args:
            id: publisher identifier

        Returns:
            publisher object
        """
        return self.fetch(
            f"{self.BASE_URL}/publisher/{id}",
            "GET",
            PublisherRetrieve,
        )

    def get_publisher_books(self, id: int) -> BooksList:
        """Retrieve Publisher Books

        Examples:

            >>> client.get_publisher_books(78)

        Args:
            id: publisher identifier

        Returns:
            list of book objects
        """
        return self.fetch(
            f"{self.BASE_URL}/publisher/{id}/books",
            "GET",
            BooksList,
        )

    def get_book_categories(self) -> BookCategoriesList:
        """Retrieve Book Categories

        Examples:

            >>> client.get_book_categories()

        Returns:
            list of category objects
        """
        return self.fetch(
            f"{self.BASE_URL}/book_categories",
            "GET",
            BookCategoriesList,
        )

    def get_category(self, id: int) -> BookCategoryRetrieve:
        """Retrieve Book Category

        Examples:

            >>> client.get_category(1857)

        Args:
            id: book identifier

        Returns:
            category object
        """
        return self.fetch(
            f"{self.BASE_URL}/book_categories/{id}",
            "GET",
            BookCategoryRetrieve,
        )

    def get_category_books(
        self, id: int, order_by: Optional[str] = None, order_dir: Optional[str] = None
    ) -> BooksList:
        """Retrieve Book Category's Books

        Examples:

            >>> client.get_category_books(1857)

        Args:
            id: category identifier

        Returns:
            list of book objects
        """
        return self.fetch(
            f"{self.BASE_URL}/book_categories/{id}/books",
            "GET",
            BooksList,
        )
