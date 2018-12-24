class GPUBatch:
    '''Reusable container for drawable geometry. '''

    def draw(self, program=None):
        '''Run the drawing program with the parameters assigned to the batch. 

        :param program: Program that performs the drawing operations. If None is passed, the last program setted to this batch will run. 
        :type program: gpu.types.GPUShader
        '''
        pass

    def program_set(self, program):
        '''Assign a shader to this batch that will be used for drawing when not overwritten later. Note: This method has to be called in the draw context that the batch will be drawn in. This function does not need to be called when you always set the shader when calling batch.draw. 

        :param program: The program/shader the batch will use in future draw calls. 
        :type program: gpu.types.GPUShader
        '''
        pass

    def vertbuf_add(self, buf):
        '''Add another vertex buffer to the Batch. It is not possible to add more vertices to the batch using this method. Instead it can be used to add more attributes to the existing vertices. A good use case would be when you have a separate vertex buffer for vertex positions and vertex normals. Current a batch can have at most 3 vertex buffers. 

        :param buf: The vertex buffer that will be added to the batch. 
        :type buf: gpu.types.GPUVertBuf
        '''
        pass


class GPUIndexBuf:
    '''Contains an index buffer. '''

    pass


class GPUOffScreen:
    '''This object gives access to off screen buffers. '''

    color_texture = None
    '''OpenGL bindcode for the color texture. 

    :type:  int 
    '''

    height = None
    '''Height of the texture. 

    :type:  int 
    '''

    width = None
    '''Width of the texture. 

    :type:  int 
    '''

    def bind(self, save=True):
        '''Bind the offscreen object. To make sure that the offscreen gets unbind whether an exception occurs or not, pack it into a with statement. 

        :param save: Save the current OpenGL state, so that it can be restored when unbinding. 
        :type save: bool
        '''
        pass

    def draw_view3d(self, scene, view3d, region, view_matrix,
                    projection_matrix):
        '''Draw the 3d viewport in the offscreen object. 

        :param scene: Scene to draw. 
        :type scene: bpy.types.Scene
        :param view_layer: View layer to draw. 
        :type view_layer: bpy.types.ViewLayer
        :param view3d: 3D View to get the drawing settings from. 
        :type view3d: bpy.types.SpaceView3D
        :param region: Region of the 3D View (required as temporary draw target). 
        :type region: bpy.types.Region
        :param view_matrix: View Matrix (e.g. camera.matrix_world.inverted()). 
        :type view_matrix: mathutils.Matrix
        :param projection_matrix: Projection Matrix (e.g. camera.calc_matrix_camera(...)). 
        :type projection_matrix: mathutils.Matrix
        '''
        pass

    def free(self):
        '''Free the offscreen object. The framebuffer, texture and render objects will no longer be accessible. 

        '''
        pass

    def unbind(self, restore=True):
        '''Unbind the offscreen object. 

        :param restore: Restore the OpenGL state, can only be used when the state has been saved before. 
        :type restore: bool
        '''
        pass


class GPUShader:
    '''To debug shaders, use the –debug-gpu-shaders command line option to see full GLSL shader compilation and linking errors. '''

    program = None
    '''The name of the program object for use by the OpenGL API (read-only). 

    :type:  int 
    '''

    def attr_from_name(self, name):
        '''Get attribute location by name. 

        :param name: The name of the attribute variable whose location is to be queried. 
        :type name: str
        :rtype: int 
        :return:  The location of an attribute variable. 
        '''
        pass

    def bind(self):
        '''Bind the shader object. Required to be able to change uniforms of this shader. 

        '''
        pass

    def calc_format(self):
        '''Build a new format based on the attributes of the shader. 

        :rtype: GPUVertFormat 
        :return:  vertex attribute format for the shader 
        '''
        pass

    def uniform_block_from_name(self, name):
        '''Get uniform block location by name. 

        :param name: Name of the uniform block variable whose location is to be queried. 
        :type name: str
        :rtype: int 
        :return:  The location of the uniform block variable. 
        '''
        pass

    def uniform_bool(self, name, seq):
        '''Specify the value of a uniform variable for the current program object. 

        :param name: Name of the uniform variable whose value is to be changed. 
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable. 
        :type seq: sequence of bools
        '''
        pass

    def uniform_float(self, name, value):
        '''Specify the value of a uniform variable for the current program object. 

        :param name: Name of the uniform variable whose value is to be changed. 
        :type name: str
        :param value: Value that will be used to update the specified uniform variable. 
        :type value: single number or sequence of numbers
        '''
        pass

    def uniform_from_name(self, name):
        '''Get uniform location by name. 

        :param name: Name of the uniform variable whose location is to be queried. 
        :type name: str
        :rtype: int 
        :return:  Location of the uniform variable. 
        '''
        pass

    def uniform_int(self, name, seq):
        '''Specify the value of a uniform variable for the current program object. 

        :param name: name of the uniform variable whose value is to be changed. 
        :type name: str
        :param seq: Value that will be used to update the specified uniform variable. 
        :type seq: sequence of numbers
        '''
        pass

    def uniform_vector_float(self, location, buffer, length, count):
        '''Set the buffer to fill the uniform. 

        :param location: Location of the uniform variable to be modified. 
        :type location: int
        :param buffer: The data that should be set. Can support the buffer protocol. 
        :type buffer: sequence of floats
        :param length: Size of the uniform data type:1: float2: vec2 or float[2]3: vec3 or float[3]4: vec4 or float[4]9: mat316: mat4 
        :type length: int
        :param count: Specifies the number of elements, vector or matrices that are to be modified. 
        :type count: int
        '''
        pass

    def uniform_vector_int(self, location, buffer, length, count):
        '''See GPUShader.uniform_vector_float(…) description. 

        '''
        pass


class GPUVertBuf:
    '''Contains a VBO. '''

    def attr_fill(self, id, data):
        '''Insert data into the buffer for a single attribute. 

        :param id: Either the name or the id of the attribute. 
        :type id: int or str
        :param data: Sequence of data that should be stored in the buffer 
        :type data: sequence of values or tuples
        '''
        pass


class GPUVertFormat:
    '''This object contains information about the structure of a vertex buffer. '''

    def attr_add(self, id, comp_type, len, fetch_mode):
        '''Add a new attribute to the format. 

        :param id: Name the attribute. Often position, normal, … 
        :type id: str
        :param comp_type: The data type that will be used store the value in memory. Possible values are I8, U8, I16, U16, I32, U32, F32 and I10. 
        :type comp_type: str
        :param len: How many individual values the attribute consists of (e.g. 2 for uv coordinates). 
        :type len: int
        :param fetch_mode: How values from memory will be converted when used in the shader. This is mainly useful for memory optimizations when you want to store values with reduced precision. E.g. you can store a float in only 1 byte but it will be converted to a normal 4 byte float when used. Possible values are FLOAT, INT, INT_TO_FLOAT_UNIT and INT_TO_FLOAT. 
        :type fetch_mode: str
        '''
        pass
