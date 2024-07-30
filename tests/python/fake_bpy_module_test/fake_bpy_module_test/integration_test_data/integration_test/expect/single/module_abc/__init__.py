import typing
import collections.abc
import typing_extensions

_GenericType1 = typing.TypeVar("_GenericType1")
_GenericType2 = typing.TypeVar("_GenericType2")


class Class123:
    """Class123 description"""

    attr_1: float = None
    """ attr_1 description

    :type: float
    """

    def method_1(self) -> int:
        """method_1 description

        :return: method_1 return description
        :rtype: int
        """
