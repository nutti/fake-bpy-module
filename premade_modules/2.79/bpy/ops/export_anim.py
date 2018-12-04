def bvh(filepath="",
        check_existing=True,
        filter_glob="*.bvh",
        global_scale=1.0,
        frame_start=0,
        frame_end=0,
        rotate_mode='NATIVE',
        root_transform_only=False):
    '''Save a BVH motion capture file from an armature 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param global_scale: Scale, Scale the BVH by this value 
    :type global_scale: float in [0.0001, 1e+06], (optional)
    :param frame_start: Start Frame, Starting frame to export 
    :type frame_start: int in [-inf, inf], (optional)
    :param frame_end: End Frame, End frame to export 
    :type frame_end: int in [-inf, inf], (optional)
    :param rotate_mode: Rotation, Rotation conversionNATIVE Euler (Native), Use the rotation order defined in the BVH file.XYZ Euler (XYZ), Convert rotations to euler XYZ.XZY Euler (XZY), Convert rotations to euler XZY.YXZ Euler (YXZ), Convert rotations to euler YXZ.YZX Euler (YZX), Convert rotations to euler YZX.ZXY Euler (ZXY), Convert rotations to euler ZXY.ZYX Euler (ZYX), Convert rotations to euler ZYX. 
    :type rotate_mode: enum in ['NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional)
    :param root_transform_only: Root Translation Only, Only write out translation channels for the root bone 
    :type root_transform_only: boolean, (optional)
    '''

    pass
