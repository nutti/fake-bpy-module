def active_frame_delete():
    '''Delete the active frame for the active Grease Pencil Layer 

    '''

    pass


def active_frames_delete_all():
    '''Delete the active frame(s) of all editable Grease Pencil layers 

    '''

    pass


def annotate(mode='DRAW', stroke=None, wait_for_input=True):
    '''Make annotations on the active data 

    :param mode: Mode, Way to interpret mouse movementsDRAW Draw Freehand, Draw freehand stroke(s).DRAW_STRAIGHT Draw Straight Lines, Draw straight line segment(s).DRAW_POLY Draw Poly Line, Click to place endpoints of straight line segments (connected).ERASER Eraser, Erase Annotation strokes. 
    :type mode: enum in ['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER'], (optional)
    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def blank_frame_add(all_layers=False):
    '''Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame) 

    :param all_layers: All Layers, Create blank frame in all layers, not only active 
    :type all_layers: boolean, (optional)
    '''

    pass


def brush_presets_create():
    '''Create a set of predefined Grease Pencil drawing brushes 

    '''

    pass


def color_hide(unselected=False):
    '''Hide selected/unselected Grease Pencil colors 

    :param unselected: Unselected, Hide unselected rather than selected colors 
    :type unselected: boolean, (optional)
    '''

    pass


def color_isolate(affect_visibility=False):
    '''Toggle whether the active color is the only one that is editable and/or visible 

    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility 
    :type affect_visibility: boolean, (optional)
    '''

    pass


def color_lock_all():
    '''Lock all Grease Pencil colors to prevent them from being accidentally modified 

    '''

    pass


def color_reveal():
    '''Unhide all hidden Grease Pencil colors 

    '''

    pass


def color_select(deselect=False):
    '''Select all Grease Pencil strokes using current color 

    :param deselect: Deselect, Unselect strokes 
    :type deselect: boolean, (optional)
    '''

    pass


def color_unlock_all():
    '''Unlock all Grease Pencil colors so that they can be edited 

    '''

    pass


def convert(type='PATH',
            use_normalize_weights=True,
            radius_multiplier=1.0,
            use_link_strokes=False,
            timing_mode='FULL',
            frame_range=100,
            start_frame=1,
            use_realtime=False,
            end_frame=250,
            gap_duration=0.0,
            gap_randomness=0.0,
            seed=0,
            use_timing_data=False):
    '''Convert the active Grease Pencil layer to a new Curve Object 

    :param type: Type, Which type of curve to convert toPATH Path, Animation path.CURVE Bezier Curve, Smooth Bezier curve.POLY Polygon Curve, Bezier curve with straight-line segments (vector handles). 
    :type type: enum in ['PATH', 'CURVE', 'POLY'], (optional)
    :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width) 
    :type use_normalize_weights: boolean, (optional)
    :param radius_multiplier: Radius Fac, Multiplier for the points’ radii (set from stroke width) 
    :type radius_multiplier: float in [0, 1000], (optional)
    :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves 
    :type use_link_strokes: boolean, (optional)
    :param timing_mode: Timing Mode, How to use timing data stored in strokesNONE No Timing, Ignore timing.LINEAR Linear, Simple linear timing.FULL Original, Use the original timing, gaps included.CUSTOMGAP Custom Gaps, Use the original timing, but with custom gap lengths (in frames). 
    :type timing_mode: enum in ['NONE', 'LINEAR', 'FULL', 'CUSTOMGAP'], (optional)
    :param frame_range: Frame Range, The duration of evaluation of the path control curve 
    :type frame_range: int in [1, 10000], (optional)
    :param start_frame: Start Frame, The start frame of the path control curve 
    :type start_frame: int in [1, 100000], (optional)
    :param use_realtime: Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame 
    :type use_realtime: boolean, (optional)
    :param end_frame: End Frame, The end frame of the path control curve (if Realtime is not set) 
    :type end_frame: int in [1, 100000], (optional)
    :param gap_duration: Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set) 
    :type gap_duration: float in [0, 10000], (optional)
    :param gap_randomness: Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary 
    :type gap_randomness: float in [0, 10000], (optional)
    :param seed: Random Seed, Custom Gap mode: Random generator seed 
    :type seed: int in [0, 1000], (optional)
    :param use_timing_data: Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use) 
    :type use_timing_data: boolean, (optional)
    '''

    pass


def convert_old_files():
    '''Convert 2.7x grease pencil files to 2.8 

    '''

    pass


def copy():
    '''Copy selected Grease Pencil points and strokes 

    '''

    pass


def data_add():
    '''Add new Grease Pencil data-block 

    '''

    pass


def data_unlink():
    '''Unlink active Grease Pencil data-block 

    '''

    pass


def delete(type='POINTS'):
    '''Delete selected Grease Pencil strokes, vertices, or frames 

    :param type: Type, Method used for deleting Grease Pencil dataPOINTS Points, Delete selected points and split strokes into segments.STROKES Strokes, Delete selected strokes.FRAME Frame, Delete active frame. 
    :type type: enum in ['POINTS', 'STROKES', 'FRAME'], (optional)
    '''

    pass


def dissolve(type='POINTS'):
    '''Delete selected points without splitting strokes 

    :param type: Type, Method used for dissolving Stroke pointsPOINTS Dissolve, Dissolve selected points.BETWEEN Dissolve Between, Dissolve points between selected points.UNSELECT Dissolve Unselect, Dissolve all unselected points. 
    :type type: enum in ['POINTS', 'BETWEEN', 'UNSELECT'], (optional)
    '''

    pass


def draw(mode='DRAW',
         stroke=None,
         wait_for_input=True,
         disable_straight=False,
         disable_fill=False):
    '''Draw a new stroke in the active Grease Pencil Object 

    :param mode: Mode, Way to interpret mouse movementsDRAW Draw Freehand, Draw freehand stroke(s).DRAW_STRAIGHT Draw Straight Lines, Draw straight line segment(s).DRAW_POLY Draw Poly Line, Click to place endpoints of straight line segments (connected).ERASER Eraser, Erase Grease Pencil strokes. 
    :type mode: enum in ['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER'], (optional)
    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately 
    :type wait_for_input: boolean, (optional)
    :param disable_straight: No Straight lines, Disable key for straight lines 
    :type disable_straight: boolean, (optional)
    :param disable_fill: No Fill Areas, Disable fill to use stroke as fill boundary 
    :type disable_fill: boolean, (optional)
    '''

    pass


def duplicate():
    '''Duplicate the selected Grease Pencil strokes 

    '''

    pass


def duplicate_move(GPENCIL_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Make copies of the selected Grease Pencil strokes and move them 

    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes 
    :type GPENCIL_OT_duplicate: GPENCIL_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def editmode_toggle(back=False):
    '''Enter/Exit edit mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: boolean, (optional)
    '''

    pass


def fill(on_back=False):
    '''Fill with color the shape formed by strokes 

    :param on_back: Draw On Back, Send new stroke to Back 
    :type on_back: boolean, (optional)
    '''

    pass


def frame_clean_fill(mode='ACTIVE'):
    '''Remove ‘no fill’ boundary strokes 

    :param mode: ModeACTIVE Active Frame Only, Clean active frame only.ALL All Frames, Clean all frames in all layers. 
    :type mode: enum in ['ACTIVE', 'ALL'], (optional)
    '''

    pass


def frame_clean_loose(limit=1):
    '''Remove loose points 

    :param limit: Limit, Number of points to consider stroke as loose 
    :type limit: int in [1, inf], (optional)
    '''

    pass


def frame_duplicate(mode='ACTIVE'):
    '''Make a copy of the active Grease Pencil Frame 

    :param mode: ModeACTIVE Active, Duplicate frame in active layer only.ALL All, Duplicate active frames in all layers. 
    :type mode: enum in ['ACTIVE', 'ALL'], (optional)
    '''

    pass


def generate_weights(mode='NAME', armature='DEFAULT', ratio=0.1, decay=0.8):
    '''Generate automatic weights for armatures (requires armature modifier) 

    :param mode: Mode 
    :type mode: enum in ['NAME', 'AUTO'], (optional)
    :param armature: Armature, Armature to use 
    :type armature: enum in ['DEFAULT'], (optional)
    :param ratio: Ratio, Ratio between bone length and influence radius 
    :type ratio: float in [0, 2], (optional)
    :param decay: Decay, Factor to reduce influence depending of distance to bone axis 
    :type decay: float in [0, 1], (optional)
    '''

    pass


def hide(unselected=False):
    '''Hide selected/unselected Grease Pencil layers 

    :param unselected: Unselected, Hide unselected rather than selected layers 
    :type unselected: boolean, (optional)
    '''

    pass


def interpolate(shift=0.0):
    '''Interpolate grease pencil strokes between frames 

    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes 
    :type shift: float in [-1, 1], (optional)
    '''

    pass


def interpolate_reverse():
    '''Remove breakdown frames generated by interpolating between two Grease Pencil frames 

    '''

    pass


def interpolate_sequence():
    '''Generate ‘in-betweens’ to smoothly interpolate between Grease Pencil frames 

    '''

    pass


def layer_add():
    '''Add new layer or note for the active data-block 

    '''

    pass


def layer_change(layer='DEFAULT'):
    '''Change active Grease Pencil layer 

    :param layer: Grease Pencil Layer 
    :type layer: enum in ['DEFAULT'], (optional)
    '''

    pass


def layer_duplicate():
    '''Make a copy of the active Grease Pencil layer 

    '''

    pass


def layer_duplicate_object(object="", mode='ALL'):
    '''Make a copy of the active Grease Pencil layer to new object 

    :param object: Object, Name of the destination object 
    :type object: string, (optional, never None)
    :param mode: Mode 
    :type mode: enum in ['ALL', 'ACTIVE'], (optional)
    '''

    pass


def layer_isolate(affect_visibility=False):
    '''Toggle whether the active layer is the only one that can be edited and/or visible 

    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility 
    :type affect_visibility: boolean, (optional)
    '''

    pass


def layer_merge():
    '''Merge the current layer with the layer below 

    '''

    pass


def layer_move(type='UP'):
    '''Move the active Grease Pencil layer up/down in the list 

    :param type: Type 
    :type type: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def layer_remove():
    '''Remove active Grease Pencil layer 

    '''

    pass


def lock_all():
    '''Lock all Grease Pencil layers to prevent them from being accidentally modified 

    '''

    pass


def lock_layer():
    '''Lock and hide any color not used in any layer 

    '''

    pass


def move_to_layer(layer='DEFAULT'):
    '''Move selected strokes to another layer 

    :param layer: Grease Pencil Layer 
    :type layer: enum in ['DEFAULT'], (optional)
    '''

    pass


def paintmode_toggle(back=False):
    '''Enter/Exit paint mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: boolean, (optional)
    '''

    pass


def paste(type='COPY'):
    '''Paste previously copied strokes or copy and merge in active layer 

    :param type: Type 
    :type type: enum in ['COPY', 'MERGE'], (optional)
    '''

    pass


def primitive(edges=4, type='BOX', wait_for_input=True):
    '''Create predefined grease pencil stroke shapes 

    :param edges: Edges, Number of polygon edges 
    :type edges: int in [2, 128], (optional)
    :param type: Type, Type of shape 
    :type type: enum in ['BOX', 'LINE', 'CIRCLE', 'ARC', 'CURVE'], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def reproject(type='VIEW'):
    '''Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry) 

    :param type: Projection TypeFRONT Front, Reproject the strokes using the X-Z plane.SIDE Side, Reproject the strokes using the Y-Z plane.TOP Top, Reproject the strokes using the X-Y plane.VIEW View, Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using ‘Cursor’ Stroke Placement.SURFACE Surface, Reproject the strokes on to the scene geometry, as if drawn using ‘Surface’ placement. 
    :type type: enum in ['FRONT', 'SIDE', 'TOP', 'VIEW', 'SURFACE'], (optional)
    '''

    pass


def reveal(select=True):
    '''Show all Grease Pencil layers 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def sculpt_paint(stroke=None, wait_for_input=True):
    '''Apply tweaks to strokes by painting over the strokes 

    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input, Enter a mini ‘sculpt-mode’ if enabled, otherwise, exit after drawing a single stroke 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def sculptmode_toggle(back=False):
    '''Enter/Exit sculpt mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: boolean, (optional)
    '''

    pass


def select(extend=False,
           deselect=False,
           toggle=False,
           entire_strokes=False,
           location=(0, 0)):
    '''Select Grease Pencil strokes and/or stroke points 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param deselect: Deselect, Remove from selection 
    :type deselect: boolean, (optional)
    :param toggle: Toggle Selection, Toggle the selection 
    :type toggle: boolean, (optional)
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex 
    :type entire_strokes: boolean, (optional)
    :param location: Location, Mouse location 
    :type location: int array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all Grease Pencil strokes currently visible 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_alternate(unselect_ends=True):
    '''Select alternative points in same strokes as already selected points 

    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke 
    :type unselect_ends: boolean, (optional)
    '''

    pass


def select_box(mode='SET', xmin=0, xmax=0, ymin=0, ymax=0,
               wait_for_input=True):
    '''Select Grease Pencil strokes within a rectangular region 

    :param mode: Mode 
    :type mode: enum in ['SET', 'ADD', 'SUB', 'XOR', 'AND'], (optional)
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


def select_circle(x=0, y=0, radius=25, wait_for_input=True, deselect=False):
    '''Select Grease Pencil strokes using brush selection 

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


def select_first(only_selected_strokes=False, extend=False):
    '''Select first point in Grease Pencil strokes 

    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected 
    :type only_selected_strokes: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting all other selected points 
    :type extend: boolean, (optional)
    '''

    pass


def select_grouped(type='LAYER'):
    '''Select all strokes with similar characteristics 

    :param type: TypeLAYER Layer, Shared layers.MATERIAL Material, Shared materials. 
    :type type: enum in ['LAYER', 'MATERIAL'], (optional)
    '''

    pass


def select_lasso(mode='SET', path=None):
    '''Select Grease Pencil strokes using lasso selection 

    :param mode: Mode 
    :type mode: enum in ['SET', 'ADD', 'SUB', 'XOR', 'AND'], (optional)
    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    '''

    pass


def select_last(only_selected_strokes=False, extend=False):
    '''Select last point in Grease Pencil strokes 

    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected 
    :type only_selected_strokes: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting all other selected points 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Shrink sets of selected Grease Pencil points 

    '''

    pass


def select_linked():
    '''Select all points in same strokes as already selected points 

    '''

    pass


def select_more():
    '''Grow sets of selected Grease Pencil points 

    '''

    pass


def selection_opacity_toggle():
    '''Hide/Unhide selected points for Grease Pencil strokes setting alpha factor 

    '''

    pass


def selectmode_toggle(mode=0):
    '''Set selection mode for Grease Pencil strokes 

    :param mode: Select mode, Select mode 
    :type mode: int in [0, 1], (optional)
    '''

    pass


def snap_cursor_to_selected():
    '''Snap cursor to center of selected points 

    '''

    pass


def snap_to_cursor(use_offset=True):
    '''Snap selected points/strokes to the cursor 

    :param use_offset: With Offset, Offset the entire stroke instead of selected points only 
    :type use_offset: boolean, (optional)
    '''

    pass


def snap_to_grid():
    '''Snap selected points to the nearest grid points 

    '''

    pass


def stroke_apply_thickness():
    '''Apply the thickness change of the layer to its strokes 

    '''

    pass


def stroke_arrange(direction='UP'):
    '''Arrange selected strokes up/down in the drawing order of the active layer 

    :param direction: Direction 
    :type direction: enum in ['UP', 'DOWN', 'TOP', 'BOTTOM'], (optional)
    '''

    pass


def stroke_change_color(material=""):
    '''Move selected strokes to active material 

    :param material: Material, Name of the material 
    :type material: string, (optional, never None)
    '''

    pass


def stroke_cyclical_set(type='TOGGLE'):
    '''Close or open the selected stroke adding an edge from last to first point 

    :param type: Type 
    :type type: enum in ['CLOSE', 'OPEN', 'TOGGLE'], (optional)
    '''

    pass


def stroke_flip():
    '''Change direction of the points of the selected strokes 

    '''

    pass


def stroke_join(type='JOIN', leave_gaps=False):
    '''Join selected strokes (optionally as new stroke) 

    :param type: Type 
    :type type: enum in ['JOIN', 'JOINCOPY'], (optional)
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them 
    :type leave_gaps: boolean, (optional)
    '''

    pass


def stroke_lock_color():
    '''Lock any color not used in any selected stroke 

    '''

    pass


def stroke_separate(mode='POINT'):
    '''Separate the selected strokes or layer in a new grease pencil object 

    :param mode: ModePOINT Selected Points, Separate the selected points.STROKE Selected Strokes, Separate the selected strokes.LAYER Active Layer, Separate the strokes of the current layer. 
    :type mode: enum in ['POINT', 'STROKE', 'LAYER'], (optional)
    '''

    pass


def stroke_simplify(factor=0.0):
    '''Simplify selected stroked reducing number of points 

    :param factor: Factor 
    :type factor: float in [0, 100], (optional)
    '''

    pass


def stroke_simplify_fixed(step=1):
    '''Simplify selected stroked reducing number of points using fixed algorithm 

    :param step: Steps, Number of simplify steps 
    :type step: int in [1, 100], (optional)
    '''

    pass


def stroke_smooth(repeat=1,
                  factor=0.5,
                  only_selected=True,
                  smooth_position=True,
                  smooth_thickness=True,
                  smooth_strength=False,
                  smooth_uv=False):
    '''Smooth selected strokes 

    :param repeat: Repeat 
    :type repeat: int in [1, 10], (optional)
    :param factor: Factor 
    :type factor: float in [0, 2], (optional)
    :param only_selected: Selected Points, Smooth only selected points in the stroke 
    :type only_selected: boolean, (optional)
    :param smooth_position: Position 
    :type smooth_position: boolean, (optional)
    :param smooth_thickness: Thickness 
    :type smooth_thickness: boolean, (optional)
    :param smooth_strength: Strength 
    :type smooth_strength: boolean, (optional)
    :param smooth_uv: UV 
    :type smooth_uv: boolean, (optional)
    '''

    pass


def stroke_split():
    '''Split selected points as new stroke on same frame 

    '''

    pass


def stroke_subdivide(number_cuts=1,
                     factor=0.0,
                     repeat=1,
                     only_selected=True,
                     smooth_position=True,
                     smooth_thickness=True,
                     smooth_strength=False,
                     smooth_uv=False):
    '''Subdivide between continuous selected points of the stroke adding a point half way between them 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [1, 10], (optional)
    :param factor: Smooth 
    :type factor: float in [0, 2], (optional)
    :param repeat: Repeat 
    :type repeat: int in [1, 10], (optional)
    :param only_selected: Selected Points, Smooth only selected points in the stroke 
    :type only_selected: boolean, (optional)
    :param smooth_position: Position 
    :type smooth_position: boolean, (optional)
    :param smooth_thickness: Thickness 
    :type smooth_thickness: boolean, (optional)
    :param smooth_strength: Strength 
    :type smooth_strength: boolean, (optional)
    :param smooth_uv: UV 
    :type smooth_uv: boolean, (optional)
    '''

    pass


def unlock_all():
    '''Unlock all Grease Pencil layers so that they can be edited 

    '''

    pass


def vertex_group_assign():
    '''Assign the selected vertices to the active vertex group 

    '''

    pass


def vertex_group_deselect():
    '''Deselect all selected vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_invert():
    '''Invert weights to the active vertex group 

    '''

    pass


def vertex_group_remove_from():
    '''Remove the selected vertices from active or all vertex group(s) 

    '''

    pass


def vertex_group_select():
    '''Select all the vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_smooth(factor=0.5, repeat=1):
    '''Smooth weights to the active vertex group 

    :param factor: Factor 
    :type factor: float in [0, 1], (optional)
    :param repeat: Iterations 
    :type repeat: int in [1, 10000], (optional)
    '''

    pass


def weightmode_toggle(back=False):
    '''Enter/Exit weight paint mode for Grease Pencil strokes 

    :param back: Return to Previous Mode, Return to previous mode 
    :type back: boolean, (optional)
    '''

    pass
