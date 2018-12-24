def delete_metaelems():
    '''Delete selected metaelement(s) 

    '''

    pass


def duplicate_metaelems():
    '''Duplicate selected metaelement(s) 

    '''

    pass


def duplicate_move(MBALL_OT_duplicate_metaelems=None,
                   TRANSFORM_OT_translate=None):
    '''Make copies of the selected metaelements and move them 

    :param MBALL_OT_duplicate_metaelems: Duplicate Metaelements, Duplicate selected metaelement(s) 
    :type MBALL_OT_duplicate_metaelems: MBALL_OT_duplicate_metaelems, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def hide_metaelems(unselected=False):
    '''Hide (un)selected metaelement(s) 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: boolean, (optional)
    '''

    pass


def reveal_metaelems(select=True):
    '''Reveal all hidden metaelements 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all meta elements 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_random_metaelems(percent=50.0, seed=0, action='SELECT'):
    '''Randomly select metaelements 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float in [0, 100], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: enum in ['SELECT', 'DESELECT'], (optional)
    '''

    pass


def select_similar(type='TYPE', threshold=0.1):
    '''Select similar metaballs by property types 

    :param type: Type 
    :type type: enum in ['TYPE', 'RADIUS', 'STIFFNESS', 'ROTATION'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, inf], (optional)
    '''

    pass
