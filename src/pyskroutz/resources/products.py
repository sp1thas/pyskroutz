from .base import ApiResource
from ..models.products import (
    ProductsList,
    ProductRetrieve,
    CardsList,
    PersonalizationRetrieve,
)


class Products(ApiResource):
    """This Class holds the group of Products related endpoints.
    More details in [category](https://developer.skroutz.gr/api/v3/category/) section.
    """

    ENDPOINT_PATH: str = "products"

    def get(self, id: int) -> None:
        """Retrieve a single product

        Args:
            id: Product identifier

        Examples:

            >>> pyskroutz.products(client).get(242327).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}", model=ProductRetrieve
        )

    def get_sku_products(self, id: int) -> None:
        """Retrieve an SKU's products

        Args:
            id: SKU Identifier
        Examples:

            >>> pyskroutz.products(client).get_sku_products(242327).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{id}/products", model=ProductsList
        )

    def get_sku_products_grouped_cards(self, id: int) -> None:
        """Retrieve an SKU's products grouped in cards

        Args:
            id: SKU Identifier

        Examples:

            >>> pyskroutz.products(client).get_sku_products_grouped_cards(3783654).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/skus/{id}/product_cards", model=CardsList
        )

    def get_personalization(self) -> None:
        """Show Personalization info

        Examples:

            >>> pyskroutz.products(client).get_personalization().execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/personalization", model=PersonalizationRetrieve
        )
