from ..client.base import _SkroutzClient
from ..models.products import (
    ProductsList,
    ProductRetrieve,
    CardsList,
    PersonalizationRetrieve,
    PersonalizationItem,
)
from . import PaginationParams
from typing import Dict, Any, Optional


class Products(_SkroutzClient):
    """This Class holds the group of Products related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/category/) section."""

    ENDPOINT_PATH: str = "products"

    def get(self, id: int) -> ProductRetrieve:
        """Retrieve a single product

        Examples:

            >>> client.products.get(242327)

        Args:
            id: Product identifier

        Returns:
            Product object.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            "GET",
            ProductRetrieve,
        )

    def get_sku_products(self, id: int) -> ProductsList:
        """Retrieve an SKU's products

        Args:
            id: SKU Identifier

        Returns:
            List of product objects
        """
        return self.fetch(
            f"{self.BASE_URL}/skus/{id}/products",
            "GET",
            ProductsList,
        )

    def get_sku_products_grouped_cards(self, id: int) -> CardsList:
        """Retrieve an SKU's products grouped in cards

        Args:
            id: SKU Identifier

        Examples:

            >>> client.products.get_sku_products_grouped_cards()

        """
        return self.fetch(
            f"{self.BASE_URL}/skus/{id}/product_cards",
            "GET",
            CardsList,
        )

    def get_personalization(self) -> PersonalizationRetrieve:
        """Show Personalization info

        Returns:
            Personalization object

        Examples:

            >>> client.products.get_personalization()
        """
        return self.fetch(
            f"{self.BASE_URL}/personalization",
            "GET",
            PersonalizationRetrieve,
        )
