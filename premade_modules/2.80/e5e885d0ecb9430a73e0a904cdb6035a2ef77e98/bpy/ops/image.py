def add_render_slot():
    '''Add a new render slot 

    '''

    pass


def change_frame(frame=0):
    '''Interactively change the current frame number 

    :param frame: Frame 
    :type frame: int in [-1048574, 1048574], (optional)
    '''

    pass


def clear_render_border():
    '''Clear the boundaries of the border render and disable border render 

    '''

    pass


def clear_render_slot():
    '''Clear the currently selected render slot 

    '''

    pass


def curves_point_set(point='BLACK_POINT'):
    '''Set black point or white point for curves 

    :param point: Point, Set black point or white point for curves 
    :type point: enum in ['BLACK_POINT', 'WHITE_POINT'], (optional)
    '''

    pass


def cycle_render_slot(reverse=False):
    '''Cycle through all non-void render slots 

    :param reverse: Cycle in Reverse 
    :type reverse: boolean, (optional)
    '''

    pass


def external_edit(filepath=""):
    '''Edit image in an external application 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    '''

    pass


def invert(invert_r=False, invert_g=False, invert_b=False, invert_a=False):
    '''Invert image’s channels 

    :param invert_r: Red, Invert Red Channel 
    :type invert_r: boolean, (optional)
    :param invert_g: Green, Invert Green Channel 
    :type invert_g: boolean, (optional)
    :param invert_b: Blue, Invert Blue Channel 
    :type invert_b: boolean, (optional)
    :param invert_a: Alpha, Invert Alpha Channel 
    :type invert_a: boolean, (optional)
    '''

    pass


def match_movie_length():
    '''Set image’s user’s length to the one of this video 

    '''

    pass


def new(name="Untitled",
        width=1024,
        height=1024,
        color=(0.0, 0.0, 0.0, 1.0),
        alpha=True,
        generated_type='BLANK',
        float=False,
        use_stereo_3d=False):
    '''Create a new image 

    :param name: Name, Image data-block name 
    :type name: string, (optional, never None)
    :param width: Width, Image width 
    :type width: int in [1, inf], (optional)
    :param height: Height, Image height 
    :type height: int in [1, inf], (optional)
    :param color: Color, Default fill color 
    :type color: float array of 4 items in [0, inf], (optional)
    :param alpha: Alpha, Create an image with an alpha channel 
    :type alpha: boolean, (optional)
    :param generated_type: Generated Type, Fill the image with a grid for UV map testingBLANK Blank, Generate a blank image.UV_GRID UV Grid, Generated grid to test UV mappings.COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings. 
    :type generated_type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth 
    :type float: boolean, (optional)
    :param use_stereo_3d: Stereo 3D, Create an image with left and right views 
    :type use_stereo_3d: boolean, (optional)
    '''

    pass


def open(filepath="",
         directory="",
         files=None,
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
         use_sequence_detection=True):
    '''Open image 

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
    :param show_multiview: Enable Multi-View 
    :type show_multiview: boolean, (optional)
    :param use_multiview: Use Multi-View 
    :type use_multiview: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names) 
    :type use_sequence_detection: boolean, (optional)
    '''

    pass


def pack(as_png=False):
    '''Pack an image as embedded data into the .blend file 

    :param as_png: Pack As PNG, Pack image as lossless PNG 
    :type as_png: boolean, (optional)
    '''

    pass


def project_apply():
    '''Project edited image back onto the object 

    '''

    pass


def project_edit():
    '''Edit a snapshot of the view-port in an external image editor 

    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def read_viewlayers():
    '''Read all the current scene’s view layers from cache, as needed 

    '''

    pass


def reload():
    '''Reload current image from disk 

    '''

    pass


def remove_render_slot():
    '''Remove the current render slot 

    '''

    pass


def render_border(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    '''Set the boundaries of the border render and enable border render 

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


def replace(filepath="",
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
            sort_method='FILE_SORT_ALPHA'):
    '''Replace current image by another one from disk 

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
    '''

    pass


def sample():
    '''Use mouse to sample a color in current image 

    '''

    pass


def sample_line(xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
    '''Sample a line and show it in Scope panels 

    :param xstart: X Start 
    :type xstart: int in [-inf, inf], (optional)
    :param xend: X End 
    :type xend: int in [-inf, inf], (optional)
    :param ystart: Y Start 
    :type ystart: int in [-inf, inf], (optional)
    :param yend: Y End 
    :type yend: int in [-inf, inf], (optional)
    :param cursor: Cursor, Mouse cursor style to use during the modal operator 
    :type cursor: int in [0, inf], (optional)
    '''

    pass


def save():
    '''Save the image with current name and settings 

    '''

    pass


def save_as(save_as_render=False,
            copy=False,
            filepath="",
            check_existing=True,
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
            sort_method='FILE_SORT_ALPHA'):
    '''Save the image with another name and/or settings 

    :param save_as_render: Save As Render, Apply render part of display transform when saving byte image 
    :type save_as_render: boolean, (optional)
    :param copy: Copy, Create a new image file without modifying the current image in blender 
    :type copy: boolean, (optional)
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
    '''

    pass


def save_dirty():
    '''Save all modified textures 

    '''

    pass


def save_sequence():
    '''Save a sequence of images 

    '''

    pass


def toolshelf():
    '''Toggles tool shelf display 

    '''

    pass


def unpack(method='USE_LOCAL', id=""):
    '''Save an image packed in the .blend file to disk 

    :param method: Method, How to unpack 
    :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
    :param id: Image Name, Image data-block name to unpack 
    :type id: string, (optional, never None)
    '''

    pass


def view_all(fit_view=False):
    '''View the entire image 

    :param fit_view: Fit View, Fit frame to the viewport 
    :type fit_view: boolean, (optional)
    '''

    pass


def view_ndof():
    '''Use a 3D mouse device to pan/zoom the view 

    '''

    pass


def view_pan(offset=(0.0, 0.0)):
    '''Pan the view 

    :param offset: Offset, Offset in floating point units, 1.0 is the width and height of the image 
    :type offset: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def view_selected():
    '''View all selected UVs 

    '''

    pass


def view_zoom(factor=0.0):
    '''Zoom in/out the image 

    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out 
    :type factor: float in [-inf, inf], (optional)
    '''

    pass


def view_zoom_border(xmin=0,
                     xmax=0,
                     ymin=0,
                     ymax=0,
                     wait_for_input=True,
                     zoom_out=False):
    '''Zoom in the view to the nearest item contained in the border 

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
    :param zoom_out: Zoom Out 
    :type zoom_out: boolean, (optional)
    '''

    pass


def view_zoom_in(location=(0.0, 0.0)):
    '''Zoom in the image (centered around 2D cursor) 

    :param location: Location, Cursor location in screen coordinates 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def view_zoom_out(location=(0.0, 0.0)):
    '''Zoom out the image (centered around 2D cursor) 

    :param location: Location, Cursor location in screen coordinates 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def view_zoom_ratio(ratio=0.0):
    '''Set zoom ratio of the view 

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out 
    :type ratio: float in [-inf, inf], (optional)
    '''

    pass
