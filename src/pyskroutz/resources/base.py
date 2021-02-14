from typing import Type

import requests
from pydantic import BaseModel
from pyskroutz.client import SkroutzClient


class ApiResource:
    _session: requests.Session
    _client: SkroutzClient

    BASE_URL: str = "https://api.skroutz.gr"

    def __init__(self, client: SkroutzClient) -> None:
        self._client = client

    def _set_prepared_request(
        self,
        url: str = None,
        method: str = "GET",
        data=None,
        headers: dict = None,
        params: dict = None,
        json=None,
        model: Type[BaseModel] = None,
    ) -> None:
        """Set pre

        Args:
            url:
            method:
            data:
            headers:
            params:
            json:

        Returns:

        """
        self._model = model
        self._prepared_request = self._client._session.prepare_request(
            requests.Request(
                method=method,
                url=url,
                data=data,
                headers=self._client._headers,
                params=params,
                json=json,
            )
        )

    def execute(
        self,
    ):
        if not hasattr(self, "_prepared_request"):
            raise ValueError("You have to select the retrieve method first")
        resp = self._client._session.send(self._prepared_request).json()
        if self._model is not None:
            return self._model(**resp)
