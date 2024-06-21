.. mod-type:: append

.. module:: bmesh.types

.. class:: BMElemSeq

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: GenericType1
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[GenericType1, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: BMIter[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMVertSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMVert`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[:class:`BMVert`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: BMIter[BMVert]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMEdgeSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMEdge`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[:class:`BMEdge`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: BMIter[BMEdge]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMFaceSeq

   .. method:: __getitem__(key)

      :type key: int
      :mod-option arg key: skip-refine
      :rtype: :class:`BMFace`
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[:class:`BMFace`, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __iter__()

      :rtype: BMIter[BMFace]
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

.. class:: BMIter

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

   .. method:: __iter__()

      :rtype: BMIter[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: GenericType1
      :mod-option rtype: skip-refine

.. class:: BMLayerCollection

   .. method:: get()

      :rtype: BMLayerItem | GenericType2
      :mod-option rtype: skip-refine

.. class:: BMVert

   .. method:: __getitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :rtype: typing.Any
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :type value: typing.Any
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine

.. class:: BMEdge

   .. method:: __getitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :rtype: typing.Any
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :type value: typing.Any
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine

.. class:: BMFace

   .. method:: __getitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :rtype: typing.Any
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :type value: typing.Any
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine

.. class:: BMLoop

   .. method:: __getitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :rtype: typing.Any
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
      :type value: typing.Any
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: BMLayerItem
      :mod-option arg key: skip-refine
