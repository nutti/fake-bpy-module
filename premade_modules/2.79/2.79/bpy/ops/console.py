def autocomplete():
    '''Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one 

    '''

    pass


def banner():
    '''Print a message when the terminal initializes 

    '''

    pass


def clear(scrollback=True, history=False):
    '''Clear text by type 

    :param scrollback: Scrollback, Clear the scrollback history 
    :type scrollback: boolean, (optional)
    :param history: History, Clear the command history 
    :type history: boolean, (optional)
    '''

    pass


def clear_line():
    '''Clear the line and store in history 

    '''

    pass


def copy():
    '''Copy selected text to clipboard 

    '''

    pass


def copy_as_script():
    '''Copy the console contents for use in a script 

    '''

    pass


def delete(type='NEXT_CHARACTER'):
    '''Delete text by cursor position 

    :param type: Type, Which part of the text to delete 
    :type type: enum in ['NEXT_CHARACTER', 'PREVIOUS_CHARACTER', 'NEXT_WORD', 'PREVIOUS_WORD'], (optional)
    '''

    pass


def execute(interactive=False):
    '''Execute the current console line as a python expression 

    :param interactive: interactive 
    :type interactive: boolean, (optional)
    '''

    pass


def history_append(text="", current_character=0, remove_duplicates=False):
    '''Append history at cursor position 

    :param text: Text, Text to insert at the cursor position 
    :type text: string, (optional, never None)
    :param current_character: Cursor, The index of the cursor 
    :type current_character: int in [0, inf], (optional)
    :param remove_duplicates: Remove Duplicates, Remove duplicate items in the history 
    :type remove_duplicates: boolean, (optional)
    '''

    pass


def history_cycle(reverse=False):
    '''Cycle through history 

    :param reverse: Reverse, Reverse cycle history 
    :type reverse: boolean, (optional)
    '''

    pass


def indent():
    '''Add 4 spaces at line beginning 

    '''

    pass


def insert(text=""):
    '''Insert text at cursor position 

    :param text: Text, Text to insert at the cursor position 
    :type text: string, (optional, never None)
    '''

    pass


def language(language=""):
    '''Set the current language for this console 

    :param language: Language 
    :type language: string, (optional, never None)
    '''

    pass


def move(type='LINE_BEGIN'):
    '''Move cursor position 

    :param type: Type, Where to move cursor to 
    :type type: enum in ['LINE_BEGIN', 'LINE_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD'], (optional)
    '''

    pass


def paste():
    '''Paste text from clipboard 

    '''

    pass


def scrollback_append(text="", type='OUTPUT'):
    '''Append scrollback text by type 

    :param text: Text, Text to insert at the cursor position 
    :type text: string, (optional, never None)
    :param type: Type, Console output type 
    :type type: enum in ['OUTPUT', 'INPUT', 'INFO', 'ERROR'], (optional)
    '''

    pass


def select_set():
    '''Set the console selection 

    '''

    pass


def select_word():
    '''Select word at cursor position 

    '''

    pass


def unindent():
    '''Delete 4 spaces from line beginning 

    '''

    pass
