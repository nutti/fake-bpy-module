def draw_circle_2d(position, color, radius, segments=32):
    '''Draw a circle. 

    :param position: Position where the circle will be drawn. 
    :type position: 2D Vector
    :param color: Color of the circle. To use transparency GL_BLEND has to be enabled. 
    :type color: tuple containing RGBA values
    :param radius: Radius of the circle. 
    :type radius: float
    :param segments: How many segments will be used to draw the circle. Higher values give besser results but the drawing will take longer. 
    :type segments: int
    '''

    pass


def draw_texture_2d(texture_id, position, width, height):
    '''Draw a 2d texture. 

    :param texture_id: OpenGL id of the texture (e.g. bpy.types.Image.bindcode). 
    :type texture_id: int
    :param position: Position of the lower left corner. 
    :type position: 2D Vector
    :param width: Width of the image when drawn (not necessarily the original width of the texture). 
    :type width: float
    :param height: Height of the image when drawn. 
    :type height: float
    '''

    pass
