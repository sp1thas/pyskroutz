"""Response models for flag resources
"""
import datetime
from typing import List

from pydantic import BaseModel


class FlagBaseItem(BaseModel):
    reason: str
    description: str


class FlagItem(BaseModel):
    id: int
    flaggable_id: int
    flaggable_type: str
    user_id: int
    reason: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class FlagRetrieve(BaseModel):
    flag: FlagItem


class FlagList(BaseModel):
    flags: List[FlagBaseItem]
