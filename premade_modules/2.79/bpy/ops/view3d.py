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
    '''Add a new background image (Ctrl for Empty Object) 

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


def clip_border(xmin=0, xmax=0, ymin=0, ymax=0):
    '''Set the view clipping border 

    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    '''

    pass


def copybuffer():
    '''Selected objects are saved in a temp file 

    '''

    pass


def cursor3d():
    '''Set the location of the 3D cursor 

    '''

    pass


def dolly(delta=0, mx=0, my=0):
    '''Dolly in/out in the view 

    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    :param mx: Zoom Position X 
    :type mx: int in [0, inf], (optional)
    :param my: Zoom Position Y 
    :type my: int in [0, inf], (optional)
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


def enable_manipulator(translate=False, rotate=False, scale=False):
    '''Enable the transform manipulator for use 

    :param translate: Translate, Enable the translate manipulator 
    :type translate: boolean, (optional)
    :param rotate: Rotate, Enable the rotate manipulator 
    :type rotate: boolean, (optional)
    :param scale: Scale, Enable the scale manipulator 
    :type scale: boolean, (optional)
    '''

    pass


def fly():
    '''Interactively fly around the scene 

    '''

    pass


def game_start():
    '''Start game engine 

    '''

    pass


def layers(nr=1, extend=False, toggle=True):
    '''Toggle layer(s) visibility 

    :param nr: Number, The layer number to set, zero for all layers 
    :type nr: int in [0, 20], (optional)
    :param extend: Extend, Add this layer to the current view layers 
    :type extend: boolean, (optional)
    :param toggle: Toggle, Toggle the layer 
    :type toggle: boolean, (optional)
    '''

    pass


def localview():
    '''Toggle display of selected object(s) separately and centered in view 

    '''

    pass


def manipulator(
        constraint_axis=(False, False, False),
        constraint_orientation='GLOBAL',
        release_confirm=False,
        use_accurate=False,
        use_planar_constraint=False):
    '''Manipulate selected item by axis 

    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    :param use_planar_constraint: Planar Constraint, Limit the transformation to the two axes that have not been clicked (translate/scale only) 
    :type use_planar_constraint: boolean, (optional)
    '''

    pass


def move():
    '''Move the view 

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


def pastebuffer(autoselect=True, active_layer=True):
    '''Contents of copy buffer gets pasted 

    :param autoselect: Select, Select pasted objects 
    :type autoselect: boolean, (optional)
    :param active_layer: Active Layer, Put pasted objects on the active layer 
    :type active_layer: boolean, (optional)
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def render_border(xmin=0, xmax=0, ymin=0, ymax=0, camera_only=False):
    '''Set the boundaries of the border render and enable border render 

    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param camera_only: Camera Only, Set render border for camera view and final render only 
    :type camera_only: boolean, (optional)
    '''

    pass


def rotate():
    '''Rotate the view 

    '''

    pass


def ruler():
    '''Interactive ruler 

    '''

    pass


def select(extend=False,
           deselect=False,
           toggle=False,
           center=False,
           enumerate=False,
           object=False,
           location=(0, 0)):
    '''Activate/select item(s) 

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


def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    '''Select items using border selection 

    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int in [-inf, inf], (optional)
    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_circle(x=0, y=0, radius=1, gesture_mode=0):
    '''Select items using circle selection 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    :param radius: Radius 
    :type radius: int in [1, inf], (optional)
    :param gesture_mode: Event Type 
    :type gesture_mode: int in [-inf, inf], (optional)
    '''

    pass


def select_lasso(path=None, deselect=False, extend=True):
    '''Select items using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
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
    '''Undocumented 

    '''

    pass


def snap_cursor_to_active():
    '''Snap cursor to active item 

    '''

    pass


def snap_cursor_to_center():
    '''Snap cursor to the Center 

    '''

    pass


def snap_cursor_to_grid():
    '''Snap cursor to nearest grid division 

    '''

    pass


def snap_cursor_to_selected():
    '''Snap cursor to center of selected item(s) 

    '''

    pass


def snap_selected_to_active():
    '''Snap selected item(s) to the active item 

    '''

    pass


def snap_selected_to_cursor(use_offset=True):
    '''Snap selected item(s) to cursor 

    :param use_offset: Offset 
    :type use_offset: boolean, (optional)
    '''

    pass


def snap_selected_to_grid():
    '''Snap selected item(s) to nearest grid division 

    '''

    pass


def toggle_render():
    '''Toggle rendered shading mode of the viewport 

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
    '''Pan the view 

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


def viewnumpad(type='LEFT', align_active=False):
    '''Use a preset viewpoint 

    :param type: View, Preset viewpoint to useLEFT Left, View From the Left.RIGHT Right, View From the Right.BOTTOM Bottom, View From the Bottom.TOP Top, View From the Top.FRONT Front, View From the Front.BACK Back, View From the Back.CAMERA Camera, View From the Active Camera. 
    :type type: enum in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'FRONT', 'BACK', 'CAMERA'], (optional)
    :param align_active: Align Active, Align to the active object’s axis 
    :type align_active: boolean, (optional)
    '''

    pass


def walk():
    '''Interactively walk around the scene 

    '''

    pass


def zoom(delta=0, mx=0, my=0):
    '''Zoom in/out in the view 

    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    :param mx: Zoom Position X 
    :type mx: int in [0, inf], (optional)
    :param my: Zoom Position Y 
    :type my: int in [0, inf], (optional)
    '''

    pass


def zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    '''Zoom in the view to the nearest object contained in the border 

    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int in [-inf, inf], (optional)
    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    '''

    pass


def zoom_camera_1_to_1():
    '''Match the camera to 1:1 to the render output 

    '''

    pass
