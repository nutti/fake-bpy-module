.. module:: module_1.submodule_1


.. data:: data_1

   :type: :class:`module_1.submodule_2.RefinedClassB`

.. data:: data_2

   :type: :enum:`module_1.submodule_2.RefinedEnumB`


.. function:: function_1(arg_1)

   :type arg_1: :class:`module_1.submodule_1.RefinedClassA`
   :rtype: :class:`module_1.submodule_2.RefinedClassC`

.. function:: function_2(arg_1)

   :type arg_1: :enum:`module_1.submodule_1.RefinedEnumA`
   :rtype: :enum:`module_1.submodule_2.RefinedEnumC`


.. class:: ClassA

   .. base-class:: `module_1.submodule_2.RefinedClassD`

   .. attribute:: attr_1

      :type: :class:`module_2.RefinedClassE`

   .. method:: method_1(arg_1)

      :type arg_1: :class:`module_2.submodule_3.RefinedClassF`
      :rtype: :class:`module_2.submodule_3.RefinedClassG`

.. class:: ClassB

   .. base-class:: `module_1.submodule_2.RefinedClassD`

   .. attribute:: attr_1

      :type: :enum:`module_3.RefinedEnumE`

   .. method:: method_1(arg_1)

      :type arg_1: :enum:`module_3.submodule_4.RefinedEnumF`
      :rtype: :enum:`module_3.submodule_4.RefinedEnumG`
