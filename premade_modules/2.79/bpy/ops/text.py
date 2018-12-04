def autocomplete():
    '''Show a list of used text in the open document 

    '''

    pass


def comment():
    '''Convert selected text to comment 

    '''

    pass


def convert_whitespace(type='SPACES'):
    '''Convert whitespaces by type 

    :param type: Type, Type of whitespace to convert to 
    :type type: enum in ['SPACES', 'TABS'], (optional)
    '''

    pass


def copy():
    '''Copy selected text to clipboard 

    '''

    pass


def cursor_set(x=0, y=0):
    '''Set cursor position 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    '''

    pass


def cut():
    '''Cut selected text to clipboard 

    '''

    pass


def delete(type='NEXT_CHARACTER'):
    '''Delete text by cursor position 

    :param type: Type, Which part of the text to delete 
    :type type: enum in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)
    '''

    pass


def duplicate_line():
    '''Duplicate the current line 

    '''

    pass


def find():
    '''Find specified text 

    '''

    pass


def find_set_selected():
    '''Find specified text and set as selected 

    '''

    pass


def indent():
    '''Indent selected text 

    '''

    pass


def insert(text=""):
    '''Insert text at cursor position 

    :param text: Text, Text to insert at the cursor position 
    :type text: string, (optional, never None)
    '''

    pass


def jump(line=1):
    '''Jump cursor to line 

    :param line: Line, Line number to jump to 
    :type line: int in [1, inf], (optional)
    '''

    pass


def line_break():
    '''Insert line break at cursor position 

    '''

    pass


def line_number():
    '''The current line number 

    '''

    pass


def make_internal():
    '''Make active text file internal 

    '''

    pass


def move(type='LINE_BEGIN'):
    '''Move cursor to position type 

    :param type: Type, Where to move cursor to 
    :type type: enum in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)
    '''

    pass


def move_lines(direction='DOWN'):
    '''Move the currently selected line(s) up/down 

    :param direction: Direction 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def move_select(type='LINE_BEGIN'):
    '''Move the cursor while selecting 

    :param type: Type, Where to move cursor to, to make a selection 
    :type type: enum in ['LINE_BEGIN', 'LINE_END', 'FILE_TOP', 'FILE_BOTTOM', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)
    '''

    pass


def new():
    '''Create a new text data-block 

    '''

    pass


def open(filepath="",
         filter_blender=False,
         filter_backup=False,
         filter_image=False,
         filter_movie=False,
         filter_python=True,
         filter_font=False,
         filter_sound=False,
         filter_text=True,
         filter_btx=False,
         filter_collada=False,
         filter_alembic=False,
         filter_folder=True,
         filter_blenlib=False,
         filemode=9,
         display_type='DEFAULT',
         sort_method='FILE_SORT_ALPHA',
         internal=False):
    '''Open a new text data-block 

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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param internal: Make internal, Make text file internal after loading 
    :type internal: boolean, (optional)
    '''

    pass


def overwrite_toggle():
    '''Toggle overwrite while typing 

    '''

    pass


def paste(selection=False):
    '''Paste text from clipboard 

    :param selection: Selection, Paste text selected elsewhere rather than copied (X11 only) 
    :type selection: boolean, (optional)
    '''

    pass


def properties():
    '''Toggle the properties region visibility 

    '''

    pass


def refresh_pyconstraints():
    '''Refresh all pyconstraints 

    '''

    pass


def reload():
    '''Reload active text data-block from its file 

    '''

    pass


def replace():
    '''Replace text with the specified text 

    '''

    pass


def replace_set_selected():
    '''Replace text with specified text and set as selected 

    '''

    pass


def resolve_conflict(resolution='IGNORE'):
    '''When external text is out of sync, resolve the conflict 

    :param resolution: Resolution, How to solve conflict due to differences in internal and external text 
    :type resolution: enum in ['IGNORE', 'RELOAD', 'SAVE', 'MAKE_INTERNAL'], (optional)
    '''

    pass


def run_script():
    '''Run active script 

    '''

    pass


def save():
    '''Save active text data-block 

    '''

    pass


def save_as(filepath="",
            check_existing=True,
            filter_blender=False,
            filter_backup=False,
            filter_image=False,
            filter_movie=False,
            filter_python=True,
            filter_font=False,
            filter_sound=False,
            filter_text=True,
            filter_btx=False,
            filter_collada=False,
            filter_alembic=False,
            filter_folder=True,
            filter_blenlib=False,
            filemode=9,
            display_type='DEFAULT',
            sort_method='FILE_SORT_ALPHA'):
    '''Save active text file with options 

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


def scroll(lines=1):
    '''Undocumented 

    :param lines: Lines, Number of lines to scroll 
    :type lines: int in [-inf, inf], (optional)
    '''

    pass


def scroll_bar(lines=1):
    '''Undocumented 

    :param lines: Lines, Number of lines to scroll 
    :type lines: int in [-inf, inf], (optional)
    '''

    pass


def select_all():
    '''Select all text 

    '''

    pass


def select_line():
    '''Select text by line 

    '''

    pass


def select_word():
    '''Select word under cursor 

    '''

    pass


def selection_set(select=False):
    '''Set cursor selection 

    :param select: Select, Set selection end rather than cursor 
    :type select: boolean, (optional)
    '''

    pass


def start_find():
    '''Start searching text 

    '''

    pass


def to_3d_object(split_lines=False):
    '''Create 3D text object from active text data-block 

    :param split_lines: Split Lines, Create one object per line in the text 
    :type split_lines: boolean, (optional)
    '''

    pass


def uncomment():
    '''Convert selected comment to text 

    '''

    pass


def unindent():
    '''Unindent selected text 

    '''

    pass


def unlink():
    '''Unlink active text data-block 

    '''

    pass
