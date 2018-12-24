def fbx(filepath="",
        check_existing=True,
        filter_glob="*.fbx",
        ui_tab='MAIN',
        use_selection=False,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        bake_space_transform=False,
        object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='OFF',
        use_mesh_edges=False,
        use_tspace=False,
        use_custom_props=False,
        add_leaf_bones=True,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=False,
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='AUTO',
        embed_textures=False,
        batch_mode='OFF',
        use_batch_own_dir=True,
        use_metadata=True,
        axis_forward='-Z',
        axis_up='Y'):
    '''Write a FBX file 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param ui_tab: ui_tab, Export options categoriesMAIN Main, Main basic settings.GEOMETRY Geometries, Geometry-related settings.ARMATURE Armatures, Armature-related settings.ANIMATION Animation, Animation-related settings. 
    :type ui_tab: enum in ['MAIN', 'GEOMETRY', 'ARMATURE', 'ANIMATION'], (optional)
    :param use_selection: Selected Objects, Export selected and visible objects only 
    :type use_selection: boolean, (optional)
    :param use_active_collection: Active Collection, Export only objects from the active collection (and its children) 
    :type use_active_collection: boolean, (optional)
    :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!) 
    :type global_scale: float in [0.001, 1000], (optional)
    :param apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is) 
    :type apply_unit_scale: boolean, (optional)
    :param apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)FBX_SCALE_NONE All Local, Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.FBX_SCALE_UNITS FBX Units Scale, Apply custom scaling to each object transformation, and units scaling to FBX scale.FBX_SCALE_CUSTOM FBX Custom Scale, Apply custom scaling to FBX scale, and units scaling to each object transformation.FBX_SCALE_ALL FBX All, Apply custom scaling and units scaling to FBX scale. 
    :type apply_scale_options: enum in ['FBX_SCALE_NONE', 'FBX_SCALE_UNITS', 'FBX_SCALE_CUSTOM', 'FBX_SCALE_ALL'], (optional)
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risks, known broken with armatures/animations) 
    :type bake_space_transform: boolean, (optional)
    :param object_types: Object Types, Which kind of object to exportEMPTY Empty.CAMERA Camera.LIGHT Lamp.ARMATURE Armature, WARNING: not supported in dupli/group instances.MESH Mesh.OTHER Other, Other geometry types, like curve, metaball, etc. (converted to meshes). 
    :type object_types: enum set in {'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'}, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys 
    :type use_mesh_modifiers: boolean, (optional)
    :param use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects 
    :type use_mesh_modifiers_render: boolean, (optional)
    :param mesh_smooth_type: Smoothing, Export smoothing information (prefer ‘Normals Only’ option if your target importer understand split normals)OFF Normals Only, Export only normals instead of writing edge or face smoothing data.FACE Face, Write face smoothing.EDGE Edge, Write edge smoothing. 
    :type mesh_smooth_type: enum in ['OFF', 'FACE', 'EDGE'], (optional)
    :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons) 
    :type use_mesh_edges: boolean, (optional)
    :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!) 
    :type use_tspace: boolean, (optional)
    :param use_custom_props: Custom Properties, Export custom properties 
    :type use_custom_props: boolean, (optional)
    :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data) 
    :type add_leaf_bones: boolean, (optional)
    :param primary_bone_axis: Primary Bone Axis 
    :type primary_bone_axis: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param secondary_bone_axis: Secondary Bone Axis 
    :type secondary_bone_axis: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children) 
    :type use_armature_deform_only: boolean, (optional)
    :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender’s armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender…)NULL Null, ‘Null’ FBX node, similar to Blender’s Empty (default).ROOT Root, ‘Root’ FBX node, supposed to be the root of chains of bones….LIMBNODE LimbNode, ‘LimbNode’ FBX node, a regular joint between two bones…. 
    :type armature_nodetype: enum in ['NULL', 'ROOT', 'LIMBNODE'], (optional)
    :param bake_anim: Baked Animation, Export baked keyframe animation 
    :type bake_anim: boolean, (optional)
    :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4) 
    :type bake_anim_use_all_bones: boolean, (optional)
    :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation 
    :type bake_anim_use_nla_strips: boolean, (optional)
    :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all) 
    :type bake_anim_use_all_actions: boolean, (optional)
    :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels 
    :type bake_anim_force_startend_keying: boolean, (optional)
    :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames) 
    :type bake_anim_step: float in [0.01, 100], (optional)
    :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified) 
    :type bake_anim_simplify_factor: float in [0, 100], (optional)
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)
    :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!) 
    :type embed_textures: boolean, (optional)
    :param batch_mode: Batch ModeOFF Off, Active scene to file.SCENE Scene, Each scene as a file.COLLECTION Collection, Each collection (data-block ones) as a file, does not include content of children collections.SCENE_COLLECTION Scene Collections, Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.ACTIVE_SCENE_COLLECTION Active Scene Collections, Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections. 
    :type batch_mode: enum in ['OFF', 'SCENE', 'COLLECTION', 'SCENE_COLLECTION', 'ACTIVE_SCENE_COLLECTION'], (optional)
    :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file 
    :type use_batch_own_dir: boolean, (optional)
    :param use_metadata: Use Metadata 
    :type use_metadata: boolean, (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    '''

    pass


def gltf(export_format='GLB',
         ui_tab='GENERAL',
         export_copyright="",
         export_texcoords=True,
         export_normals=True,
         export_tangents=False,
         export_materials=True,
         export_colors=True,
         export_cameras=False,
         export_selected=False,
         export_extras=False,
         export_yup=True,
         export_apply=False,
         export_animations=True,
         export_frame_range=True,
         export_frame_step=1,
         export_move_keyframes=True,
         export_force_sampling=False,
         export_current_frame=True,
         export_skins=True,
         export_bake_skins=False,
         export_all_influences=False,
         export_morph=True,
         export_morph_normal=True,
         export_morph_tangent=False,
         export_lights=False,
         export_texture_transform=False,
         export_displacement=False,
         will_save_settings=False,
         filepath="",
         check_existing=True,
         filter_glob="*.glb;*.gltf"):
    '''Export scene as glTF 2.0 file 

    :param export_format: Format, Output format and embedding options. Binary is most efficient, but JSON (embedded or separate) may be easier to edit laterGLB glTF Binary (.glb), Exports a single file, with all data packed in binary form. Most efficient and portable, but more difficult to edit later.GLTF_EMBEDDED glTF Embedded (.gltf), Exports a single file, with all data packed in JSON. Less efficient than binary, but easier to edit later.GLTF_SEPARATE glTF Separate (.gltf + .bin + textures), Exports multiple files, with separate JSON, binary and texture data. Easiest to edit later. 
    :type export_format: enum in ['GLB', 'GLTF_EMBEDDED', 'GLTF_SEPARATE'], (optional)
    :param ui_tab: ui_tab, Export setting categoriesGENERAL General, General settings.MESHES Meshes, Mesh settings.OBJECTS Objects, Object settings.MATERIALS Materials, Material settings.ANIMATION Animation, Animation settings. 
    :type ui_tab: enum in ['GENERAL', 'MESHES', 'OBJECTS', 'MATERIALS', 'ANIMATION'], (optional)
    :param export_copyright: Copyright, Legal rights and conditions for the model 
    :type export_copyright: string, (optional, never None)
    :param export_texcoords: UVs, Export UVs (texture coordinates) with meshes 
    :type export_texcoords: boolean, (optional)
    :param export_normals: Normals, Export vertex normals with meshes 
    :type export_normals: boolean, (optional)
    :param export_tangents: Tangents, Export vertex tangents with meshes 
    :type export_tangents: boolean, (optional)
    :param export_materials: Materials, Export materials 
    :type export_materials: boolean, (optional)
    :param export_colors: Vertex Colors, Export vertex colors with meshes 
    :type export_colors: boolean, (optional)
    :param export_cameras: Cameras, Export cameras 
    :type export_cameras: boolean, (optional)
    :param export_selected: Selected Objects, Export selected objects only 
    :type export_selected: boolean, (optional)
    :param export_extras: Custom Properties, Export custom properties as glTF extras 
    :type export_extras: boolean, (optional)
    :param export_yup: +Y Up, Export using glTF convention, +Y up 
    :type export_yup: boolean, (optional)
    :param export_apply: Apply Modifiers, Apply modifiers to mesh objects 
    :type export_apply: boolean, (optional)
    :param export_animations: Animations, Exports active actions and NLA tracks as glTF animations 
    :type export_animations: boolean, (optional)
    :param export_frame_range: Limit to Playback Range, Clips animations to selected playback range 
    :type export_frame_range: boolean, (optional)
    :param export_frame_step: Sampling Rate, How often to evaluate animated values (in frames) 
    :type export_frame_step: int in [1, 120], (optional)
    :param export_move_keyframes: Keyframes Start at 0, Keyframes start at 0, instead of 1 
    :type export_move_keyframes: boolean, (optional)
    :param export_force_sampling: Always Sample Animations, Apply sampling to all animations 
    :type export_force_sampling: boolean, (optional)
    :param export_current_frame: Use Current Frame, Export the scene in the current animation frame 
    :type export_current_frame: boolean, (optional)
    :param export_skins: Skinning, Export skinning (armature) data 
    :type export_skins: boolean, (optional)
    :param export_bake_skins: Bake Skinning Constraints, Apply skinning constraints to armatures 
    :type export_bake_skins: boolean, (optional)
    :param export_all_influences: Include All Bone Influences, Allow >4 joint vertex influences. Models may appear incorrectly in many viewers 
    :type export_all_influences: boolean, (optional)
    :param export_morph: Shape Keys, Export shape keys (morph targets) 
    :type export_morph: boolean, (optional)
    :param export_morph_normal: Shape Key Normals, Export vertex normals with shape keys (morph targets) 
    :type export_morph_normal: boolean, (optional)
    :param export_morph_tangent: Shape Key Tangents, Export vertex tangents with shape keys (morph targets) 
    :type export_morph_tangent: boolean, (optional)
    :param export_lights: Punctual Lights, Export directional, point, and spot lights. Uses “KHR_lights_punctual” glTF extension 
    :type export_lights: boolean, (optional)
    :param export_texture_transform: Texture Transforms, Export texture or UV position, rotation, and scale. Uses “KHR_texture_transform” glTF extension 
    :type export_texture_transform: boolean, (optional)
    :param export_displacement: Displacement Textures (EXPERIMENTAL), EXPERIMENTAL: Export displacement textures. Uses incomplete “KHR_materials_displacement” glTF extension 
    :type export_displacement: boolean, (optional)
    :param will_save_settings: will_save_settings 
    :type will_save_settings: boolean, (optional)
    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    '''

    pass


def obj(filepath="",
        check_existing=True,
        filter_glob="*.obj;*.mtl",
        use_selection=False,
        use_animation=False,
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=False,
        use_edges=True,
        use_smooth_groups=False,
        use_smooth_groups_bitflags=False,
        use_normals=True,
        use_uvs=True,
        use_materials=True,
        use_triangles=False,
        use_nurbs=False,
        use_vertex_groups=False,
        use_blen_objects=True,
        group_by_object=False,
        group_by_material=False,
        keep_vertex_order=False,
        global_scale=1.0,
        path_mode='AUTO',
        axis_forward='-Z',
        axis_up='Y'):
    '''Save a Wavefront OBJ File 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: boolean, (optional)
    :param use_animation: Animation, Write out an OBJ for each frame 
    :type use_animation: boolean, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers 
    :type use_mesh_modifiers: boolean, (optional)
    :param use_mesh_modifiers_render: Use Modifiers Render Settings, Use render settings when applying modifiers to mesh objects 
    :type use_mesh_modifiers_render: boolean, (optional)
    :param use_edges: Include Edges 
    :type use_edges: boolean, (optional)
    :param use_smooth_groups: Smooth Groups, Write sharp edges as smooth groups 
    :type use_smooth_groups: boolean, (optional)
    :param use_smooth_groups_bitflags: Bitflag Smooth Groups, Same as ‘Smooth Groups’, but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less) 
    :type use_smooth_groups_bitflags: boolean, (optional)
    :param use_normals: Write Normals, Export one normal per vertex and per face, to represent flat faces and sharp edges 
    :type use_normals: boolean, (optional)
    :param use_uvs: Include UVs, Write out the active UV coordinates 
    :type use_uvs: boolean, (optional)
    :param use_materials: Write Materials, Write out the MTL file 
    :type use_materials: boolean, (optional)
    :param use_triangles: Triangulate Faces, Convert all faces to triangles 
    :type use_triangles: boolean, (optional)
    :param use_nurbs: Write Nurbs, Write nurbs curves as OBJ nurbs rather than converting to geometry 
    :type use_nurbs: boolean, (optional)
    :param use_vertex_groups: Polygroups 
    :type use_vertex_groups: boolean, (optional)
    :param use_blen_objects: Objects as OBJ Objects 
    :type use_blen_objects: boolean, (optional)
    :param group_by_object: Objects as OBJ Groups 
    :type group_by_object: boolean, (optional)
    :param group_by_material: Material Groups 
    :type group_by_material: boolean, (optional)
    :param keep_vertex_order: Keep Vertex Order 
    :type keep_vertex_order: boolean, (optional)
    :param global_scale: Scale 
    :type global_scale: float in [0.01, 1000], (optional)
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    '''

    pass
