def flip(axis='U'):
    '''Mirror all control points without inverting the lattice deform 

    :param axis: Flip Axis, Coordinates along this axis get flipped 
    :type axis: enum in ['U', 'V', 'W'], (optional)
    '''

    pass


def make_regular():
    '''Set UVW control points a uniform distance apart 

    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all UVW control points 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_less():
    '''Deselect vertices at the boundary of each selection region 

    '''

    pass


def select_mirror(axis={'X'}, extend=False):
    '''Select mirrored lattice points 

    :param axis: Axis 
    :type axis: enum set in {'X', 'Y', 'Z'}, (optional)
    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_more():
    '''Select vertex directly linked to already selected ones 

    '''

    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    '''Randomly select UVW control points 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float in [0, 100], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: enum in ['SELECT', 'DESELECT'], (optional)
    '''

    pass


def select_ungrouped(extend=False):
    '''Select vertices without a group 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass
