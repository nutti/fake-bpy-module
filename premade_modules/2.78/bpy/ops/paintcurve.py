def add_point(location=(0, 0)):
    '''Add New Paint Curve Point 

    :param location: Location, Location of vertex in area space 
    :type location: int array of 2 items in [0, 32767], (optional)
    '''

    pass


def add_point_slide(PAINTCURVE_OT_add_point=None, PAINTCURVE_OT_slide=None):
    '''Add new curve point and slide it 

    :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point 
    :type PAINTCURVE_OT_add_point: PAINTCURVE_OT_add_point, (optional)
    :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point 
    :type PAINTCURVE_OT_slide: PAINTCURVE_OT_slide, (optional)
    '''

    pass


def cursor():
    '''Place cursor 

    '''

    pass


def delete_point():
    '''Remove Paint Curve Point 

    '''

    pass


def draw():
    '''Draw curve 

    '''

    pass


def new():
    '''Add new paint curve 

    '''

    pass


def select(location=(0, 0), toggle=False, extend=False):
    '''Select a paint curve point 

    :param location: Location, Location of vertex in area space 
    :type location: int array of 2 items in [0, 32767], (optional)
    :param toggle: Toggle, (De)select all 
    :type toggle: boolean, (optional)
    :param extend: Extend, Extend selection 
    :type extend: boolean, (optional)
    '''

    pass


def slide(align=False, select=True):
    '''Select and slide paint curve point 

    :param align: Align Handles, Aligns opposite point handle during transform 
    :type align: boolean, (optional)
    :param select: Select, Attempt to select a point handle before transform 
    :type select: boolean, (optional)
    '''

    pass
