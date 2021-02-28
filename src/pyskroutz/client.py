from typing import Dict

import requests


class SkroutzClient:
    """Skroutz Client Class. This is the main class that let's you interact with Skroutz API.

    Examples:
        In order to interact with Skroutz API you have to initiate a `SkroutzClient` object.
        You have to provide the client id and the client secret.

        >>> import pyskroutz
        >>> client = pyskroutz.client("<client-id>", "<client-secret>")

        Check out the available endpoints for further details.

    Attributes:
        BASE_URL (str): The base url of Skroutz API.
    """

    _access_token: str
    _access_token_type: str

    def __init__(
        self, client_id: str, client_secret: str, raise_auth_error: bool = True
    ) -> None:
        """
        Initiates an SkroutzClient object.

        Args:
            client_id: The client id.
            client_secret: The client secret.
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._authenticate(raise_auth_error=raise_auth_error)
        self._session = requests.Session()

    def _authenticate(self, raise_auth_error: bool = True) -> None:
        req = requests.post(
            "https://www.skroutz.gr/oauth2/token",
            data={
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "grant_type": "client_credentials",
                "scope": "public",
            },
        )
        if raise_auth_error:
            req.raise_for_status()

        self._access_token = req.json().get("access_token", "test")
        self._access_token_type = req.json().get("token_type", "test")

    @property
    def _headers(self) -> Dict[str, str]:
        """Get headers using the access token.

        Returns: Headers dictionary.
        """
        return {
            "Accept": "application/vnd.skroutz+json; version=3",
            "Authorization": "%s %s"
            % (
                getattr(self, "_access_token_type", "").capitalize(),
                getattr(self, "_access_token", ""),
            ),
        }
