from .base_models import *


class CategoryResponseModel(ItemBaseResponseModel, WebUriResponseModel):
    children_count: int
    image_url: HttpUrl
    parent_id: int
    fashion: bool
    layout_mode: str
    code: str
    path: str
    show_specifications: bool
    manufacturer_title: str


class CategoryListResponseModel(BaseModel):
    categories: List[CategoryResponseModel]
    meta: MetaResponseModel


class CategoryRetrieveResponseModel(BaseModel):
    category: CategoryResponseModel
