from pydantic import BaseModel
from .models.items import Category
from typing import List


class CategoriesList(BaseModel):
    categories: List[Category]
