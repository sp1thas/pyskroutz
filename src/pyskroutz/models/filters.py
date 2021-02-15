"""Response models for Filter resources
"""
import datetime
from enum import Enum

from pydantic import AnyHttpUrl, EmailStr

from .base import *


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
