from .base import ApiResource
from ..models import shops, skus
from ..utils import fluent


class Shops(ApiResource):
    """This Class holds the group of shops endpoint.
    More details in [shops](https://developer.skroutz.gr/api/v3/shops) section.
    """

    ENDPOINT_PATH: str = "shops"

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single shop

        Examples:

            >>> pyskroutz.shops(client).get(452).execute()
        """

        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            model=shops.ShopRetrieve,
        )

    @fluent
    def get_reviews(self, id: int) -> None:
        """Retrieve a shop's reviews

        Args:
            id: shop identifier

        Examples:
            >>> pyskroutz.shops(client).get_reviews(452).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews",
            model=skus.ReviewList,
        )
