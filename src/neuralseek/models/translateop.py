"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TranslateRequestBodyTypedDict(TypedDict):
    r"""The request object."""

    text: NotRequired[List[str]]
    r"""An array of input text to be translated"""
    model_id: NotRequired[str]
    r"""Convienence input for legacy connections. Define a traget language by setting a source to target relationship using 2-digit language codes, for example en-es to translate into spanish.  The source language is ignored. Either this or the target parameter is required."""
    target: NotRequired[str]
    r"""The 2-digit language code for the target language.  Either this or the model_id parameter is required."""
    llm_id: NotRequired[str]
    r"""Optional - Pass an llm card id to override the LLM used for translation"""
    max_chunk: NotRequired[int]
    r"""Optional - Pass a maximum translation chunk token size. This can help speed up translations in the 200-2000 word range when using slower LLM's.  Use a setting between 200 and 500 in these scenarios. Setting 0 or omitting this parameter unsets it."""
    additional_instructions: NotRequired[str]
    r"""Optional - Additional prompting to be passed to the LLM. Do not casusally use this field, you will break things."""


class TranslateRequestBody(BaseModel):
    r"""The request object."""

    text: Optional[List[str]] = None
    r"""An array of input text to be translated"""

    model_id: Optional[str] = ""
    r"""Convienence input for legacy connections. Define a traget language by setting a source to target relationship using 2-digit language codes, for example en-es to translate into spanish.  The source language is ignored. Either this or the target parameter is required."""

    target: Optional[str] = ""
    r"""The 2-digit language code for the target language.  Either this or the model_id parameter is required."""

    llm_id: Annotated[Optional[str], pydantic.Field(alias="llmId")] = ""
    r"""Optional - Pass an llm card id to override the LLM used for translation"""

    max_chunk: Annotated[Optional[int], pydantic.Field(alias="maxChunk")] = 0
    r"""Optional - Pass a maximum translation chunk token size. This can help speed up translations in the 200-2000 word range when using slower LLM's.  Use a setting between 200 and 500 in these scenarios. Setting 0 or omitting this parameter unsets it."""

    additional_instructions: Annotated[
        Optional[str], pydantic.Field(alias="additionalInstructions")
    ] = ""
    r"""Optional - Additional prompting to be passed to the LLM. Do not casusally use this field, you will break things."""


class TranslationsTypedDict(TypedDict):
    translation: NotRequired[str]
    r"""The translation"""


class Translations(BaseModel):
    translation: Optional[str] = ""
    r"""The translation"""


class TranslateResponseBodyTypedDict(TypedDict):
    r"""Success"""

    word_count: NotRequired[int]
    r"""The word count."""
    character_count: NotRequired[int]
    r"""The word count."""
    detected_language: NotRequired[str]
    r"""The 2-digit language code for the detected language."""
    detected_language_confidence: NotRequired[float]
    r"""The detected language confidence."""
    translation_glossary: NotRequired[bool]
    r"""Returns true if a glossary is loaded and matched any input."""
    translation_glossary_exact: NotRequired[bool]
    r"""Returns true if a glossary is loaded and an entry exactly matched the input."""
    translations: NotRequired[List[TranslationsTypedDict]]


class TranslateResponseBody(BaseModel):
    r"""Success"""

    word_count: Optional[int] = None
    r"""The word count."""

    character_count: Optional[int] = None
    r"""The word count."""

    detected_language: Optional[str] = ""
    r"""The 2-digit language code for the detected language."""

    detected_language_confidence: Optional[float] = None
    r"""The detected language confidence."""

    translation_glossary: Optional[bool] = None
    r"""Returns true if a glossary is loaded and matched any input."""

    translation_glossary_exact: Optional[bool] = None
    r"""Returns true if a glossary is loaded and an entry exactly matched the input."""

    translations: Optional[List[Translations]] = None
