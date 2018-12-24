def add_target():
    '''Add a target to the constraint 

    '''

    pass


def childof_clear_inverse(constraint="", owner='OBJECT'):
    '''Clear inverse correction for ChildOf constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def childof_set_inverse(constraint="", owner='OBJECT'):
    '''Set inverse correction for ChildOf constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def delete():
    '''Remove constraint from constraint stack 

    '''

    pass


def followpath_path_animate(constraint="",
                            owner='OBJECT',
                            frame_start=1,
                            length=100):
    '''Add default animation for path used by constraint if it isn’t animated already 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    :param frame_start: Start Frame, First frame of path animation 
    :type frame_start: int in [-1048574, 1048574], (optional)
    :param length: Length, Number of frames that path animation should take 
    :type length: int in [0, 1048574], (optional)
    '''

    pass


def limitdistance_reset(constraint="", owner='OBJECT'):
    '''Reset limiting distance for Limit Distance Constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def move_down(constraint="", owner='OBJECT'):
    '''Move constraint down in constraint stack 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def move_up(constraint="", owner='OBJECT'):
    '''Move constraint up in constraint stack 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def normalize_target_weights():
    '''Normalize weights of all target bones 

    '''

    pass


def objectsolver_clear_inverse(constraint="", owner='OBJECT'):
    '''Clear inverse correction for ObjectSolver constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def objectsolver_set_inverse(constraint="", owner='OBJECT'):
    '''Set inverse correction for ObjectSolver constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass


def remove_target(index=0):
    '''Remove the target from the constraint 

    :param index: index 
    :type index: int in [-inf, inf], (optional)
    '''

    pass


def stretchto_reset(constraint="", owner='OBJECT'):
    '''Reset original length of bone for Stretch To Constraint 

    :param constraint: Constraint, Name of the constraint to edit 
    :type constraint: string, (optional, never None)
    :param owner: Owner, The owner of this constraintOBJECT Object, Edit a constraint on the active object.BONE Bone, Edit a constraint on the active bone. 
    :type owner: enum in ['OBJECT', 'BONE'], (optional)
    '''

    pass
