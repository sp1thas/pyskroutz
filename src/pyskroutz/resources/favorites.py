from typing import Optional

from .base import ApiResource
from ..models import favorites
from ..utils import fluent


class Favorites(ApiResource):
    """This Class holds the group of favorites related endpoints.
    More details in [favorites](https://developer.skroutz.gr/api/v3/favorites) section.
    """

    ENDPOINT_PATH: str = "favorites"

    @fluent
    def get_lists(
        self,
    ) -> None:
        """List favorite lists"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorite_lists", model=favorites.FavoriteList
        )

    @fluent
    def create_list(self, name: str) -> None:
        """Create a favorite_list.
        It trying to create a custom list with the same name as an
        existing custom list you will be presented with an error message.

        Args:
            name: favorite list name
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorite_lists",
            model=favorites.FavoriteListRetrieve,
            method="POST",
            json={"favorite_list": {"name": name}},
        )

    @fluent
    def destroy_list(self, id: int) -> None:
        """Destroy a favorite_list.
        The response status is 204 and with an empty response body when resource is destroyed.
        Status code is 404 when the resource does not exist.

        Args:
            id: favorite list identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorite_lists/{id}", model=None, method="DELETE"
        )

    @fluent
    def list_favorites(self, favorite_list: Optional[int] = None) -> None:
        """List favorites (all or specify a favorite list)"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorites"
            if favorite_list is None
            else f"{self.BASE_URL}/favorite_lists/{favorite_list}/favorites",
            model=favorites.FavoriteList,
        )

    @fluent
    def get_favorite(self, id: int) -> None:
        """Retrieve a single favorite

        Args:
            id: favorite identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorites/{id}", model=favorites.FavoriteRetrieve
        )

    @fluent
    def create_favorite(self, sku_id: int) -> None:
        """Create a new favorite

        Args:
            sku_id: SKU identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorites",
            model=favorites.FavoriteRetrieve,
            method="POST",
            json={"favorite": {"sku_id": sku_id}},
        )

    @fluent
    def destroy_favorite(self, id: int) -> None:
        """Destroy a favorite

        Args:
            id: Favorite identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/favorites/{id}",
            model=None,
            method="DELETE",
        )
