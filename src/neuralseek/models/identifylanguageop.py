"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ResponseBodyTypedDict(TypedDict):
    language: NotRequired[str]
    r"""The 2-character language code of the identified language."""
    confidence: NotRequired[float]
    r"""The confidence of the language identification."""


class ResponseBody(BaseModel):
    language: Optional[str] = ""
    r"""The 2-character language code of the identified language."""

    confidence: Optional[float] = None
    r"""The confidence of the language identification."""
