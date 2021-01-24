from .base import _SkroutzClient
from pyskroutz.endpoints.categories import Categories


class SkroutzClient(_SkroutzClient):
    """Skroutz Client Class. This is the main class that let's you interact with Skroutz API.

    Examples:
        In order to interact with Skroutz API you have to initiate a `SkroutzClient` object.
        You have to provide the client id and the client secret.

        >>> from pyskroutz import SkroutzClient
        >>> client = SkroutzClient("<client-id>", "<client-secret>")
        >>> client.categories.list(per=10)

        Check out the available endpoint for further details.

    Attributes:
        BASE_URL:
    """

    _endpoints = [("categories", Categories)]

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initiates an SkroutzClient object.

        Args:
            client_id: The client id.
            client_secret: The client secret.
        """
        super().__init__(client_id, client_secret, SkroutzClient._endpoints)
