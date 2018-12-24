def addon_disable(module=""):
    '''Disable an add-on 

    :param module: Module, Module name of the add-on to disable 
    :type module: string, (optional, never None)
    '''

    pass


def addon_enable(module=""):
    '''Enable an add-on 

    :param module: Module, Module name of the add-on to enable 
    :type module: string, (optional, never None)
    '''

    pass


def addon_expand(module=""):
    '''Display information and preferences for this add-on 

    :param module: Module, Module name of the add-on to expand 
    :type module: string, (optional, never None)
    '''

    pass


def addon_install(overwrite=True,
                  target='DEFAULT',
                  filepath="",
                  filter_folder=True,
                  filter_python=True,
                  filter_glob="*.py;*.zip"):
    '''Install an add-on 

    :param overwrite: Overwrite, Remove existing add-ons with the same ID 
    :type overwrite: boolean, (optional)
    :param target: Target Path 
    :type target: enum in ['DEFAULT', 'PREFS'], (optional)
    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_python: Filter python 
    :type filter_python: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    '''

    pass


def addon_refresh():
    '''Scan add-on directories for new modules 

    '''

    pass


def addon_remove(module=""):
    '''Delete the add-on from the file system 

    :param module: Module, Module name of the add-on to remove 
    :type module: string, (optional, never None)
    '''

    pass


def addon_userpref_show(module=""):
    '''Show add-on preferences 

    :param module: Module, Module name of the add-on to expand 
    :type module: string, (optional, never None)
    '''

    pass


def alembic_export(filepath="",
                   check_existing=True,
                   filter_blender=False,
                   filter_backup=False,
                   filter_image=False,
                   filter_movie=False,
                   filter_python=False,
                   filter_font=False,
                   filter_sound=False,
                   filter_text=False,
                   filter_btx=False,
                   filter_collada=False,
                   filter_alembic=True,
                   filter_folder=True,
                   filter_blenlib=False,
                   filemode=8,
                   display_type='DEFAULT',
                   sort_method='FILE_SORT_ALPHA',
                   start=-2147483648,
                   end=-2147483648,
                   xsamples=1,
                   gsamples=1,
                   sh_open=0.0,
                   sh_close=1.0,
                   selected=False,
                   renderable_only=True,
                   visible_layers_only=False,
                   flatten=False,
                   uvs=True,
                   packuv=True,
                   normals=True,
                   vcolors=False,
                   face_sets=False,
                   subdiv_schema=False,
                   apply_subdiv=False,
                   compression_type='OGAWA',
                   global_scale=1.0,
                   triangulate=False,
                   quad_method='SHORTEST_DIAGONAL',
                   ngon_method='BEAUTY',
                   export_hair=True,
                   export_particles=True,
                   as_background_job=True,
                   init_scene_frame_range=False):
    '''Export current scene in an Alembic archive 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene 
    :type start: int in [-inf, inf], (optional)
    :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene 
    :type end: int in [-inf, inf], (optional)
    :param xsamples: Transform Samples, Number of times per frame transformations are sampled 
    :type xsamples: int in [1, 128], (optional)
    :param gsamples: Geometry Samples, Number of times per frame object data are sampled 
    :type gsamples: int in [1, 128], (optional)
    :param sh_open: Shutter Open, Time at which the shutter is open 
    :type sh_open: float in [-1, 1], (optional)
    :param sh_close: Shutter Close, Time at which the shutter is closed 
    :type sh_close: float in [-1, 1], (optional)
    :param selected: Selected Objects Only, Export only selected objects 
    :type selected: boolean, (optional)
    :param renderable_only: Renderable Objects Only, Export only objects marked renderable in the outliner 
    :type renderable_only: boolean, (optional)
    :param visible_layers_only: Visible Layers Only, Export only objects in visible layers 
    :type visible_layers_only: boolean, (optional)
    :param flatten: Flatten Hierarchy, Do not preserve objects’ parent/children relationship 
    :type flatten: boolean, (optional)
    :param uvs: UVs, Export UVs 
    :type uvs: boolean, (optional)
    :param packuv: Pack UV Islands, Export UVs with packed island 
    :type packuv: boolean, (optional)
    :param normals: Normals, Export normals 
    :type normals: boolean, (optional)
    :param vcolors: Vertex Colors, Export vertex colors 
    :type vcolors: boolean, (optional)
    :param face_sets: Face Sets, Export per face shading group assignments 
    :type face_sets: boolean, (optional)
    :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic’s subdivision schema 
    :type subdiv_schema: boolean, (optional)
    :param apply_subdiv: Apply Subsurf, Export subdivision surfaces as meshes 
    :type apply_subdiv: boolean, (optional)
    :param compression_type: Compression 
    :type compression_type: enum in ['OGAWA', 'HDF5'], (optional)
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin 
    :type global_scale: float in [0.0001, 1000], (optional)
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles 
    :type triangulate: boolean, (optional)
    :param quad_method: Quad Method, Method for splitting the quads into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type quad_method: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
    :param ngon_method: Polygon Method, Method for splitting the polygons into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type ngon_method: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
    :param export_hair: Export Hair, Exports hair particle systems as animated curves 
    :type export_hair: boolean, (optional)
    :param export_particles: Export Particles, Exports non-hair particle systems 
    :type export_particles: boolean, (optional)
    :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing 
    :type as_background_job: boolean, (optional)
    '''

    pass


def alembic_import(filepath="",
                   check_existing=True,
                   filter_blender=False,
                   filter_backup=False,
                   filter_image=False,
                   filter_movie=False,
                   filter_python=False,
                   filter_font=False,
                   filter_sound=False,
                   filter_text=False,
                   filter_btx=False,
                   filter_collada=False,
                   filter_alembic=True,
                   filter_folder=True,
                   filter_blenlib=False,
                   filemode=8,
                   display_type='DEFAULT',
                   sort_method='FILE_SORT_ALPHA',
                   scale=1.0,
                   set_frame_range=True,
                   validate_meshes=False,
                   is_sequence=False,
                   as_background_job=True):
    '''Load an Alembic archive 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world’s origin 
    :type scale: float in [0.0001, 1000], (optional)
    :param set_frame_range: Set Frame Range, If checked, update scene’s start and end frame to match those of the Alembic archive 
    :type set_frame_range: boolean, (optional)
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow) 
    :type validate_meshes: boolean, (optional)
    :param is_sequence: Is Sequence, Set to true if the cache is split into separate files 
    :type is_sequence: boolean, (optional)
    :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting 
    :type as_background_job: boolean, (optional)
    '''

    pass


def app_template_install(overwrite=True,
                         filepath="",
                         filter_folder=True,
                         filter_glob="*.zip"):
    '''Install an application-template 

    :param overwrite: Overwrite, Remove existing template with the same ID 
    :type overwrite: boolean, (optional)
    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    '''

    pass


def append(filepath="",
           directory="",
           filename="",
           files=None,
           filter_blender=True,
           filter_backup=False,
           filter_image=False,
           filter_movie=False,
           filter_python=False,
           filter_font=False,
           filter_sound=False,
           filter_text=False,
           filter_btx=False,
           filter_collada=False,
           filter_alembic=False,
           filter_folder=True,
           filter_blenlib=True,
           filemode=1,
           display_type='DEFAULT',
           sort_method='FILE_SORT_ALPHA',
           link=False,
           autoselect=True,
           active_collection=True,
           instance_collections=False,
           set_fake=False,
           use_recursive=True):
    '''Append from a Library .blend file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param filename: File Name, Name of the file 
    :type filename: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param link: Link, Link the objects or data-blocks rather than appending 
    :type link: boolean, (optional)
    :param autoselect: Select, Select new objects 
    :type autoselect: boolean, (optional)
    :param active_collection: Active Collection, Put new objects on the active collection 
    :type active_collection: boolean, (optional)
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene 
    :type instance_collections: boolean, (optional)
    :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups) 
    :type set_fake: boolean, (optional)
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries 
    :type use_recursive: boolean, (optional)
    '''

    pass


def blend_strings_utf8_validate():
    '''Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files) 

    '''

    pass


def call_menu(name=""):
    '''Call (draw) a pre-defined menu 

    :param name: Name, Name of the menu 
    :type name: string, (optional, never None)
    '''

    pass


def call_menu_pie(name=""):
    '''Call (draw) a pre-defined pie menu 

    :param name: Name, Name of the pie menu 
    :type name: string, (optional, never None)
    '''

    pass


def call_panel(name="", keep_open=True):
    '''Call (draw) a pre-defined panel 

    :param name: Name, Name of the menu 
    :type name: string, (optional, never None)
    :param keep_open: Keep Open 
    :type keep_open: boolean, (optional)
    '''

    pass


def collada_export(filepath="",
                   check_existing=True,
                   filter_blender=False,
                   filter_backup=False,
                   filter_image=False,
                   filter_movie=False,
                   filter_python=False,
                   filter_font=False,
                   filter_sound=False,
                   filter_text=False,
                   filter_btx=False,
                   filter_collada=True,
                   filter_alembic=False,
                   filter_folder=True,
                   filter_blenlib=False,
                   filemode=8,
                   display_type='DEFAULT',
                   sort_method='FILE_SORT_ALPHA',
                   prop_bc_export_ui_section='main',
                   apply_modifiers=False,
                   export_mesh_type=0,
                   export_mesh_type_selection='view',
                   selected=False,
                   include_children=False,
                   include_armatures=False,
                   include_shapekeys=False,
                   deform_bones_only=False,
                   include_animations=True,
                   include_all_actions=True,
                   export_animation_type_selection='sample',
                   sampling_rate=1,
                   keep_smooth_curves=False,
                   keep_keyframes=False,
                   active_uv_only=False,
                   use_texture_copies=True,
                   triangulate=True,
                   use_object_instantiation=True,
                   use_blender_profile=True,
                   sort_by_name=False,
                   export_transformation_type=0,
                   export_transformation_type_selection='matrix',
                   open_sim=False,
                   limit_precision=False,
                   keep_bind_info=False):
    '''Save a Collada file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param prop_bc_export_ui_section: Export Section, Only for User Interface Organisationmain Main, Data Export Section.geometry Geom, Geometry Export Section.armature Arm, Armature Export Section.animation Anim, Animation Export Section.collada Extra, Collada Export Section. 
    :type prop_bc_export_ui_section: enum in ['main', 'geometry', 'armature', 'animation', 'collada'], (optional)
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)) 
    :type apply_modifiers: boolean, (optional)
    :param export_mesh_type: Resolution, Modifier resolution for export 
    :type export_mesh_type: int in [-inf, inf], (optional)
    :param export_mesh_type_selection: Resolution, Modifier resolution for exportview View, Apply modifier’s view settings.render Render, Apply modifier’s render settings. 
    :type export_mesh_type_selection: enum in ['view', 'render'], (optional)
    :param selected: Selection Only, Export only selected elements 
    :type selected: boolean, (optional)
    :param include_children: Include Children, Export all children of selected objects (even if not selected) 
    :type include_children: boolean, (optional)
    :param include_armatures: Include Armatures, Export related armatures (even if not selected) 
    :type include_armatures: boolean, (optional)
    :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects 
    :type include_shapekeys: boolean, (optional)
    :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures 
    :type deform_bones_only: boolean, (optional)
    :param include_animations: Include Animations, Export Animations if available. 
    :type include_animations: 
    '''

    pass


def collada_import(filepath="",
                   filter_blender=False,
                   filter_backup=False,
                   filter_image=False,
                   filter_movie=False,
                   filter_python=False,
                   filter_font=False,
                   filter_sound=False,
                   filter_text=False,
                   filter_btx=False,
                   filter_collada=True,
                   filter_alembic=False,
                   filter_folder=True,
                   filter_blenlib=False,
                   filemode=8,
                   display_type='DEFAULT',
                   sort_method='FILE_SORT_ALPHA',
                   import_units=False,
                   fix_orientation=False,
                   find_chains=False,
                   auto_connect=False,
                   min_chain_length=0,
                   keep_bind_info=False):
    '''Load a Collada file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param import_units: Import Units, If disabled match import to Blender’s current Unit settings, otherwise use the settings from the Imported scene 
    :type import_units: boolean, (optional)
    :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints) 
    :type fix_orientation: boolean, (optional)
    :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected 
    :type find_chains: boolean, (optional)
    :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone 
    :type auto_connect: boolean, (optional)
    :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value 
    :type min_chain_length: int in [0, inf], (optional)
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export 
    :type keep_bind_info: boolean, (optional)
    '''

    pass


def context_collection_boolean_set(data_path_iter="",
                                   data_path_item="",
                                   type='TOGGLE'):
    '''Set boolean values for a collection of items 

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable 
    :type data_path_iter: string, (optional, never None)
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) 
    :type data_path_item: string, (optional, never None)
    :param type: Type 
    :type type: enum in ['TOGGLE', 'ENABLE', 'DISABLE'], (optional)
    '''

    pass


def context_cycle_array(data_path="", reverse=False):
    '''Set a context array value (useful for cycling the active mesh edit mode) 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param reverse: Reverse, Cycle backwards 
    :type reverse: boolean, (optional)
    '''

    pass


def context_cycle_enum(data_path="", reverse=False, wrap=False):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param reverse: Reverse, Cycle backwards 
    :type reverse: boolean, (optional)
    :param wrap: Wrap, Wrap back to the first/last values 
    :type wrap: boolean, (optional)
    '''

    pass


def context_cycle_int(data_path="", reverse=False, wrap=False):
    '''Set a context value (useful for cycling active material, vertex keys, groups, etc.) 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param reverse: Reverse, Cycle backwards 
    :type reverse: boolean, (optional)
    :param wrap: Wrap, Wrap back to the first/last values 
    :type wrap: boolean, (optional)
    '''

    pass


def context_menu_enum(data_path=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    '''

    pass


def context_modal_mouse(data_path_iter="",
                        data_path_item="",
                        header_text="",
                        input_scale=0.01,
                        invert=False,
                        initial_x=0):
    '''Adjust arbitrary values with mouse input 

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable 
    :type data_path_iter: string, (optional, never None)
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float) 
    :type data_path_item: string, (optional, never None)
    :param header_text: Header Text, Text to display in header during scale 
    :type header_text: string, (optional, never None)
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta 
    :type input_scale: float in [-inf, inf], (optional)
    :param invert: invert, Invert the mouse input 
    :type invert: boolean, (optional)
    :param initial_x: initial_x 
    :type initial_x: int in [-inf, inf], (optional)
    '''

    pass


def context_pie_enum(data_path=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    '''

    pass


def context_scale_float(data_path="", value=1.0):
    '''Scale a float context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assign value 
    :type value: float in [-inf, inf], (optional)
    '''

    pass


def context_scale_int(data_path="", value=1.0, always_step=True):
    '''Scale an int context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assign value 
    :type value: float in [-inf, inf], (optional)
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when ‘value’ is not 1.0 
    :type always_step: boolean, (optional)
    '''

    pass


def context_set_boolean(data_path="", value=True):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assignment value 
    :type value: boolean, (optional)
    '''

    pass


def context_set_enum(data_path="", value=""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assignment value (as a string) 
    :type value: string, (optional, never None)
    '''

    pass


def context_set_float(data_path="", value=0.0, relative=False):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assignment value 
    :type value: float in [-inf, inf], (optional)
    :param relative: Relative, Apply relative to the current value (delta) 
    :type relative: boolean, (optional)
    '''

    pass


def context_set_id(data_path="", value=""):
    '''Set a context value to an ID data-block 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assign value 
    :type value: string, (optional, never None)
    '''

    pass


def context_set_int(data_path="", value=0, relative=False):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assign value 
    :type value: int in [-inf, inf], (optional)
    :param relative: Relative, Apply relative to the current value (delta) 
    :type relative: boolean, (optional)
    '''

    pass


def context_set_string(data_path="", value=""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assign value 
    :type value: string, (optional, never None)
    '''

    pass


def context_set_value(data_path="", value=""):
    '''Set a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value: Value, Assignment value (as a string) 
    :type value: string, (optional, never None)
    '''

    pass


def context_toggle(data_path=""):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    '''

    pass


def context_toggle_enum(data_path="", value_1="", value_2=""):
    '''Toggle a context value 

    :param data_path: Context Attributes, RNA context string 
    :type data_path: string, (optional, never None)
    :param value_1: Value, Toggle enum 
    :type value_1: string, (optional, never None)
    :param value_2: Value, Toggle enum 
    :type value_2: string, (optional, never None)
    '''

    pass


def copy_prev_settings():
    '''Copy settings from previous version 

    '''

    pass


def debug_menu(debug_value=0):
    '''Open a popup to set the debug level 

    :param debug_value: Debug Value 
    :type debug_value: int in [-32768, 32767], (optional)
    '''

    pass


def doc_view(doc_id=""):
    '''Load online reference docs 

    :param doc_id: Doc ID 
    :type doc_id: string, (optional, never None)
    '''

    pass


def doc_view_manual(doc_id=""):
    '''Load online manual 

    :param doc_id: Doc ID 
    :type doc_id: string, (optional, never None)
    '''

    pass


def doc_view_manual_ui_context():
    '''View a context based online manual in a web browser 

    '''

    pass


def drop_blend_file(filepath=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    '''

    pass


def interface_theme_preset_add(name="", remove_name=False,
                               remove_active=False):
    '''Add or remove a theme preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def keyconfig_activate(filepath=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    '''

    pass


def keyconfig_export(all=False,
                     filepath="keymap.py",
                     filter_folder=True,
                     filter_text=True,
                     filter_python=True):
    '''Export key configuration to a python script 

    :param all: All Keymaps, Write all keymaps (not just user modified) 
    :type all: boolean, (optional)
    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_text: Filter text 
    :type filter_text: boolean, (optional)
    :param filter_python: Filter python 
    :type filter_python: boolean, (optional)
    '''

    pass


def keyconfig_import(filepath="keymap.py",
                     filter_folder=True,
                     filter_text=True,
                     filter_python=True,
                     keep_original=True):
    '''Import key configuration from a python script 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_text: Filter text 
    :type filter_text: boolean, (optional)
    :param filter_python: Filter python 
    :type filter_python: boolean, (optional)
    :param keep_original: Keep original, Keep original file after copying to configuration folder 
    :type keep_original: boolean, (optional)
    '''

    pass


def keyconfig_preset_add(name="", remove_name=False, remove_active=False):
    '''Add or remove a Key-config Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def keyconfig_remove():
    '''Remove key config 

    '''

    pass


def keyconfig_test():
    '''Test key-config for conflicts 

    '''

    pass


def keyitem_add():
    '''Add key map item 

    '''

    pass


def keyitem_remove(item_id=0):
    '''Remove key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int in [-inf, inf], (optional)
    '''

    pass


def keyitem_restore(item_id=0):
    '''Restore key map item 

    :param item_id: Item Identifier, Identifier of the item to remove 
    :type item_id: int in [-inf, inf], (optional)
    '''

    pass


def keymap_restore(all=False):
    '''Restore key map(s) 

    :param all: All Keymaps, Restore all keymaps to default 
    :type all: boolean, (optional)
    '''

    pass


def lib_reload(library="",
               filepath="",
               directory="",
               filename="",
               filter_blender=True,
               filter_backup=False,
               filter_image=False,
               filter_movie=False,
               filter_python=False,
               filter_font=False,
               filter_sound=False,
               filter_text=False,
               filter_btx=False,
               filter_collada=False,
               filter_alembic=False,
               filter_folder=True,
               filter_blenlib=False,
               filemode=8,
               relative_path=True,
               display_type='DEFAULT',
               sort_method='FILE_SORT_ALPHA'):
    '''Reload the given library 

    :param library: Library, Library to reload 
    :type library: string, (optional, never None)
    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param filename: File Name, Name of the file 
    :type filename: string, (optional, never None)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def lib_relocate(library="",
                 filepath="",
                 directory="",
                 filename="",
                 files=None,
                 filter_blender=True,
                 filter_backup=False,
                 filter_image=False,
                 filter_movie=False,
                 filter_python=False,
                 filter_font=False,
                 filter_sound=False,
                 filter_text=False,
                 filter_btx=False,
                 filter_collada=False,
                 filter_alembic=False,
                 filter_folder=True,
                 filter_blenlib=False,
                 filemode=8,
                 relative_path=True,
                 display_type='DEFAULT',
                 sort_method='FILE_SORT_ALPHA'):
    '''Relocate the given library to one or several others 

    :param library: Library, Library to relocate 
    :type library: string, (optional, never None)
    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param filename: File Name, Name of the file 
    :type filename: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def link(filepath="",
         directory="",
         filename="",
         files=None,
         filter_blender=True,
         filter_backup=False,
         filter_image=False,
         filter_movie=False,
         filter_python=False,
         filter_font=False,
         filter_sound=False,
         filter_text=False,
         filter_btx=False,
         filter_collada=False,
         filter_alembic=False,
         filter_folder=True,
         filter_blenlib=True,
         filemode=1,
         relative_path=True,
         display_type='DEFAULT',
         sort_method='FILE_SORT_ALPHA',
         link=True,
         autoselect=True,
         active_collection=True,
         instance_collections=True):
    '''Link from a Library .blend file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param filename: File Name, Name of the file 
    :type filename: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param link: Link, Link the objects or data-blocks rather than appending 
    :type link: boolean, (optional)
    :param autoselect: Select, Select new objects 
    :type autoselect: boolean, (optional)
    :param active_collection: Active Collection, Put new objects on the active collection 
    :type active_collection: boolean, (optional)
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene 
    :type instance_collections: boolean, (optional)
    '''

    pass


def memory_statistics():
    '''Print memory statistics to the console 

    '''

    pass


def open_mainfile(filepath="",
                  filter_blender=True,
                  filter_backup=False,
                  filter_image=False,
                  filter_movie=False,
                  filter_python=False,
                  filter_font=False,
                  filter_sound=False,
                  filter_text=False,
                  filter_btx=False,
                  filter_collada=False,
                  filter_alembic=False,
                  filter_folder=True,
                  filter_blenlib=False,
                  filemode=8,
                  display_type='DEFAULT',
                  sort_method='FILE_SORT_ALPHA',
                  load_ui=True,
                  use_scripts=True):
    '''Open a Blender file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param load_ui: Load UI, Load user interface setup in the .blend file 
    :type load_ui: boolean, (optional)
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences 
    :type use_scripts: boolean, (optional)
    '''

    pass


def operator_cheat_sheet():
    '''List all the Operators in a text-block, useful for scripting 

    '''

    pass


def operator_defaults():
    '''Set the active operator to its default values 

    '''

    pass


def operator_pie_enum(data_path="", prop_string=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param data_path: Operator, Operator name (in python as string) 
    :type data_path: string, (optional, never None)
    :param prop_string: Property, Property name (as a string) 
    :type prop_string: string, (optional, never None)
    '''

    pass


def operator_preset_add(name="",
                        remove_name=False,
                        remove_active=False,
                        operator=""):
    '''Add or remove an Operator Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    :param operator: Operator 
    :type operator: string, (optional, never None)
    '''

    pass


def owner_disable(owner_id=""):
    '''Enable workspace owner ID 

    :param owner_id: UI Tag 
    :type owner_id: string, (optional, never None)
    '''

    pass


def owner_enable(owner_id=""):
    '''Enable workspace owner ID 

    :param owner_id: UI Tag 
    :type owner_id: string, (optional, never None)
    '''

    pass


def path_open(filepath=""):
    '''Open a path in a file browser 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    '''

    pass


def previews_batch_clear(files=None,
                         directory="",
                         filter_blender=True,
                         filter_folder=True,
                         use_scenes=True,
                         use_collections=True,
                         use_objects=True,
                         use_intern_data=True,
                         use_trusted=False,
                         use_backups=True):
    '''Clear selected .blend file’s previews 

    :param files: files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param directory: directory 
    :type directory: string, (optional, never None)
    :param filter_blender: filter_blender 
    :type filter_blender: boolean, (optional)
    :param filter_folder: filter_folder 
    :type filter_folder: boolean, (optional)
    :param use_scenes: Scenes, Clear scenes’ previews 
    :type use_scenes: boolean, (optional)
    :param use_collections: Collections, Clear collections’ previews 
    :type use_collections: boolean, (optional)
    :param use_objects: Objects, Clear objects’ previews 
    :type use_objects: boolean, (optional)
    :param use_intern_data: Mat/Tex/…, Clear ‘internal’ previews (materials, textures, images, etc.) 
    :type use_intern_data: boolean, (optional)
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files 
    :type use_trusted: boolean, (optional)
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews 
    :type use_backups: boolean, (optional)
    '''

    pass


def previews_batch_generate(files=None,
                            directory="",
                            filter_blender=True,
                            filter_folder=True,
                            use_scenes=True,
                            use_collections=True,
                            use_objects=True,
                            use_intern_data=True,
                            use_trusted=False,
                            use_backups=True):
    '''Generate selected .blend file’s previews 

    :param files: files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param directory: directory 
    :type directory: string, (optional, never None)
    :param filter_blender: filter_blender 
    :type filter_blender: boolean, (optional)
    :param filter_folder: filter_folder 
    :type filter_folder: boolean, (optional)
    :param use_scenes: Scenes, Generate scenes’ previews 
    :type use_scenes: boolean, (optional)
    :param use_collections: Collections, Generate collections’ previews 
    :type use_collections: boolean, (optional)
    :param use_objects: Objects, Generate objects’ previews 
    :type use_objects: boolean, (optional)
    :param use_intern_data: Mat/Tex/…, Generate ‘internal’ previews (materials, textures, images, etc.) 
    :type use_intern_data: boolean, (optional)
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files 
    :type use_trusted: boolean, (optional)
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews 
    :type use_backups: boolean, (optional)
    '''

    pass


def previews_clear(id_type={
        'GROUP', 'IMAGE', 'LIGHT', 'MATERIAL', 'OBJECT', 'SCENE', 'TEXTURE',
        'WORLD'
}):
    '''Clear data-block previews (only for some types like objects, materials, textures, etc.) 

    :param id_type: Data-Block Type, Which data-block previews to clear 
    :type id_type: enum set in {'SCENE', 'GROUP', 'OBJECT', 'MATERIAL', 'LIGHT', 'WORLD', 'TEXTURE', 'IMAGE'}, (optional)
    '''

    pass


def previews_ensure():
    '''Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.) 

    '''

    pass


def properties_add(data_path=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: string, (optional, never None)
    '''

    pass


def properties_context_change(context=""):
    '''Jump to a different tab inside the properties editor 

    :param context: Context 
    :type context: string, (optional, never None)
    '''

    pass


def properties_edit(data_path="",
                    property="",
                    value="",
                    default="",
                    min=-10000,
                    max=10000.0,
                    use_soft_limits=False,
                    is_overridable_static=False,
                    soft_min=-10000,
                    soft_max=10000.0,
                    description=""):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: string, (optional, never None)
    :param property: Property Name, Property name edit 
    :type property: string, (optional, never None)
    :param value: Property Value, Property value edit 
    :type value: string, (optional, never None)
    :param default: Default Value, Default value of the property. Important for NLA mixing 
    :type default: string, (optional, never None)
    :param min: Min 
    :type min: float in [-inf, inf], (optional)
    :param max: Max 
    :type max: float in [-inf, inf], (optional)
    :param use_soft_limits: Use Soft Limits 
    :type use_soft_limits: boolean, (optional)
    :param is_overridable_static: Is Statically Overridable 
    :type is_overridable_static: boolean, (optional)
    :param soft_min: Min 
    :type soft_min: float in [-inf, inf], (optional)
    :param soft_max: Max 
    :type soft_max: float in [-inf, inf], (optional)
    :param description: Tooltip 
    :type description: string, (optional, never None)
    '''

    pass


def properties_remove(data_path="", property=""):
    '''Internal use (edit a property data_path) 

    :param data_path: Property Edit, Property data_path edit 
    :type data_path: string, (optional, never None)
    :param property: Property Name, Property name edit 
    :type property: string, (optional, never None)
    '''

    pass


def quit_blender():
    '''Quit Blender 

    '''

    pass


def radial_control(data_path_primary="",
                   data_path_secondary="",
                   use_secondary="",
                   rotation_path="",
                   color_path="",
                   fill_color_path="",
                   fill_color_override_path="",
                   fill_color_override_test_path="",
                   zoom_path="",
                   image_id="",
                   secondary_tex=False):
    '''Set some size property (like e.g. brush size) with mouse wheel 

    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control 
    :type data_path_primary: string, (optional, never None)
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control 
    :type data_path_secondary: string, (optional, never None)
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths 
    :type use_secondary: string, (optional, never None)
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display 
    :type rotation_path: string, (optional, never None)
    :param color_path: Color Path, Path of property used to set the color of the control 
    :type color_path: string, (optional, never None)
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control 
    :type fill_color_path: string, (optional, never None)
    :param fill_color_override_path: Fill Color Override Path 
    :type fill_color_override_path: string, (optional, never None)
    :param fill_color_override_test_path: Fill Color Override Test 
    :type fill_color_override_test_path: string, (optional, never None)
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control 
    :type zoom_path: string, (optional, never None)
    :param image_id: Image ID, Path of ID that is used to generate an image for the control 
    :type image_id: string, (optional, never None)
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture 
    :type secondary_tex: boolean, (optional)
    '''

    pass


def read_factory_settings(app_template="Template", use_empty=False):
    '''Load default file and user preferences 

    :param use_empty: Empty 
    :type use_empty: boolean, (optional)
    '''

    pass


def read_history():
    '''Reloads history and bookmarks 

    '''

    pass


def read_homefile(filepath="",
                  load_ui=True,
                  use_empty=False,
                  use_splash=False,
                  app_template="Template"):
    '''Open the default file (doesn’t save the current file) 

    :param filepath: File Path, Path to an alternative start-up file 
    :type filepath: string, (optional, never None)
    :param load_ui: Load UI, Load user interface setup from the .blend file 
    :type load_ui: boolean, (optional)
    :param use_empty: Empty 
    :type use_empty: boolean, (optional)
    :param use_splash: Splash 
    :type use_splash: boolean, (optional)
    '''

    pass


def recover_auto_save(filepath="",
                      filter_blender=True,
                      filter_backup=False,
                      filter_image=False,
                      filter_movie=False,
                      filter_python=False,
                      filter_font=False,
                      filter_sound=False,
                      filter_text=False,
                      filter_btx=False,
                      filter_collada=False,
                      filter_alembic=False,
                      filter_folder=False,
                      filter_blenlib=False,
                      filemode=8,
                      display_type='LIST_LONG',
                      sort_method='FILE_SORT_TIME'):
    '''Open an automatically saved file to recover it 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def recover_last_session():
    '''Open the last closed file (“quit.blend”) 

    '''

    pass


def redraw_timer(type='DRAW', iterations=10, time_limit=0.0):
    '''Simple redraw timer to test the speed of updating the interface 

    :param type: TypeDRAW Draw Region, Draw Region.DRAW_SWAP Draw Region + Swap, Draw Region and Swap.DRAW_WIN Draw Window, Draw Window.DRAW_WIN_SWAP Draw Window + Swap, Draw Window and Swap.ANIM_STEP Anim Step, Animation Steps.ANIM_PLAY Anim Play, Animation Playback.UNDO Undo/Redo, Undo/Redo. 
    :type type: enum in ['DRAW', 'DRAW_SWAP', 'DRAW_WIN', 'DRAW_WIN_SWAP', 'ANIM_STEP', 'ANIM_PLAY', 'UNDO'], (optional)
    :param iterations: Iterations, Number of times to redraw 
    :type iterations: int in [1, inf], (optional)
    :param time_limit: Time Limit, Seconds to run the test for (override iterations) 
    :type time_limit: float in [0, inf], (optional)
    '''

    pass


def revert_mainfile(use_scripts=True):
    '''Reload the saved file 

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences 
    :type use_scripts: boolean, (optional)
    '''

    pass


def save_as_mainfile(filepath="",
                     check_existing=True,
                     filter_blender=True,
                     filter_backup=False,
                     filter_image=False,
                     filter_movie=False,
                     filter_python=False,
                     filter_font=False,
                     filter_sound=False,
                     filter_text=False,
                     filter_btx=False,
                     filter_collada=False,
                     filter_alembic=False,
                     filter_folder=True,
                     filter_blenlib=False,
                     filemode=8,
                     display_type='DEFAULT',
                     sort_method='FILE_SORT_ALPHA',
                     compress=False,
                     relative_remap=True,
                     copy=False):
    '''Save the current file in the desired location 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param compress: Compress, Write compressed .blend file 
    :type compress: boolean, (optional)
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory 
    :type relative_remap: boolean, (optional)
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active 
    :type copy: boolean, (optional)
    '''

    pass


def save_homefile():
    '''Make the current file the default .blend file 

    '''

    pass


def save_mainfile(filepath="",
                  check_existing=True,
                  filter_blender=True,
                  filter_backup=False,
                  filter_image=False,
                  filter_movie=False,
                  filter_python=False,
                  filter_font=False,
                  filter_sound=False,
                  filter_text=False,
                  filter_btx=False,
                  filter_collada=False,
                  filter_alembic=False,
                  filter_folder=True,
                  filter_blenlib=False,
                  filemode=8,
                  display_type='DEFAULT',
                  sort_method='FILE_SORT_ALPHA',
                  compress=False,
                  relative_remap=False,
                  exit=False):
    '''Save the current Blender file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param compress: Compress, Write compressed .blend file 
    :type compress: boolean, (optional)
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory 
    :type relative_remap: boolean, (optional)
    :param exit: Exit, Exit Blender after saving 
    :type exit: boolean, (optional)
    '''

    pass


def save_userpref():
    '''Save user preferences separately, overrides startup file preferences 

    '''

    pass


def search_menu():
    '''Pop-up a search menu over all available operators in current context 

    '''

    pass


def set_stereo_3d(display_mode='ANAGLYPH',
                  anaglyph_type='RED_CYAN',
                  interlace_type='ROW_INTERLEAVED',
                  use_interlace_swap=False,
                  use_sidebyside_crosseyed=False):
    '''Toggle 3D stereo support for current window (or change the display mode) 

    :param display_mode: Display ModeANAGLYPH Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).INTERLACE Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).TIMESEQUENTIAL Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).SIDEBYSIDE Side-by-Side, Render views for left and right eyes side-by-side.TOPBOTTOM Top-Bottom, Render views for left and right eyes one above another. 
    :type display_mode: enum in ['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM'], (optional)
    :param anaglyph_type: Anaglyph Type 
    :type anaglyph_type: enum in ['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], (optional)
    :param interlace_type: Interlace Type 
    :type interlace_type: enum in ['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], (optional)
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels 
    :type use_interlace_swap: boolean, (optional)
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice-versa 
    :type use_sidebyside_crosseyed: boolean, (optional)
    '''

    pass


def splash():
    '''Open the splash screen with release info 

    '''

    pass


def studiolight_copy_settings(index=0):
    '''Copy Studio Light settings to the Studio light editor 

    :param index: index 
    :type index: int in [-inf, inf], (optional)
    '''

    pass


def studiolight_install(files=None,
                        directory="",
                        filter_folder=True,
                        filter_glob="*.png;*.jpg;*.hdr;*.exr",
                        type='MATCAP'):
    '''Install a user defined studio light 

    :param files: File Path 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param directory: directory 
    :type directory: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param type: type 
    :type type: enum in ['MATCAP', 'WORLD', 'STUDIO'], (optional)
    '''

    pass


def studiolight_new(filename="StudioLight"):
    '''Save custom studio light from the studio light editor settings 

    :param filename: Name 
    :type filename: string, (optional, never None)
    '''

    pass


def studiolight_uninstall(index=0):
    '''Delete Studio Light 

    :param index: index 
    :type index: int in [-inf, inf], (optional)
    '''

    pass


def studiolight_userpref_show():
    '''Show light preferences 

    '''

    pass


def sysinfo(filepath=""):
    '''Generate system information, saved into a text file 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    '''

    pass


def theme_install(overwrite=True,
                  filepath="",
                  filter_folder=True,
                  filter_glob="*.xml"):
    '''Load and apply a Blender XML theme file 

    :param overwrite: Overwrite, Remove existing theme file if exists 
    :type overwrite: boolean, (optional)
    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    '''

    pass


def tool_set_by_name(name="", cycle=False, space_type='EMPTY'):
    '''Set the tool by name (for keymaps) 

    :param name: Text, Display name of the tool 
    :type name: string, (optional, never None)
    :param cycle: Cycle, Cycle through tools in this group 
    :type cycle: boolean, (optional)
    :param space_type: Type 
    :type space_type: enum in ['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES'], (optional)
    '''

    pass


def toolbar():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def url_open(url=""):
    '''Open a website in the web-browser 

    :param url: URL, URL to open 
    :type url: string, (optional, never None)
    '''

    pass


def userpref_autoexec_path_add():
    '''Add path to exclude from autoexecution 

    '''

    pass


def userpref_autoexec_path_remove(index=0):
    '''Remove path to exclude from autoexecution 

    :param index: Index 
    :type index: int in [0, inf], (optional)
    '''

    pass


def window_close():
    '''Close the current window 

    '''

    pass


def window_fullscreen_toggle():
    '''Toggle the current window fullscreen 

    '''

    pass


def window_new():
    '''Create a new window 

    '''

    pass


def window_new_main():
    '''Create a new main window with its own workspace and scene selection 

    '''

    pass
