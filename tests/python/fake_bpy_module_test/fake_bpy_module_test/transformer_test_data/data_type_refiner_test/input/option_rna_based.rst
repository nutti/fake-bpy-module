.. module:: bpy.types

.. function:: function_1(arg_optional, arg_readonly, arg_never_none)

   :arg arg_optional: function_1 arg_optional description
   :type arg_optional: int (optional)
   :arg arg_readonly: function_1 arg_readonly description
   :type arg_readonly: int (readonly)
   :arg arg_never_none: function_1 arg_never_none description
   :type arg_never_none: int (never none)

.. function:: function_2(arg_1)

   :arg arg_1: function_2 arg_1 description
   :type arg_1: int (optional, readonly, never none)

.. class:: ClassA

   .. attribute:: active_attr

      :type: int

.. class:: ClassB

.. class:: ID

   .. attribute:: library

      :type: int

   .. method:: draw_handler_add(arg_1)

      :arg arg_1: draw_handler_add arg_1 description
      :type arg_1: str

   .. method:: function_1(arg_1)

      :arg arg_1: function_1 arg_1 description
      :type arg_1: str

.. data:: active_data

   :type: int

.. data:: collection_property_1

   :type: :class:`bpy_prop_collection` of :class:`RefinedClassA`

.. data:: collection_property_2

   :type: :class:`bpy_prop_array`\ [int]

.. data:: collection_property_3

   :type: :class:`RefinedClassA`\ [:class:`RefinedClassB`]

.. function:: option_description_function_1(arg_1)

   :arg arg_1: option_description_function_1 arg_1 description (optional, readonly, never None)
   :type arg_1: int

.. data:: option_description_data_1

   option_description_data_1 description (never none, readonly)

   :type: int

.. class:: ClassA

   .. attribute:: option_description_attr_1

      option_description_attr_1 description (never None, readonly)

      :type: float

   .. method:: option_description_method_1(arg_1)

      :arg arg_1: option_description_method_1 arg_1 description (optional)
      :type arg_1: int

