.. mod-type:: new

.. module:: bpy.types

.. class:: bpy_prop_array

   .. base-class:: typing.Generic[GenericType]

      :mod-option base-class: skip-refine

   .. method:: foreach_get(attr, seq)

   .. method:: foreach_set(attr, seq)

   .. method:: __getitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine
      :rtype: GenericType
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: int | str
      :mod-option arg key: skip-refine
      :type value: GenericType
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine
      :rtype: GenericType
      :mod-option rtype: skip-refine

   .. method:: __iter__()

      :rtype: typing.Iterator[GenericType]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: GenericType
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine