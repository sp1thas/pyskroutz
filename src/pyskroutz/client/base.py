from typing import Any, Type, Dict, Optional

import requests
from pydantic import BaseModel

from ..exceptions import SkroutzApiError
from ..utils import rsetattr


class _SkroutzClient:
    _client_id: str
    _client_secret: str
    _session: requests.Session

    BASE_URL: str = "https://api.skroutz.gr"

    _access_token_type: str
    _access_token: str

    def headers(self) -> Dict[str, str]:
        """Get headers using the access token.

        Returns: Headers dictionary.
        """
        return {
            "Accept": "application/vnd.skroutz+json; version=3",
            "Authorization": "%s sdfsdfsdfsd %s"
            % (
                getattr(self, "_access_token_type", "").capitalize(),
                getattr(self, "_access_token", ""),
            ),
        }

    def fetch(
        self,
        url: str,
        method: str,
        model: Type[BaseModel],
        data: Optional[Any] = None,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
    ):
        resp = self._session.send(
            self._session.prepare_request(
                requests.Request(
                    method=method,
                    url=url,
                    data=data,
                    headers=self.headers(),
                    params=params,
                    json=json,
                )
            )
        )
        return model(
            **self._request(url=url, method=method, data=data, params=params, json=json)
        )

    def _request(
        self,
        url: str,
        method: str,
        data: Optional[Any] = None,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
    ):
        resp = self._session.send(
            self._session.prepare_request(
                requests.Request(
                    method=method,
                    url=url,
                    data=data,
                    headers=self.headers(),
                    params=params,
                    json=json,
                )
            )
        )
        return resp.json()

    def __init__(
        self, client_id: str, client_secret: str, endpoints: list, dev: bool
    ) -> None:
        self._session = requests.Session()
        self._client_id = client_id
        self._client_secret = client_secret
        self._endpoints = endpoints
        self._authenticate(self._client_id, client_secret=self._client_secret, dev=dev)

    def _authenticate(self, client_id, client_secret, dev: bool = False) -> None:
        if dev:
            return
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
