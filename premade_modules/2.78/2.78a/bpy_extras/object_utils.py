def add_object_align_init(context, operator):
    '''Return a matrix using the operator settings and view context. 

    :param context: The context to use. 
    :type context: bpy.types.Context
    :param operator: The operator, checked for location and rotation properties. 
    :type operator: bpy.types.Operator
    :return:  the matrix from the context and settings. 
    '''

    pass


def object_data_add(context,
                    obdata,
                    operator=None,
                    use_active_layer=True,
                    name=None):
    '''Add an object using the view context and preference to to initialize the location, rotation and layer. 

    :param context: The context to use. 
    :type context: bpy.types.Context
    :param obdata: the data used for the new object. 
    :type obdata: valid object data type or None.
    :param operator: The operator, checked for location and rotation properties. 
    :type operator: bpy.types.Operator
    :param name: Optional name 
    :type name: string
    :return:  the newly created object in the scene. 
    '''

    pass


def object_add_grid_scale(context):
    '''Return scale which should be applied on object data to align it to grid scale 

    '''

    pass


def object_add_grid_scale_apply_operator(operator, context):
    '''Scale an operators distance values by the grid size. 

    '''

    pass


def object_image_guess(obj, bm=None):
    '''Return a single image used by the object, first checking the texture-faces, then the material. 

    '''

    pass


def world_to_camera_view(scene, obj, coord):
    '''Takes shift-x/y, lens angle and sensor size into account as well as perspective/ortho projections. 

    :param scene: Scene to use for frame size. 
    :type scene: bpy.types.Scene
    :param obj: Camera object. 
    :type obj: bpy.types.Object
    :param coord: World space location. 
    :type coord: mathutils.Vector
    :return:  a vector where X and Y map to the view plane and Z is the depth on the view axis. 
    '''

    pass


class AddObjectHelper:
    def view_align_update_callback(self, context):
        '''

        '''
        pass
