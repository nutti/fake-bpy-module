.. mod-type:: new

.. module:: bpy.types

.. class:: bpy_prop_array

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

   .. method:: foreach_get(seq)

      :type seq: collections.abc.MutableSequence[GenericType1]
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(seq)

      :type seq: typing.Sequence[GenericType1]
      :mod-option arg seq: skip-refine

   .. method:: __getitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine
      :rtype: GenericType1
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: int | str
      :mod-option arg key: skip-refine
      :type value: GenericType1
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine

   .. method:: __iter__()

      :rtype: collections.abc.Iterator[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: GenericType1
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine