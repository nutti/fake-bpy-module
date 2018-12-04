def bake_action(frame_start,
                frame_end,
                frame_step=1,
                only_selected=False,
                do_pose=True,
                do_object=True,
                do_visual_keying=True,
                do_constraint_clear=False,
                do_parents_clear=False,
                do_clean=False,
                action=None):
    '''Return an image from the file path with options to search multiple paths and return a placeholder if its not found. 

    :param frame_start: First frame to bake. 
    :type frame_start: int
    :param frame_end: Last frame to bake. 
    :type frame_end: int
    :param frame_step: Frame step. 
    :type frame_step: int
    :param only_selected: Only bake selected bones. 
    :type only_selected: bool
    :param do_pose: Bake pose channels. 
    :type do_pose: bool
    :param do_object: Bake objects. 
    :type do_object: bool
    :param do_visual_keying: Use the final transformations for baking (‘visual keying’) 
    :type do_visual_keying: bool
    :param do_constraint_clear: Remove constraints after baking. 
    :type do_constraint_clear: bool
    :param do_parents_clear: Unparent after baking objects. 
    :type do_parents_clear: bool
    :param do_clean: Remove redundant keyframes after baking. 
    :type do_clean: bool
    :param action: An action to bake the data into, or None for a new action to be created. 
    :type action: bpy.types.Action or None
    :return:  an action or None 
    '''

    pass
