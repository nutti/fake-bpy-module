def mesh_linked_uv_islands(mesh):
    '''Splits the mesh into connected polygons, use this for separating cubes from other mesh elements within 1 mesh datablock. 

    :param mesh: the mesh used to group with. 
    :type mesh: bpy.types.Mesh
    :return:  lists of lists containing polygon indices 
    '''

    pass


def mesh_linked_triangles(mesh):
    '''Splits the mesh into connected triangles, use this for separating cubes from other mesh elements within 1 mesh datablock. 

    :param mesh: the mesh used to group with. 
    :type mesh: bpy.types.Mesh
    :return:  lists of lists containing triangles. 
    '''

    pass


def edge_face_count_dict(mesh):
    '''

    :return:  dict of edge keys with their value set to the number of faces using each edge. 
    '''

    pass


def edge_face_count(mesh):
    '''

    :return:  list face users for each item in mesh.edges. 
    '''

    pass


def edge_loops_from_edges(mesh, edges=None):
    '''closed loops have matching start and end values. 

    '''

    pass


def ngon_tessellate(from_data, indices, fix_loops=True, debug_print=True):
    '''Takes a polyline of indices (fgon) and returns a list of face index lists. Designed to be used for importers that need indices for an fgon to create from existing verts. 

    :param from_data: either a mesh, or a list/tuple of vectors. 
    :type from_data: list or bpy.types.Mesh
    :param indices: a list of indices to use this list is the ordered closed polyline to fill, and can be a subset of the data given. 
    :type indices: list
    :param fix_loops: If this is enabled polylines that use loops to make multiple polylines are delt with correctly. 
    :type fix_loops: bool
    '''

    pass


def triangle_random_points(num_points, loop_triangles):
    '''Generates a list of random points over mesh loop triangles. 

    :param num_points: the number of random points to generate on each triangle. 
    :type num_points: 
    :param loop_triangles: list of the triangles to generate points on. 
    :type loop_triangles: bpy.types.MeshLoopTriangle, sequence
    :return:  list of random points over all triangles. 
    '''

    pass
