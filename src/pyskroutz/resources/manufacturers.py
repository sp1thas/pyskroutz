from typing import Optional

from .base import ApiResource
from ..models.categories import CategoryList
from ..models.manufacturers import ManufacturerRetrieve, ManufacturersList
from ..resources import PaginationParams
from ..utils import fluent


class Manufacturers(ApiResource):
    """This Class holds the group of Manufacturers related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/category/) section."""

    ENDPOINT_PATH: str = "manufacturers"

    @fluent
    def get(self, id: Optional[int] = None) -> None:
        """Retrieve a single manufacturer or list them all.

        Args:
            id: manufacturer identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
            if id is not None
            else f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            method="GET",
            model=ManufacturerRetrieve if id is not None else ManufacturersList,
        )

    @fluent
    def get_manufacturer_categories(
        self, id: int, **pag_params: PaginationParams
    ) -> None:
        """

        Args:
            id: Manufacturer identifier
            pag_params: Pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/categories",
            method="GET",
            model=CategoryList,
            params=pag_params,
        )
