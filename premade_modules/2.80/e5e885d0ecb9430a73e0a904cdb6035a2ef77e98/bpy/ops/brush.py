def add():
    '''Add brush by mode type 

    '''

    pass


def add_gpencil():
    '''Add brush for Grease Pencil 

    '''

    pass


def curve_preset(shape='SMOOTH'):
    '''Set brush shape 

    :param shape: Mode 
    :type shape: enum in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)
    '''

    pass


def reset():
    '''Return brush to defaults based on current tool 

    '''

    pass


def scale_size(scalar=1.0):
    '''Change brush size by a scalar 

    :param scalar: Scalar, Factor to scale brush size by 
    :type scalar: float in [0, 2], (optional)
    '''

    pass


def stencil_control(mode='TRANSLATION', texmode='PRIMARY'):
    '''Control the stencil brush 

    :param mode: Tool 
    :type mode: enum in ['TRANSLATION', 'SCALE', 'ROTATION'], (optional)
    :param texmode: Tool 
    :type texmode: enum in ['PRIMARY', 'SECONDARY'], (optional)
    '''

    pass


def stencil_fit_image_aspect(use_repeat=True, use_scale=True, mask=False):
    '''When using an image texture, adjust the stencil size to fit the image aspect ratio 

    :param use_repeat: Use Repeat, Use repeat mapping values 
    :type use_repeat: boolean, (optional)
    :param use_scale: Use Scale, Use texture scale values 
    :type use_scale: boolean, (optional)
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil 
    :type mask: boolean, (optional)
    '''

    pass


def stencil_reset_transform(mask=False):
    '''Reset the stencil transformation to the default 

    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil 
    :type mask: boolean, (optional)
    '''

    pass


def uv_sculpt_tool_set(tool='PINCH'):
    '''Set the UV sculpt tool 

    :param tool: ToolPINCH Pinch, Pinch UVs.RELAX Relax, Relax UVs.GRAB Grab, Grab UVs. 
    :type tool: enum in ['PINCH', 'RELAX', 'GRAB'], (optional)
    '''

    pass
