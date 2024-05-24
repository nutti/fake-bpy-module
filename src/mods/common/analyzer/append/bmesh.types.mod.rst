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
