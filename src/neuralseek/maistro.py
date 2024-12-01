"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from neuralseek import models, utils
from neuralseek._hooks import HookContext
from neuralseek.types import BaseModel, OptionalNullable, UNSET
from neuralseek.utils import eventstreaming, get_security_from_env
from typing import Optional, Union, cast


class Maistro(BaseSDK):
    def execute(
        self,
        *,
        request_body: Union[
            models.MaistroRequestBody, models.MaistroRequestBodyTypedDict
        ],
        overrideschema: Optional[str] = "",
        templatename: Optional[str] = "",
        debug: Optional[str] = "",
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.MaistroResponseBody:
        r"""Run mAistro NTL or template

        Freeform prompting using NeuralSeek Template Language

        :param request_body: The request object.
        :param overrideschema: Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate
        :param templatename: If using overrideSchema you must pass your template name here. All other POST options will be ignored.
        :param debug: Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.MaistroRequest(
            overrideschema=overrideschema,
            templatename=templatename,
            debug=debug,
            request_body=utils.get_pydantic_model(
                request_body, models.MaistroRequestBody
            ),
        )

        req = self.build_request(
            method="POST",
            path="/maistro",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body, False, False, "json", models.MaistroRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="maistro",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.MaistroResponseBody)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def execute_async(
        self,
        *,
        request_body: Union[
            models.MaistroRequestBody, models.MaistroRequestBodyTypedDict
        ],
        overrideschema: Optional[str] = "",
        templatename: Optional[str] = "",
        debug: Optional[str] = "",
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.MaistroResponseBody:
        r"""Run mAistro NTL or template

        Freeform prompting using NeuralSeek Template Language

        :param request_body: The request object.
        :param overrideschema: Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate
        :param templatename: If using overrideSchema you must pass your template name here. All other POST options will be ignored.
        :param debug: Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.MaistroRequest(
            overrideschema=overrideschema,
            templatename=templatename,
            debug=debug,
            request_body=utils.get_pydantic_model(
                request_body, models.MaistroRequestBody
            ),
        )

        req = self.build_request_async(
            method="POST",
            path="/maistro",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body, False, False, "json", models.MaistroRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="maistro",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.MaistroResponseBody)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def stream(
        self,
        *,
        request: Union[
            models.MaistroStreamRequestBody, models.MaistroStreamRequestBodyTypedDict
        ] = models.MaistroStreamRequestBody(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> eventstreaming.EventStream[models.MaistroStreamResponseBody]:
        r"""Stream mAIstro NTL or a template

        Freeform prompting using NeuralSeek Template Language

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.MaistroStreamRequestBody)
        request = cast(models.MaistroStreamRequestBody, request)

        req = self.build_request(
            method="POST",
            path="/maistro_stream",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="text/event-stream",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.MaistroStreamRequestBody]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="maistro_stream",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "text/event-stream"):
            return eventstreaming.EventStream(
                http_res,
                lambda raw: utils.unmarshal_json(raw, models.MaistroStreamResponseBody),
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def stream_async(
        self,
        *,
        request: Union[
            models.MaistroStreamRequestBody, models.MaistroStreamRequestBodyTypedDict
        ] = models.MaistroStreamRequestBody(),
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> eventstreaming.EventStreamAsync[models.MaistroStreamResponseBody]:
        r"""Stream mAIstro NTL or a template

        Freeform prompting using NeuralSeek Template Language

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.MaistroStreamRequestBody)
        request = cast(models.MaistroStreamRequestBody, request)

        req = self.build_request_async(
            method="POST",
            path="/maistro_stream",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="text/event-stream",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, True, "json", Optional[models.MaistroStreamRequestBody]
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="maistro_stream",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "text/event-stream"):
            return eventstreaming.EventStreamAsync(
                http_res,
                lambda raw: utils.unmarshal_json(raw, models.MaistroStreamResponseBody),
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
