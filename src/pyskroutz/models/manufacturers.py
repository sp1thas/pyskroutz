"""Response models for manufacturer resources
"""
from pydantic import BaseModel, HttpUrl
from typing import List, Any, Optional
from .base import ItemBase, MetaItemBase


class ManufacturerItem(ItemBase):
    image_url: Optional[HttpUrl]


class ManufacturersList(BaseModel):
    manufacturers: Optional[List[ManufacturerItem]]
    meta: MetaItemBase


class ManufacturerRetrieve(BaseModel):
    manufacturer: ManufacturerItem
