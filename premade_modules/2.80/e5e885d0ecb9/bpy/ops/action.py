def clean(threshold=0.001, channels=False):
    '''Simplify F-Curves by removing closely spaced keyframes 

    :param threshold: Threshold 
    :type threshold: float in [0, inf], (optional)
    :param channels: Channels 
    :type channels: boolean, (optional)
    '''

    pass


def clickselect(extend=False, column=False, channel=False):
    '''Select keyframes by clicking on them 

    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only 
    :type extend: boolean, (optional)
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse 
    :type column: boolean, (optional)
    :param channel: Only Channel, Select all the keyframes in the channel under the mouse 
    :type channel: boolean, (optional)
    '''

    pass


def copy():
    '''Copy selected keyframes to the copy/paste buffer 

    '''

    pass


def delete():
    '''Remove all selected keyframes 

    '''

    pass


def duplicate():
    '''Make a copy of all selected keyframes 

    '''

    pass


def duplicate_move(ACTION_OT_duplicate=None, TRANSFORM_OT_transform=None):
    '''Make a copy of all selected keyframes and move them 

    :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes 
    :type ACTION_OT_duplicate: ACTION_OT_duplicate, (optional)
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type 
    :type TRANSFORM_OT_transform: TRANSFORM_OT_transform, (optional)
    '''

    pass


def extrapolation_type(type='CONSTANT'):
    '''Set extrapolation mode for selected F-Curves 

    :param type: TypeCONSTANT Constant Extrapolation, Values on endpoint keyframes are held.LINEAR Linear Extrapolation, Straight-line slope of end segments are extended past the endpoint keyframes.MAKE_CYCLIC Make Cyclic (F-Modifier), Add Cycles F-Modifier if one doesn’t exist already.CLEAR_CYCLIC Clear Cyclic (F-Modifier), Remove Cycles F-Modifier if not needed anymore. 
    :type type: enum in ['CONSTANT', 'LINEAR', 'MAKE_CYCLIC', 'CLEAR_CYCLIC'], (optional)
    '''

    pass


def frame_jump():
    '''Set the current frame to the average frame value of selected keyframes 

    '''

    pass


def handle_type(type='FREE'):
    '''Set type of handle for selected keyframes 

    :param type: TypeFREE Free, Completely independent manually set handle.ALIGNED Aligned, Manually set handle with rotation locked together with its pair.VECTOR Vector, Automatic handles that create straight lines.AUTO Automatic, Automatic handles that create smooth curves.AUTO_CLAMPED Auto Clamped, Automatic handles that create smooth curves which only change direction at keyframes. 
    :type type: enum in ['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED'], (optional)
    '''

    pass


def interpolation_type(type='CONSTANT'):
    '''Set interpolation mode for the F-Curve segments starting from the selected keyframes 

    :param type: TypeCONSTANT Constant, No interpolation, value of A gets held until B is encountered.LINEAR Linear, Straight-line interpolation between A and B (i.e. no ease in/out).BEZIER Bezier, Smooth interpolation between A and B, with some control over curve shape.SINE Sinusoidal, Sinusoidal easing (weakest, almost linear but with a slight curvature).QUAD Quadratic, Quadratic easing.CUBIC Cubic, Cubic easing.QUART Quartic, Quartic easing.QUINT Quintic, Quintic easing.EXPO Exponential, Exponential easing (dramatic).CIRC Circular, Circular easing (strongest and most dynamic).BACK Back, Cubic easing with overshoot and settle.BOUNCE Bounce, Exponentially decaying parabolic bounce, like when objects collide.ELASTIC Elastic, Exponentially decaying sine wave, like an elastic band. 
    :type type: enum in ['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC'], (optional)
    '''

    pass


def keyframe_insert(type='ALL'):
    '''Insert keyframes for the specified channels 

    :param type: Type 
    :type type: enum in ['ALL', 'SEL', 'GROUP'], (optional)
    '''

    pass


def keyframe_type(type='KEYFRAME'):
    '''Set type of keyframe for the selected keyframes 

    :param type: TypeKEYFRAME Keyframe, Normal keyframe - e.g. for key poses.BREAKDOWN Breakdown, A breakdown pose - e.g. for transitions between key poses.MOVING_HOLD Moving Hold, A keyframe that is part of a moving hold.EXTREME Extreme, An ‘extreme’ pose, or some other purpose as needed.JITTER Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed. 
    :type type: enum in ['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER'], (optional)
    '''

    pass


def layer_next():
    '''Switch to editing action in animation layer above the current action in the NLA Stack 

    '''

    pass


def layer_prev():
    '''Switch to editing action in animation layer below the current action in the NLA Stack 

    '''

    pass


def markers_make_local():
    '''Move selected scene markers to the active Action as local ‘pose’ markers 

    '''

    pass


def mirror(type='CFRA'):
    '''Flip selected keyframes over the selected mirror line 

    :param type: TypeCFRA By Times over Current frame, Flip times of selected keyframes using the current frame as the mirror line.XAXIS By Values over Value=0, Flip values of selected keyframes (i.e. negative values become positive, and vice versa).MARKER By Times over First Selected Marker, Flip times of selected keyframes using the first selected marker as the reference point. 
    :type type: enum in ['CFRA', 'XAXIS', 'MARKER'], (optional)
    '''

    pass


def new():
    '''Create new action 

    '''

    pass


def paste(offset='START', merge='MIX', flipped=False):
    '''Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame 

    :param offset: Offset, Paste time offset of keysSTART Frame Start, Paste keys starting at current frame.END Frame End, Paste keys ending at current frame.RELATIVE Frame Relative, Paste keys relative to the current frame when copying.NONE No Offset, Paste keys from original time. 
    :type offset: enum in ['START', 'END', 'RELATIVE', 'NONE'], (optional)
    :param merge: Type, Method of merging pasted keys and existingMIX Mix, Overlay existing with new keys.OVER_ALL Overwrite All, Replace all keys.OVER_RANGE Overwrite Range, Overwrite keys in pasted range.OVER_RANGE_ALL Overwrite Entire Range, Overwrite keys in pasted range, using the range of all copied keys. 
    :type merge: enum in ['MIX', 'OVER_ALL', 'OVER_RANGE', 'OVER_RANGE_ALL'], (optional)
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist 
    :type flipped: boolean, (optional)
    '''

    pass


def previewrange_set():
    '''Set Preview Range based on extents of selected Keyframes 

    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def push_down():
    '''Push action down on to the NLA stack as a new strip 

    '''

    pass


def sample():
    '''Add keyframes on every frame between the selected keyframes 

    '''

    pass


def select_all(action='TOGGLE'):
    '''Toggle selection of all keyframes 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_box(xmin=0,
               xmax=0,
               ymin=0,
               ymax=0,
               wait_for_input=True,
               deselect=False,
               extend=True,
               axis_range=False):
    '''Select all keyframes within the specified region 

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
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param axis_range: Axis Range 
    :type axis_range: boolean, (optional)
    '''

    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, deselect=False):
    '''Select keyframe points using circle selection 

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


def select_column(mode='KEYS'):
    '''Select all keyframes on the specified frame(s) 

    :param mode: Mode 
    :type mode: enum in ['KEYS', 'CFRA', 'MARKERS_COLUMN', 'MARKERS_BETWEEN'], (optional)
    '''

    pass


def select_lasso(path=None, deselect=False, extend=True):
    '''Select keyframe points using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_leftright(mode='CHECK', extend=False):
    '''Select keyframes to the left or the right of the current frame 

    :param mode: Mode 
    :type mode: enum in ['CHECK', 'LEFT', 'RIGHT'], (optional)
    :param extend: Extend Select 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Deselect keyframes on ends of selection islands 

    '''

    pass


def select_linked():
    '''Select keyframes occurring in the same F-Curves as selected ones 

    '''

    pass


def select_more():
    '''Select keyframes beside already selected ones 

    '''

    pass


def snap(type='CFRA'):
    '''Snap selected keyframes to the times specified 

    :param type: TypeCFRA Current frame, Snap selected keyframes to the current frame.NEAREST_FRAME Nearest Frame, Snap selected keyframes to the nearest (whole) frame (use to fix accidental sub-frame offsets).NEAREST_SECOND Nearest Second, Snap selected keyframes to the nearest second.NEAREST_MARKER Nearest Marker, Snap selected keyframes to the nearest marker. 
    :type type: enum in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)
    '''

    pass


def stash(create_new=True):
    '''Store this action in the NLA stack as a non-contributing strip for later use 

    :param create_new: Create New Action, Create a new action once the existing one has been safely stored 
    :type create_new: boolean, (optional)
    '''

    pass


def stash_and_create():
    '''Store this action in the NLA stack as a non-contributing strip for later use, and create a new action 

    '''

    pass


def unlink(force_delete=False):
    '''Unlink this action from the active action slot (and/or exit Tweak Mode) 

    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block’s NLA stack 
    :type force_delete: boolean, (optional)
    '''

    pass


def view_all():
    '''Reset viewable area to show full keyframe range 

    '''

    pass


def view_frame():
    '''Reset viewable area to show range around current frame 

    '''

    pass


def view_selected():
    '''Reset viewable area to show selected keyframes range 

    '''

    pass
