.. mod-type:: new

.. module:: module_1

.. class:: ClassA

   Duplication Skip

.. class:: ClassB

   ClassB description

   :generic-types: _GenericType1

   .. base-class:: typing.Generic

      :mod-option base-class: skip-refine

   .. attribute:: attr_1

      attr_1 description

      :type: attr_1 type

   .. method:: method_1()

      method_1 description

      :return: method_1 return description
      :rtype: method_1 return type

   .. classmethod:: classmethod_1(arg_1)

      classmethod_1 description

      :arg arg_1: classmethod_1 arg_1 description
      :type arg_1: classmethod_1 arg_1 type
      :generic-types: _GenericType2

   .. staticmethod:: staticmethod_1(arg_1, arg_2=(0, 0))

      staticmethod_1 description

      :arg arg_1: staticmethod_1 arg_1 description
      :type arg_1: staticmethod_1 arg_1 type
      :arg arg_2: staticmethod_1 arg_2 description
      :type arg_2: staticmethod_1 arg_2 type
