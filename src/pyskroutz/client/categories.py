from .base_client import _SkroutzClient
from ..models.categories import CategoryListResponseModel


class Categories(_SkroutzClient):
    ENDPOINT_PATH: str = "categories"

    def list(self, **pag_params):
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}"
        self._params = pag_params
        self._json = {}
        self._data = None
        self._model = CategoryListResponseModel
        self._method = "GET"
        return self.fetch()
