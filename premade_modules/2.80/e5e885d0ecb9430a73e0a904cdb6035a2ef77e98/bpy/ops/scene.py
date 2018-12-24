def delete():
    '''Delete active scene 

    '''

    pass


def freestyle_add_edge_marks_to_keying_set():
    '''Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set 

    '''

    pass


def freestyle_add_face_marks_to_keying_set():
    '''Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set 

    '''

    pass


def freestyle_alpha_modifier_add(type='ALONG_STROKE'):
    '''Add an alpha transparency modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: enum in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)
    '''

    pass


def freestyle_color_modifier_add(type='ALONG_STROKE'):
    '''Add a line color modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: enum in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)
    '''

    pass


def freestyle_fill_range_by_selection(type='COLOR', name=""):
    '''Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object 

    :param type: Type, Type of the modifier to work onCOLOR Color, Color modifier type.ALPHA Alpha, Alpha modifier type.THICKNESS Thickness, Thickness modifier type. 
    :type type: enum in ['COLOR', 'ALPHA', 'THICKNESS'], (optional)
    :param name: Name, Name of the modifier to work on 
    :type name: string, (optional, never None)
    '''

    pass


def freestyle_geometry_modifier_add(type='2D_OFFSET'):
    '''Add a stroke geometry modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: enum in ['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER'], (optional)
    '''

    pass


def freestyle_lineset_add():
    '''Add a line set into the list of line sets 

    '''

    pass


def freestyle_lineset_copy():
    '''Copy the active line set to a buffer 

    '''

    pass


def freestyle_lineset_move(direction='UP'):
    '''Change the position of the active line set within the list of line sets 

    :param direction: Direction, Direction to move the active line set towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def freestyle_lineset_paste():
    '''Paste the buffer content to the active line set 

    '''

    pass


def freestyle_lineset_remove():
    '''Remove the active line set from the list of line sets 

    '''

    pass


def freestyle_linestyle_new():
    '''Create a new line style, reusable by multiple line sets 

    '''

    pass


def freestyle_modifier_copy():
    '''Duplicate the modifier within the list of modifiers 

    '''

    pass


def freestyle_modifier_move(direction='UP'):
    '''Move the modifier within the list of modifiers 

    :param direction: Direction, Direction to move the chosen modifier towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def freestyle_modifier_remove():
    '''Remove the modifier from the list of modifiers 

    '''

    pass


def freestyle_module_add():
    '''Add a style module into the list of modules 

    '''

    pass


def freestyle_module_move(direction='UP'):
    '''Change the position of the style module within in the list of style modules 

    :param direction: Direction, Direction to move the chosen style module towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def freestyle_module_open(filepath="", make_internal=True):
    '''Open a style module file 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param make_internal: Make internal, Make module file internal after loading 
    :type make_internal: boolean, (optional)
    '''

    pass


def freestyle_module_remove():
    '''Remove the style module from the stack 

    '''

    pass


def freestyle_stroke_material_create():
    '''Create Freestyle stroke material for testing 

    '''

    pass


def freestyle_thickness_modifier_add(type='ALONG_STROKE'):
    '''Add a line thickness modifier to the line style associated with the active lineset 

    :param type: Type 
    :type type: enum in ['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)
    '''

    pass


def gpencil_brush_preset_add(name="", remove_name=False, remove_active=False):
    '''Add or remove grease pencil brush preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def gpencil_material_preset_add(name="",
                                remove_name=False,
                                remove_active=False):
    '''Add or remove grease pencil material preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def light_cache_bake(delay=0, subset='ALL'):
    '''Bake the active view layer lighting 

    :param delay: Delay, Delay in millisecond before baking starts 
    :type delay: int in [0, 2000], (optional)
    :param subset: Subset, Subset of probes to updateALL All LightProbes, Bake both irradiance grids and reflection cubemaps.DIRTY Dirty Only, Only bake lightprobes that are marked as dirty.CUBEMAPS Cubemaps Only, Try to only bake reflection cubemaps if irradiance grids are up to date. 
    :type subset: enum in ['ALL', 'DIRTY', 'CUBEMAPS'], (optional)
    '''

    pass


def light_cache_free():
    '''Free cached indirect lighting 

    '''

    pass


def new(type='NEW'):
    '''Add new scene by type 

    :param type: TypeNEW New, Add new scene.EMPTY Copy Settings, Make a copy without any objects.LINK_OBJECTS Link Objects, Link to the objects from the current scene.LINK_OBJECT_DATA Link Object Data, Copy objects linked to data from the current scene.FULL_COPY Full Copy, Make a full copy of the current scene. 
    :type type: enum in ['NEW', 'EMPTY', 'LINK_OBJECTS', 'LINK_OBJECT_DATA', 'FULL_COPY'], (optional)
    '''

    pass


def render_view_add():
    '''Add a render view 

    '''

    pass


def render_view_remove():
    '''Remove the selected render view 

    '''

    pass


def view_layer_add():
    '''Add a view layer 

    '''

    pass


def view_layer_remove():
    '''Remove the selected view layer 

    '''

    pass
