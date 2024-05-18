.. mod-type:: append

.. module:: bpy.types

.. class:: AddonPreferences

   .. attribute:: layout

      :type: :class:`bpy.types.UILayout`

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

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

   .. method:: __getitem__(key)

      :type key: int | str | slice
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
      :rtype: GenericType1
      :mod-option rtype: skip-refine

   .. method:: __iter__()

      :rtype: typing.Iterator[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: __next__()

      :rtype: GenericType1
      :mod-option rtype: skip-refine

   .. method:: __len__()

      :rtype: int
      :mod-option rtype: skip-refine

   .. method:: get()

      :rtype: GenericType1 | GenericType2
      :mod-option rtype: skip-refine

.. class:: bpy_struct

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

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
      :rtype: typing.Any
      :mod-option rtype: skip-refine
