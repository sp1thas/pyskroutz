from .base import ApiResource
from ..models.flags import FlagList
from ..utils import fluent


class Flags(ApiResource):
    """This Class holds the group of Flags related endpoints.
    More details in [flags](https://developer.skroutz.gr/api/v3/flag/) section.
    """

    ENDPOINT_PATH: str = "flags"

    @fluent
    def get(self) -> None:
        """List all flags"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            method="GET",
            model=FlagList,
        )
