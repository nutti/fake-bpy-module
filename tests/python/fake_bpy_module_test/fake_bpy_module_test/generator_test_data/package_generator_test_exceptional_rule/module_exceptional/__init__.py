import sys
import typing

GenericType = typing.TypeVar("GenericType")


class ClassExp:
    """ClassExp description"""

    attr: float = None
    """ attr description

    :type: float
    """

    def method_with_keyword_only_argument(
        self, arg_1: float, arg_2: float = 5.0, arg_3: int = None
    ) -> int:
        """method_with_keyword_only_argument description

        :param arg_1: method_with_keyword_only_argument arg_1 description
        :type arg_1: float
        :param arg_2: method_with_keyword_only_argument arg_2 description
        :type arg_2: float
        :param arg_3: method_with_keyword_only_argument arg_3 description
        :type arg_3: int
        :rtype: int
        :return: method_with_keyword_only_argument return description
        """
        pass


def function_with_type_hint(arg_1: float, arg_2: bool) -> int:
    """function_with_type_hint description

    :param arg_1: function_with_type_hint arg_1 description
    :type arg_1: float
    :param arg_2: function_with_type_hint arg_2 description
    :type arg_2: bool
    :rtype: int
    :return: function_with_type_hint return description
    """

    pass
