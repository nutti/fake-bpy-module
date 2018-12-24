def background_image_add(name="Image",
                         filepath="",
                         filter_blender=False,
                         filter_backup=False,
                         filter_image=True,
                         filter_movie=True,
                         filter_python=False,
                         filter_font=False,
                         filter_sound=False,
                         filter_text=False,
                         filter_btx=False,
                         filter_collada=False,
                         filter_alembic=False,
                         filter_folder=True,
                         filter_blenlib=False,
                         filemode=9,
                         relative_path=True,
                         show_multiview=False,
                         use_multiview=False,
                         display_type='DEFAULT',
                         sort_method='FILE_SORT_ALPHA'):
    '''Add a new background image 

    :param name: Name, Image name to assign 
    :type name: string, (optional, never None)
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
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param show_multiview: Enable Multi-View 
    :type show_multiview: boolean, (optional)
    :param use_multiview: Use Multi-View 
    :type use_multiview: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def background_image_remove(index=0):
    '''Remove a background image from the 3D view 

    :param index: Index, Background image index to remove 
    :type index: int in [0, inf], (optional)
    '''

    pass


def camera_to_view():
    '''Set camera view to active view 

    '''

    pass


def camera_to_view_selected():
    '''Move the camera so selected objects are framed 

    '''

    pass


def clear_render_border():
    '''Clear the boundaries of the border render and disable border render 

    '''

    pass


def copybuffer():
    '''Selected objects are saved in a temp file 

    '''

    pass


def cursor3d(use_depth=True, orientation='VIEW'):
    '''Set the location of the 3D cursor 

    :param use_depth: Surface Project, Project onto the surface 
    :type use_depth: boolean, (optional)
    :param orientation: Orientation, Preset viewpoint to useNONE None, Leave orientation unchanged.VIEW View, Orient to the viewport.XFORM Transform, Orient to the current transform setting.GEOM Geometry, Match the surface normal. 
    :type orientation: enum in ['NONE', 'VIEW', 'XFORM', 'GEOM'], (optional)
    '''

    pass


def dolly(mx=0, my=0, delta=0, use_mouse_init=True):
    '''Dolly in/out in the view 

    :param mx: Region Position X 
    :type mx: int in [0, inf], (optional)
    :param my: Region Position Y 
    :type my: int in [0, inf], (optional)
    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    :param use_mouse_init: Mouse Init, Use initial mouse position 
    :type use_mouse_init: boolean, (optional)
    '''

    pass


def edit_mesh_extrude_individual_move():
    '''Extrude individual elements and move 

    '''

    pass


def edit_mesh_extrude_move_normal():
    '''Extrude and move along normals 

    '''

    pass


def edit_mesh_extrude_move_shrink_fatten():
    '''Extrude and move along individual normals 

    '''

    pass


def fly():
    '''Interactively fly around the scene 

    '''

    pass


def localview():
    '''Toggle display of selected object(s) separately and centered in view 

    '''

    pass


def localview_remove_from():
    '''Move selected objects out of local view 

    '''

    pass


def move(use_mouse_init=True):
    '''Move the view 

    :param use_mouse_init: Mouse Init, Use initial mouse position 
    :type use_mouse_init: boolean, (optional)
    '''

    pass


def navigate():
    '''Interactively navigate around the scene (uses the mode (walk/fly) preference) 

    '''

    pass


def ndof_all():
    '''Pan and rotate the view with the 3D mouse 

    '''

    pass


def ndof_orbit():
    '''Orbit the view using the 3D mouse 

    '''

    pass


def ndof_orbit_zoom():
    '''Orbit and zoom the view using the 3D mouse 

    '''

    pass


def ndof_pan():
    '''Pan the view with the 3D mouse 

    '''

    pass


def object_as_camera():
    '''Set the active object as the active camera for this view or scene 

    '''

    pass


def object_mode_pie_or_toggle():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def pastebuffer(autoselect=True, active_collection=True):
    '''Contents of copy buffer gets pasted 

    :param autoselect: Select, Select pasted objects 
    :type autoselect: boolean, (optional)
    :param active_collection: Active Collection, Put pasted objects on the active collection 
    :type active_collection: boolean, (optional)
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def render_border(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    '''Set the boundaries of the border render and enable border render 

    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def rotate(use_mouse_init=True):
    '''Rotate the view 

    :param use_mouse_init: Mouse Init, Use initial mouse position 
    :type use_mouse_init: boolean, (optional)
    '''

    pass


def ruler_add():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def select(extend=False,
           deselect=False,
           toggle=False,
           center=False,
           enumerate=False,
           object=False,
           location=(0, 0)):
    '''Select and activate item(s) 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param deselect: Deselect, Remove from selection 
    :type deselect: boolean, (optional)
    :param toggle: Toggle Selection, Toggle the selection 
    :type toggle: boolean, (optional)
    :param center: Center, Use the object center when selecting, in editmode used to extend object selection 
    :type center: boolean, (optional)
    :param enumerate: Enumerate, List objects under the mouse (object mode only) 
    :type enumerate: boolean, (optional)
    :param object: Object, Use object selection (editmode only) 
    :type object: boolean, (optional)
    :param location: Location, Mouse location 
    :type location: int array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_box(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True,
               mode='SET'):
    '''Select items using box selection 

    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    :param mode: Mode 
    :type mode: enum in ['SET', 'ADD', 'SUB', 'XOR', 'AND'], (optional)
    '''

    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, deselect=False):
    '''Select items using circle selection 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    :param radius: Radius 
    :type radius: int in [1, inf], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    '''

    pass


def select_lasso(path=None, mode='SET'):
    '''Select items using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param mode: Mode 
    :type mode: enum in ['SET', 'ADD', 'SUB', 'XOR', 'AND'], (optional)
    '''

    pass


def select_menu(name='', toggle=False):
    '''Menu object selection 

    :param name: Object Name 
    :type name: enum in [], (optional)
    :param toggle: Toggle, Toggle selection instead of deselecting everything first 
    :type toggle: boolean, (optional)
    '''

    pass


def select_or_deselect_all(extend=False,
                           toggle=False,
                           deselect=False,
                           center=False,
                           enumerate=False,
                           object=False):
    '''Select element under the mouse, deselect everything is there’s nothing under the mouse 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param toggle: Toggle, Toggle the selection 
    :type toggle: boolean, (optional)
    :param deselect: Deselect, Remove from selection 
    :type deselect: boolean, (optional)
    :param center: Center, Use the object center when selecting, in editmode used to extend object selection 
    :type center: boolean, (optional)
    :param enumerate: Enumerate, List objects under the mouse (object mode only) 
    :type enumerate: boolean, (optional)
    :param object: Object, Use object selection (editmode only) 
    :type object: boolean, (optional)
    '''

    pass


def smoothview():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def snap_cursor_to_active():
    '''Snap 3D cursor to the active item 

    '''

    pass


def snap_cursor_to_center():
    '''Snap 3D cursor to the world origin 

    '''

    pass


def snap_cursor_to_grid():
    '''Snap 3D cursor to the nearest grid division 

    '''

    pass


def snap_cursor_to_selected():
    '''Snap 3D cursor to the middle of the selected item(s) 

    '''

    pass


def snap_selected_to_active():
    '''Snap selected item(s) to the active item 

    '''

    pass


def snap_selected_to_cursor(use_offset=True):
    '''Snap selected item(s) to the 3D cursor 

    :param use_offset: Offset, If the selection should be snapped as a whole or by each object center 
    :type use_offset: boolean, (optional)
    '''

    pass


def snap_selected_to_grid():
    '''Snap selected item(s) to their nearest grid division 

    '''

    pass


def toggle_matcap_flip():
    '''Flip MatCap 

    '''

    pass


def toggle_shading(type='WIREFRAME'):
    '''Toggle shading type in 3D viewport 

    :param type: Type, Shading type to toggleWIREFRAME Wireframe, Toggle wireframe shading.SOLID Solid, Toggle solid shading.MATERIAL LookDev, Toggle lookdev shading.RENDERED Rendered, Toggle rendered shading. 
    :type type: enum in ['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED'], (optional)
    '''

    pass


def toggle_xray():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def toolshelf():
    '''Toggles tool shelf display 

    '''

    pass


def view_all(use_all_regions=False, center=False):
    '''View all objects in scene 

    :param use_all_regions: All Regions, View selected for all regions 
    :type use_all_regions: boolean, (optional)
    :param center: Center 
    :type center: boolean, (optional)
    '''

    pass


def view_axis(type='LEFT', align_active=False, relative=False):
    '''Use a preset viewpoint 

    :param type: View, Preset viewpoint to useLEFT Left, View From the Left.RIGHT Right, View From the Right.BOTTOM Bottom, View From the Bottom.TOP Top, View From the Top.FRONT Front, View From the Front.BACK Back, View From the Back. 
    :type type: enum in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'FRONT', 'BACK'], (optional)
    :param align_active: Align Active, Align to the active object’s axis 
    :type align_active: boolean, (optional)
    :param relative: Relative, Rotate relative to the current orientation 
    :type relative: boolean, (optional)
    '''

    pass


def view_camera():
    '''Toggle the camera view 

    '''

    pass


def view_center_camera():
    '''Center the camera view 

    '''

    pass


def view_center_cursor():
    '''Center the view so that the cursor is in the middle of the view 

    '''

    pass


def view_center_lock():
    '''Center the view lock offset 

    '''

    pass


def view_center_pick():
    '''Center the view to the Z-depth position under the mouse cursor 

    '''

    pass


def view_lock_clear():
    '''Clear all view locking 

    '''

    pass


def view_lock_to_active():
    '''Lock the view to the active object/bone 

    '''

    pass


def view_orbit(angle=0.0, type='ORBITLEFT'):
    '''Orbit the view 

    :param angle: Roll 
    :type angle: float in [-inf, inf], (optional)
    :param type: Orbit, Direction of View OrbitORBITLEFT Orbit Left, Orbit the view around to the Left.ORBITRIGHT Orbit Right, Orbit the view around to the Right.ORBITUP Orbit Up, Orbit the view Up.ORBITDOWN Orbit Down, Orbit the view Down. 
    :type type: enum in ['ORBITLEFT', 'ORBITRIGHT', 'ORBITUP', 'ORBITDOWN'], (optional)
    '''

    pass


def view_pan(type='PANLEFT'):
    '''Pan the view in a given direction 

    :param type: Pan, Direction of View PanPANLEFT Pan Left, Pan the view to the Left.PANRIGHT Pan Right, Pan the view to the Right.PANUP Pan Up, Pan the view Up.PANDOWN Pan Down, Pan the view Down. 
    :type type: enum in ['PANLEFT', 'PANRIGHT', 'PANUP', 'PANDOWN'], (optional)
    '''

    pass


def view_persportho():
    '''Switch the current view from perspective/orthographic projection 

    '''

    pass


def view_roll(angle=0.0, type='ANGLE'):
    '''Roll the view 

    :param angle: Roll 
    :type angle: float in [-inf, inf], (optional)
    :param type: Roll Angle Source, How roll angle is calculatedANGLE Roll Angle, Roll the view using an angle value.LEFT Roll Left, Roll the view around to the Left.RIGHT Roll Right, Roll the view around to the Right. 
    :type type: enum in ['ANGLE', 'LEFT', 'RIGHT'], (optional)
    '''

    pass


def view_selected(use_all_regions=False):
    '''Move the view to the selection center 

    :param use_all_regions: All Regions, View selected for all regions 
    :type use_all_regions: boolean, (optional)
    '''

    pass


def walk():
    '''Interactively walk around the scene 

    '''

    pass


def zoom(mx=0, my=0, delta=0, use_mouse_init=True):
    '''Zoom in/out in the view 

    :param mx: Region Position X 
    :type mx: int in [0, inf], (optional)
    :param my: Region Position Y 
    :type my: int in [0, inf], (optional)
    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    :param use_mouse_init: Mouse Init, Use initial mouse position 
    :type use_mouse_init: boolean, (optional)
    '''

    pass


def zoom_border(xmin=0,
                xmax=0,
                ymin=0,
                ymax=0,
                wait_for_input=True,
                zoom_out=False):
    '''Zoom in the view to the nearest object contained in the border 

    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    :param zoom_out: Zoom Out 
    :type zoom_out: boolean, (optional)
    '''

    pass


def zoom_camera_1_to_1():
    '''Match the camera to 1:1 to the render output 

    '''

    pass
