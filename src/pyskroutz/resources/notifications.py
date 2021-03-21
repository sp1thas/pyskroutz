from typing import Optional, List

from .base import ApiResource
from ..models import notifications
from ..utils import fluent


class Notifications(ApiResource):
    """This Class holds the group of Notifications related endpoints. More details in [category](https://developer.skroutz.gr/api/v3/notifications/) section."""

    ENDPOINT_PATH: str = "notifications"

    @fluent
    def get(self, id: Optional[int] = None) -> None:
        """List notifications or retrieve a single notification

        Args:
            id: manufacturer identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
            if id is not None
            else f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            method="GET",
            model=notifications.NotificationRetrieve
            if id is not None
            else notifications.NotificationList,
        )

    @fluent
    def mark_as_viewed(self, ids: List[int]) -> None:
        """Mark notifications as viewed

        Args:
            id:notification identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/view",
            json={"ids": ids},
            method="POST",
            model=None,
        )
