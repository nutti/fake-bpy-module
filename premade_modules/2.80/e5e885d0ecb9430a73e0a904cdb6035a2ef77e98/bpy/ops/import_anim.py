def bvh(filepath="",
        filter_glob="*.bvh",
        target='ARMATURE',
        global_scale=1.0,
        frame_start=1,
        use_fps_scale=False,
        update_scene_fps=False,
        update_scene_duration=False,
        use_cyclic=False,
        rotate_mode='NATIVE',
        axis_forward='-Z',
        axis_up='Y'):
    '''Load a BVH motion capture file 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: string, (optional, never None)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param target: Target, Import target type 
    :type target: enum in ['ARMATURE', 'OBJECT'], (optional)
    :param global_scale: Scale, Scale the BVH by this value 
    :type global_scale: float in [0.0001, 1e+06], (optional)
    :param frame_start: Start Frame, Starting frame for the animation 
    :type frame_start: int in [-inf, inf], (optional)
    :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame 
    :type use_fps_scale: boolean, (optional)
    :param update_scene_fps: Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the ‘Scale FPS’ option, as the scale will be 1:1) 
    :type update_scene_fps: boolean, (optional)
    :param update_scene_duration: Update Scene Duration, Extend the scene’s duration to the BVH duration (never shortens the scene) 
    :type update_scene_duration: boolean, (optional)
    :param use_cyclic: Loop, Loop the animation playback 
    :type use_cyclic: boolean, (optional)
    :param rotate_mode: Rotation, Rotation conversionQUATERNION Quaternion, Convert rotations to quaternions.NATIVE Euler (Native), Use the rotation order defined in the BVH file.XYZ Euler (XYZ), Convert rotations to euler XYZ.XZY Euler (XZY), Convert rotations to euler XZY.YXZ Euler (YXZ), Convert rotations to euler YXZ.YZX Euler (YZX), Convert rotations to euler YZX.ZXY Euler (ZXY), Convert rotations to euler ZXY.ZYX Euler (ZYX), Convert rotations to euler ZYX. 
    :type rotate_mode: enum in ['QUATERNION', 'NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    '''

    pass
