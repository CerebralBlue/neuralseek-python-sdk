"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from neuralseek.types import BaseModel
from neuralseek.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MaistroParamsTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The parameter name"""
    value: NotRequired[str]
    r"""The parameter value"""


class MaistroParams(BaseModel):
    name: Optional[str] = ""
    r"""The parameter name"""

    value: Optional[str] = ""
    r"""The parameter value"""


class MaistroLastTurnTypedDict(TypedDict):
    input: NotRequired[str]
    r"""The user input"""
    response: NotRequired[str]
    r"""The system response.  Text strings only here."""


class MaistroLastTurn(BaseModel):
    input: Optional[str] = ""
    r"""The user input"""

    response: Optional[str] = ""
    r"""The system response.  Text strings only here."""


class MaistroOptionsTypedDict(TypedDict):
    r"""Override options"""

    streaming: NotRequired[bool]
    r"""Return the response via SSE streaming.  This is not compatible with most Virtual Agent platforms, and is intentded for direct website use."""
    llm: NotRequired[str]
    r"""Override the LLM load balancer and force seek to use a specific LLM.  Input the LLM code here.  You must have a valid model card set up on the configure tab for the code you input."""
    user_id: NotRequired[str]
    r"""Set the user_id. Useful and required if you have a corporate document filter set"""
    timeout: NotRequired[float]
    r"""Timeout in miliseconds. (optional)"""
    temperature_mod: NotRequired[float]
    r"""Shift the model's baseline temperature weighting by a percentage"""
    topp_mod: NotRequired[float]
    r"""Shift the model's baseline probability weighting by a percentage"""
    freqpenalty_mod: NotRequired[float]
    r"""Shift the model's baseline frequency penalty weighting by a percentage"""
    min_tokens: NotRequired[float]
    r"""Set the minimum tokens you  want the model to produce"""
    max_tokens: NotRequired[float]
    r"""Set the maximum tokens you  want the model to produce"""
    last_turn: NotRequired[List[MaistroLastTurnTypedDict]]
    r"""lastTurn is a flexible object. It is backwards compatible with the original single turn object, as well as compatible with the Watson Assistant session history format."""
    return_variables: NotRequired[bool]
    r"""Return the final state of all variables in a dense object"""
    return_variables_expanded: NotRequired[bool]
    r"""Return the final state of all variables in the same format as the input params"""
    return_render: NotRequired[bool]
    r"""Return the midstate renders"""
    return_source: NotRequired[bool]
    r"""Return the source parts"""
    max_recursion: NotRequired[int]
    r"""The maximum number of recursive calls to Explore.  Use caution that you have not created an endless loop as you increase the maximum, as each Explore is charged."""


class MaistroOptions(BaseModel):
    r"""Override options"""

    streaming: Optional[bool] = False
    r"""Return the response via SSE streaming.  This is not compatible with most Virtual Agent platforms, and is intentded for direct website use."""

    llm: Optional[str] = ""
    r"""Override the LLM load balancer and force seek to use a specific LLM.  Input the LLM code here.  You must have a valid model card set up on the configure tab for the code you input."""

    user_id: Optional[str] = ""
    r"""Set the user_id. Useful and required if you have a corporate document filter set"""

    timeout: Optional[float] = None
    r"""Timeout in miliseconds. (optional)"""

    temperature_mod: Annotated[
        Optional[float], pydantic.Field(alias="temperatureMod")
    ] = None
    r"""Shift the model's baseline temperature weighting by a percentage"""

    topp_mod: Annotated[Optional[float], pydantic.Field(alias="toppMod")] = None
    r"""Shift the model's baseline probability weighting by a percentage"""

    freqpenalty_mod: Annotated[
        Optional[float], pydantic.Field(alias="freqpenaltyMod")
    ] = None
    r"""Shift the model's baseline frequency penalty weighting by a percentage"""

    min_tokens: Annotated[Optional[float], pydantic.Field(alias="minTokens")] = None
    r"""Set the minimum tokens you  want the model to produce"""

    max_tokens: Annotated[Optional[float], pydantic.Field(alias="maxTokens")] = None
    r"""Set the maximum tokens you  want the model to produce"""

    last_turn: Annotated[
        Optional[List[MaistroLastTurn]], pydantic.Field(alias="lastTurn")
    ] = None
    r"""lastTurn is a flexible object. It is backwards compatible with the original single turn object, as well as compatible with the Watson Assistant session history format."""

    return_variables: Annotated[
        Optional[bool], pydantic.Field(alias="returnVariables")
    ] = False
    r"""Return the final state of all variables in a dense object"""

    return_variables_expanded: Annotated[
        Optional[bool], pydantic.Field(alias="returnVariablesExpanded")
    ] = False
    r"""Return the final state of all variables in the same format as the input params"""

    return_render: Annotated[Optional[bool], pydantic.Field(alias="returnRender")] = (
        False
    )
    r"""Return the midstate renders"""

    return_source: Annotated[Optional[bool], pydantic.Field(alias="returnSource")] = (
        False
    )
    r"""Return the source parts"""

    max_recursion: Annotated[Optional[int], pydantic.Field(alias="maxRecursion")] = 10
    r"""The maximum number of recursive calls to Explore.  Use caution that you have not created an endless loop as you increase the maximum, as each Explore is charged."""


class MaistroRequestBodyTypedDict(TypedDict):
    r"""The request object."""

    ntl: NotRequired[str]
    r"""The NTL script to evaluate.  Include either this or agent - not both"""
    agent: NotRequired[str]
    r"""The agent to use. Include either this or NTL"""
    params: NotRequired[List[MaistroParamsTypedDict]]
    r"""An array of parameters to use in evaluation of the NTL"""
    options: NotRequired[MaistroOptionsTypedDict]
    r"""Override options"""


class MaistroRequestBody(BaseModel):
    r"""The request object."""

    ntl: Optional[str] = ""
    r"""The NTL script to evaluate.  Include either this or agent - not both"""

    agent: Optional[str] = ""
    r"""The agent to use. Include either this or NTL"""

    params: Optional[List[MaistroParams]] = None
    r"""An array of parameters to use in evaluation of the NTL"""

    options: Optional[MaistroOptions] = None
    r"""Override options"""


class MaistroRequestTypedDict(TypedDict):
    request_body: MaistroRequestBodyTypedDict
    r"""The request object."""
    overrideschema: NotRequired[str]
    r"""Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate"""
    overrideagent: NotRequired[str]
    r"""If using overrideSchema you must pass your agent name here. All other POST options will be ignored."""
    debug: NotRequired[str]
    r"""Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate"""


class MaistroRequest(BaseModel):
    request_body: Annotated[
        MaistroRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""The request object."""

    overrideschema: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = ""
    r"""Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate"""

    overrideagent: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = ""
    r"""If using overrideSchema you must pass your agent name here. All other POST options will be ignored."""

    debug: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = ""
    r"""Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate"""


class VarsTypedDict(TypedDict):
    r"""The variable values"""


class Vars(BaseModel):
    r"""The variable values"""


class RenderTypedDict(TypedDict):
    node: NotRequired[str]
    r"""The node type"""
    vars: NotRequired[VarsTypedDict]
    r"""The variable values"""
    out: NotRequired[str]
    r"""The output"""
    chained: NotRequired[bool]
    r"""True if the step is chained"""


class Render(BaseModel):
    node: Optional[str] = ""
    r"""The node type"""

    vars: Optional[Vars] = None
    r"""The variable values"""

    out: Optional[str] = ""
    r"""The output"""

    chained: Optional[bool] = None
    r"""True if the step is chained"""


class MaistroVariablesTypedDict(TypedDict):
    r"""The returned variable."""


class MaistroVariables(BaseModel):
    r"""The returned variable."""


class MaistroVariablesExpandedTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The variable name"""
    value: NotRequired[str]
    r"""The variable value"""


class MaistroVariablesExpanded(BaseModel):
    name: Optional[str] = ""
    r"""The variable name"""

    value: Optional[str] = ""
    r"""The variable value"""


class MaistroResponseBodyTypedDict(TypedDict):
    r"""Success"""

    answer: NotRequired[str]
    r"""The generated response"""
    source_parts: NotRequired[List[str]]
    render: NotRequired[List[RenderTypedDict]]
    r"""The steps used to render the result."""
    variables: NotRequired[MaistroVariablesTypedDict]
    r"""The returned variable."""
    variables_expanded: NotRequired[List[MaistroVariablesExpandedTypedDict]]
    r"""The returned variable, in the format of the input params"""


class MaistroResponseBody(BaseModel):
    r"""Success"""

    answer: Optional[str] = ""
    r"""The generated response"""

    source_parts: Annotated[
        Optional[List[str]], pydantic.Field(alias="sourceParts")
    ] = None

    render: Optional[List[Render]] = None
    r"""The steps used to render the result."""

    variables: Optional[MaistroVariables] = None
    r"""The returned variable."""

    variables_expanded: Annotated[
        Optional[List[MaistroVariablesExpanded]],
        pydantic.Field(alias="variablesExpanded"),
    ] = None
    r"""The returned variable, in the format of the input params"""
