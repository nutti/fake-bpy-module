import typing
import collections.abc
import typing_extensions
import numpy.typing as npt


class ClassExp:
    """ClassExp description"""

    attr: float = None
    """ attr description"""

    def method_with_keyword_only_argument(
        self, arg_1: float, arg_2: float = 5.0, arg_3: int | None = None
    ) -> int:
        """method_with_keyword_only_argument description

        :param arg_1: method_with_keyword_only_argument arg_1 description
        :param arg_2: method_with_keyword_only_argument arg_2 description
        :param arg_3: method_with_keyword_only_argument arg_3 description
        :return: method_with_keyword_only_argument return description
        """


def function_with_type_hint(arg_1: float, arg_2: bool) -> int:
    """function_with_type_hint description

    :param arg_1: function_with_type_hint arg_1 description
    :param arg_2: function_with_type_hint arg_2 description
    :return: function_with_type_hint return description
    """
