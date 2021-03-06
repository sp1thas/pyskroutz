from typing import Optional

from pyskroutz.resources.base import ApiResource

from ..models.categories import (
    CategoryList,
    CategoryRetrieve,
    SpecificationList,
)
from ..resources import PaginationParams
from ..utils import fluent


class Categories(ApiResource):
    """This Class holds the group of Categories related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/category/) section."""

    ENDPOINT_PATH: str = "categories"

    @fluent
    def get(self, id: Optional[int] = None, **pag_params: PaginationParams) -> None:
        """Retrieve a single category or list them all.

        Args:
            id: category identifier
            pag_params: pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
            if id is not None
            else f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            model=CategoryRetrieve if id is not None else CategoryList,
            params=pag_params,
        )

    @fluent
    def get_parent(self, id: int) -> None:
        """Retrieve the parent of a category.

        Args:
            id: category identifier.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/parent",
            model=CategoryRetrieve,
        )

    @fluent
    def get_root(self) -> None:
        """Retrieve the root category."""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/root", model=CategoryRetrieve
        )

    @fluent
    def list_children(self, id: int, **pag_params: PaginationParams) -> None:
        """List the children categories of a category.

        Args:
            id: category identifier.
            **pag_params: pagination params.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/children",
            model=CategoryList,
            params=pag_params,
        )

    @fluent
    def get_specifications(
        self, id: int, include_group: bool = None, **pag_params: PaginationParams
    ) -> None:
        """List a category's specifications.

        Args:
            id: category identifier.
            include_group: Include group.
            **pag_params: pagination params.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/specifications",
            model=SpecificationList,
            params=pag_params
            if include_group is None
            else dict(include="group", **pag_params),  # type: ignore
        )

    @fluent
    def get_manufacturers(
        self, id: int, order_dir: str = None, **pag_params: PaginationParams
    ) -> None:
        """List a category's manufacturers.

        Args:
            id: category identifier.
            order_dir: Order ascending or descending (`asc`, `desc` default)
            **pag_params: pagination params.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/manufacturers",
            model=SpecificationList,
            params=dict(**pag_params)
            if order_dir is None
            else dict(order_dir=order_dir, **dict(pag_params)),  # type: ignore
        )

    @fluent
    def get_favorites(self, id: int) -> None:
        """List a category's favorites.

        Args:
            id: category identifier.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/favorites",
            model=SpecificationList,
        )
