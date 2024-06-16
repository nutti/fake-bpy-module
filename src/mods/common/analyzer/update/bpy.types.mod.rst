.. mod-type:: update

.. module:: bpy.types

.. class:: bpy_prop_collection

   .. method:: values()

      :rtype: list[GenericType1]
      :mod-option rtype: skip-refine

   .. method:: get(key, default=None)

      :type default: GenericType2
      :mod-option arg default: skip-refine

   .. method:: items()

      :rtype: list[tuple[str, GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: foreach_get(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.MutableSequence[bool] | collections.abc.MutableSequence[int] | collections.abc.MutableSequence[float]
      :mod-option arg seq: skip-refine

   .. method:: foreach_set(attr, seq)

      :type attr: str
      :mod-option arg attr: skip-refine
      :type seq: collections.abc.Sequence[bool] | collections.abc.Sequence[int] | collections.abc.Sequence[float]
      :mod-option arg seq: skip-refine

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
