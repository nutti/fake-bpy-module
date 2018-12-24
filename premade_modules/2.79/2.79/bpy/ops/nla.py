def action_pushdown(channel_index=-1):
    '''Push action down onto the top of the NLA stack as a new strip 

    :param channel_index: Channel Index, Index of NLA action channel to perform pushdown operation on 
    :type channel_index: int in [-1, inf], (optional)
    '''

    pass


def action_sync_length(active=True):
    '''Synchronize the length of the referenced Action with the length used in the strip 

    :param active: Active Strip Only, Only sync the active length for the active strip 
    :type active: boolean, (optional)
    '''

    pass


def action_unlink(force_delete=False):
    '''Unlink this action from the active action slot (and/or exit Tweak Mode) 

    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this datablock’s NLA stack 
    :type force_delete: boolean, (optional)
    '''

    pass


def actionclip_add(action=''):
    '''Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track 

    :param action: Action 
    :type action: enum in [], (optional)
    '''

    pass


def apply_scale():
    '''Apply scaling of selected strips to their referenced Actions 

    '''

    pass


def bake(frame_start=1,
         frame_end=250,
         step=1,
         only_selected=True,
         visual_keying=False,
         clear_constraints=False,
         clear_parents=False,
         use_current_action=False,
         bake_types={'POSE'}):
    '''Bake object/pose loc/scale/rotation animation to a new action 

    :param frame_start: Start Frame, Start frame for baking 
    :type frame_start: int in [0, 300000], (optional)
    :param frame_end: End Frame, End frame for baking 
    :type frame_end: int in [1, 300000], (optional)
    :param step: Frame Step, Frame Step 
    :type step: int in [1, 120], (optional)
    :param only_selected: Only Selected, Only key selected bones (Pose baking only) 
    :type only_selected: boolean, (optional)
    :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied) 
    :type visual_keying: boolean, (optional)
    :param clear_constraints: Clear Constraints, Remove all constraints from keyed object/bones, and do ‘visual’ keying 
    :type clear_constraints: boolean, (optional)
    :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only) 
    :type clear_parents: boolean, (optional)
    :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature) 
    :type use_current_action: boolean, (optional)
    :param bake_types: Bake Data, Which data’s transformations to bakePOSE Pose, Bake bones transformations.OBJECT Object, Bake object transformations. 
    :type bake_types: enum set in {'POSE', 'OBJECT'}, (optional)
    '''

    pass


def channels_click(extend=False):
    '''Handle clicks to select NLA channels 

    :param extend: Extend Select 
    :type extend: boolean, (optional)
    '''

    pass


def clear_scale():
    '''Reset scaling of selected strips 

    '''

    pass


def click_select(extend=False):
    '''Handle clicks to select NLA Strips 

    :param extend: Extend Select 
    :type extend: boolean, (optional)
    '''

    pass


def delete():
    '''Delete selected strips 

    '''

    pass


def duplicate(linked=False, mode='TRANSLATION'):
    '''Duplicate selected NLA-Strips, adding the new strips in new tracks above the originals 

    :param linked: Linked, When duplicating strips, assign new copies of the actions they use 
    :type linked: boolean, (optional)
    :param mode: Mode 
    :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
    '''

    pass


def fmodifier_add(type='NULL', only_active=True):
    '''Add F-Modifier to the active/selected NLA-Strips 

    :param type: TypeNULL Invalid.GENERATOR Generator, Generate a curve using a factorized or expanded polynomial.FNGENERATOR Built-In Function, Generate a curve using standard math functions such as sin and cos.ENVELOPE Envelope, Reshape F-Curve values - e.g. change amplitude of movements.CYCLES Cycles, Cyclic extend/repeat keyframe sequence.NOISE Noise, Add pseudo-random noise on top of F-Curves.LIMITS Limits, Restrict maximum and minimum values of F-Curve.STEPPED Stepped Interpolation, Snap values to nearest grid-step - e.g. for a stop-motion look. 
    :type type: enum in ['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED'], (optional)
    :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip 
    :type only_active: boolean, (optional)
    '''

    pass


def fmodifier_copy():
    '''Copy the F-Modifier(s) of the active NLA-Strip 

    '''

    pass


def fmodifier_paste(only_active=True, replace=False):
    '''Add copied F-Modifiers to the selected NLA-Strips 

    :param only_active: Only Active, Only paste F-Modifiers on active strip 
    :type only_active: boolean, (optional)
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list 
    :type replace: boolean, (optional)
    '''

    pass


def make_single_user():
    '''Ensure that each action is only used once in the set of strips selected 

    '''

    pass


def meta_add():
    '''Add new meta-strips incorporating the selected strips 

    '''

    pass


def meta_remove():
    '''Separate out the strips held by the selected meta-strips 

    '''

    pass


def move_down():
    '''Move selected strips down a track if there’s room 

    '''

    pass


def move_up():
    '''Move selected strips up a track if there’s room 

    '''

    pass


def mute_toggle():
    '''Mute or un-mute selected strips 

    '''

    pass


def previewrange_set():
    '''Automatically set Preview Range based on range of keyframes 

    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def select_all_toggle(invert=False):
    '''Select or deselect all NLA-Strips 

    :param invert: Invert 
    :type invert: boolean, (optional)
    '''

    pass


def select_border(gesture_mode=0,
                  xmin=0,
                  xmax=0,
                  ymin=0,
                  ymax=0,
                  extend=True,
                  axis_range=False):
    '''Use box selection to grab NLA-Strips 

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
    :param axis_range: Axis Range 
    :type axis_range: boolean, (optional)
    '''

    pass


def select_leftright(mode='CHECK', extend=False):
    '''Select strips to the left or the right of the current frame 

    :param mode: Mode 
    :type mode: enum in ['CHECK', 'LEFT', 'RIGHT'], (optional)
    :param extend: Extend Select 
    :type extend: boolean, (optional)
    '''

    pass


def selected_objects_add():
    '''Make selected objects appear in NLA Editor by adding Animation Data 

    '''

    pass


def snap(type='CFRA'):
    '''Move start of strips to specified time 

    :param type: Type 
    :type type: enum in ['CFRA', 'NEAREST_FRAME', 'NEAREST_SECOND', 'NEAREST_MARKER'], (optional)
    '''

    pass


def soundclip_add():
    '''Add a strip for controlling when speaker plays its sound clip 

    '''

    pass


def split():
    '''Split selected strips at their midpoints 

    '''

    pass


def swap():
    '''Swap order of selected strips within tracks 

    '''

    pass


def tracks_add(above_selected=False):
    '''Add NLA-Tracks above/after the selected tracks 

    :param above_selected: Above Selected, Add a new NLA Track above every existing selected one 
    :type above_selected: boolean, (optional)
    '''

    pass


def tracks_delete():
    '''Delete selected NLA-Tracks and the strips they contain 

    '''

    pass


def transition_add():
    '''Add a transition strip between two adjacent selected strips 

    '''

    pass


def tweakmode_enter(isolate_action=False):
    '''Enter tweaking mode for the action referenced by the active strip to edit its keyframes 

    :param isolate_action: Isolate Action, Enable ‘solo’ on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack 
    :type isolate_action: boolean, (optional)
    '''

    pass


def tweakmode_exit(isolate_action=False):
    '''Exit tweaking mode for the action referenced by the active strip 

    :param isolate_action: Isolate Action, Disable ‘solo’ on any of the NLA Tracks after exiting tweak mode to get things back to normal 
    :type isolate_action: boolean, (optional)
    '''

    pass


def view_all():
    '''Reset viewable area to show full strips range 

    '''

    pass


def view_frame():
    '''Reset viewable area to show range around current frame 

    '''

    pass


def view_selected():
    '''Reset viewable area to show selected strips range 

    '''

    pass
