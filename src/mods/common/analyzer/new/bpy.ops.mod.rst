.. mod-type:: new

.. module:: bpy.ops

.. class:: _BPyOpsSubModOp

   .. attribute:: bl_options

      Set of option flags for this operator (e.g. ``'REGISTER'``, ``'UNDO'``).

      :type: set[str]
      :mod-option attribute: skip-refine

   .. method:: poll(context='EXEC_DEFAULT', /)

      Test if the operator can be executed in the current context.

      :arg context: Execution context
      :type context: str
      :option arg context: optional
      :return: True if the operator can be executed
      :rtype: bool
      :mod-option rtype: skip-refine

   .. method:: idname()

      :return: Return the Blender-format operator idname (e.g., ``'OBJECT_OT_select_all'``).
      :rtype: str
      :mod-option rtype: skip-refine

   .. method:: idname_py()

      :return: Return the Python-format operator idname (e.g., ``'object.select_all'``).
      :rtype: str
      :mod-option rtype: skip-refine

   .. method:: get_rna_type()

      Get the RNA type definition for this operator.

      :return: RNA type object for introspection
      :rtype: :class:`bpy.types.Struct`
      :mod-option rtype: skip-refine
