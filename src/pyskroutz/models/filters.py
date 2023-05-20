"""Response models for Filter resources
"""
import datetime
from typing import List, Optional

from pydantic import BaseModel

from pyskroutz.models.base import MetaItemBase


class FilterGroupsItem(BaseModel):
    id: int
    name: str
    active: bool
    category_id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    hint: str
    combined: bool
    filter_type: int


class FilterGroupsList(BaseModel):
    filter_groups: Optional[List[FilterGroupsItem]]
    meta: MetaItemBase
