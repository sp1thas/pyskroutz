from typing import Any, Type, Dict

import requests
from pydantic import BaseModel

from ..exceptions import SkroutzApiError
from ..utils import rsetattr


class _SkroutzClient:
    _client_id: str
    _client_secret: str
    _session: requests.Session

    BASE_URL: str = "https://api.skroutz.gr"

    _url: str
    _data: Any
    _params: dict
    _json: Dict[str, Any]
    _method: str
    _model: Type[BaseModel]
    _access_token_type: str
    _access_token: str

    def headers(self) -> Dict[str, str]:
        """Get headers using the access token.

        Returns: Headers dictionary.
        """
        return {
            "Accept": "application/vnd.skroutz+json; version=3",
            "Authorization": "%s %s"
            % (self._access_token_type.capitalize(), self._access_token),
        }

    def fetch(self) -> BaseModel:
        resp = self._session.send(
            self._session.prepare_request(
                requests.Request(
                    method=self._method,
                    url=self._url,
                    data=self._data,
                    headers=self.headers(),
                    params=self._params,
                    json=self._json,
                )
            )
        )
        import pprint

        pprint.pprint(resp.json())
        return self._model(**resp.json())

    def __init__(self, client_id: str, client_secret: str, endpoints: list) -> None:
        self._session = requests.Session()
        self._client_id = client_id
        self._client_secret = client_secret
        self._endpoints = endpoints
        self.authenticate(self._client_id, client_secret=self._client_secret)

    def authenticate(self, client_id, client_secret) -> None:
        req = requests.post(
            "https://www.skroutz.gr/oauth2/token",
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials",
                "scope": "public",
            },
        )
        if req.status_code == 200:
            for name, _ in self._endpoints:
                if not hasattr(self, name):
                    setattr(self, name, _(client_id, client_secret, []))
                rsetattr(self, f"{name}._access_token", req.json()["access_token"])
                rsetattr(self, f"{name}._access_token_type", req.json()["token_type"])
            return
        elif req.status_code == 401:
            raise SkroutzApiError(req.json()["error"])
        else:
            raise SkroutzApiError("Something bad happened")
