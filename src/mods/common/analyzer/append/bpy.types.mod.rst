.. mod-type:: append

.. module:: bpy.types

.. class:: AddonPreferences

   .. attribute:: layout

      :type: :class:`bpy.types.UILayout` (never None)

.. class:: Menu

   .. classmethod:: append(draw_func)

   .. classmethod:: prepend(draw_func)

   .. classmethod:: remove(draw_func)

.. class:: Panel

   .. attribute:: is_registered

      :type: bool

.. class:: Operator

   .. attribute:: is_registered

      :type: bool

.. class:: bpy_prop_collection

   .. base-class:: typing.Generic[_GenericType1]

      :mod-option base-class: skip-refine

   .. method:: __getitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __getitem__(key)

      :type key: slice
      :mod-option arg key: skip-refine
      :rtype: tuple[_GenericType1, ...]
      :mod-option rtype: skip-refine
      :option function: overload

   .. method:: __setitem__(key, value)

      :type key: int
      :mod-option arg key: skip-refine
      :type value: _GenericType1
      :mod-option arg value: skip-refine

   .. method:: __iter__()

      :rtype: collections.abc.Iterator[_GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

   .. method:: __contains__(key)

      :type key: str | tuple[str, ...]
      :mod-option arg key: skip-refine
      :rtype: bool
      :mod-option rtype: skip-refine

   .. method:: get()

      :rtype: _GenericType1 | _GenericType2
      :mod-option rtype: skip-refine

.. class:: bpy_struct

   .. base-class:: typing.Generic[_GenericType1]

      :mod-option base-class: skip-refine

   .. attribute:: bl_rna

      :type: :class:`bpy.types.BlenderRNA`, (never none)

   .. method:: __getitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine
      :rtype: typing.Any
      :mod-option rtype: skip-refine

   .. method:: __setitem__(key, value)

      :type key: int | str
      :mod-option arg key: skip-refine
      :type value: typing.Any
      :mod-option arg value: skip-refine

   .. method:: __delitem__(key)

      :type key: int | str
      :mod-option arg key: skip-refine

.. class:: BlenderRNA

   .. attribute:: properties

      :type: :class:`bpy_prop_collection` of :class:`Property`
