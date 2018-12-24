def active_frame_delete():
    '''Delete the active frame for the active Grease Pencil Layer 

    '''

    pass


def active_frames_delete_all():
    '''Delete the active frame(s) of all editable Grease Pencil layers 

    '''

    pass


def brush_add():
    '''Add new Grease Pencil drawing brush for the active Grease Pencil datablock 

    '''

    pass


def brush_change(brush='DEFAULT'):
    '''Change active Grease Pencil drawing brush 

    :param brush: Grease Pencil Brush 
    :type brush: enum in ['DEFAULT'], (optional)
    '''

    pass


def brush_copy():
    '''Copy current Grease Pencil drawing brush 

    '''

    pass


def brush_move(type='UP'):
    '''Move the active Grease Pencil drawing brush up/down in the list 

    :param type: Type 
    :type type: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def brush_paint(stroke=None, wait_for_input=True):
    '''Apply tweaks to strokes by painting over the strokes 

    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input, Enter a mini ‘sculpt-mode’ if enabled, otherwise, exit after drawing a single stroke 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def brush_presets_create():
    '''Create a set of predefined Grease Pencil drawing brushes 

    '''

    pass


def brush_remove():
    '''Remove active Grease Pencil drawing brush 

    '''

    pass


def brush_select(index=0):
    '''Select a Grease Pencil drawing brush 

    :param index: Index, Index of Drawing Brush 
    :type index: int in [0, inf], (optional)
    '''

    pass


def convert(type='PATH',
            use_normalize_weights=True,
            radius_multiplier=1.0,
            use_link_strokes=True,
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


def copy():
    '''Copy selected Grease Pencil points and strokes 

    '''

    pass


def data_add():
    '''Add new Grease Pencil datablock 

    '''

    pass


def data_unlink():
    '''Unlink active Grease Pencil datablock 

    '''

    pass


def delete(type='POINTS'):
    '''Delete selected Grease Pencil strokes, vertices, or frames 

    :param type: Type, Method used for deleting Grease Pencil dataPOINTS Points, Delete selected points and split strokes into segments.STROKES Strokes, Delete selected strokes.FRAME Frame, Delete active frame. 
    :type type: enum in ['POINTS', 'STROKES', 'FRAME'], (optional)
    '''

    pass


def dissolve():
    '''Delete selected points without splitting strokes 

    '''

    pass


def draw(mode='DRAW', stroke=None, wait_for_input=True):
    '''Make annotations on the active data 

    :param mode: Mode, Way to interpret mouse movementsDRAW Draw Freehand, Draw freehand stroke(s).DRAW_STRAIGHT Draw Straight Lines, Draw straight line segment(s).DRAW_POLY Draw Poly Line, Click to place endpoints of straight line segments (connected).ERASER Eraser, Erase Grease Pencil strokes. 
    :type mode: enum in ['DRAW', 'DRAW_STRAIGHT', 'DRAW_POLY', 'ERASER'], (optional)
    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately 
    :type wait_for_input: boolean, (optional)
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
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def editmode_toggle():
    '''Enter/Exit edit mode for Grease Pencil strokes 

    '''

    pass


def hide(unselected=False):
    '''Hide selected/unselected Grease Pencil layers 

    :param unselected: Unselected, Hide unselected rather than selected layers 
    :type unselected: boolean, (optional)
    '''

    pass


def layer_add():
    '''Add new Grease Pencil layer for the active Grease Pencil datablock 

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


def move_to_layer(layer='DEFAULT'):
    '''Move selected strokes to another layer 

    :param layer: Grease Pencil Layer 
    :type layer: enum in ['DEFAULT'], (optional)
    '''

    pass


def palette_add():
    '''Add new Grease Pencil palette for the active Grease Pencil datablock 

    '''

    pass


def palette_change(palette='DEFAULT'):
    '''Change active Grease Pencil palette 

    :param palette: Grease Pencil Palette 
    :type palette: enum in ['DEFAULT'], (optional)
    '''

    pass


def palette_lock_layer():
    '''Lock and hide any color not used in any layer 

    '''

    pass


def palette_remove():
    '''Remove active Grease Pencil palette 

    '''

    pass


def palettecolor_add():
    '''Add new Grease Pencil palette color for the active Grease Pencil datablock 

    '''

    pass


def palettecolor_copy():
    '''Copy current Grease Pencil palette color 

    '''

    pass


def palettecolor_hide(unselected=False):
    '''Hide selected/unselected Grease Pencil colors 

    :param unselected: Unselected, Hide unselected rather than selected colors 
    :type unselected: boolean, (optional)
    '''

    pass


def palettecolor_isolate(affect_visibility=False):
    '''Toggle whether the active color is the only one that is editable and/or visible 

    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility 
    :type affect_visibility: boolean, (optional)
    '''

    pass


def palettecolor_lock_all():
    '''Lock all Grease Pencil colors to prevent them from being accidentally modified 

    '''

    pass


def palettecolor_move(direction='UP'):
    '''Move the active Grease Pencil palette color up/down in the list 

    :param direction: Direction 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def palettecolor_remove():
    '''Remove active Grease Pencil palette color 

    '''

    pass


def palettecolor_reveal():
    '''Unhide all hidden Grease Pencil palette colors 

    '''

    pass


def palettecolor_select():
    '''Select all Grease Pencil strokes using current color 

    '''

    pass


def palettecolor_unlock_all():
    '''Unlock all Grease Pencil colors so that they can be edited 

    '''

    pass


def paste(type='COPY'):
    '''Paste previously copied strokes or copy and merge in active layer 

    :param type: Type 
    :type type: enum in ['COPY', 'MERGE'], (optional)
    '''

    pass


def reproject():
    '''Reproject the selected strokes from the current viewpoint to get all points on the same plane again (e.g. to fix problems from accidental 3D cursor movement, or viewport changes) 

    '''

    pass


def reveal():
    '''Show all Grease Pencil layers 

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


def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    '''Select Grease Pencil strokes within a rectangular region 

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
    '''Select Grease Pencil strokes using brush selection 

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

    :param type: TypeLAYER Layer, Shared layers.COLOR Color, Shared colors. 
    :type type: enum in ['LAYER', 'COLOR'], (optional)
    '''

    pass


def select_lasso(path=None, deselect=False, extend=True):
    '''Select Grease Pencil strokes using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
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


def stroke_change_color():
    '''Move selected strokes to active color 

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


def unlock_all():
    '''Unlock all Grease Pencil layers so that they can be edited 

    '''

    pass
