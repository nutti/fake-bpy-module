.. mod-type:: update

.. module:: bpy.types

.. class:: bpy_prop_collection

   .. method:: values()

      :rtype: list[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: get(key, default=None)

      :arg key: The identifier for the collection member.
      :type key: string
      :arg default: Optional argument for the value to return if
         *key* is not found.
      :type default: GenericType2
      :mod-option arg default: skip-refine

   .. method:: items()

      :rtype: list[tuple[str, GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: foreach_get(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.MutableSequence[bool] | collections.abc.MutableSequence[int] | collections.abc.MutableSequence[float]
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.Sequence[bool] | collections.abc.Sequence[int] | collections.abc.Sequence[float]
      :mod-option arg seq: skip-refine
