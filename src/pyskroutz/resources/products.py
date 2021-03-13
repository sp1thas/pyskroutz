from .base import ApiResource
from ..models.products import (
    ProductsList,
    ProductRetrieve,
    CardsList,
    PersonalizationRetrieve,
)
from ..utils import fluent


class Products(ApiResource):
    """This Class holds the group of Products related endpoints.
    More details in [product](https://developer.skroutz.gr/api/v3/product/) section.
    """

    ENDPOINT_PATH: str = "products"

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single product

        Args:
            id: Product identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}", model=ProductRetrieve
        )

    @fluent
    def get_sku_products(self, id: int) -> None:
        """Retrieve an SKU's products

        Args:
            id: SKU Identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{id}/products", model=ProductsList
        )

    @fluent
    def get_sku_products_grouped_cards(self, id: int) -> None:
        """Retrieve an SKU's products grouped in cards

        Args:
            id: SKU Identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{id}/product_cards", model=CardsList
        )

    @fluent
    def get_personalization(self) -> None:
        """Show Personalization info"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/personalization", model=PersonalizationRetrieve
        )
