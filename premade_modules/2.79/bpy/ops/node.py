def add_and_link_node(type="",
                      use_transform=False,
                      settings=None,
                      link_socket_index=0):
    '''Add a node to the active tree and link to an existing socket 

    :param type: Node Type, Node type 
    :type type: string, (optional, never None)
    :param use_transform: Use Transform, Start transform operator after inserting the node 
    :type use_transform: boolean, (optional)
    :param settings: Settings, Settings to be applied on the newly created node 
    :type settings: bpy_prop_collection of NodeSetting, (optional)
    :param link_socket_index: Link Socket Index, Index of the socket to link 
    :type link_socket_index: int in [-inf, inf], (optional)
    '''

    pass


def add_file(filepath="",
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
             sort_method='FILE_SORT_ALPHA',
             name="Image"):
    '''Add a file node to the current node editor 

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
    :param name: Name, Data-block name to assign 
    :type name: string, (optional, never None)
    '''

    pass


def add_mask(name="Mask"):
    '''Add a mask node to the current node editor 

    :param name: Name, Data-block name to assign 
    :type name: string, (optional, never None)
    '''

    pass


def add_node(type="", use_transform=False, settings=None):
    '''Add a node to the active tree 

    :param type: Node Type, Node type 
    :type type: string, (optional, never None)
    :param use_transform: Use Transform, Start transform operator after inserting the node 
    :type use_transform: boolean, (optional)
    :param settings: Settings, Settings to be applied on the newly created node 
    :type settings: bpy_prop_collection of NodeSetting, (optional)
    '''

    pass


def add_reroute(path=None, cursor=6):
    '''Add a reroute node 

    :param path: path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param cursor: Cursor 
    :type cursor: int in [0, inf], (optional)
    '''

    pass


def add_search(type="", use_transform=False, settings=None, node_item=''):
    '''Add a node to the active tree 

    :param type: Node Type, Node type 
    :type type: string, (optional, never None)
    :param use_transform: Use Transform, Start transform operator after inserting the node 
    :type use_transform: boolean, (optional)
    :param settings: Settings, Settings to be applied on the newly created node 
    :type settings: bpy_prop_collection of NodeSetting, (optional)
    :param node_item: Node Type, Node type 
    :type node_item: enum in [], (optional)
    '''

    pass


def attach():
    '''Attach active node to a frame 

    '''

    pass


def backimage_fit():
    '''Fit the background image to the view 

    '''

    pass


def backimage_move():
    '''Move Node backdrop 

    '''

    pass


def backimage_sample():
    '''Use mouse to sample background image 

    '''

    pass


def backimage_zoom(factor=1.2):
    '''Zoom in/out the background image 

    :param factor: Factor 
    :type factor: float in [0, 10], (optional)
    '''

    pass


def clear_viewer_border():
    '''Clear the boundaries for viewer operations 

    '''

    pass


def clipboard_copy():
    '''Copies selected nodes to the clipboard 

    '''

    pass


def clipboard_paste():
    '''Pastes nodes from the clipboard to the active node tree 

    '''

    pass


def collapse_hide_unused_toggle():
    '''Toggle collapsed nodes and hide unused sockets 

    '''

    pass


def delete():
    '''Delete selected nodes 

    '''

    pass


def delete_reconnect():
    '''Delete nodes; will reconnect nodes as if deletion was muted 

    '''

    pass


def detach():
    '''Detach selected nodes from parents 

    '''

    pass


def detach_translate_attach(NODE_OT_detach=None,
                            TRANSFORM_OT_translate=None,
                            NODE_OT_attach=None):
    '''Detach nodes, move and attach to frame 

    :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents 
    :type NODE_OT_detach: NODE_OT_detach, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame 
    :type NODE_OT_attach: NODE_OT_attach, (optional)
    '''

    pass


def duplicate(keep_inputs=False):
    '''Duplicate selected nodes 

    :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes 
    :type keep_inputs: boolean, (optional)
    '''

    pass


def duplicate_move(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
    '''Duplicate selected nodes and move them 

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes 
    :type NODE_OT_duplicate: NODE_OT_duplicate, (optional)
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame 
    :type NODE_OT_translate_attach: NODE_OT_translate_attach, (optional)
    '''

    pass


def duplicate_move_keep_inputs(NODE_OT_duplicate=None,
                               NODE_OT_translate_attach=None):
    '''Duplicate selected nodes keeping input links and move them 

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes 
    :type NODE_OT_duplicate: NODE_OT_duplicate, (optional)
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame 
    :type NODE_OT_translate_attach: NODE_OT_translate_attach, (optional)
    '''

    pass


def find_node(prev=False):
    '''Search for named node and allow to select and activate it 

    :param prev: Previous 
    :type prev: boolean, (optional)
    '''

    pass


def group_edit(exit=False):
    '''Edit node group 

    :param exit: Exit 
    :type exit: boolean, (optional)
    '''

    pass


def group_insert():
    '''Insert selected nodes into a node group 

    '''

    pass


def group_make():
    '''Make group from selected nodes 

    '''

    pass


def group_separate(type='COPY'):
    '''Separate selected nodes from the node group 

    :param type: TypeCOPY Copy, Copy to parent node tree, keep group intact.MOVE Move, Move to parent node tree, remove from group. 
    :type type: enum in ['COPY', 'MOVE'], (optional)
    '''

    pass


def group_ungroup():
    '''Ungroup selected nodes 

    '''

    pass


def hide_socket_toggle():
    '''Toggle unused node socket display 

    '''

    pass


def hide_toggle():
    '''Toggle hiding of selected nodes 

    '''

    pass


def insert_offset():
    '''Automatically offset nodes on insertion 

    '''

    pass


def join():
    '''Attach selected nodes to a new common frame 

    '''

    pass


def link(detach=False):
    '''Use the mouse to create a link between two nodes 

    :param detach: Detach, Detach and redirect existing links 
    :type detach: boolean, (optional)
    '''

    pass


def link_make(replace=False):
    '''Makes a link between selected output in input sockets 

    :param replace: Replace, Replace socket connections with the new links 
    :type replace: boolean, (optional)
    '''

    pass


def link_viewer():
    '''Link to viewer node 

    '''

    pass


def links_cut(path=None, cursor=9):
    '''Use the mouse to cut (remove) some links 

    :param path: path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param cursor: Cursor 
    :type cursor: int in [0, inf], (optional)
    '''

    pass


def links_detach():
    '''Remove all links to selected nodes, and try to connect neighbor nodes together 

    '''

    pass


def move_detach_links(NODE_OT_links_detach=None,
                      TRANSFORM_OT_translate=None,
                      NODE_OT_insert_offset=None):
    '''Move a node to detach links 

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together 
    :type NODE_OT_links_detach: NODE_OT_links_detach, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion 
    :type NODE_OT_insert_offset: NODE_OT_insert_offset, (optional)
    '''

    pass


def move_detach_links_release(NODE_OT_links_detach=None,
                              NODE_OT_translate_attach=None):
    '''Move a node to detach links 

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together 
    :type NODE_OT_links_detach: NODE_OT_links_detach, (optional)
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame 
    :type NODE_OT_translate_attach: NODE_OT_translate_attach, (optional)
    '''

    pass


def mute_toggle():
    '''Toggle muting of the nodes 

    '''

    pass


def new_node_tree(type='', name="NodeTree"):
    '''Create a new node tree 

    :param type: Tree Type 
    :type type: enum in [], (optional)
    :param name: Name 
    :type name: string, (optional, never None)
    '''

    pass


def node_color_preset_add(name="", remove_active=False):
    '''Add or remove a Node Color Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def node_copy_color():
    '''Copy color to all selected nodes 

    '''

    pass


def options_toggle():
    '''Toggle option buttons display for selected nodes 

    '''

    pass


def output_file_add_socket(file_path="Image"):
    '''Add a new input to a file output node 

    :param file_path: File Path, Sub-path of the output file 
    :type file_path: string, (optional, never None)
    '''

    pass


def output_file_move_active_socket(direction='DOWN'):
    '''Move the active input of a file output node up or down the list 

    :param direction: Direction 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def output_file_remove_active_socket():
    '''Remove active input from a file output node 

    '''

    pass


def parent_set():
    '''Attach selected nodes 

    '''

    pass


def preview_toggle():
    '''Toggle preview display for selected nodes 

    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def read_fullsamplelayers():
    '''Read all render layers of current scene, in full sample 

    '''

    pass


def read_renderlayers():
    '''Read all render layers of all used scenes 

    '''

    pass


def render_changed():
    '''Render current scene, when input node’s layer has been changed 

    '''

    pass


def resize():
    '''Resize a node 

    '''

    pass


def select(mouse_x=0, mouse_y=0, extend=False):
    '''Select the node under the cursor 

    :param mouse_x: Mouse X 
    :type mouse_x: int in [-inf, inf], (optional)
    :param mouse_y: Mouse Y 
    :type mouse_y: int in [-inf, inf], (optional)
    :param extend: Extend 
    :type extend: boolean, (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''(De)select all nodes 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_border(gesture_mode=0,
                  xmin=0,
                  xmax=0,
                  ymin=0,
                  ymax=0,
                  extend=True,
                  tweak=False):
    '''Use box selection to select nodes 

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
    :param tweak: Tweak, Only activate when mouse is not over a node - useful for tweak gesture 
    :type tweak: boolean, (optional)
    '''

    pass


def select_circle(x=0, y=0, radius=1, gesture_mode=0):
    '''Use circle selection to select nodes 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    :param radius: Radius 
    :type radius: int in [1, inf], (optional)
    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int in [-inf, inf], (optional)
    '''

    pass


def select_grouped(extend=False, type='TYPE'):
    '''Select nodes with similar properties 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param type: Type 
    :type type: enum in ['TYPE', 'COLOR', 'PREFIX', 'SUFFIX'], (optional)
    '''

    pass


def select_lasso(path=None, deselect=False, extend=True):
    '''Select nodes using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_link_viewer(NODE_OT_select=None, NODE_OT_link_viewer=None):
    '''Select node and link it to a viewer node 

    :param NODE_OT_select: Select, Select the node under the cursor 
    :type NODE_OT_select: NODE_OT_select, (optional)
    :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node 
    :type NODE_OT_link_viewer: NODE_OT_link_viewer, (optional)
    '''

    pass


def select_linked_from():
    '''Select nodes linked from the selected ones 

    '''

    pass


def select_linked_to():
    '''Select nodes linked to the selected ones 

    '''

    pass


def select_same_type_step(prev=False):
    '''Activate and view same node type, step by step 

    :param prev: Previous 
    :type prev: boolean, (optional)
    '''

    pass


def shader_script_update():
    '''Update shader script node with new sockets and options from the script 

    '''

    pass


def switch_view_update():
    '''Update views of selected node 

    '''

    pass


def toolbar():
    '''Toggles tool shelf display 

    '''

    pass


def translate_attach(TRANSFORM_OT_translate=None,
                     NODE_OT_attach=None,
                     NODE_OT_insert_offset=None):
    '''Move nodes and attach to frame 

    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame 
    :type NODE_OT_attach: NODE_OT_attach, (optional)
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion 
    :type NODE_OT_insert_offset: NODE_OT_insert_offset, (optional)
    '''

    pass


def translate_attach_remove_on_cancel(TRANSFORM_OT_translate=None,
                                      NODE_OT_attach=None,
                                      NODE_OT_insert_offset=None):
    '''Move nodes and attach to frame 

    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame 
    :type NODE_OT_attach: NODE_OT_attach, (optional)
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion 
    :type NODE_OT_insert_offset: NODE_OT_insert_offset, (optional)
    '''

    pass


def tree_path_parent():
    '''Go to parent node tree 

    '''

    pass


def tree_socket_add(in_out='IN'):
    '''Add an input or output socket to the current node tree 

    :param in_out: Socket Type 
    :type in_out: enum in ['IN', 'OUT'], (optional)
    '''

    pass


def tree_socket_move(direction='UP'):
    '''Move a socket up or down in the current node tree’s sockets stack 

    :param direction: Direction 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def tree_socket_remove():
    '''Remove an input or output socket to the current node tree 

    '''

    pass


def view_all():
    '''Resize view so you can see all nodes 

    '''

    pass


def view_selected():
    '''Resize view so you can see selected nodes 

    '''

    pass


def viewer_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    '''Set the boundaries for viewer operations 

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
