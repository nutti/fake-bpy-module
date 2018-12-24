def case_set(case='LOWER'):
    '''Set font case 

    :param case: Case, Lower or upper case 
    :type case: enum in ['LOWER', 'UPPER'], (optional)
    '''

    pass


def case_toggle():
    '''Toggle font case 

    '''

    pass


def change_character(delta=1):
    '''Change font character code 

    :param delta: Delta, Number to increase or decrease character code with 
    :type delta: int in [-255, 255], (optional)
    '''

    pass


def change_spacing(delta=1):
    '''Change font spacing 

    :param delta: Delta, Amount to decrease or increase character spacing with 
    :type delta: int in [-20, 20], (optional)
    '''

    pass


def delete(type='ALL'):
    '''Delete text by cursor position 

    :param type: Type, Which part of the text to delete 
    :type type: enum in ['ALL', 'NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'SELECTION', 'NEXT_OR_SELECTION', 'PREVIOUS_OR_SELECTION'], (optional)
    '''

    pass


def line_break():
    '''Insert line break at cursor position 

    '''

    pass


def move(type='LINE_BEGIN'):
    '''Move cursor to position type 

    :param type: Type, Where to move cursor to 
    :type type: enum in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)
    '''

    pass


def move_select(type='LINE_BEGIN'):
    '''Move the cursor while selecting 

    :param type: Type, Where to move cursor to, to make a selection 
    :type type: enum in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE', 'PREVIOUS_PAGE', 'NEXT_PAGE'], (optional)
    '''

    pass


def open(filepath="",
         filter_blender=False,
         filter_backup=False,
         filter_image=False,
         filter_movie=False,
         filter_python=False,
         filter_font=True,
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
         sort_method='FILE_SORT_ALPHA'):
    '''Load a new font from a file 

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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    '''

    pass


def select_all():
    '''Select all text 

    '''

    pass


def style_set(style='BOLD', clear=False):
    '''Set font style 

    :param style: Style, Style to set selection to 
    :type style: enum in ['BOLD', 'ITALIC', 'UNDERLINE', 'SMALL_CAPS'], (optional)
    :param clear: Clear, Clear style rather than setting it 
    :type clear: boolean, (optional)
    '''

    pass


def style_toggle(style='BOLD'):
    '''Toggle font style 

    :param style: Style, Style to set selection to 
    :type style: enum in ['BOLD', 'ITALIC', 'UNDERLINE', 'SMALL_CAPS'], (optional)
    '''

    pass


def text_copy():
    '''Copy selected text to clipboard 

    '''

    pass


def text_cut():
    '''Cut selected text to clipboard 

    '''

    pass


def text_insert(text="", accent=False):
    '''Insert text at cursor position 

    :param text: Text, Text to insert at the cursor position 
    :type text: string, (optional, never None)
    :param accent: Accent mode, Next typed character will strike through previous, for special character input 
    :type accent: boolean, (optional)
    '''

    pass


def text_paste():
    '''Paste text from clipboard 

    '''

    pass


def text_paste_from_file(filepath="",
                         filter_blender=False,
                         filter_backup=False,
                         filter_image=False,
                         filter_movie=False,
                         filter_python=False,
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
    '''Paste contents from file 

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
    '''

    pass


def textbox_add():
    '''Add a new text box 

    '''

    pass


def textbox_remove(index=0):
    '''Remove the textbox 

    :param index: Index, The current text box 
    :type index: int in [0, inf], (optional)
    '''

    pass


def unlink():
    '''Unlink active font data-block 

    '''

    pass
