import typing
import os
import module_2
from .submodule_2 import ClassZ

from . import submodule_1

GenericType = typing.TypeVar("GenericType")

class BaseClassA:
    """BaseClassA description"""

    ...

class BaseClassB:
    """BaseClassB description"""

    ...

class ClassA(BaseClassB, BaseClassA):
    """ClassA description"""

    attr_1: typing.Union[str, typing.Set["custom_data_type"]]
    """ attr_1 description

    :type: typing.Union[str, typing.Set['custom_data_type']]
    """

    def method_1(self, param_1: int):
        """method_1 description

        :param param_1: param_1 description
        :type param_1: int
        """
        ...

def function_1(
    param_1: int = 10,
    param_2: typing.List["ClassA"] = [],
    param_3: typing.Optional[float] = 4.5,
) -> bool:
    """function_1 description

    :param param_1: param_1 description
    :type param_1: int
    :param param_2: param_2 description
    :type param_2: typing.List['ClassA']
    :param param_3: param_3 description
    :type param_3: typing.Optional[float]
    :rtype: bool
    :return: return description
    """

    ...

constant_1: int
""" constant_1 description
"""
