"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SlotsTypedDict(TypedDict):
    r"""Provide an object of variable names, with a type property set to an entity type to match to in total across multiple turns of a conversation. NeuralSeek will return a promptEntity to display to the user to continue to fil the slots.  As slots are filled the value field will be populated.  Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""


class Slots(BaseModel):
    r"""Provide an object of variable names, with a type property set to an entity type to match to in total across multiple turns of a conversation. NeuralSeek will return a promptEntity to display to the user to continue to fil the slots.  As slots are filled the value field will be populated.  Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""


class ExtractEntitiesRequestBodyTypedDict(TypedDict):
    r"""The request object."""

    text: NotRequired[str]
    r"""The text to extract entitites from"""
    language: NotRequired[str]
    r"""The 2-char language code to be used when generating a promptEntity response. Only set this if you want to override the configured language in NeuralSeek."""
    entities: NotRequired[str]
    r"""An array of objects, stringified. The properties of the object are name, description, and format"""
    slots: NotRequired[SlotsTypedDict]
    r"""Provide an object of variable names, with a type property set to an entity type to match to in total across multiple turns of a conversation. NeuralSeek will return a promptEntity to display to the user to continue to fil the slots.  As slots are filled the value field will be populated.  Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""
    confirm_slots: NotRequired[bool]
    r"""When using Slots, once all slots have been filled display a summary and ask for a confirmation before setting the 'complete' flag"""
    confirm_every_slot: NotRequired[bool]
    r"""When using Slots, on every turn recite the slot that was just previously filled."""


class ExtractEntitiesRequestBody(BaseModel):
    r"""The request object."""

    text: Optional[str] = None
    r"""The text to extract entitites from"""

    language: Optional[str] = None
    r"""The 2-char language code to be used when generating a promptEntity response. Only set this if you want to override the configured language in NeuralSeek."""

    entities: Optional[str] = None
    r"""An array of objects, stringified. The properties of the object are name, description, and format"""

    slots: Optional[Slots] = None
    r"""Provide an object of variable names, with a type property set to an entity type to match to in total across multiple turns of a conversation. NeuralSeek will return a promptEntity to display to the user to continue to fil the slots.  As slots are filled the value field will be populated.  Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""

    confirm_slots: Annotated[Optional[bool], pydantic.Field(alias="confirmSlots")] = (
        None
    )
    r"""When using Slots, once all slots have been filled display a summary and ask for a confirmation before setting the 'complete' flag"""

    confirm_every_slot: Annotated[
        Optional[bool], pydantic.Field(alias="confirmEverySlot")
    ] = None
    r"""When using Slots, on every turn recite the slot that was just previously filled."""


class ExtractedEntitiesTypedDict(TypedDict):
    entity: NotRequired[str]
    r"""The found entity"""


class ExtractedEntities(BaseModel):
    entity: Optional[str] = ""
    r"""The found entity"""


class ExtractEntitiesSlotsTypedDict(TypedDict):
    r"""If the slots parameter is filled on the input, NeuralSeek will return it and begin filling the value fields. Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""


class ExtractEntitiesSlots(BaseModel):
    r"""If the slots parameter is filled on the input, NeuralSeek will return it and begin filling the value fields. Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""


class ExtractEntitiesResponseBodyTypedDict(TypedDict):
    r"""Success"""

    extracted_entities: NotRequired[List[ExtractedEntitiesTypedDict]]
    complete: NotRequired[bool]
    r"""If slots are passed, complete will be set to true when all slots are filled"""
    prompt_entity: NotRequired[str]
    r"""A message to display to the user asking them to provide input for the next group of unfilled slots."""
    slots: NotRequired[ExtractEntitiesSlotsTypedDict]
    r"""If the slots parameter is filled on the input, NeuralSeek will return it and begin filling the value fields. Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""


class ExtractEntitiesResponseBody(BaseModel):
    r"""Success"""

    extracted_entities: Annotated[
        Optional[List[ExtractedEntities]], pydantic.Field(alias="extractedEntities")
    ] = None

    complete: Optional[bool] = False
    r"""If slots are passed, complete will be set to true when all slots are filled"""

    prompt_entity: Annotated[Optional[str], pydantic.Field(alias="promptEntity")] = None
    r"""A message to display to the user asking them to provide input for the next group of unfilled slots."""

    slots: Optional[ExtractEntitiesSlots] = None
    r"""If the slots parameter is filled on the input, NeuralSeek will return it and begin filling the value fields. Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled"""
