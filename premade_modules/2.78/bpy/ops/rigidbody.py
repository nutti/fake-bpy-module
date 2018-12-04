def bake_to_keyframes(frame_start=1, frame_end=250, step=1):
    '''Bake rigid body transformations of selected objects to keyframes 

    :param frame_start: Start Frame, Start frame for baking 
    :type frame_start: int in [0, 300000], (optional)
    :param frame_end: End Frame, End frame for baking 
    :type frame_end: int in [1, 300000], (optional)
    :param step: Frame Step, Frame Step 
    :type step: int in [1, 120], (optional)
    '''

    pass


def connect(con_type='FIXED',
            pivot_type='CENTER',
            connection_pattern='SELECTED_TO_ACTIVE'):
    '''Create rigid body constraints between selected rigid bodies 

    :param con_type: Type, Type of generated constraintFIXED Fixed, Glue rigid bodies together.POINT Point, Constrain rigid bodies to move around common pivot point.HINGE Hinge, Restrict rigid body rotation to one axis.SLIDER Slider, Restrict rigid body translation to one axis.PISTON Piston, Restrict rigid body translation and rotation to one axis.GENERIC Generic, Restrict translation and rotation to specified axes.GENERIC_SPRING Generic Spring, Restrict translation and rotation to specified axes with springs.MOTOR Motor, Drive rigid body around or along an axis. 
    :type con_type: enum in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional)
    :param pivot_type: Location, Constraint pivot locationCENTER Center, Pivot location is between the constrained rigid bodies.ACTIVE Active, Pivot location is at the active object position.SELECTED Selected, Pivot location is at the selected object position. 
    :type pivot_type: enum in ['CENTER', 'ACTIVE', 'SELECTED'], (optional)
    :param connection_pattern: Connection Pattern, Pattern used to connect objectsSELECTED_TO_ACTIVE Selected to Active, Connect selected objects to the active object.CHAIN_DISTANCE Chain by Distance, Connect objects as a chain based on distance, starting at the active object. 
    :type connection_pattern: enum in ['SELECTED_TO_ACTIVE', 'CHAIN_DISTANCE'], (optional)
    '''

    pass


def constraint_add(type='FIXED'):
    '''Add Rigid Body Constraint to active object 

    :param type: Rigid Body Constraint TypeFIXED Fixed, Glue rigid bodies together.POINT Point, Constrain rigid bodies to move around common pivot point.HINGE Hinge, Restrict rigid body rotation to one axis.SLIDER Slider, Restrict rigid body translation to one axis.PISTON Piston, Restrict rigid body translation and rotation to one axis.GENERIC Generic, Restrict translation and rotation to specified axes.GENERIC_SPRING Generic Spring, Restrict translation and rotation to specified axes with springs.MOTOR Motor, Drive rigid body around or along an axis. 
    :type type: enum in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional)
    '''

    pass


def constraint_remove():
    '''Remove Rigid Body Constraint from Object 

    '''

    pass


def mass_calculate(material='DEFAULT', density=1.0):
    '''Automatically calculate mass values for Rigid Body Objects based on volume 

    :param material: Material Preset, Type of material that objects are made of (determines material density) 
    :type material: enum in ['DEFAULT'], (optional)
    :param density: Density, Custom density value (kg/m^3) to use instead of material preset 
    :type density: float in [1.17549e-38, inf], (optional)
    '''

    pass


def object_add(type='ACTIVE'):
    '''Add active object as Rigid Body 

    :param type: Rigid Body TypeACTIVE Active, Object is directly controlled by simulation results.PASSIVE Passive, Object is directly controlled by animation system. 
    :type type: enum in ['ACTIVE', 'PASSIVE'], (optional)
    '''

    pass


def object_remove():
    '''Remove Rigid Body settings from Object 

    '''

    pass


def object_settings_copy():
    '''Copy Rigid Body settings from active object to selected 

    '''

    pass


def objects_add(type='ACTIVE'):
    '''Add selected objects as Rigid Bodies 

    :param type: Rigid Body TypeACTIVE Active, Object is directly controlled by simulation results.PASSIVE Passive, Object is directly controlled by animation system. 
    :type type: enum in ['ACTIVE', 'PASSIVE'], (optional)
    '''

    pass


def objects_remove():
    '''Remove selected objects from Rigid Body simulation 

    '''

    pass


def shape_change(type='MESH'):
    '''Change collision shapes for selected Rigid Body Objects 

    :param type: Rigid Body ShapeBOX Box, Box-like shapes (i.e. cubes), including planes (i.e. ground planes).SPHERE Sphere.CAPSULE Capsule.CYLINDER Cylinder.CONE Cone.CONVEX_HULL Convex Hull, A mesh-like surface encompassing (i.e. shrinkwrap over) all vertices (best results with fewer vertices).MESH Mesh, Mesh consisting of triangles only, allowing for more detailed interactions than convex hulls. 
    :type type: enum in ['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH'], (optional)
    '''

    pass


def world_add():
    '''Add Rigid Body simulation world to the current scene 

    '''

    pass


def world_remove():
    '''Remove Rigid Body simulation world from the current scene 

    '''

    pass
