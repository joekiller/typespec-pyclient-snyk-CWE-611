# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, List, Literal, Mapping, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class AnalyzeResult(_Model):
    """AnalyzeResult.

    :ivar id: Required.
    :vartype id: str
    :ivar analysis: Required.
    :vartype analysis: str
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    analysis: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        analysis: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Error(_Model):
    """Error.

    :ivar code: Required.
    :vartype code: int
    :ivar message: Required.
    :vartype message: str
    """

    code: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    message: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        code: int,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Widget(_Model):
    """Widget.

    :ivar id: Required.
    :vartype id: str
    :ivar weight: Required.
    :vartype weight: int
    :ivar color: Required. Is either a Literal["red"] type or a Literal["blue"] type.
    :vartype color: str or str
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    weight: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    color: Literal["red", "blue"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required. Is either a Literal[\"red\"] type or a Literal[\"blue\"] type."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        weight: int,
        color: Literal["red", "blue"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class WidgetList(_Model):
    """WidgetList.

    :ivar items_property: Required.
    :vartype items_property: list[~demoservice.models.Widget]
    """

    items_property: List["_models.Widget"] = rest_field(
        name="items", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        items_property: List["_models.Widget"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
