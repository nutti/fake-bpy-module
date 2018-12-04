def autodesk_3ds(filepath="",
                 check_existing=True,
                 axis_forward='Y',
                 axis_up='Z',
                 filter_glob="*.3ds",
                 use_selection=False):
    '''Export to 3DS file format (.3ds) 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: boolean, (optional)
    '''

    pass


def fbx(filepath="",
        check_existing=True,
        axis_forward='-Z',
        axis_up='Y',
        filter_glob="*.fbx",
        version='BIN7400',
        ui_tab='MAIN',
        use_selection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        bake_space_transform=False,
        object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'},
        use_mesh_modifiers=True,
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
        use_anim=True,
        use_anim_action_all=True,
        use_default_take=True,
        use_anim_optimize=True,
        anim_optimize_precision=6.0,
        path_mode='AUTO',
        embed_textures=False,
        batch_mode='OFF',
        use_batch_own_dir=True,
        use_metadata=True):
    '''Write a FBX file 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param version: Version, Choose which version of the exporter to useBIN7400 FBX 7.4 binary, Modern 7.4 binary version.ASCII6100 FBX 6.1 ASCII, Legacy 6.1 ascii version - WARNING: Deprecated and no more maintained. 
    :type version: enum in ['BIN7400', 'ASCII6100'], (optional)
    :param ui_tab: ui_tab, Export options categoriesMAIN Main, Main basic settings.GEOMETRY Geometries, Geometry-related settings.ARMATURE Armatures, Armature-related settings.ANIMATION Animation, Animation-related settings. 
    :type ui_tab: enum in ['MAIN', 'GEOMETRY', 'ARMATURE', 'ANIMATION'], (optional)
    :param use_selection: Selected Objects, Export selected objects on visible layers 
    :type use_selection: boolean, (optional)
    :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!) 
    :type global_scale: float in [0.001, 1000], (optional)
    :param apply_unit_scale: Apply Unit, Scale all data according to current Blender size, to match default FBX unit (centimeter, some importers do not handle UnitScaleFactor properly) 
    :type apply_unit_scale: boolean, (optional)
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risks, known broken with armatures/animations) 
    :type bake_space_transform: boolean, (optional)
    :param object_types: Object Types, Which kind of object to exportEMPTY Empty.CAMERA Camera.LAMP Lamp.ARMATURE Armature, WARNING: not supported in dupli/group instances.MESH Mesh.OTHER Other, Other geometry types, like curve, metaball, etc. (converted to meshes). 
    :type object_types: enum set in {'EMPTY', 'CAMERA', 'LAMP', 'ARMATURE', 'MESH', 'OTHER'}, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys 
    :type use_mesh_modifiers: boolean, (optional)
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
    :param use_anim: Animation, Export keyframe animation 
    :type use_anim: boolean, (optional)
    :param use_anim_action_all: All Actions, Export all actions for armatures or just the currently selected action 
    :type use_anim_action_all: boolean, (optional)
    :param use_default_take: Default Take, Export currently assigned object and armature animations into a default take from the scene start/end frames 
    :type use_default_take: boolean, (optional)
    :param use_anim_optimize: Optimize Keyframes, Remove double keyframes 
    :type use_anim_optimize: boolean, (optional)
    :param anim_optimize_precision: Precision, Tolerance for comparing double keyframes (higher for greater accuracy) 
    :type anim_optimize_precision: float in [0, 20], (optional)
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)
    :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!) 
    :type embed_textures: boolean, (optional)
    :param batch_mode: Batch ModeOFF Off, Active scene to file.SCENE Scene, Each scene as a file.GROUP Group, Each group as a file. 
    :type batch_mode: enum in ['OFF', 'SCENE', 'GROUP'], (optional)
    :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file 
    :type use_batch_own_dir: boolean, (optional)
    :param use_metadata: Use Metadata 
    :type use_metadata: boolean, (optional)
    '''

    pass


def obj(filepath="",
        check_existing=True,
        axis_forward='-Z',
        axis_up='Y',
        filter_glob="*.obj;*.mtl",
        use_selection=False,
        use_animation=False,
        use_mesh_modifiers=True,
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
        path_mode='AUTO'):
    '''Save a Wavefront OBJ File 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: boolean, (optional)
    :param use_animation: Animation, Write out an OBJ for each frame 
    :type use_animation: boolean, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers (preview resolution) 
    :type use_mesh_modifiers: boolean, (optional)
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
    '''

    pass


def x3d(filepath="",
        check_existing=True,
        axis_forward='Z',
        axis_up='Y',
        filter_glob="*.x3d",
        use_selection=False,
        use_mesh_modifiers=True,
        use_triangulate=False,
        use_normals=False,
        use_compress=False,
        use_hierarchy=True,
        name_decorations=True,
        use_h3d=False,
        global_scale=1.0,
        path_mode='AUTO'):
    '''Export selection to Extensible 3D file (.x3d) 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: boolean, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Use transformed mesh data from each object 
    :type use_mesh_modifiers: boolean, (optional)
    :param use_triangulate: Triangulate, Write quads into ‘IndexedTriangleSet’ 
    :type use_triangulate: boolean, (optional)
    :param use_normals: Normals, Write normals with geometry 
    :type use_normals: boolean, (optional)
    :param use_compress: Compress, Compress the exported file 
    :type use_compress: boolean, (optional)
    :param use_hierarchy: Hierarchy, Export parent child relationships 
    :type use_hierarchy: boolean, (optional)
    :param name_decorations: Name decorations, Add prefixes to the names of exported nodes to indicate their type 
    :type name_decorations: boolean, (optional)
    :param use_h3d: H3D Extensions, Export shaders for H3D 
    :type use_h3d: boolean, (optional)
    :param global_scale: Scale 
    :type global_scale: float in [0.01, 1000], (optional)
    :param path_mode: Path Mode, Method used to reference pathsAUTO Auto, Use Relative paths with subdirectories only.ABSOLUTE Absolute, Always write absolute paths.RELATIVE Relative, Always write relative paths (where possible).MATCH Match, Match Absolute/Relative setting with input path.STRIP Strip Path, Filename only.COPY Copy, Copy the file to the destination path (or subdirectory). 
    :type path_mode: enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)
    '''

    pass
