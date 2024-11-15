"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel
from typing import Literal, Union


"""
The associated String contains some opaque context
"""
class SomeEnumContext(BaseModel):
    SomeEnumTypes: Literal["Context"] = "Context"
    content: str

class SomeEnumOther(BaseModel):
    SomeEnumTypes: Literal["Other"] = "Other"
    content: int

SomeEnum = Union[SomeEnumContext, SomeEnumOther]
