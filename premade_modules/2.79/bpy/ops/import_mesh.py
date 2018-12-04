def ply(filepath="", files=None, directory="", filter_glob="*.ply"):
    '''Load a PLY geometry file 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: string, (optional, never None)
    :param files: File Path, File path used for importing the PLY file 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param directory: directory 
    :type directory: string, (optional, never None)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    '''

    pass


def stl(filepath="",
        axis_forward='Y',
        axis_up='Z',
        filter_glob="*.stl",
        files=None,
        directory="",
        global_scale=1.0,
        use_scene_unit=False,
        use_facet_normal=False):
    '''Load STL triangle mesh data 

    :param filepath: File Path, Filepath used for importing the file 
    :type filepath: string, (optional, never None)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param files: File Path 
    :type files: bpy_prop_collection of OperatorFileListElement, (optional)
    :param directory: directory 
    :type directory: string, (optional, never None)
    :param global_scale: Scale 
    :type global_scale: float in [1e-06, 1e+06], (optional)
    :param use_scene_unit: Scene Unit, Apply current scene’s unit (as defined by unit scale) to imported data 
    :type use_scene_unit: boolean, (optional)
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading) 
    :type use_facet_normal: boolean, (optional)
    '''

    pass
