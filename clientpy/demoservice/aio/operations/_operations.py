# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._utils.model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from ..._utils.serialization import Deserializer, Serializer
from ...operations._operations import (
    build_widgets_analyze_request,
    build_widgets_create_request,
    build_widgets_delete_request,
    build_widgets_list_request,
    build_widgets_read_request,
    build_widgets_update_request,
)
from .._configuration import DemoServiceClientConfiguration

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class WidgetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~demoservice.aio.DemoServiceClient`'s
        :attr:`widgets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: DemoServiceClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def list(self, **kwargs: Any) -> _models.WidgetList:
        """List widgets.

        :return: WidgetList. The WidgetList is compatible with MutableMapping
        :rtype: ~demoservice.models.WidgetList
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.WidgetList] = kwargs.pop("cls", None)

        _request = build_widgets_list_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.WidgetList, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def read(self, id: str, **kwargs: Any) -> _models.Widget:
        """Read widgets.

        :param id: Required.
        :type id: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Widget] = kwargs.pop("cls", None)

        _request = build_widgets_read_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Widget, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create(
        self, body: _models.Widget, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Widget:
        """Create a widget.

        :param body: Required.
        :type body: ~demoservice.models.Widget
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(self, body: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Widget:
        """Create a widget.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> _models.Widget:
        """Create a widget.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create(self, body: Union[_models.Widget, JSON, IO[bytes]], **kwargs: Any) -> _models.Widget:
        """Create a widget.

        :param body: Is one of the following types: Widget, JSON, IO[bytes] Required.
        :type body: ~demoservice.models.Widget or JSON or IO[bytes]
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Widget] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_widgets_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Widget, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self, id: str, body: _models.Widget, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Widget:
        """Update a widget.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: ~demoservice.models.Widget
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, id: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Widget:
        """Update a widget.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, id: str, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Widget:
        """Update a widget.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(self, id: str, body: Union[_models.Widget, JSON, IO[bytes]], **kwargs: Any) -> _models.Widget:
        """Update a widget.

        :param id: Required.
        :type id: str
        :param body: Is one of the following types: Widget, JSON, IO[bytes] Required.
        :type body: ~demoservice.models.Widget or JSON or IO[bytes]
        :return: Widget. The Widget is compatible with MutableMapping
        :rtype: ~demoservice.models.Widget
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Widget] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_widgets_update_request(
            id=id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Widget, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def delete(self, id: str, **kwargs: Any) -> None:
        """Delete a widget.

        :param id: Required.
        :type id: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_widgets_delete_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def analyze(self, id: str, **kwargs: Any) -> _models.AnalyzeResult:
        """Analyze a widget.

        :param id: Required.
        :type id: str
        :return: AnalyzeResult. The AnalyzeResult is compatible with MutableMapping
        :rtype: ~demoservice.models.AnalyzeResult
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.AnalyzeResult] = kwargs.pop("cls", None)

        _request = build_widgets_analyze_request(
            id=id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.Error, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.AnalyzeResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
