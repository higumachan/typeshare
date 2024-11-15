"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel
from typing import List, Literal, Union


class ItemDetailsFieldValue(BaseModel):
    """
    Struct comment
    """
    pass

"""
This is a case comment
"""
class AdvancedColorsString(BaseModel):
    AdvancedColorsTypes: Literal["String"] = "String"
    content: str

class AdvancedColorsNumber(BaseModel):
    AdvancedColorsTypes: Literal["Number"] = "Number"
    content: int

class AdvancedColorsUnsignedNumber(BaseModel):
    AdvancedColorsTypes: Literal["UnsignedNumber"] = "UnsignedNumber"
    content: int

class AdvancedColorsNumberArray(BaseModel):
    AdvancedColorsTypes: Literal["NumberArray"] = "NumberArray"
    content: List[int]

"""
Comment on the last element
"""
class AdvancedColorsReallyCoolType(BaseModel):
    AdvancedColorsTypes: Literal["ReallyCoolType"] = "ReallyCoolType"
    content: ItemDetailsFieldValue

"""
Enum comment
"""
AdvancedColors = Union[AdvancedColorsString, AdvancedColorsNumber, AdvancedColorsUnsignedNumber, AdvancedColorsNumberArray, AdvancedColorsReallyCoolType]
"""
This is a case comment
"""
class AdvancedColors2String(BaseModel):
    AdvancedColors2Types: Literal["string"] = "string"
    content: str

class AdvancedColors2Number(BaseModel):
    AdvancedColors2Types: Literal["number"] = "number"
    content: int

class AdvancedColors2NumberArray(BaseModel):
    AdvancedColors2Types: Literal["number-array"] = "number-array"
    content: List[int]

"""
Comment on the last element
"""
class AdvancedColors2ReallyCoolType(BaseModel):
    AdvancedColors2Types: Literal["really-cool-type"] = "really-cool-type"
    content: ItemDetailsFieldValue

AdvancedColors2 = Union[AdvancedColors2String, AdvancedColors2Number, AdvancedColors2NumberArray, AdvancedColors2ReallyCoolType]
