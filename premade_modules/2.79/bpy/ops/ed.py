def flush_edits():
    '''Flush edit data from active editing modes 

    '''

    pass


def redo():
    '''Redo previous action 

    '''

    pass


def undo():
    '''Undo previous action 

    '''

    pass


def undo_history(item=0):
    '''Redo specific action in history 

    :param item: Item 
    :type item: int in [0, inf], (optional)
    '''

    pass


def undo_push(message="Add an undo step *function may be moved*"):
    '''Add an undo state (internal use only) 

    :param message: Undo Message 
    :type message: string, (optional, never None)
    '''

    pass


def undo_redo():
    '''Undo and redo previous action 

    '''

    pass
