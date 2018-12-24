def change_effect_input(swap='A_B'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param swap: Swap, The effect inputs to swap 
    :type swap: enum in ['A_B', 'B_C', 'A_C'], (optional)
    '''

    pass


def change_effect_type(type='CROSS'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Type, Sequencer effect typeCROSS Crossfade, Crossfade effect strip type.ADD Add, Add effect strip type.SUBTRACT Subtract, Subtract effect strip type.ALPHA_OVER Alpha Over, Alpha Over effect strip type.ALPHA_UNDER Alpha Under, Alpha Under effect strip type.GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type.MULTIPLY Multiply, Multiply effect strip type.OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type.WIPE Wipe, Wipe effect strip type.GLOW Glow, Glow effect strip type.TRANSFORM Transform, Transform effect strip type.COLOR Color, Color effect strip type.SPEED Speed, Color effect strip type.MULTICAM Multicam Selector.ADJUSTMENT Adjustment Layer.GAUSSIAN_BLUR Gaussian Blur.TEXT Text.COLORMIX Color Mix. 
    :type type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)
    '''

    pass


def change_path(filepath="",
                directory="",
                files=None,
                filter_blender=False,
                filter_backup=False,
                filter_image=False,
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
                relative_path=True,
                display_type='DEFAULT',
                sort_method='FILE_SORT_ALPHA',
                use_placeholders=False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip 
    :type use_placeholders: boolean, (optional)
    '''

    pass


def copy():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def crossfade_sounds():
    '''Do cross-fading volume animation of two selected sound strips 

    '''

    pass


def cut(frame=0, type='SOFT', side='MOUSE'):
    '''Cut the selected strips 

    :param frame: Frame, Frame where selected strips will be cut 
    :type frame: int in [-inf, inf], (optional)
    :param type: Type, The type of cut operation to perform on strips 
    :type type: enum in ['SOFT', 'HARD'], (optional)
    :param side: Side, The side that remains selected after cutting 
    :type side: enum in ['MOUSE', 'LEFT', 'RIGHT', 'BOTH'], (optional)
    '''

    pass


def cut_multicam(camera=1):
    '''Cut multi-cam strip and select camera 

    :param camera: Camera 
    :type camera: int in [1, 32], (optional)
    '''

    pass


def deinterlace_selected_movies():
    '''Deinterlace all selected movie sources 

    '''

    pass


def delete():
    '''Erase selected strips from the sequencer 

    '''

    pass


def duplicate(mode='TRANSLATION'):
    '''Duplicate the selected strips 

    :param mode: Mode 
    :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
    '''

    pass


def duplicate_move(SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None):
    '''Duplicate selected strips and move them 

    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips 
    :type SEQUENCER_OT_duplicate: SEQUENCER_OT_duplicate, (optional)
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time 
    :type TRANSFORM_OT_seq_slide: TRANSFORM_OT_seq_slide, (optional)
    '''

    pass


def effect_strip_add(frame_start=0,
                     frame_end=0,
                     channel=1,
                     replace_sel=True,
                     overlap=False,
                     type='CROSS',
                     color=(0.0, 0.0, 0.0)):
    '''Add an effect to the sequencer, most are applied on top of existing strips 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param frame_end: End Frame, End frame for the color strip 
    :type frame_end: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param type: Type, Sequencer effect typeCROSS Crossfade, Crossfade effect strip type.ADD Add, Add effect strip type.SUBTRACT Subtract, Subtract effect strip type.ALPHA_OVER Alpha Over, Alpha Over effect strip type.ALPHA_UNDER Alpha Under, Alpha Under effect strip type.GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type.MULTIPLY Multiply, Multiply effect strip type.OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type.WIPE Wipe, Wipe effect strip type.GLOW Glow, Glow effect strip type.TRANSFORM Transform, Transform effect strip type.COLOR Color, Color effect strip type.SPEED Speed, Color effect strip type.MULTICAM Multicam Selector.ADJUSTMENT Adjustment Layer.GAUSSIAN_BLUR Gaussian Blur.TEXT Text.COLORMIX Color Mix. 
    :type type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)
    :param color: Color, Initialize the strip with this color (only used when type=’COLOR’) 
    :type color: float array of 3 items in [0, 1], (optional)
    '''

    pass


def enable_proxies(proxy_25=False,
                   proxy_50=False,
                   proxy_75=False,
                   proxy_100=False,
                   overwrite=False):
    '''Enable selected proxies on all selected Movie strips 

    :param proxy_25: 25% 
    :type proxy_25: boolean, (optional)
    :param proxy_50: 50% 
    :type proxy_50: boolean, (optional)
    :param proxy_75: 75% 
    :type proxy_75: boolean, (optional)
    :param proxy_100: 100% 
    :type proxy_100: boolean, (optional)
    :param overwrite: Overwrite 
    :type overwrite: boolean, (optional)
    '''

    pass


def export_subtitles(filepath="",
                     check_existing=True,
                     filter_blender=False,
                     filter_backup=False,
                     filter_image=False,
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
                     filemode=8,
                     display_type='DEFAULT',
                     sort_method='FILE_SORT_ALPHA'):
    '''Export .srt file containing text strips 

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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def gap_insert(frames=10):
    '''Insert gap at current frame to first strips at the right, independent of selection or locked state of strips 

    :param frames: Frames, Frames to insert after current strip 
    :type frames: int in [0, inf], (optional)
    '''

    pass


def gap_remove(all=False):
    '''Remove gap at current frame to first strip at the right, independent of selection or locked state of strips 

    :param all: All Gaps, Do all gaps to right of current frame 
    :type all: boolean, (optional)
    '''

    pass


def image_strip_add(directory="",
                    files=None,
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
                    relative_path=True,
                    show_multiview=False,
                    use_multiview=False,
                    display_type='DEFAULT',
                    sort_method='FILE_SORT_ALPHA',
                    frame_start=0,
                    frame_end=0,
                    channel=1,
                    replace_sel=True,
                    overlap=False,
                    use_placeholders=False):
    '''Add an image or image sequence to the sequencer 

    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
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
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param frame_end: End Frame, End frame for the color strip 
    :type frame_end: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip 
    :type use_placeholders: boolean, (optional)
    '''

    pass


def images_separate(length=1):
    '''On image sequence strips, it returns a strip for each image 

    :param length: Length, Length of each frame 
    :type length: int in [1, inf], (optional)
    '''

    pass


def lock():
    '''Lock the active strip so that it can’t be transformed 

    '''

    pass


def mask_strip_add(frame_start=0,
                   channel=1,
                   replace_sel=True,
                   overlap=False,
                   mask=''):
    '''Add a mask strip to the sequencer 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param mask: Mask 
    :type mask: enum in [], (optional)
    '''

    pass


def meta_make():
    '''Group selected strips into a metastrip 

    '''

    pass


def meta_separate():
    '''Put the contents of a metastrip back in the sequencer 

    '''

    pass


def meta_toggle():
    '''Toggle a metastrip (to edit enclosed strips) 

    '''

    pass


def movie_strip_add(filepath="",
                    files=None,
                    filter_blender=False,
                    filter_backup=False,
                    filter_image=False,
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
                    frame_start=0,
                    channel=1,
                    replace_sel=True,
                    overlap=False,
                    sound=True,
                    use_framerate=True):
    '''Add a movie strip to the sequencer 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
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
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param sound: Sound, Load sound with the movie 
    :type sound: boolean, (optional)
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync 
    :type use_framerate: boolean, (optional)
    '''

    pass


def movieclip_strip_add(frame_start=0,
                        channel=1,
                        replace_sel=True,
                        overlap=False,
                        clip=''):
    '''Add a movieclip strip to the sequencer 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param clip: Clip 
    :type clip: enum in [], (optional)
    '''

    pass


def mute(unselected=False):
    '''Mute (un)selected strips 

    :param unselected: Unselected, Mute unselected rather than selected strips 
    :type unselected: boolean, (optional)
    '''

    pass


def offset_clear():
    '''Clear strip offsets from the start and end frames 

    '''

    pass


def paste():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def reassign_inputs():
    '''Reassign the inputs for the effect strip 

    '''

    pass


def rebuild_proxy():
    '''Rebuild all selected proxies and timecode indices using the job system 

    '''

    pass


def refresh_all():
    '''Refresh the sequencer editor 

    '''

    pass


def reload(adjust_length=False):
    '''Reload strips in the sequencer 

    :param adjust_length: Adjust Length, Adjust length of strips to their data length 
    :type adjust_length: boolean, (optional)
    '''

    pass


def rendersize():
    '''Set render size and aspect from active sequence 

    '''

    pass


def sample():
    '''Use mouse to sample color in current frame 

    '''

    pass


def scene_strip_add(frame_start=0,
                    channel=1,
                    replace_sel=True,
                    overlap=False,
                    scene=''):
    '''Add a strip to the sequencer using a blender scene as a source 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param scene: Scene 
    :type scene: enum in [], (optional)
    '''

    pass


def select(extend=False,
           linked_handle=False,
           left_right='NONE',
           linked_time=False):
    '''Select a strip (last selected becomes the “active strip”) 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    :param linked_handle: Linked Handle, Select handles next to the active strip 
    :type linked_handle: boolean, (optional)
    :param left_right: Left/Right, Select based on the current frame side the cursor is onNONE None, Don’t do left-right selection.MOUSE Mouse, Use mouse position for selection.LEFT Left, Select left.RIGHT Right, Select right. 
    :type left_right: enum in ['NONE', 'MOUSE', 'LEFT', 'RIGHT'], (optional)
    :param linked_time: Linked Time, Select other strips at the same time 
    :type linked_time: boolean, (optional)
    '''

    pass


def select_active_side(side='BOTH'):
    '''Select strips on the nominated side of the active strip 

    :param side: Side, The side of the handle that is selected 
    :type side: enum in ['MOUSE', 'LEFT', 'RIGHT', 'BOTH'], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Select or deselect all strips 

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
               extend=True):
    '''Select strips using box selection 

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


def select_grouped(type='TYPE', extend=False, use_active_channel=False):
    '''Select all strips grouped by various properties 

    :param type: TypeTYPE Type, Shared strip type.TYPE_BASIC Global Type, All strips of same basic type (Graphical or Sound).TYPE_EFFECT Effect Type, Shared strip effect type (if active strip is not an effect one, select all non-effect strips).DATA Data, Shared data (scene, image, sound, etc.).EFFECT Effect, Shared effects.EFFECT_LINK Effect/Linked, Other strips affected by the active one (sharing some time, and below or effect-assigned).OVERLAP Overlap, Overlapping time. 
    :type type: enum in ['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP'], (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one 
    :type use_active_channel: boolean, (optional)
    '''

    pass


def select_handles(side='BOTH'):
    '''Select gizmo handles on the sides of the selected strip 

    :param side: Side, The side of the handle that is selected 
    :type side: enum in ['MOUSE', 'LEFT', 'RIGHT', 'BOTH'], (optional)
    '''

    pass


def select_less():
    '''Shrink the current selection of adjacent selected strips 

    '''

    pass


def select_linked():
    '''Select all strips adjacent to the current selection 

    '''

    pass


def select_linked_pick(extend=False):
    '''Select a chain of linked strips nearest to the mouse pointer 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_more():
    '''Select more strips adjacent to the current selection 

    '''

    pass


def slip(offset=0):
    '''Trim the contents of the active strip 

    :param offset: Offset, Offset to the data of the strip 
    :type offset: int in [-inf, inf], (optional)
    '''

    pass


def snap(frame=0):
    '''Frame where selected strips will be snapped 

    :param frame: Frame, Frame where selected strips will be snapped 
    :type frame: int in [-inf, inf], (optional)
    '''

    pass


def sound_strip_add(filepath="",
                    files=None,
                    filter_blender=False,
                    filter_backup=False,
                    filter_image=False,
                    filter_movie=False,
                    filter_python=False,
                    filter_font=False,
                    filter_sound=True,
                    filter_text=False,
                    filter_btx=False,
                    filter_collada=False,
                    filter_alembic=False,
                    filter_folder=True,
                    filter_blenlib=False,
                    filemode=9,
                    relative_path=True,
                    display_type='DEFAULT',
                    sort_method='FILE_SORT_ALPHA',
                    frame_start=0,
                    channel=1,
                    replace_sel=True,
                    overlap=False,
                    cache=False,
                    mono=False):
    '''Add a sound strip to the sequencer 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param files: Files 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int in [-inf, inf], (optional)
    :param channel: Channel, Channel to place this strip into 
    :type channel: int in [1, 32], (optional)
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: boolean, (optional)
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: boolean, (optional)
    :param cache: Cache, Cache the sound in memory 
    :type cache: boolean, (optional)
    :param mono: Mono, Merge all the sound’s channels into one 
    :type mono: boolean, (optional)
    '''

    pass


def strip_jump(next=True, center=True):
    '''Move frame to previous edit point 

    :param next: Next Strip 
    :type next: boolean, (optional)
    :param center: Use strip center 
    :type center: boolean, (optional)
    '''

    pass


def strip_modifier_add(type='COLOR_BALANCE'):
    '''Add a modifier to the strip 

    :param type: Type 
    :type type: enum in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP'], (optional)
    '''

    pass


def strip_modifier_copy(type='REPLACE'):
    '''Copy modifiers of the active strip to all selected strips 

    :param type: TypeREPLACE Replace, Replace modifiers in destination.APPEND Append, Append active modifiers to selected strips. 
    :type type: enum in ['REPLACE', 'APPEND'], (optional)
    '''

    pass


def strip_modifier_move(name="Name", direction='UP'):
    '''Move modifier up and down in the stack 

    :param name: Name, Name of modifier to remove 
    :type name: string, (optional, never None)
    :param direction: TypeUP Up, Move modifier up in the stack.DOWN Down, Move modifier down in the stack. 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def strip_modifier_remove(name="Name"):
    '''Remove a modifier from the strip 

    :param name: Name, Name of modifier to remove 
    :type name: string, (optional, never None)
    '''

    pass


def swap(side='RIGHT'):
    '''Swap active strip with strip to the right or left 

    :param side: Side, Side of the strip to swap 
    :type side: enum in ['LEFT', 'RIGHT'], (optional)
    '''

    pass


def swap_data():
    '''Swap 2 sequencer strips 

    '''

    pass


def swap_inputs():
    '''Swap the first two inputs for the effect strip 

    '''

    pass


def unlock():
    '''Unlock the active strip so that it can’t be transformed 

    '''

    pass


def unmute(unselected=False):
    '''Unmute (un)selected strips 

    :param unselected: Unselected, Unmute unselected rather than selected strips 
    :type unselected: boolean, (optional)
    '''

    pass


def view_all():
    '''View all the strips in the sequencer 

    '''

    pass


def view_all_preview():
    '''Zoom preview to fit in the area 

    '''

    pass


def view_frame():
    '''Reset viewable area to show range around current frame 

    '''

    pass


def view_ghost_border(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    '''Set the boundaries of the border used for offset-view 

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


def view_selected():
    '''Zoom the sequencer on the selected strips 

    '''

    pass


def view_toggle():
    '''Toggle between sequencer views (sequence, preview, both) 

    '''

    pass


def view_zoom_ratio(ratio=1.0):
    '''Change zoom ratio of sequencer preview 

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out 
    :type ratio: float in [-inf, inf], (optional)
    '''

    pass
