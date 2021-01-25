from pydantic import BaseModel
from typing import List, Optional

from ..models.base import (
    MetaResponseModel,
    ItemBaseResponseModel,
    WebUriResponseModel,
    HttpUrl,
)


class GroupItem(BaseModel):
    """

    Attributes:
        id:
        name:
        order:
    """

    id: int
    name: str
    order: int


class GroupList(BaseModel):
    groups: GroupItem


class SpecificationItem(BaseModel):
    """Specification base model

    Attributes:
        id:
        name:
        values:
        order:
        unit:
    """

    id: int
    name: str
    values: List
    order: int
    unit: str


class SpecificationList(BaseModel):
    groups: Optional[List[GroupItem]]
    specifications: List[SpecificationItem]


class CategoryItem(ItemBaseResponseModel, WebUriResponseModel):
    """Category Item response model.

    Attributes:
        children_count:
        image_url:
        parent_id:
        fashion:
        layout_mode:
        code:
        path:
        show_specifications:
        manufacturer_title:
    """

    children_count: int
    image_url: HttpUrl
    parent_id: int
    fashion: bool
    layout_mode: str
    code: str
    path: str
    show_specifications: bool
    manufacturer_title: str


class CategoryList(BaseModel):
    """Response for a list of categories with meta details.

    Attributes:
        categories: A list of categories items.
        meta: response meta details.
    """

    categories: List[CategoryItem]
    meta: MetaResponseModel


class CategoryRetrieve(BaseModel):
    category: CategoryItem
