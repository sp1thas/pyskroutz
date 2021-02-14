"""Response models for manufacturer resources
"""
from typing import List, Optional

from pydantic import BaseModel, HttpUrl

from .base import ItemBase, MetaItemBase


class ManufacturerItem(ItemBase):
    image_url: Optional[HttpUrl]


class ManufacturersList(BaseModel):
    manufacturers: Optional[List[ManufacturerItem]]
    meta: MetaItemBase


class ManufacturerRetrieve(BaseModel):
    manufacturer: ManufacturerItem
