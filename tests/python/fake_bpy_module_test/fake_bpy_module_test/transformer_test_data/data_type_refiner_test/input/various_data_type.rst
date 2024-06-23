.. module:: module_1


.. data:: data_space

   :type:  

.. data:: data_list_of_callable

   :type: list of callable[:class:`RefinedClassA`]

.. class:: ClassA

   .. attribute:: attr_self_type

      :type: Same type with self class

.. data:: data_type

   :type: type

.. data:: data_object

   :type: object

.. data:: data_function

   :type: function

.. data:: data_function_prototype

   :type: Depends on function prototype

.. data:: data_any_type_1

   :type: :class:`AnyType`

.. data:: data_any_type_2

   :type: any

.. data:: data_any_type_3

   :type: Any type.

.. data:: data_d_vector

   :type: 2d vector

.. data:: data_4x4_matrix

   :type: 4x4 :class:`Matrix`

.. data:: data_4x4_mathutils_matrix

   :type: 4x4 :class:`mathutils.Matrix`

.. data:: data_enum_in_default

   :type: enum in ['ONE', 'TWO'], default 'ONE'

.. data:: data_enum_in

   :type: enum in ['ONE', 'TWO']

.. data:: data_set_in

   :type: enum set in {'ONE', 'TWO'}

.. data:: data_enum_set_in_rna

   :type: enum set in :ref:`rna_enum`

.. data:: data_enum_in_rna

   :type: enum in :ref:`rna_enum`

.. data:: data_enumerated_constant

   :type: Enumerated constant

.. data:: data_boolean_default

   :type: boolean, default False

.. data:: data_boolean_array_of

   :type: boolean array of 3 items

.. function:: function_1(arg_boolean_array_of)

   :type arg_boolean_array_of: boolean array of 3 items

.. data:: data_boolean

   :type: boolean

.. data:: data_bool

   :type: bool

.. data:: data_bytes

   :type: bytes

.. data:: data_byte_sequence

   :type: byte sequence

.. data:: data_callable

   :type: callable

.. data:: data_mathutils_values

   :type: :class:`mathutils.Vector`

.. data:: data_number_array_of

   :type: int array of 2 items in [-32768, 32767], default (0, 0)

.. function:: function_1(arg_number_array_of)

   :type arg_number_array_of: float array of 2 items in [-1.0, 1.0], default (0.0, 0.0)

.. data:: data_mathutils_array_of

   :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

.. data:: data_float_triplet

   :type: float triplet

.. data:: data_number_in

   :type: int in [-inf, inf], default 0

.. data:: data_int

   :type: int

.. data:: data_float

   :type: float

.. data:: data_unsigned_int

   :type: unsigned int

.. data:: data_int_boolean

   :type: int (boolean)

.. data:: data_int_sequence

   :type: int sequence

.. data:: data_float_multi_dimensional_array_of

   :type: float multi-dimensional array of 3 * 3 items in [-inf, inf]

.. data:: data_mathutils_matrix_of

   :type: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf]

.. data:: data_double

   :type: double

.. data:: data_double_float

   :type: double (float)

.. data:: data_string

   :type: string

.. data:: data_integer

   :type: integer

.. data:: data_tuple

   :type: tuple

.. data:: data_sequence

   :type: sequence

.. data:: data_bgl_buffer

   :type: :class:`bgl.Buffer` type

.. data:: data_value_bpy_prop_collection_of

   :type: :class:`RefinedClassA` :class:`bpy_prop_collection` of :class:`ClassA`, 

.. data:: data_set_of_strings

   :type: set of strings

.. data:: data_sequence_of_string_tuples_or_a_function

   :type: sequence of string tuples or a function

.. data:: data_sequence_of

   :type: sequence of :class:`RefinedClassA`

.. data:: data_bpy_prop_collection_of

   :type: :class:`bpy_prop_collection` of :class:`RefinedClassA`,

.. data:: data_list_of_value_objects

   :type: List of :class:`RefinedClassA` objects

.. data:: data_list_of_value

   :type: List of :class:`RefinedClassA`

.. data:: data_list_of_number_or_string

   :type: list of floats

.. data:: data_list_of_parentheses_value

   :type: list of (:class:`RefinedClassA`, :class:`ClassA`)

.. data:: data_pair_of_value

   :type: pair of :class:`RefinedClassA`

.. data:: data_bmelemseq_of_value

   :type: :class:`BMElemSeq` of :class:`RefinedClassA`

.. data:: data_tuple_of_value

   :type: tuple of :class:`RefinedClassA`'s

.. data:: data_dict_with_string_keys

   :type: dict with string keys

.. data:: data_iterable_object

   :type: iterable object

.. data:: data_list

   :type: list.

.. data:: data_dict

   :type: dict.

.. data:: data_set

   :type: set.

.. data:: data_tuple

   :type: tuple.

.. data:: data_bpy_types_struct_subclass

   :type: :class:`bpy.types.Struct` subclass

.. data:: data_bpy_struct

   :type: :class:`bpy_struct`

.. data:: data_ot

   :type: :class:`TEST_OT_op`, 

.. data:: data_dot

   :type: :class:`module_1.ClassA`

.. data:: data_dot_comma

   :type: :class:`module_1.ClassA`,

.. data:: data_name

   :type: module_1.ClassA

.. data:: data_start_and_end_with_parentheses

   :type: (:class:`RefinedClassA`, :class:`bpy_prop_collection`, :class:`ClassA`)
