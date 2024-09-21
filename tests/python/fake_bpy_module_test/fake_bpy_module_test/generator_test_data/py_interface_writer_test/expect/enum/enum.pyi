import typing
import collections.abc
import typing_extensions

_GenericType1 = typing.TypeVar("_GenericType1")
_GenericType2 = typing.TypeVar("_GenericType2")
type EnumA = typing.Literal[
    "ENUM_ITEM_1",  # ENUM_ITEM_1 description
]
