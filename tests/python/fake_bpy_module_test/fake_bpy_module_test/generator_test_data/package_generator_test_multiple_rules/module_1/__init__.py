import sys
import typing
from . import submodule_1


class ClassA(submodule_1.BaseClass1):
    ''' ClassA description
    '''

    attr_1: str = None
    ''' attr_1 description

    :type: str
    '''

    def method_1(self, arg_1: float = 5.4) -> int:
        ''' method_1 description

        :param arg_1: method_1 arg_1 description
        :type arg_1: float
        :rtype: int
        :return: method_1 return description
        '''
        pass
