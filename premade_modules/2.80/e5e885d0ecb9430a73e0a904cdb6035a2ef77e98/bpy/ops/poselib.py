def action_sanitize():
    '''Make action suitable for use as a Pose Library 

    '''

    pass


def apply_pose(pose_index=-1):
    '''Apply specified Pose Library pose to the rig 

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose) 
    :type pose_index: int in [-2, inf], (optional)
    '''

    pass


def browse_interactive(pose_index=-1):
    '''Interactively browse poses in 3D-View 

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose) 
    :type pose_index: int in [-2, inf], (optional)
    '''

    pass


def new():
    '''Add New Pose Library to active Object 

    '''

    pass


def pose_add(frame=1, name="Pose"):
    '''Add the current Pose to the active Pose Library 

    :param frame: Frame, Frame to store pose on 
    :type frame: int in [0, inf], (optional)
    :param name: Pose Name, Name of newly added Pose 
    :type name: string, (optional, never None)
    '''

    pass


def pose_move(pose='', direction='UP'):
    '''Move the pose up or down in the active Pose Library 

    :param pose: Pose, The pose to move 
    :type pose: enum in [], (optional)
    :param direction: Direction, Direction to move the chosen pose towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def pose_remove(pose=''):
    '''Remove nth pose from the active Pose Library 

    :param pose: Pose, The pose to remove 
    :type pose: enum in [], (optional)
    '''

    pass


def pose_rename(name="RenamedPose", pose=''):
    '''Rename specified pose from the active Pose Library 

    :param name: New Pose Name, New name for pose 
    :type name: string, (optional, never None)
    :param pose: Pose, The pose to rename 
    :type pose: enum in [], (optional)
    '''

    pass


def unlink():
    '''Remove Pose Library from active Object 

    '''

    pass
