def autopack_toggle():
    '''Automatically pack all external files into the .blend file 

    '''

    pass


def bookmark_add():
    '''Add a bookmark for the selected/active directory 

    '''

    pass


def bookmark_cleanup():
    '''Delete all invalid bookmarks 

    '''

    pass


def bookmark_delete(index=-1):
    '''Delete selected bookmark 

    :param index: Index 
    :type index: int in [-1, 20000], (optional)
    '''

    pass


def bookmark_move(direction='TOP'):
    '''Move the active bookmark up/down in the list 

    :param direction: Direction, Direction to move the active bookmark towardsTOP Top, Top of the list.UP Up.DOWN Down.BOTTOM Bottom, Bottom of the list. 
    :type direction: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)
    '''

    pass


def bookmark_toggle():
    '''Toggle bookmarks display 

    '''

    pass


def cancel():
    '''Cancel loading of selected file 

    '''

    pass


def delete():
    '''Delete selected files 

    '''

    pass


def directory_new(directory="", open=False):
    '''Create a new directory 

    :param directory: Directory, Name of new directory 
    :type directory: string, (optional, never None)
    :param open: Open, Open new directory 
    :type open: boolean, (optional)
    '''

    pass


def execute(need_active=False):
    '''Execute selected file 

    :param need_active: Need Active, Only execute if there’s an active selected file in the file list 
    :type need_active: boolean, (optional)
    '''

    pass


def filenum(increment=1):
    '''Increment number in filename 

    :param increment: Increment 
    :type increment: int in [-100, 100], (optional)
    '''

    pass


def filepath_drop(filepath="Path"):
    '''Undocumented 

    '''

    pass


def find_missing_files(find_all=False,
                       directory="",
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
                       filter_folder=False,
                       filter_blenlib=False,
                       filemode=9,
                       display_type='DEFAULT',
                       sort_method='FILE_SORT_ALPHA'):
    '''Try to find missing external files 

    :param find_all: Find All, Find all files in the search path (not just missing) 
    :type find_all: boolean, (optional)
    :param directory: Directory, Directory of the file 
    :type directory: string, (optional, never None)
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


def hidedot():
    '''Toggle hide hidden dot files 

    '''

    pass


def highlight():
    '''Highlight selected file(s) 

    '''

    pass


def make_paths_absolute():
    '''Make all paths to external files absolute 

    '''

    pass


def make_paths_relative():
    '''Make all paths to external files relative to current .blend 

    '''

    pass


def next():
    '''Move to next folder 

    '''

    pass


def pack_all():
    '''Pack all used external files into the .blend 

    '''

    pass


def pack_libraries():
    '''Pack all used Blender library files into the current .blend 

    '''

    pass


def parent():
    '''Move to parent directory 

    '''

    pass


def previous():
    '''Move to previous folder 

    '''

    pass


def refresh():
    '''Refresh the file list 

    '''

    pass


def rename():
    '''Rename file or file directory 

    '''

    pass


def report_missing_files():
    '''Report all missing external files 

    '''

    pass


def reset_recent():
    '''Reset Recent files 

    '''

    pass


def select(extend=False, fill=False, open=True):
    '''Activate/select file 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param fill: Fill, Select everything beginning with the last selection 
    :type fill: boolean, (optional)
    :param open: Open, Open a directory when selecting it 
    :type open: boolean, (optional)
    '''

    pass


def select_all_toggle():
    '''Select or deselect all files 

    '''

    pass


def select_bookmark(dir=""):
    '''Select a bookmarked directory 

    :param dir: Dir 
    :type dir: string, (optional, never None)
    '''

    pass


def select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    '''Activate/select the file(s) contained in the border 

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


def select_walk(direction='UP', extend=False, fill=False):
    '''Select/Deselect files by walking through them 

    :param direction: Walk Direction, Select/Deselect file in this direction 
    :type direction: enum in ['UP', 'DOWN', 'LEFT', 'RIGHT'], (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param fill: Fill, Select everything beginning with the last selection 
    :type fill: boolean, (optional)
    '''

    pass


def smoothscroll():
    '''Smooth scroll to make editable file visible 

    '''

    pass


def unpack_all(method='USE_LOCAL'):
    '''Unpack all files packed into this .blend to external ones 

    :param method: Method, How to unpack 
    :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL', 'KEEP'], (optional)
    '''

    pass


def unpack_item(method='USE_LOCAL', id_name="", id_type=19785):
    '''Unpack this file to an external file 

    :param method: Method, How to unpack 
    :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
    :param id_name: ID name, Name of ID block to unpack 
    :type id_name: string, (optional, never None)
    :param id_type: ID Type, Identifier type of ID block 
    :type id_type: int in [0, inf], (optional)
    '''

    pass


def unpack_libraries():
    '''Unpack all used Blender library files from this .blend file 

    '''

    pass
