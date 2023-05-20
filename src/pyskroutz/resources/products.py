from pyskroutz.models.products import (
    CardsList,
    PersonalizationRetrieve,
    ProductRetrieve,
    ProductsList,
)
from pyskroutz.resources.base import ApiResource
from pyskroutz.utils import fluent


class Products(ApiResource):
    """This Class holds the group of Products related endpoints.
    More details in [product](https://developer.skroutz.gr/api/v3/product/) section.
    """

    ENDPOINT_PATH: str = "products"

    @fluent
    def get(self, _id: int) -> None:
        """Retrieve a single product

        Args:
            _id: Product identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{_id}", model=ProductRetrieve
        )

    @fluent
    def get_sku_products(self, _id: int) -> None:
        """Retrieve an SKU's products

        Args:
            _id: SKU Identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{_id}/products", model=ProductsList
        )

    @fluent
    def get_sku_products_grouped_cards(self, _id: int) -> None:
        """Retrieve an SKU's products grouped in cards

        Args:
            _id: SKU Identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{_id}/product_cards", model=CardsList
        )

    @fluent
    def get_personalization(self) -> None:
        """Show Personalization info"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/personalization", model=PersonalizationRetrieve
        )
