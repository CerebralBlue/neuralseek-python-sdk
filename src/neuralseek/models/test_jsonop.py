"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TestJSONRequestBodyTypedDict(TypedDict):
    r"""The questions csv.  Must adhere to the template https://api.neuralseek.com/q.csv After upload you will receive a 202 response and the server will begin processing.  Check for your completed results on the getTestResults endpoint."""

    __test__ = False  # pyright: ignore[reportGeneralTypeIssues]

    proposal_id: NotRequired[str]
    r"""An optional Proposal ID to use for the test"""


class TestJSONRequestBody(BaseModel):
    r"""The questions csv.  Must adhere to the template https://api.neuralseek.com/q.csv After upload you will receive a 202 response and the server will begin processing.  Check for your completed results on the getTestResults endpoint."""

    __test__ = False

    proposal_id: Annotated[Optional[str], pydantic.Field(alias="proposalID")] = ""
    r"""An optional Proposal ID to use for the test"""
