.. mod-type:: update

.. module:: bpy.props

.. function:: BoolProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], bool] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, bool], None] | None
   :mod-option arg set: skip-refine

.. function:: BoolVectorProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[bool]] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, collections.abc.Sequence[bool]], None] | None
   :mod-option arg set: skip-refine

.. function:: EnumProperty(items, update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type items: collections.abc.Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str, int] | None] | collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context` | None], collections.abc.Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str, int] | None]]
   :mod-option arg items: skip-refine

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], int] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, int], None] | None
   :mod-option arg set: skip-refine

.. function:: FloatProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], float] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, float], None] | None
   :mod-option arg set: skip-refine

.. function:: FloatVectorProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[float]] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, collections.abc.Sequence[float]], None] | None
   :mod-option arg set: skip-refine

.. function:: IntProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], int] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, int], None] | None
   :mod-option arg set: skip-refine

.. function:: IntVectorProperty(update, get, set)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], collections.abc.Sequence[int]] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, collections.abc.Sequence[int]], None] | None
   :mod-option arg set: skip-refine

.. function:: PointerProperty(poll, update)

   :generic-types: _GenericType1: bpy.types.bpy_struct, _GenericType2: bpy.types.ID

   :type poll: collections.abc.Callable[[_GenericType1, _GenericType2], bool] | None
   :mod-option arg poll: skip-refine

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

.. function:: StringProperty(update, get, set, search)

   :generic-types: _GenericType1: bpy.types.bpy_struct

   :type update: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`], None] | None
   :mod-option arg update: skip-refine

   :type get: collections.abc.Callable[[_GenericType1], str] | None
   :mod-option arg get: skip-refine

   :type set: collections.abc.Callable[[_GenericType1, str], None] | None
   :mod-option arg set: skip-refine

   :type search: collections.abc.Callable[[_GenericType1, :class:`bpy.types.Context`, str], collections.abc.Iterable[str | tuple[str, str]]] | None
   :mod-option arg search: skip-refine
