from ..models.items import Category
from .base import HttpClient
from typing import List


class Categories(HttpClient):
    endpoint_path: str = "categories"

    ENDPOINT_PATH: str = 'categories'

    def list(self, page: int = 1, per: int = 5) -> List[Category]:
        resp_json = self.fetch(
            url=f'{self.BASE_URL}/{self.ENDPOINT_PATH}'
        )
        return [Category(**item) for item in resp_json.get('categories')]
