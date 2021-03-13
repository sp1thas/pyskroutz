from .base import ApiResource
from ..models import search
from ..utils import fluent


class Search(ApiResource):
    """This Class holds the group of seach endpoint.
    More details in [search](https://developer.skroutz.gr/api/v3/search) section.
    """

    ENDPOINT_PATH: str = "search"

    @fluent
    def __call__(self, q: str) -> None:
        """Search"""

        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            model=search.SearchResultsList,
            params={"q": q},
        )

    @fluent
    def autocomplete(self, q: str) -> None:
        """Autocomplete"""

        self._set_prepared_request(
            url=f"{self.BASE_URL}/autocomplete",
            model=search.AutocompleteList,
            params={"q": q},
        )
