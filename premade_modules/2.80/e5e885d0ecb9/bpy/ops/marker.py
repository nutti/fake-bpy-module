def add():
    '''Add a new time marker 

    '''

    pass


def camera_bind():
    '''Bind the selected camera to a marker on the current frame 

    '''

    pass


def delete():
    '''Delete selected time marker(s) 

    '''

    pass


def duplicate(frames=0):
    '''Duplicate selected time marker(s) 

    :param frames: Frames 
    :type frames: int in [-inf, inf], (optional)
    '''

    pass


def make_links_scene(scene=''):
    '''Copy selected markers to another scene 

    :param scene: Scene 
    :type scene: enum in [], (optional)
    '''

    pass


def move(frames=0):
    '''Move selected time marker(s) 

    :param frames: Frames 
    :type frames: int in [-inf, inf], (optional)
    '''

    pass


def rename(name="RenamedMarker"):
    '''Rename first selected time marker 

    :param name: Name, New name for marker 
    :type name: string, (optional, never None)
    '''

    pass


def select(extend=False, camera=False):
    '''Select time marker(s) 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    :param camera: Camera, Select the camera 
    :type camera: boolean, (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all time markers 

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
    '''Select all time markers using box selection 

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
