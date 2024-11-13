.. mod-type:: update

.. module:: bpy.app.handlers

.. data:: depsgraph_update_pre

   :type: list[collections.abc.Callable[[:class:`bpy.types.Scene`, None], None]]
   :mod-option: skip-refine

.. data:: depsgraph_update_post

   :type: list[collections.abc.Callable[[:class:`bpy.types.Scene`, :class:`bpy.types.Depsgraph`], None]]
   :mod-option: skip-refine
