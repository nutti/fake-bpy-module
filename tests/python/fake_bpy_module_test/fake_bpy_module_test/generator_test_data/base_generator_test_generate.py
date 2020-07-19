import sys
import typing
import os
import module_2
from .submodule_2 import (ClassZ)

from . import submodule_1


class BaseClassA:
    ''' BaseClassA description
    '''

    pass


class BaseClassB:
    ''' BaseClassB description
    '''

    pass


class ClassA(BaseClassB, BaseClassA):
    ''' ClassA description
    '''

    attr_1: typing.Union[str, typing.Set['custom_data_type']] = None
    ''' attr_1 description

    :type: typing.Union[str, typing.Set['custom_data_type']]
    '''

    def method_1(self, param_1: int):
        ''' method_1 description

        :param param_1: param_1 description
        :type param_1: int
        '''
        pass


def function_1(param_1: int = 10, param_2: typing.List['ClassA']) -> bool:
    ''' function_1 description

    :param param_1: param_1 description
    :type param_1: int
    :param param_2: param_2 description
    :type param_2: typing.List['ClassA']
    :return: return description
    '''

    pass


constant_1: int = None
''' constant_1 description
'''
