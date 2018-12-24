def cyclic_toggle(direction='CYCLIC_U'):
    '''Make active spline closed/opened loop 

    :param direction: Direction, Direction to make surface cyclic in 
    :type direction: enum in ['CYCLIC_U', 'CYCLIC_V'], (optional)
    '''

    pass


def de_select_first():
    '''(De)select first of visible part of each NURBS 

    '''

    pass


def de_select_last():
    '''(De)select last of visible part of each NURBS 

    '''

    pass


def decimate(ratio=1.0):
    '''Simplify selected curves 

    :param ratio: Ratio 
    :type ratio: float in [0, 1], (optional)
    '''

    pass


def delete(type='VERT'):
    '''Delete selected control points or segments 

    :param type: Type, Which elements to delete 
    :type type: enum in ['VERT', 'SEGMENT'], (optional)
    '''

    pass


def dissolve_verts():
    '''Delete selected control points, correcting surrounding handles 

    '''

    pass


def draw(error_threshold=0.0,
         fit_method='REFIT',
         corner_angle=1.22173,
         use_cyclic=True,
         stroke=None,
         wait_for_input=True):
    '''Draw a freehand spline 

    :param error_threshold: Error, Error distance threshold (in object units) 
    :type error_threshold: float in [0, 10], (optional)
    :param fit_method: Fit MethodREFIT Refit, Incrementally re-fit the curve (high quality).SPLIT Split, Split the curve until the tolerance is met (fast). 
    :type fit_method: enum in ['REFIT', 'SPLIT'], (optional)
    :param corner_angle: Corner Angle 
    :type corner_angle: float in [0, 3.14159], (optional)
    :param use_cyclic: Cyclic 
    :type use_cyclic: boolean, (optional)
    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def duplicate():
    '''Duplicate selected control points 

    '''

    pass


def duplicate_move(CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Duplicate curve and move 

    :param CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points 
    :type CURVE_OT_duplicate: CURVE_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude(mode='TRANSLATION'):
    '''Extrude selected control point(s) 

    :param mode: Mode 
    :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
    '''

    pass


def extrude_move(CURVE_OT_extrude=None, TRANSFORM_OT_translate=None):
    '''Extrude curve and move result 

    :param CURVE_OT_extrude: Extrude, Extrude selected control point(s) 
    :type CURVE_OT_extrude: CURVE_OT_extrude, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def handle_type_set(type='AUTOMATIC'):
    '''Set type of handles for selected control points 

    :param type: Type, Spline type 
    :type type: enum in ['AUTOMATIC', 'VECTOR', 'ALIGNED', 'FREE_ALIGN', 'TOGGLE_FREE_ALIGN'], (optional)
    '''

    pass


def hide(unselected=False):
    '''Hide (un)selected control points 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: boolean, (optional)
    '''

    pass


def make_segment():
    '''Join two curves by their selected ends 

    '''

    pass


def match_texture_space():
    '''Match texture space to object’s bounding box 

    '''

    pass


def normals_make_consistent(calc_length=False):
    '''Recalculate the direction of selected handles 

    :param calc_length: Length, Recalculate handle length 
    :type calc_length: boolean, (optional)
    '''

    pass


def primitive_bezier_circle_add(radius=1.0,
                                view_align=False,
                                enter_editmode=False,
                                location=(0.0, 0.0, 0.0),
                                rotation=(0.0, 0.0, 0.0)):
    '''Construct a Bezier Circle 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def primitive_bezier_curve_add(radius=1.0,
                               view_align=False,
                               enter_editmode=False,
                               location=(0.0, 0.0, 0.0),
                               rotation=(0.0, 0.0, 0.0)):
    '''Construct a Bezier Curve 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def primitive_nurbs_circle_add(radius=1.0,
                               view_align=False,
                               enter_editmode=False,
                               location=(0.0, 0.0, 0.0),
                               rotation=(0.0, 0.0, 0.0)):
    '''Construct a Nurbs Circle 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def primitive_nurbs_curve_add(radius=1.0,
                              view_align=False,
                              enter_editmode=False,
                              location=(0.0, 0.0, 0.0),
                              rotation=(0.0, 0.0, 0.0)):
    '''Construct a Nurbs Curve 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def primitive_nurbs_path_add(radius=1.0,
                             view_align=False,
                             enter_editmode=False,
                             location=(0.0, 0.0, 0.0),
                             rotation=(0.0, 0.0, 0.0)):
    '''Construct a Path 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def radius_set(radius=1.0):
    '''Set per-point radius which is used for bevel tapering 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    '''

    pass


def reveal(select=True):
    '''Reveal hidden control points 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''(De)select all control points 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_less():
    '''Reduce current selection by deselecting boundary elements 

    '''

    pass


def select_linked():
    '''Select all control points linked to the current selection 

    '''

    pass


def select_linked_pick(deselect=False):
    '''Select all control points linked to already selected ones 

    :param deselect: Deselect, Deselect linked control points rather than selecting them 
    :type deselect: boolean, (optional)
    '''

    pass


def select_more():
    '''Select control points directly linked to already selected ones 

    '''

    pass


def select_next():
    '''Select control points following already selected ones along the curves 

    '''

    pass


def select_nth(nth=2, skip=1, offset=0):
    '''Deselect every other vertex 

    :param nth: Nth Element, Skip every Nth element 
    :type nth: int in [2, inf], (optional)
    :param skip: Skip, Number of elements to skip at once 
    :type skip: int in [1, inf], (optional)
    :param offset: Offset, Offset from the starting point 
    :type offset: int in [-inf, inf], (optional)
    '''

    pass


def select_previous():
    '''Select control points preceding already selected ones along the curves 

    '''

    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    '''Randomly select some control points 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float in [0, 100], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: enum in ['SELECT', 'DESELECT'], (optional)
    '''

    pass


def select_row():
    '''Select a row of control points including active one 

    '''

    pass


def select_similar(type='WEIGHT', compare='EQUAL', threshold=0.1):
    '''Select similar curve points by property type 

    :param type: Type 
    :type type: enum in ['TYPE', 'RADIUS', 'WEIGHT', 'DIRECTION'], (optional)
    :param compare: Compare 
    :type compare: enum in ['EQUAL', 'GREATER', 'LESS'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, inf], (optional)
    '''

    pass


def separate():
    '''Separate selected points from connected unselected points into a new object 

    '''

    pass


def shade_flat():
    '''Set shading to flat 

    '''

    pass


def shade_smooth():
    '''Set shading to smooth 

    '''

    pass


def shortest_path_pick():
    '''Select shortest path between two selections 

    '''

    pass


def smooth():
    '''Flatten angles of selected points 

    '''

    pass


def smooth_radius():
    '''Interpolate radii of selected points 

    '''

    pass


def smooth_tilt():
    '''Interpolate tilt of selected points 

    '''

    pass


def smooth_weight():
    '''Interpolate weight of selected points 

    '''

    pass


def spin(center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    '''Extrude selected boundary row around pivot point and current view axis 

    :param center: Center, Center in global view space 
    :type center: float array of 3 items in [-inf, inf], (optional)
    :param axis: Axis, Axis in global view space 
    :type axis: float array of 3 items in [-1, 1], (optional)
    '''

    pass


def spline_type_set(type='POLY', use_handles=False):
    '''Set type of active spline 

    :param type: Type, Spline type 
    :type type: enum in ['POLY', 'BEZIER', 'NURBS'], (optional)
    :param use_handles: Handles, Use handles when converting bezier curves into polygons 
    :type use_handles: boolean, (optional)
    '''

    pass


def spline_weight_set(weight=1.0):
    '''Set softbody goal weight for selected points 

    :param weight: Weight 
    :type weight: float in [0, 1], (optional)
    '''

    pass


def split():
    '''Split off selected points from connected unselected points 

    '''

    pass


def subdivide(number_cuts=1):
    '''Subdivide selected segments 

    :param number_cuts: Number of cuts 
    :type number_cuts: int in [1, 1000], (optional)
    '''

    pass


def switch_direction():
    '''Switch direction of selected splines 

    '''

    pass


def tilt_clear():
    '''Clear the tilt of selected control points 

    '''

    pass


def vertex_add(location=(0.0, 0.0, 0.0)):
    '''Add a new control point (linked to only selected end-curve one, if any) 

    :param location: Location, Location to add new vertex at 
    :type location: float array of 3 items in [-inf, inf], (optional)
    '''

    pass
