def ply(filepath="",
        check_existing=True,
        filter_glob="*.ply",
        use_mesh_modifiers=True,
        use_normals=True,
        use_uv_coords=True,
        use_colors=True,
        global_scale=1.0,
        axis_forward='Y',
        axis_up='Z'):
    '''Export a single object as a Stanford PLY with normals, colors and texture coordinates 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_mesh_modifiers: Apply Modifiers, Apply Modifiers to the exported mesh 
    :type use_mesh_modifiers: boolean, (optional)
    :param use_normals: Normals, Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces) 
    :type use_normals: boolean, (optional)
    :param use_uv_coords: UVs, Export the active UV layer 
    :type use_uv_coords: boolean, (optional)
    :param use_colors: Vertex Colors, Export the active vertex color layer 
    :type use_colors: boolean, (optional)
    :param global_scale: Scale 
    :type global_scale: float in [0.01, 1000], (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    '''

    pass


def stl(filepath="",
        check_existing=True,
        filter_glob="*.stl",
        use_selection=False,
        global_scale=1.0,
        use_scene_unit=False,
        ascii=False,
        use_mesh_modifiers=True,
        batch_mode='OFF',
        axis_forward='Y',
        axis_up='Z'):
    '''Save STL triangle mesh data from the active object 

    :param filepath: File Path, Filepath used for exporting the file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_glob: filter_glob 
    :type filter_glob: string, (optional, never None)
    :param use_selection: Selection Only, Export selected objects only 
    :type use_selection: boolean, (optional)
    :param global_scale: Scale 
    :type global_scale: float in [0.01, 1000], (optional)
    :param use_scene_unit: Scene Unit, Apply current scene’s unit (as defined by unit scale) to exported data 
    :type use_scene_unit: boolean, (optional)
    :param ascii: Ascii, Save the file in ASCII file format 
    :type ascii: boolean, (optional)
    :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving 
    :type use_mesh_modifiers: boolean, (optional)
    :param batch_mode: Batch ModeOFF Off, All data in one file.OBJECT Object, Each object as a file. 
    :type batch_mode: enum in ['OFF', 'OBJECT'], (optional)
    :param axis_forward: Forward 
    :type axis_forward: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    :param axis_up: Up 
    :type axis_up: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)
    '''

    pass
