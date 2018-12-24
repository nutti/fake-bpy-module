def actionzone(modifier=0):
    '''Handle area action zones for mouse actions/gestures 

    :param modifier: Modifier, Modifier state 
    :type modifier: int in [0, 2], (optional)
    '''

    pass


def animation_cancel(restore_frame=True):
    '''Cancel animation, returning to the original frame 

    :param restore_frame: Restore Frame, Restore the frame when animation was initialized 
    :type restore_frame: boolean, (optional)
    '''

    pass


def animation_play(reverse=False, sync=False):
    '''Play animation 

    :param reverse: Play in Reverse, Animation is played backwards 
    :type reverse: boolean, (optional)
    :param sync: Sync, Drop frames to maintain framerate 
    :type sync: boolean, (optional)
    '''

    pass


def animation_step():
    '''Step through animation by position 

    '''

    pass


def area_dupli():
    '''Duplicate selected area into new window 

    '''

    pass


def area_join(min_x=-100, min_y=-100, max_x=-100, max_y=-100):
    '''Join selected areas into new window 

    :param min_x: X 1 
    :type min_x: int in [-inf, inf], (optional)
    :param min_y: Y 1 
    :type min_y: int in [-inf, inf], (optional)
    :param max_x: X 2 
    :type max_x: int in [-inf, inf], (optional)
    :param max_y: Y 2 
    :type max_y: int in [-inf, inf], (optional)
    '''

    pass


def area_move(x=0, y=0, delta=0):
    '''Move selected area edges 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    '''

    pass


def area_options():
    '''Operations for splitting and merging 

    '''

    pass


def area_split(direction='HORIZONTAL', factor=0.5, mouse_x=-100, mouse_y=-100):
    '''Split selected area into new windows 

    :param direction: Direction 
    :type direction: enum in ['HORIZONTAL', 'VERTICAL'], (optional)
    :param factor: Factor 
    :type factor: float in [0, 1], (optional)
    :param mouse_x: Mouse X 
    :type mouse_x: int in [-inf, inf], (optional)
    :param mouse_y: Mouse Y 
    :type mouse_y: int in [-inf, inf], (optional)
    '''

    pass


def area_swap():
    '''Swap selected areas screen positions 

    '''

    pass


def back_to_previous():
    '''Revert back to the original screen layout, before fullscreen area overlay 

    '''

    pass


def delete():
    '''Delete active screen 

    '''

    pass


def frame_jump(end=False):
    '''Jump to first/last frame in frame range 

    :param end: Last Frame, Jump to the last frame of the frame range 
    :type end: boolean, (optional)
    '''

    pass


def frame_offset(delta=0):
    '''Move current frame forward/backward by a given number 

    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    '''

    pass


def header():
    '''Toggle header display 

    '''

    pass


def header_flip():
    '''Toggle the header over/below the main window area 

    '''

    pass


def header_toggle_menus():
    '''Expand or collapse the header pulldown menus 

    '''

    pass


def header_toolbox():
    '''Display header region toolbox 

    '''

    pass


def keyframe_jump(next=True):
    '''Jump to previous/next keyframe 

    :param next: Next Keyframe 
    :type next: boolean, (optional)
    '''

    pass


def marker_jump(next=True):
    '''Jump to previous/next marker 

    :param next: Next Marker 
    :type next: boolean, (optional)
    '''

    pass


def new():
    '''Add a new screen 

    '''

    pass


def redo_last():
    '''Display menu for last action performed 

    '''

    pass


def region_blend():
    '''Blend in and out overlapping region 

    '''

    pass


def region_flip():
    '''Toggle the region’s alignment (left/right or top/bottom) 

    '''

    pass


def region_quadview():
    '''Split selected area into camera, front, right & top views 

    '''

    pass


def region_scale():
    '''Scale selected area 

    '''

    pass


def repeat_history(index=0):
    '''Display menu for previous actions performed 

    :param index: Index 
    :type index: int in [0, inf], (optional)
    '''

    pass


def repeat_last():
    '''Repeat last action 

    '''

    pass


def screen_full_area(use_hide_panels=False):
    '''Toggle display selected area as fullscreen/maximized 

    :param use_hide_panels: Hide Panels, Hide all the panels 
    :type use_hide_panels: boolean, (optional)
    '''

    pass


def screen_set(delta=0):
    '''Cycle through available screens 

    :param delta: Delta 
    :type delta: int in [-inf, inf], (optional)
    '''

    pass


def screencast(filepath="", full=True):
    '''Capture a video of the active area or whole Blender window 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param full: Full Screen, Capture the whole window (otherwise only capture the active area) 
    :type full: boolean, (optional)
    '''

    pass


def screenshot(filepath="",
               check_existing=True,
               filter_blender=False,
               filter_backup=False,
               filter_image=True,
               filter_movie=False,
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
               show_multiview=False,
               use_multiview=False,
               display_type='DEFAULT',
               sort_method='FILE_SORT_ALPHA',
               full=True):
    '''Capture a picture of the active area or whole Blender window 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
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
    :param show_multiview: Enable Multi-View 
    :type show_multiview: boolean, (optional)
    :param use_multiview: Use Multi-View 
    :type use_multiview: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param full: Full Screen, Capture the whole window (otherwise only capture the active area) 
    :type full: boolean, (optional)
    '''

    pass


def spacedata_cleanup():
    '''Remove unused settings for invisible editors 

    '''

    pass


def userpref_show():
    '''Show user preferences 

    '''

    pass
