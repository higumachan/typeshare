"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import List, Union


class ItemDetailsFieldValue(BaseModel):
    pass

class AdvancedColorsTypes(str, Enum):
    STRING = "string"
    NUMBER = "number"
    NUMBER_ARRAY = "number-array"
    REALLY_COOL_TYPE = "reallyCoolType"

class AdvancedColorsString(BaseModel):
    type: AdvancedColorsTypes = AdvancedColorsTypes.STRING
    content: str

class AdvancedColorsNumber(BaseModel):
    type: AdvancedColorsTypes = AdvancedColorsTypes.NUMBER
    content: int

class AdvancedColorsNumberArray(BaseModel):
    type: AdvancedColorsTypes = AdvancedColorsTypes.NUMBER_ARRAY
    content: List[int]

class AdvancedColorsReallyCoolType(BaseModel):
    type: AdvancedColorsTypes = AdvancedColorsTypes.REALLY_COOL_TYPE
    content: ItemDetailsFieldValue

AdvancedColors = Union[AdvancedColorsString, AdvancedColorsNumber, AdvancedColorsNumberArray, AdvancedColorsReallyCoolType]
