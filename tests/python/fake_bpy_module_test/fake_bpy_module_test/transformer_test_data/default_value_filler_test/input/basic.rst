.. module:: module_1


.. function:: builtin(arg_bool, arg_str, arg_bytes, arg_float, arg_int, arg_list, arg_dict, arg_set, arg_tuple)

   :type arg_bool: bool
   :option arg arg_bool: optional
   :type arg_str: str
   :option arg arg_str: optional
   :type arg_bytes: bytes
   :option arg arg_bytes: optional
   :type arg_float: float
   :option arg arg_float: optional
   :type arg_int: int
   :option arg arg_int: optional
   :type arg_list: list
   :option arg arg_list: optional
   :type arg_dict: dict
   :option arg arg_dict: optional
   :type arg_set: set
   :option arg arg_set: optional
   :type arg_tuple: tuple
   :option arg arg_tuple: optional

.. function:: modifier(arg_list, arg_dict, arg_set, arg_tuple, arg_generic, arg_iterator, arg_callable, arg_any, arg_sequence)

   :type arg_list: list[int]
   :option arg arg_list: optional
   :type arg_dict: dict[str, int]
   :option arg arg_dict: optional
   :type arg_set: set[int]
   :option arg arg_set: optional
   :type arg_tuple: tuple[int, float, int]
   :option arg arg_tuple: optional
   :type arg_generic: Generic[Type]
   :option arg arg_generic: optional
   :type arg_iterator: collections.abc.Iterator
   :option arg arg_iterator: optional
   :type arg_callable: typing.Callable
   :option arg arg_callable: optional
   :type arg_any: typing.Any
   :option arg arg_any: optional
   :type arg_sequence: collections.abc.Sequence[int]
   :option arg arg_sequence: optional
