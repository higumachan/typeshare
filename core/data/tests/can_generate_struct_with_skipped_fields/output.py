from __future__ import annotations

from pydantic import BaseModel


class MyStruct(BaseModel):
    a: int
    c: int
