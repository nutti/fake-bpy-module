def bake_action(obj, *, action, frames, **kwargs):
    '''

    :param obj: Object to bake. 
    :type obj: bpy.types.Object
    :param action: An action to bake the data into, or None for a new action to be created. 
    :type action: bpy.types.Action or None
    :param frames: Frames to bake. 
    :type frames: iterable of int
    :return:  an action or None 
    '''

    pass


def bake_action_objects(object_action_pairs, *, frames, **kwargs):
    '''A version of bake_action_objects_iter() that takes frames and returns the output. 

    :param frames: Frames to bake. 
    :type frames: iterable of int
    :return:  A sequence of Action or None types (aligned with object_action_pairs) 
    '''

    pass


def bake_action_iter(obj,
                     *,
                     action,
                     only_selected=False,
                     do_pose=True,
                     do_object=True,
                     do_visual_keying=True,
                     do_constraint_clear=False,
                     do_parents_clear=False,
                     do_clean=False):
    '''An coroutine that bakes action for a single object. 

    :param obj: Object to bake. 
    :type obj: bpy.types.Object
    :param action: An action to bake the data into, or None for a new action to be created. 
    :type action: bpy.types.Action or None
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
    :return:  an action or None 
    '''

    pass


def bake_action_objects_iter(object_action_pairs, **kwargs):
    '''An coroutine that bakes actions for multiple objects. 

    :param object_action_pairs: Sequence of object action tuples, action is the destination for the baked data. When None a new action will be created. 
    :type object_action_pairs: Sequence of (bpy.types.Object, bpy.types.Action)
    '''

    pass
