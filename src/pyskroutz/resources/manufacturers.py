from typing import Optional

from pyskroutz.models.categories import CategoryList
from pyskroutz.models.manufacturers import ManufacturerRetrieve, ManufacturersList
from pyskroutz.resources import PaginationParams
from pyskroutz.resources.base import ApiResource
from pyskroutz.utils import fluent


class Manufacturers(ApiResource):
    """
    This Class holds the group of Manufacturers related endpoints.
    More details in [category](https://developer.skroutz.gr/api/v3/category/) section.
    """

    ENDPOINT_PATH: str = "manufacturers"

    @fluent
    def get(self, _id: Optional[int] = None) -> None:
        """Retrieve a single manufacturer or list them all.

        Args:
            _id: manufacturer identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}"
            if _id is not None
            else f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            method="GET",
            model=ManufacturerRetrieve if _id is not None else ManufacturersList,
        )

    @fluent
    def get_manufacturer_categories(
        self, _id: int, **pag_params: PaginationParams
    ) -> None:
        """

        Args:
            _id: Manufacturer identifier
            pag_params: Pagination parameters
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}/categories",
            method="GET",
            model=CategoryList,
            params=pag_params,
        )
