def ndof():
    '''Use a 3D mouse device to pan/zoom the view 

    '''

    pass


def pan(deltax=0, deltay=0):
    '''Pan the view 

    :param deltax: Delta X 
    :type deltax: int in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: int in [-inf, inf], (optional)
    '''

    pass


def reset():
    '''Reset the view 

    '''

    pass


def scroll_down(deltax=0, deltay=0, page=False):
    '''Scroll the view down 

    :param deltax: Delta X 
    :type deltax: int in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: int in [-inf, inf], (optional)
    :param page: Page, Scroll down one page 
    :type page: boolean, (optional)
    '''

    pass


def scroll_left(deltax=0, deltay=0):
    '''Scroll the view left 

    :param deltax: Delta X 
    :type deltax: int in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: int in [-inf, inf], (optional)
    '''

    pass


def scroll_right(deltax=0, deltay=0):
    '''Scroll the view right 

    :param deltax: Delta X 
    :type deltax: int in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: int in [-inf, inf], (optional)
    '''

    pass


def scroll_up(deltax=0, deltay=0, page=False):
    '''Scroll the view up 

    :param deltax: Delta X 
    :type deltax: int in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: int in [-inf, inf], (optional)
    :param page: Page, Scroll up one page 
    :type page: boolean, (optional)
    '''

    pass


def scroller_activate():
    '''Scroll view by mouse click and drag 

    '''

    pass


def smoothview(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    '''Undocumented 

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
    '''

    pass


def zoom(deltax=0.0, deltay=0.0):
    '''Zoom in/out the view 

    :param deltax: Delta X 
    :type deltax: float in [-inf, inf], (optional)
    :param deltay: Delta Y 
    :type deltay: float in [-inf, inf], (optional)
    '''

    pass


def zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    '''Zoom in the view to the nearest item contained in the border 

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
    '''

    pass


def zoom_in(zoomfacx=0.0, zoomfacy=0.0):
    '''Zoom in the view 

    :param zoomfacx: Zoom Factor X 
    :type zoomfacx: float in [-inf, inf], (optional)
    :param zoomfacy: Zoom Factor Y 
    :type zoomfacy: float in [-inf, inf], (optional)
    '''

    pass


def zoom_out(zoomfacx=0.0, zoomfacy=0.0):
    '''Zoom out the view 

    :param zoomfacx: Zoom Factor X 
    :type zoomfacx: float in [-inf, inf], (optional)
    :param zoomfacy: Zoom Factor Y 
    :type zoomfacy: float in [-inf, inf], (optional)
    '''

    pass
