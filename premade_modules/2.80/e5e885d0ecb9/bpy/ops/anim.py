def change_frame(frame=0.0, snap=False):
    '''Interactively change the current frame number 

    :param frame: Frame 
    :type frame: float in [-1.04857e+06, 1.04857e+06], (optional)
    :param snap: Snap 
    :type snap: boolean, (optional)
    '''

    pass


def channel_select_keys(extend=False):
    '''Select all keyframes of channel under mouse 

    :param extend: Extend, Extend selection 
    :type extend: boolean, (optional)
    '''

    pass


def channels_clean_empty():
    '''Delete all empty animation data containers from visible data-blocks 

    '''

    pass


def channels_click(extend=False, children_only=False):
    '''Handle mouse-clicks over animation channels 

    :param extend: Extend Select 
    :type extend: boolean, (optional)
    :param children_only: Select Children Only 
    :type children_only: boolean, (optional)
    '''

    pass


def channels_collapse(all=True):
    '''Collapse (i.e. close) all selected expandable animation channels 

    :param all: All, Collapse all channels (not just selected ones) 
    :type all: boolean, (optional)
    '''

    pass


def channels_delete():
    '''Delete all selected animation channels 

    '''

    pass


def channels_editable_toggle(mode='TOGGLE', type='PROTECT'):
    '''Toggle editability of selected channels 

    :param mode: Mode 
    :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
    :param type: Type 
    :type type: enum in ['PROTECT', 'MUTE'], (optional)
    '''

    pass


def channels_expand(all=True):
    '''Expand (i.e. open) all selected expandable animation channels 

    :param all: All, Expand all channels (not just selected ones) 
    :type all: boolean, (optional)
    '''

    pass


def channels_fcurves_enable():
    '''Clears ‘disabled’ tag from all F-Curves to get broken F-Curves working again 

    '''

    pass


def channels_find(query="Query"):
    '''Filter the set of channels shown to only include those with matching names 

    :param query: Text to search for in channel names 
    :type query: string, (optional, never None)
    '''

    pass


def channels_group(name="New Group"):
    '''Add selected F-Curves to a new group 

    :param name: Name, Name of newly created group 
    :type name: string, (optional, never None)
    '''

    pass


def channels_move(direction='DOWN'):
    '''Rearrange selected animation channels 

    :param direction: Direction 
    :type direction: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)
    '''

    pass


def channels_rename():
    '''Rename animation channel under mouse 

    '''

    pass


def channels_select_all(action='TOGGLE'):
    '''Toggle selection of all animation channels 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def channels_select_box(xmin=0,
                        xmax=0,
                        ymin=0,
                        ymax=0,
                        wait_for_input=True,
                        deselect=False,
                        extend=True):
    '''Select all animation channels within the specified region 

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
    '''

    pass


def channels_setting_disable(mode='DISABLE', type='PROTECT'):
    '''Disable specified setting on all selected animation channels 

    :param mode: Mode 
    :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
    :param type: Type 
    :type type: enum in ['PROTECT', 'MUTE'], (optional)
    '''

    pass


def channels_setting_enable(mode='ENABLE', type='PROTECT'):
    '''Enable specified setting on all selected animation channels 

    :param mode: Mode 
    :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
    :param type: Type 
    :type type: enum in ['PROTECT', 'MUTE'], (optional)
    '''

    pass


def channels_setting_toggle(mode='TOGGLE', type='PROTECT'):
    '''Toggle specified setting on all selected animation channels 

    :param mode: Mode 
    :type mode: enum in ['TOGGLE', 'DISABLE', 'ENABLE', 'INVERT'], (optional)
    :param type: Type 
    :type type: enum in ['PROTECT', 'MUTE'], (optional)
    '''

    pass


def channels_ungroup():
    '''Remove selected F-Curves from their current groups 

    '''

    pass


def clear_useless_actions(only_unused=True):
    '''Mark actions with no F-Curves for deletion after save & reload of file preserving “action libraries” 

    :param only_unused: Only Unused, Only unused (Fake User only) actions get considered 
    :type only_unused: boolean, (optional)
    '''

    pass


def copy_driver_button():
    '''Copy the driver for the highlighted button 

    '''

    pass


def driver_button_add():
    '''Add driver for the property under the cursor 

    '''

    pass


def driver_button_edit():
    '''Edit the drivers for the property connected represented by the highlighted button 

    '''

    pass


def driver_button_remove(all=True):
    '''Remove the driver(s) for the property(s) connected represented by the highlighted button 

    :param all: All, Delete drivers for all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def end_frame_set():
    '''Set the current frame as the preview or scene end frame 

    '''

    pass


def keyframe_clear_button(all=True):
    '''Clear all keyframes on the currently active property 

    :param all: All, Clear keyframes from all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def keyframe_clear_v3d():
    '''Remove all keyframe animation for selected objects 

    '''

    pass


def keyframe_delete(type='DEFAULT', confirm_success=True):
    '''Delete keyframes on the current frame for all properties in the specified Keying Set 

    :param type: Keying Set, The Keying Set to use 
    :type type: enum in ['DEFAULT'], (optional)
    :param confirm_success: Confirm Successful Delete, Show a popup when the keyframes get successfully removed 
    :type confirm_success: boolean, (optional)
    '''

    pass


def keyframe_delete_button(all=True):
    '''Delete current keyframe of current UI-active property 

    :param all: All, Delete keyframes from all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def keyframe_delete_v3d():
    '''Remove keyframes on current frame for selected objects and bones 

    '''

    pass


def keyframe_insert(type='DEFAULT', confirm_success=True):
    '''Insert keyframes on the current frame for all properties in the specified Keying Set 

    :param type: Keying Set, The Keying Set to use 
    :type type: enum in ['DEFAULT'], (optional)
    :param confirm_success: Confirm Successful Insert, Show a popup when the keyframes get successfully added 
    :type confirm_success: boolean, (optional)
    '''

    pass


def keyframe_insert_button(all=True):
    '''Insert a keyframe for current UI-active property 

    :param all: All, Insert a keyframe for all element of the array 
    :type all: boolean, (optional)
    '''

    pass


def keyframe_insert_menu(type='DEFAULT',
                         confirm_success=False,
                         always_prompt=False):
    '''Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined 

    :param type: Keying Set, The Keying Set to use 
    :type type: enum in ['DEFAULT'], (optional)
    :param confirm_success: Confirm Successful Insert, Show a popup when the keyframes get successfully added 
    :type confirm_success: boolean, (optional)
    :param always_prompt: Always Show Menu 
    :type always_prompt: boolean, (optional)
    '''

    pass


def keying_set_active_set(type='DEFAULT'):
    '''Select a new keying set as the active one 

    :param type: Keying Set, The Keying Set to use 
    :type type: enum in ['DEFAULT'], (optional)
    '''

    pass


def keying_set_add():
    '''Add a new (empty) Keying Set to the active Scene 

    '''

    pass


def keying_set_export(filepath="",
                      filter_folder=True,
                      filter_text=True,
                      filter_python=True):
    '''Export Keying Set to a python script 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_text: Filter text 
    :type filter_text: boolean, (optional)
    :param filter_python: Filter python 
    :type filter_python: boolean, (optional)
    '''

    pass


def keying_set_path_add():
    '''Add empty path to active Keying Set 

    '''

    pass


def keying_set_path_remove():
    '''Remove active Path from active Keying Set 

    '''

    pass


def keying_set_remove():
    '''Remove the active Keying Set 

    '''

    pass


def keyingset_button_add(all=True):
    '''Add current UI-active property to current keying set 

    :param all: All, Add all elements of the array to a Keying Set 
    :type all: boolean, (optional)
    '''

    pass


def keyingset_button_remove():
    '''Remove current UI-active property from current keying set 

    '''

    pass


def paste_driver_button():
    '''Paste the driver in the copy/paste buffer for the highlighted button 

    '''

    pass


def previewrange_clear():
    '''Clear Preview Range 

    '''

    pass


def previewrange_set(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    '''Interactively define frame range used for playback 

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


def start_frame_set():
    '''Set the current frame as the preview or scene start frame 

    '''

    pass


def update_animated_transform_constraints(use_convert_to_radians=True):
    '''Update fcurves/drivers affecting Transform constraints (use it with files from 2.70 and earlier) 

    :param use_convert_to_radians: Convert To Radians, Convert fcurves/drivers affecting rotations to radians (Warning: use this only once!) 
    :type use_convert_to_radians: boolean, (optional)
    '''

    pass
