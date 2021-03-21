"""Response models for User resources
"""
import datetime
from enum import Enum

from pydantic import AnyHttpUrl, EmailStr

from .base import *


class FavoriteListItem(BaseModel):
    id: int
    name: str
    category: Optional[str]


class FavoriteListsRetrieve(BaseModel):
    favorite_lists: Optional[List[FavoriteListItem]]
    meta: MetaItemBase


class FavoriteListRetrieve(BaseModel):
    favorite_list: Optional[FavoriteListItem]


class FavoriteItem(BaseModel):
    id: int
    have_it: bool
    user_id: int
    user_notes: Optional[str]
    sku_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    get_absolute_threshold: Optional[str]


class FavoriteList(BaseModel):
    favorites: Optional[List[FavoriteItem]]
    meta: Optional[MetaItemBase]


class FavoriteRetrieve(BaseModel):
    favorite: FavoriteItem
