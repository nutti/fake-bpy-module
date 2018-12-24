def add_feather_vertex(location=(0.0, 0.0)):
    '''Add vertex to feather 

    :param location: Location, Location of vertex in normalized space 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def add_feather_vertex_slide(MASK_OT_add_feather_vertex=None,
                             MASK_OT_slide_point=None):
    '''Add new vertex to feather and slide it 

    :param MASK_OT_add_feather_vertex: Add Feather Vertex, Add vertex to feather 
    :type MASK_OT_add_feather_vertex: MASK_OT_add_feather_vertex, (optional)
    :param MASK_OT_slide_point: Slide Point, Slide control points 
    :type MASK_OT_slide_point: MASK_OT_slide_point, (optional)
    '''

    pass


def add_vertex(location=(0.0, 0.0)):
    '''Add vertex to active spline 

    :param location: Location, Location of vertex in normalized space 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def add_vertex_slide(MASK_OT_add_vertex=None, MASK_OT_slide_point=None):
    '''Add new vertex and slide it 

    :param MASK_OT_add_vertex: Add Vertex, Add vertex to active spline 
    :type MASK_OT_add_vertex: MASK_OT_add_vertex, (optional)
    :param MASK_OT_slide_point: Slide Point, Slide control points 
    :type MASK_OT_slide_point: MASK_OT_slide_point, (optional)
    '''

    pass


def copy_splines():
    '''Copy selected splines to clipboard 

    '''

    pass


def cyclic_toggle():
    '''Toggle cyclic for selected splines 

    '''

    pass


def delete():
    '''Delete selected control points or splines 

    '''

    pass


def duplicate():
    '''Duplicate selected control points and segments between them 

    '''

    pass


def duplicate_move(MASK_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Duplicate mask and move 

    :param MASK_OT_duplicate: Duplicate Mask, Duplicate selected control points and segments between them 
    :type MASK_OT_duplicate: MASK_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def feather_weight_clear():
    '''Reset the feather weight to zero 

    '''

    pass


def handle_type_set(type='AUTO'):
    '''Set type of handles for selected control points 

    :param type: Type, Spline type 
    :type type: enum in ['AUTO', 'VECTOR', 'ALIGNED', 'ALIGNED_DOUBLESIDE', 'FREE'], (optional)
    '''

    pass


def hide_view_clear():
    '''Reveal the layer by setting the hide flag 

    '''

    pass


def hide_view_set(unselected=False):
    '''Hide the layer by setting the hide flag 

    :param unselected: Unselected, Hide unselected rather than selected layers 
    :type unselected: boolean, (optional)
    '''

    pass


def layer_move(direction='UP'):
    '''Move the active layer up/down in the list 

    :param direction: Direction, Direction to move the active layer 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def layer_new(name=""):
    '''Add new mask layer for masking 

    :param name: Name, Name of new mask layer 
    :type name: string, (optional, never None)
    '''

    pass


def layer_remove():
    '''Remove mask layer 

    '''

    pass


def new(name=""):
    '''Create new mask 

    :param name: Name, Name of new mask 
    :type name: string, (optional, never None)
    '''

    pass


def normals_make_consistent():
    '''Re-calculate the direction of selected handles 

    '''

    pass


def parent_clear():
    '''Clear the mask’s parenting 

    '''

    pass


def parent_set():
    '''Set the mask’s parenting 

    '''

    pass


def paste_splines():
    '''Paste splines from clipboard 

    '''

    pass


def primitive_circle_add(size=100.0, location=(0.0, 0.0)):
    '''Add new circle-shaped spline 

    :param size: Size, Size of new circle 
    :type size: float in [-inf, inf], (optional)
    :param location: Location, Location of new circle 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def primitive_square_add(size=100.0, location=(0.0, 0.0)):
    '''Add new square-shaped spline 

    :param size: Size, Size of new circle 
    :type size: float in [-inf, inf], (optional)
    :param location: Location, Location of new circle 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select(extend=False, deselect=False, toggle=False, location=(0.0, 0.0)):
    '''Select spline points 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param deselect: Deselect, Remove from selection 
    :type deselect: boolean, (optional)
    :param toggle: Toggle Selection, Toggle the selection 
    :type toggle: boolean, (optional)
    :param location: Location, Location of vertex in normalized space 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all curve points 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    '''Select curve points using border selection 

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
    '''Select curve points using circle selection 

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


def select_lasso(path=None, deselect=False, extend=True):
    '''Select curve points using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Deselect spline points at the boundary of each selection region 

    '''

    pass


def select_linked():
    '''Select all curve points linked to already selected ones 

    '''

    pass


def select_linked_pick(deselect=False):
    '''(De)select all points linked to the curve under the mouse cursor 

    :param deselect: Deselect 
    :type deselect: boolean, (optional)
    '''

    pass


def select_more():
    '''Select more spline points connected to initial selection 

    '''

    pass


def shape_key_clear():
    '''Undocumented 

    '''

    pass


def shape_key_feather_reset():
    '''Reset feather weights on all selected points animation values 

    '''

    pass


def shape_key_insert():
    '''Undocumented 

    '''

    pass


def shape_key_rekey(location=True, feather=True):
    '''Recalculate animation data on selected points for frames selected in the dopesheet 

    :param location: Location 
    :type location: boolean, (optional)
    :param feather: Feather 
    :type feather: boolean, (optional)
    '''

    pass


def slide_point(slide_feather=False, is_new_point=False):
    '''Slide control points 

    :param slide_feather: Slide Feather, First try to slide feather instead of vertex 
    :type slide_feather: boolean, (optional)
    :param is_new_point: Slide New Point, Newly created vertex is being slid 
    :type is_new_point: boolean, (optional)
    '''

    pass


def slide_spline_curvature():
    '''Slide a point on the spline to define it’s curvature 

    '''

    pass


def switch_direction():
    '''Switch direction of selected splines 

    '''

    pass
