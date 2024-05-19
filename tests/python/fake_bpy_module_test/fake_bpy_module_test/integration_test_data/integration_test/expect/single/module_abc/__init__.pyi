import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class Class123:
    """Class123 description"""

    attr_1: float
    """ attr_1 description

    :type: float
    """

    def method_1(self) -> int:
        """method_1 description

        :return: method_1 return description
        :rtype: int
        """
        ...
