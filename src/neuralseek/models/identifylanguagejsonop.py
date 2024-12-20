"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IdentifyLanguageJSONRequestBodyTypedDict(TypedDict):
    r"""The request object."""

    input: NotRequired[str]
    r"""The input text to identify the language of"""


class IdentifyLanguageJSONRequestBody(BaseModel):
    r"""The request object."""

    input: Optional[str] = ""
    r"""The input text to identify the language of"""


class IdentifyLanguageJSONResponseBodyTypedDict(TypedDict):
    r"""Success"""

    language: NotRequired[str]
    r"""The 2-character language code of the identified language."""
    confidence: NotRequired[float]
    r"""The confidence of the language identification"""


class IdentifyLanguageJSONResponseBody(BaseModel):
    r"""Success"""

    language: Optional[str] = ""
    r"""The 2-character language code of the identified language."""

    confidence: Optional[float] = None
    r"""The confidence of the language identification"""
