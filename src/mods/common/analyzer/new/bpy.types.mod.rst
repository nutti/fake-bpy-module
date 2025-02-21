.. mod-type:: new

.. module:: bpy.types

.. class:: bpy_prop_array

   :generic-types: _GenericType1

   .. method:: __get__(instance, owner)

      :rtype: :class:`bpy_prop_array`\ [_GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __set__(instance, value)

      :type value: collections.abc.Iterable[_GenericType1]
      :mod-option arg value: skip-refine

   .. method:: foreach_get(seq)

      :type seq: collections.abc.MutableSequence[_GenericType1] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(seq)

      :type seq: collections.abc.Sequence[_GenericType1] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: list[_GenericType1, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: slice
      :mod-option arg key: skip-refine
      :type value: collections.abc.Iterable[_GenericType1]
      :mod-option arg value: skip-refine
      :option function: overload

   .. method:: __delitem__(key)

      :type key: int
      :mod-option arg key: skip-refine

   .. method:: __iter__()

      :rtype: collections.abc.Iterator[_GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine
