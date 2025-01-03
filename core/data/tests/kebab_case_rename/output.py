from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class Things(BaseModel):
    """
    This is a comment.
    """
    model_config = ConfigDict(populate_by_name=True)

    bla: str
    some_label: Optional[str] = Field(alias="label", default=None)
    label_left: Optional[str] = Field(alias="label-left", default=None)

