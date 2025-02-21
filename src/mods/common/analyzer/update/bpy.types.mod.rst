.. mod-type:: update

.. module:: bpy.types

.. class:: Object

   .. attribute:: data

      :type: :class:`bpy.types.Mesh`, :class:`bpy.types.Curve`, :class:`bpy.types.SurfaceCurve`, :class:`bpy.types.MetaBall`, :class:`bpy.types.TextCurve`, :class:`bpy.types.Curves`, :class:`bpy.types.PointCloud`, :class:`bpy.types.Volume`, :class:`bpy.types.PointCloud`, :class:`bpy.types.GreasePencil`, :class:`bpy.types.GreasePencilv3`, :class:`bpy.types.Armature`, :class:`bpy.types.Lattice`, :class:`bpy.types.Light`, :class:`bpy.types.LightProbe`, :class:`bpy.types.Camera`, :class:`bpy.types.Speaker`

.. class:: bpy_prop_collection

   :generic-types: _GenericType1

   .. method:: values()

      :rtype: list[_GenericType1 | None]
      :mod-option rtype: skip-refine

   .. method:: find(key)

      :type key: str
      :option key: never none
      :mod-option arg key: skip-refine

   .. method:: get(key, default=None)

      :type key: str
      :option key: never none
      :mod-option arg key: skip-refine
      :type default: _GenericType2
      :mod-option arg default: skip-refine
      :generic-types: _GenericType2

   .. method:: items()

      :rtype: list[tuple[str, _GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: foreach_get(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.MutableSequence[bool] | collections.abc.MutableSequence[int] | collections.abc.MutableSequence[float] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.Sequence[bool] | collections.abc.Sequence[int] | collections.abc.Sequence[float] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

.. class:: bpy_prop_collection_idprop

   :generic-types: _GenericType1

   .. method:: add()

      :rtype: _GenericType1
      :mod-option rtype: skip-refine

   .. method:: values()

      :rtype: list[_GenericType1 | None]
      :mod-option rtype: skip-refine

   .. method:: find(key)

      :type key: str
      :option key: never none
      :mod-option arg key: skip-refine

   .. method:: get(key, default=None)

      :type key: str
      :option key: never none
      :mod-option arg key: skip-refine
      :type default: _GenericType2
      :mod-option arg default: skip-refine
      :generic-types: _GenericType2

   .. method:: items()

      :rtype: list[tuple[str, _GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: foreach_get(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.MutableSequence[bool] | collections.abc.MutableSequence[int] | collections.abc.MutableSequence[float] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.Sequence[bool] | collections.abc.Sequence[int] | collections.abc.Sequence[float] | typing_extensions.Buffer | npt.NDArray
      :mod-option arg seq: skip-refine

.. class:: Depsgraph

   .. method:: id_eval_get(id)

      :type id: _GenericType1 | None
      :mod-option arg id: skip-refine
      :rtype: _GenericType1
      :mod-option rtype: skip-refine
      :generic-types: _GenericType1

.. class:: FreestyleLineStyle

   .. attribute:: node_tree

      Node tree for node-based shaders

      :type: :class:`bpy.types.ShaderNodeTree` | None
      :mod-option: skip-refine

.. class:: Light

   .. attribute:: node_tree

      Node tree for node based lights

      :type: :class:`bpy.types.ShaderNodeTree` | None
      :mod-option: skip-refine

.. class:: Material

   .. attribute:: node_tree

      Node tree for node based materials

      :type: :class:`bpy.types.ShaderNodeTree` | None
      :mod-option: skip-refine

.. class:: Scene

   .. attribute:: node_tree

      Compositing node tree

      :type: :class:`bpy.types.CompositorNodeTree` | None
      :mod-option: skip-refine

.. class:: Texture

   .. attribute:: node_tree

      Node tree for node-based textures

      :type: :class:`bpy.types.TextureNodeTree` | None
      :mod-option: skip-refine

.. class:: World

   .. attribute:: node_tree

      Node tree for node based worlds

      :type: :class:`bpy.types.ShaderNodeTree` | None
      :mod-option: skip-refine

.. class:: CompositorNodeGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.CompositorNodeTree`

.. class:: CompositorNodeCustomGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.CompositorNodeTree`

.. class:: GeometryNodeGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.GeometryNodeTree`

.. class:: GeometryNodeCustomGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.GeometryNodeTree`

.. class:: ShaderNodeGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.ShaderNodeTree`

.. class:: ShaderNodeCustomGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.ShaderNodeTree`

.. class:: TextureNodeGroup

   .. attribute:: node_tree

      :type: :class:`bpy.types.TextureNodeTree`

.. class:: IDMaterials

   .. method:: pop(*, index=-1)

      :type index: int (never None) 
      :mod-option arg index: update-argument-type
