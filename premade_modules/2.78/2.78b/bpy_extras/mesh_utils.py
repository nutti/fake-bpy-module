def mesh_linked_uv_islands(mesh):
    '''Splits the mesh into connected polygons, use this for seperating cubes from other mesh elements within 1 mesh datablock. 

    :param mesh: the mesh used to group with. 
    :type mesh: bpy.types.Mesh
    :return:  lists of lists containing polygon indices 
    '''

    pass


def mesh_linked_tessfaces(mesh):
    '''Splits the mesh into connected faces, use this for seperating cubes from other mesh elements within 1 mesh datablock. 

    :param mesh: the mesh used to group with. 
    :type mesh: bpy.types.Mesh
    :return:  lists of lists containing faces. 
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


def edge_loops_from_tessfaces(mesh, tessfaces=None, seams=()):
    '''return a list of edge key lists [[(0, 1), (4, 8), (3, 8)], …] 

    :param mesh: the mesh used to get edge loops from. 
    :type mesh: bpy.types.Mesh
    :param tessfaces: optional face list to only use some of the meshes faces. 
    :type tessfaces: bpy.types.MeshTessFace, sequence or or NoneType
    :return:  return a list of edge vertex index lists. 
    '''

    pass


def edge_loops_from_edges(mesh, edges=None):
    '''closed loops have matching start and end values. 

    '''

    pass


def ngon_tessellate(from_data, indices, fix_loops=True):
    '''Takes a polyline of indices (fgon) and returns a list of face index lists. Designed to be used for importers that need indices for an fgon to create from existing verts. 

    :param from_data: either a mesh, or a list/tuple of vectors. 
    :type from_data: list or bpy.types.Mesh
    :param indices: a list of indices to use this list is the ordered closed polyline to fill, and can be a subset of the data given. 
    :type indices: list
    :param fix_loops: If this is enabled polylines that use loops to make multiple polylines are delt with correctly. 
    :type fix_loops: bool
    '''

    pass


def face_random_points(num_points, tessfaces):
    '''Generates a list of random points over mesh tessfaces. 

    :param num_points: the number of random points to generate on each face. 
    :type num_points: 
    :param tessfaces: list of the faces to generate points on. 
    :type tessfaces: bpy.types.MeshTessFace, sequence
    :return:  list of random points over all faces. 
    '''

    pass
