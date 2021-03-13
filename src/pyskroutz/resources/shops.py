from .base import ApiResource
from ..models import shops, skus
from ..utils import fluent
from ..resources import PaginationParams


class Shops(ApiResource):
    """This Class holds the group of shops endpoint.
    More details in [shops](https://developer.skroutz.gr/api/v3/shops) section.
    """

    ENDPOINT_PATH: str = "shops"

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single shop"""

        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            model=shops.ShopRetrieve,
        )

    @fluent
    def get_reviews(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve a shop's reviews

        Args:
            id: shop identifier
            pag_params: pagination parameters

        Examples:
            >>> pyskroutz.shops(client).get_reviews(452, per=2).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews",
            model=skus.ReviewList,
            params=pag_params,
        )
