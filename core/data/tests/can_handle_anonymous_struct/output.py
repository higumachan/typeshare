"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import Union


class AutofilledByUsInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Us` of the `AutofilledBy` Rust enum
    """
    uuid: str
    """
    The UUID for the fill
    """


class AutofilledBySomethingElseInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `SomethingElse` of the `AutofilledBy` Rust enum
    """
    uuid: str
    """
    The UUID for the fill
    """
    thing: int
    """
    Some other thing
    """


class AutofilledByTypes(str, Enum):
    US = "Us"
    SOMETHING_ELSE = "SomethingElse"

class AutofilledByUs(BaseModel):
    type: AutofilledByTypes = AutofilledByTypes.US
    content: AutofilledByUsInner

class AutofilledBySomethingElse(BaseModel):
    type: AutofilledByTypes = AutofilledByTypes.SOMETHING_ELSE
    content: AutofilledBySomethingElseInner

AutofilledBy = Union[AutofilledByUs, AutofilledBySomethingElse]
class EnumWithManyVariantsAnonVariantInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `AnonVariant` of the `EnumWithManyVariants` Rust enum
    """
    uuid: str


class EnumWithManyVariantsAnotherAnonVariantInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `AnotherAnonVariant` of the `EnumWithManyVariants` Rust enum
    """
    uuid: str
    thing: int


class EnumWithManyVariantsTypes(str, Enum):
    UNIT_VARIANT = "UnitVariant"
    TUPLE_VARIANT_STRING = "TupleVariantString"
    ANON_VARIANT = "AnonVariant"
    TUPLE_VARIANT_INT = "TupleVariantInt"
    ANOTHER_UNIT_VARIANT = "AnotherUnitVariant"
    ANOTHER_ANON_VARIANT = "AnotherAnonVariant"

class EnumWithManyVariantsUnitVariant(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.UNIT_VARIANT

class EnumWithManyVariantsTupleVariantString(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.TUPLE_VARIANT_STRING
    content: str

class EnumWithManyVariantsAnonVariant(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.ANON_VARIANT
    content: EnumWithManyVariantsAnonVariantInner

class EnumWithManyVariantsTupleVariantInt(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.TUPLE_VARIANT_INT
    content: int

class EnumWithManyVariantsAnotherUnitVariant(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.ANOTHER_UNIT_VARIANT

class EnumWithManyVariantsAnotherAnonVariant(BaseModel):
    type: EnumWithManyVariantsTypes = EnumWithManyVariantsTypes.ANOTHER_ANON_VARIANT
    content: EnumWithManyVariantsAnotherAnonVariantInner

EnumWithManyVariants = Union[EnumWithManyVariantsUnitVariant, EnumWithManyVariantsTupleVariantString, EnumWithManyVariantsAnonVariant, EnumWithManyVariantsTupleVariantInt, EnumWithManyVariantsAnotherUnitVariant, EnumWithManyVariantsAnotherAnonVariant]
