import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ClassA:
    """ClassA description"""

    attr_1: float
    """ attr_1 description

    :type: float
    """

    data_1: int
    """ data_1 description

    :type: int
    """

    def method_1(self, arg_1: float, arg_2: str = "test") -> str:
        """method_1 description

        :param arg_1: method_1 arg_1 description
        :type arg_1: float
        :param arg_2: method_1 arg_2 description
        :type arg_2: str
        :return: method_1 return description
        :rtype: str
        """

    @classmethod
    def classmethod_1(cls, arg_1: float, arg_2: int = 123) -> str:
        """classmethod_1 description

        :param arg_1: classmethod_1 arg_1 description
        :type arg_1: float
        :param arg_2: classmethod_1 arg_2 description
        :type arg_2: int
        :return: classmethod_1 return description
        :rtype: str
        """

    @staticmethod
    def staticmethod_1(arg_1: float, arg_2: tuple = (0, 0)) -> str:
        """staticmethod_1 description

        :param arg_1: staticmethod_1 arg_1 description
        :type arg_1: float
        :param arg_2: staticmethod_1 arg_2 description
        :type arg_2: tuple
        :return: staticmethod_1 return description
        :rtype: str
        """

    @typing.overload
    def function_1(self, arg_1: float, arg_2: int) -> str | None:
        """function_1 description

        :param arg_1: function_1 arg_1 description
        :type arg_1: float
        :param arg_2: function_1 arg_2 description
        :type arg_2: int
        :return: function_1 return description
        :rtype: str | None
        """

class ClassB[_GenericType1]:
    """ClassB description"""

    attr_1: _GenericType1
    """ attr_1 description

    :type: _GenericType1
    """

    def method_1[_GenericType2](
        self, arg_1: _GenericType1, arg_2: _GenericType2
    ) -> _GenericType2:
        """method_1 description

        :param arg_1: method_1 arg_1 description
        :type arg_1: _GenericType1
        :param arg_2: method_1 arg_2 description
        :type arg_2: _GenericType2
        :return: method_1 return description
        :rtype: _GenericType2
        """
