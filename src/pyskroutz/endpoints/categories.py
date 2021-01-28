from ..client.base import _SkroutzClient
from ..models.categories import (
    CategoryList,
    CategoryRetrieve,
    SpecificationList,
)
from . import PaginationParams
from typing import Dict, Any, Optional


class Categories(_SkroutzClient):
    """This Class holds the group of Categories related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/category/) section."""

    ENDPOINT_PATH: str = "categories"

    def get(self, id: Optional[int] = None) -> CategoryRetrieve:
        """Retrieve a single category or list them all.

        Examples:

            >>> client.categories.get(88)

        Args:
            id: category identifier

        Returns:
            Category details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
            if id is not None
            else f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            "GET",
            CategoryRetrieve,
        )

    def get_parent(self, id: int) -> CategoryRetrieve:
        """Retrieve the parent of a category.

        Examples:

            >>> client.categories.get_parent(88)

        Args:
            id: category identifier.

        Returns:
            Parent category details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/parent", "GET", CategoryRetrieve
        )

    def get_root(self) -> CategoryRetrieve:
        """Retrieve the root category.

        Examples:

            >>> client.categories.get_root()

        Returns:
            Root category details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/root", "GET", CategoryRetrieve
        )

    def list_children(self, id: int, **pag_params: PaginationParams) -> CategoryList:
        """List the children categories of a category.

        Examples:

            >>> client.categories.list_children(252)

        Args:
            id: category identifier.
            **pag_params: pagination params.

        Returns:
            List details of children categories.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/children",
            "GET",
            CategoryList,
            params=pag_params,
        )

    def get_specifications(
        self, id: int, include_group: bool = None, **pag_params: PaginationParams
    ) -> SpecificationList:
        """List a category's specifications.

        Examples:

            >>> client.categories.get_specifications(40, include_group=True)

        Args:
            id: category identifier.
            include_group: Include group.
            **pag_params: pagination params.

        Returns:
            List of specification details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/specifications",
            "GET",
            SpecificationList,
            params=dict(**pag_params)
            if include_group is None
            else dict(include="group", **pag_params),
        )

    def get_manufacturers(
        self, id: int, order_dir: str = None, **pag_params: PaginationParams
    ) -> SpecificationList:
        """List a category's manufacturers.

        Examples:

            >>> client.categories.get_manufacturers(2)

        Args:
            id: category identifier.
            order_dir: Order ascending or descending (`asc`, `desc` default)
            **pag_params: pagination params.

        Returns:
            List manufactures details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/manufacturers",
            "GET",
            SpecificationList,
            dict(**pag_params)
            if order_dir is None
            else dict(order_dir=order_dir, **pag_params),
        )

    def get_favorites(self, id: int) -> SpecificationList:
        """List a category's favorites.

        Examples:

            >>> client.categories.get_favorites(40)

        Args:
            id: category identifier.

        Returns:
            List favorites details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/favorites",
            "GET",
            SpecificationList,
        )
