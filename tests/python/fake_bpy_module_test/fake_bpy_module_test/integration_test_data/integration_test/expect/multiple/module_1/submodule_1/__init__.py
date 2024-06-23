import typing
import collections.abc
import typing_extensions

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")


class BaseClass1:
    """BaseClass1 description"""

    attr_1: float = None
    """ attr_1 description

    :type: float
    """

    def method_1(self) -> int:
        """method_1 description

        :return: method_1 return description
        :rtype: int
        """
        pass


def function_1(arg_1: float, arg_2: bool):
    """function_1 description

    :param arg_1: function_1 arg_1 description
    :type arg_1: float
    :param arg_2: function_1 arg_2 description
    :type arg_2: bool
    """

    pass


DATA_1: str = None
""" DATA_1 description
"""
