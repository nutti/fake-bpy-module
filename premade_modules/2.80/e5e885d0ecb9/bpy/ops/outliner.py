def action_set(action=''):
    '''Change the active action used 

    :param action: Action 
    :type action: enum in [], (optional)
    '''

    pass


def animdata_operation(type='CLEAR_ANIMDATA'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Animation OperationCLEAR_ANIMDATA Clear Animation Data, Remove this animation data container.SET_ACT Set Action.CLEAR_ACT Unlink Action.REFRESH_DRIVERS Refresh Drivers.CLEAR_DRIVERS Clear Drivers. 
    :type type: enum in ['CLEAR_ANIMDATA', 'SET_ACT', 'CLEAR_ACT', 'REFRESH_DRIVERS', 'CLEAR_DRIVERS'], (optional)
    '''

    pass


def collection_delete(hierarchy=False):
    '''Delete selected collections 

    :param hierarchy: Hierarchy, Delete child objects and collections 
    :type hierarchy: boolean, (optional)
    '''

    pass


def collection_drop():
    '''Drag to move to collection in Outliner 

    '''

    pass


def collection_duplicate():
    '''Duplicate selected collections 

    '''

    pass


def collection_exclude_clear():
    '''Include collection in the active view layer 

    '''

    pass


def collection_exclude_set():
    '''Exclude collection from the active view layer 

    '''

    pass


def collection_holdout_clear():
    '''Clear masking of collection in the active view layer 

    '''

    pass


def collection_holdout_set():
    '''Mask collection in the active view layer 

    '''

    pass


def collection_indirect_only_clear():
    '''Clear collection contributing only indirectly in the view layer 

    '''

    pass


def collection_indirect_only_set():
    '''Set collection to only contribute indirectly (through shadows and reflections) in the view layer 

    '''

    pass


def collection_instance():
    '''Instance selected collections to active scene 

    '''

    pass


def collection_link():
    '''Link selected collections to active scene 

    '''

    pass


def collection_new(nested=True):
    '''Add a new collection inside selected collection 

    :param nested: Nested, Add as child of selected collection 
    :type nested: boolean, (optional)
    '''

    pass


def collection_objects_deselect():
    '''Deselect objects in collection 

    '''

    pass


def collection_objects_select():
    '''Select objects in collection 

    '''

    pass


def constraint_operation(type='ENABLE'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Constraint Operation 
    :type type: enum in ['ENABLE', 'DISABLE', 'DELETE'], (optional)
    '''

    pass


def data_operation(type='SELECT'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

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


def highlight_update():
    '''Update the item highlight based on the current mouse position 

    '''

    pass


def id_delete():
    '''Delete the ID under cursor 

    '''

    pass


def id_operation(type='UNLINK'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: ID data OperationUNLINK Unlink.LOCAL Make Local.STATIC_OVERRIDE Add Static Override, Add a local static override of this data-block.SINGLE Make Single User.DELETE Delete, WARNING: no undo.REMAP Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.ADD_FAKE Add Fake User, Ensure data-block gets saved even if it isn’t in use (e.g. for motion and material libraries).CLEAR_FAKE Clear Fake User.RENAME Rename.SELECT_LINKED Select Linked. 
    :type type: enum in ['UNLINK', 'LOCAL', 'STATIC_OVERRIDE', 'SINGLE', 'DELETE', 'REMAP', 'ADD_FAKE', 'CLEAR_FAKE', 'RENAME', 'SELECT_LINKED'], (optional)
    '''

    pass


def id_remap(id_type='OBJECT', old_id='', new_id=''):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param id_type: ID Type 
    :type id_type: enum in ['ACTION', 'ARMATURE', 'BRUSH', 'CAMERA', 'CACHEFILE', 'CURVE', 'FONT', 'GREASEPENCIL', 'COLLECTION', 'IMAGE', 'KEY', 'LIGHT', 'LIBRARY', 'LINESTYLE', 'LATTICE', 'MASK', 'MATERIAL', 'META', 'MESH', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'LIGHT_PROBE', 'SCENE', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'WINDOWMANAGER', 'WORLD', 'WORKSPACE'], (optional)
    :param old_id: Old ID, Old ID to replace 
    :type old_id: enum in [], (optional)
    :param new_id: New ID, New ID to remap all selected IDs’ users to 
    :type new_id: enum in [], (optional)
    '''

    pass


def item_activate(extend=True, recursive=False):
    '''Handle mouse clicks to select and activate items 

    :param extend: Extend, Extend selection for activation 
    :type extend: boolean, (optional)
    :param recursive: Recursive, Select Objects and their children 
    :type recursive: boolean, (optional)
    '''

    pass


def item_drag_drop():
    '''Drag and drop element to another place 

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
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Library OperationRENAME Rename.DELETE Delete, Delete this library and all its item from Blender - WARNING: no undo.RELOCATE Relocate, Select a new path for this library, and reload all its data.RELOAD Reload, Reload all data from this library. 
    :type type: enum in ['RENAME', 'DELETE', 'RELOCATE', 'RELOAD'], (optional)
    '''

    pass


def lib_relocate():
    '''Relocate the library under cursor 

    '''

    pass


def material_drop():
    '''Drag material to object in Outliner 

    '''

    pass


def modifier_operation(type='TOGVIS'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Modifier Operation 
    :type type: enum in ['TOGVIS', 'TOGREN', 'DELETE'], (optional)
    '''

    pass


def object_operation(type='SELECT'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Object OperationSELECT Select.DESELECT Deselect.SELECT_HIERARCHY Select Hierarchy.DELETE Delete.DELETE_HIERARCHY Delete Hierarchy.REMAP Remap Users, Make all users of selected data-blocks to use instead a new chosen one.RENAME Rename.OBJECT_MODE_ENTER Enter Mode.OBJECT_MODE_EXIT Exit Mode. 
    :type type: enum in ['SELECT', 'DESELECT', 'SELECT_HIERARCHY', 'DELETE', 'DELETE_HIERARCHY', 'REMAP', 'RENAME', 'OBJECT_MODE_ENTER', 'OBJECT_MODE_EXIT'], (optional)
    '''

    pass


def operation():
    '''Context menu for item operations 

    '''

    pass


def orphans_purge():
    '''Clear all orphaned data-blocks without any users from the file (cannot be undone, saves to current .blend file) 

    '''

    pass


def parent_clear():
    '''Drag to clear parent in Outliner 

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


def scene_drop():
    '''Drag object to scene in Outliner 

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


def select_all(action='TOGGLE'):
    '''Toggle the Outliner selection of items 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_box(xmin=0,
               xmax=0,
               ymin=0,
               ymax=0,
               wait_for_input=True,
               deselect=False):
    '''Use box selection to select tree elements 

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
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
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
