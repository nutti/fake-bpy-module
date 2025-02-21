import typing
import collections.abc
import typing_extensions
import numpy.typing as npt


def function_1(arg_1: float, arg_2: str = "test", arg_3: int = 1234) -> str:
    """function_1 description

    :param arg_1: function_1 arg_1 description
    :type arg_1: float
    :param arg_2: function_1 arg_2 description
    :type arg_2: str
    :param arg_3: function_1 arg_3 description
    :type arg_3: int
    :return: function_1 return description
    :rtype: str
    """


def function_2() -> str | None:
    """

    :return: function_2 return description
    :rtype: str | None
    """


def function_3[_GenericType1]() -> _GenericType1:
    """

    :return: function_3 return description
    :rtype: _GenericType1
    """
