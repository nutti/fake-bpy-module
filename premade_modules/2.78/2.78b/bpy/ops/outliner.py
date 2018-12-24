def action_set(action=''):
    '''Change the active action used 

    :param action: Action 
    :type action: enum in [], (optional)
    '''

    pass


def animdata_operation(type='CLEAR_ANIMDATA'):
    '''Undocumented 

    :param type: Animation OperationCLEAR_ANIMDATA Clear Animation Data, Remove this animation data container.SET_ACT Set Action.CLEAR_ACT Unlink Action.REFRESH_DRIVERS Refresh Drivers.CLEAR_DRIVERS Clear Drivers. 
    :type type: enum in ['CLEAR_ANIMDATA', 'SET_ACT', 'CLEAR_ACT', 'REFRESH_DRIVERS', 'CLEAR_DRIVERS'], (optional)
    '''

    pass


def constraint_operation(type='ENABLE'):
    '''Undocumented 

    :param type: Constraint Operation 
    :type type: enum in ['ENABLE', 'DISABLE', 'DELETE'], (optional)
    '''

    pass


def data_operation(type='SELECT'):
    '''Undocumented 

    :param type: Data Operation 
    :type type: enum in ['SELECT', 'DESELECT', 'HIDE', 'UNHIDE', 'SELECT_LINKED'], (optional)
    '''

    pass


def drivers_add_selected():
    '''Add drivers to selected items 

    '''

    pass


def drivers_delete_selected():
    '''Delete drivers assigned to selected items 

    '''

    pass


def expanded_toggle():
    '''Expand/Collapse all items 

    '''

    pass


def group_link(object="Object"):
    '''Link Object to Group in Outliner 

    :param object: Object, Target Object 
    :type object: string, (optional, never None)
    '''

    pass


def group_operation(type='UNLINK'):
    '''Undocumented 

    :param type: Group OperationUNLINK Unlink Group.LOCAL Make Local Group.LINK Link Group Objects to Scene.DELETE Delete Group, WARNING: no undo.REMAP Remap Users, Make all users of selected datablocks to use instead current (clicked) one.INSTANCE Instance Groups in Scene.TOGVIS Toggle Visible Group.TOGSEL Toggle Selectable.TOGREN Toggle Renderable.RENAME Rename. 
    :type type: enum in ['UNLINK', 'LOCAL', 'LINK', 'DELETE', 'REMAP', 'INSTANCE', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)
    '''

    pass


def id_delete():
    '''Delete the ID under cursor 

    '''

    pass


def id_operation(type='UNLINK'):
    '''Undocumented 

    :param type: ID data OperationUNLINK Unlink.LOCAL Make Local.SINGLE Make Single User.DELETE Delete, WARNING: no undo.REMAP Remap Users, Make all users of selected datablocks to use instead current (clicked) one.ADD_FAKE Add Fake User, Ensure datablock gets saved even if it isn’t in use (e.g. for motion and material libraries).CLEAR_FAKE Clear Fake User.RENAME Rename.SELECT_LINKED Select Linked. 
    :type type: enum in ['UNLINK', 'LOCAL', 'SINGLE', 'DELETE', 'REMAP', 'ADD_FAKE', 'CLEAR_FAKE', 'RENAME', 'SELECT_LINKED'], (optional)
    '''

    pass


def id_remap(id_type='OBJECT', old_id='', new_id=''):
    '''Undocumented 

    :param id_type: ID Type 
    :type id_type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'GROUP', 'IMAGE', 'KEY', 'LAMP', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD'], (optional)
    :param old_id: Old ID, Old ID to replace 
    :type old_id: enum in [], (optional)
    :param new_id: New ID, New ID to remap all selected IDs’ users to 
    :type new_id: enum in [], (optional)
    '''

    pass


def item_activate(extend=True, recursive=False):
    '''Handle mouse clicks to activate/select items 

    :param extend: Extend, Extend selection for activation 
    :type extend: boolean, (optional)
    :param recursive: Recursive, Select Objects and their children 
    :type recursive: boolean, (optional)
    '''

    pass


def item_openclose(all=True):
    '''Toggle whether item under cursor is enabled or closed 

    :param all: All, Close or open all items 
    :type all: boolean, (optional)
    '''

    pass


def item_rename():
    '''Rename item under cursor 

    '''

    pass


def keyingset_add_selected():
    '''Add selected items (blue-gray rows) to active Keying Set 

    '''

    pass


def keyingset_remove_selected():
    '''Remove selected items (blue-gray rows) from active Keying Set 

    '''

    pass


def lib_operation(type='RENAME'):
    '''Undocumented 

    :param type: Library OperationRENAME Rename.DELETE Delete, Delete this library and all its item from Blender - WARNING: no undo.RELOCATE Relocate, Select a new path for this library, and reload all its data.RELOAD Reload, Reload all data from this library. 
    :type type: enum in ['RENAME', 'DELETE', 'RELOCATE', 'RELOAD'], (optional)
    '''

    pass


def lib_relocate():
    '''Relocate the library under cursor 

    '''

    pass


def material_drop(object="Object", material="Material"):
    '''Drag material to object in Outliner 

    :param object: Object, Target Object 
    :type object: string, (optional, never None)
    :param material: Material, Target Material 
    :type material: string, (optional, never None)
    '''

    pass


def modifier_operation(type='TOGVIS'):
    '''Undocumented 

    :param type: Modifier Operation 
    :type type: enum in ['TOGVIS', 'TOGREN', 'DELETE'], (optional)
    '''

    pass


def object_operation(type='SELECT'):
    '''Undocumented 

    :param type: Object OperationSELECT Select.DESELECT Deselect.SELECT_HIERARCHY Select Hierarchy.DELETE Delete.DELETE_HIERARCHY Delete Hierarchy.REMAP Remap Users, Make all users of selected datablocks to use instead a new chosen one.TOGVIS Toggle Visible.TOGSEL Toggle Selectable.TOGREN Toggle Renderable.RENAME Rename. 
    :type type: enum in ['SELECT', 'DESELECT', 'SELECT_HIERARCHY', 'DELETE', 'DELETE_HIERARCHY', 'REMAP', 'TOGVIS', 'TOGSEL', 'TOGREN', 'RENAME'], (optional)
    '''

    pass


def operation():
    '''Context menu for item operations 

    '''

    pass


def orphans_purge():
    '''Clear all orphaned datablocks without any users from the file (cannot be undone) 

    '''

    pass


def parent_clear(dragged_obj="Object", type='CLEAR'):
    '''Drag to clear parent in Outliner 

    :param dragged_obj: Child, Child Object 
    :type dragged_obj: string, (optional, never None)
    :param type: TypeCLEAR Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.CLEAR_KEEP_TRANSFORM Clear and Keep Transformation, As ‘Clear Parent’, but keep the current visual transformations of the object.CLEAR_INVERSE Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself. 
    :type type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional)
    '''

    pass


def parent_drop(child="Object", parent="Object", type='OBJECT'):
    '''Drag to parent in Outliner 

    :param child: Child, Child Object 
    :type child: string, (optional, never None)
    :param parent: Parent, Parent Object 
    :type parent: string, (optional, never None)
    :param type: Type 
    :type type: enum in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional)
    '''

    pass


def renderability_toggle():
    '''Toggle the renderability of selected items 

    '''

    pass


def scene_drop(object="Object", scene="Scene"):
    '''Drag object to scene in Outliner 

    :param object: Object, Target Object 
    :type object: string, (optional, never None)
    :param scene: Scene, Target Scene 
    :type scene: string, (optional, never None)
    '''

    pass


def scene_operation(type='DELETE'):
    '''Context menu for scene operations 

    :param type: Scene Operation 
    :type type: enum in ['DELETE'], (optional)
    '''

    pass


def scroll_page(up=False):
    '''Scroll page up or down 

    :param up: Up, Scroll up one page 
    :type up: boolean, (optional)
    '''

    pass


def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    '''Use box selection to select tree elements 

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


def selectability_toggle():
    '''Toggle the selectability 

    '''

    pass


def selected_toggle():
    '''Toggle the Outliner selection of items 

    '''

    pass


def show_active():
    '''Open up the tree and adjust the view so that the active Object is shown centered 

    '''

    pass


def show_hierarchy():
    '''Open all object entries and close all others 

    '''

    pass


def show_one_level(open=True):
    '''Expand/collapse all entries by one level 

    :param open: Open, Expand all entries one level deep 
    :type open: boolean, (optional)
    '''

    pass


def visibility_toggle():
    '''Toggle the visibility of selected items 

    '''

    pass
