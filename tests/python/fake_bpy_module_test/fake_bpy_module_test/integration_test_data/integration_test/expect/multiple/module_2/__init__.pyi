import typing
import collections.abc
import typing_extensions
import module_1
import module_1.submodule_1

_GenericType1 = typing.TypeVar("_GenericType1")
_GenericType2 = typing.TypeVar("_GenericType2")

def function_1(arg_1: int, arg_2: module_1.ClassA) -> module_1.submodule_1.BaseClass1:
    """function_1 description

    :param arg_1: function_1 arg_1 description
    :type arg_1: int
    :param arg_2: function_1 arg_2 description
    :type arg_2: module_1.ClassA
    :return: method_1 return description
    :rtype: module_1.submodule_1.BaseClass1
    """
