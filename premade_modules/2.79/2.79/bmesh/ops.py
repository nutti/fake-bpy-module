def smooth_vert(bm, verts, factor, mirror_clip_x, mirror_clip_y, mirror_clip_z,
                clip_dist, use_axis_x, use_axis_y, use_axis_z):
    '''Smooths vertices by using a basic vertex averaging scheme. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param factor: smoothing factor 
    :type factor: float
    :param mirror_clip_x: set vertices close to the x axis before the operation to 0 
    :type mirror_clip_x: bool
    :param mirror_clip_y: set vertices close to the y axis before the operation to 0 
    :type mirror_clip_y: bool
    :param mirror_clip_z: set vertices close to the z axis before the operation to 0 
    :type mirror_clip_z: bool
    :param clip_dist: clipping threshold for the above three slots 
    :type clip_dist: float
    :param use_axis_x: smooth vertices along X axis 
    :type use_axis_x: bool
    :param use_axis_y: smooth vertices along Y axis 
    :type use_axis_y: bool
    :param use_axis_z: smooth vertices along Z axis 
    :type use_axis_z: bool
    '''

    pass


def smooth_laplacian_vert(bm, verts, lambda_factor, lambda_border, use_x,
                          use_y, use_z, preserve_volume):
    '''Smooths vertices by using Laplacian smoothing propose by. Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param lambda_factor: lambda param 
    :type lambda_factor: float
    :param lambda_border: lambda param in border 
    :type lambda_border: float
    :param use_x: Smooth object along X axis 
    :type use_x: bool
    :param use_y: Smooth object along Y axis 
    :type use_y: bool
    :param use_z: Smooth object along Z axis 
    :type use_z: bool
    :param preserve_volume: Apply volume preservation after smooth 
    :type preserve_volume: bool
    '''

    pass


def recalc_face_normals(bm, faces):
    '''Computes an “outside” normal for the specified input faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: Undocumented. 
    :type faces: list of (bmesh.types.BMFace)
    '''

    pass


def planar_faces(bm, faces, iterations, factor):
    '''Iteratively flatten faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input geometry. 
    :type faces: list of (bmesh.types.BMFace)
    :param iterations: Number of times to flatten faces (for when connected faces are used) 
    :type iterations: int
    :param factor: Influence for making planar each iteration 
    :type factor: float
    :return:  geom: output slot, computed boundary geometry.type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def region_extend(bm, geom, use_contract, use_faces, use_face_step):
    '''if use_faces is 0 then geom.out spits out verts and edges, otherwise it spits out faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: input geometry 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param use_contract: find boundary inside the regions, not outside. 
    :type use_contract: bool
    :param use_faces: extend from faces instead of edges 
    :type use_faces: bool
    :param use_face_step: step over connected faces 
    :type use_face_step: bool
    :return:  geom: output slot, computed boundary geometry.type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def rotate_edges(bm, edges, use_ccw):
    '''Rotates edges topologically. Also known as “spin edge” to some people. Simple example: [/] becomes [|] then [\]. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_ccw: rotate edge counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    :return:  edges: newly spun edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def reverse_faces(bm, faces, flip_multires):
    '''Reverses the winding (vertex order) of faces. This has the effect of flipping the normal. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param flip_multires: maintain multi-res offset 
    :type flip_multires: bool
    '''

    pass


def bisect_edges(bm, edges, cuts, edge_percents):
    '''Splits input edges (but doesn’t do anything else). This creates a 2-valence vert. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param cuts: number of cuts 
    :type cuts: int
    :param edge_percents: Undocumented. 
    :type edge_percents: dict mapping vert/edge/face types to float
    :return:  geom_split: newly created vertices and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def mirror(bm, geom, matrix, merge_dist, axis, mirror_u, mirror_v):
    '''Mirrors geometry along an axis. The resulting geometry is welded on using merge_dist. Pairs of original/mirrored vertices are welded using the merge_dist parameter (which defines the minimum distance for welding to happen). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: input geometry 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param matrix: matrix defining the mirror transformation 
    :type matrix: mathutils.Matrix
    :param merge_dist: maximum distance for merging. does no merging if 0. 
    :type merge_dist: float
    :param axis: the axis to use, 0, 1, or 2 for x, y, z 
    :type axis: int
    :param mirror_u: mirror UVs across the u axis 
    :type mirror_u: bool
    :param mirror_v: mirror UVs across the v axis 
    :type mirror_v: bool
    :return:  geom: output geometry, mirroredtype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def find_doubles(bm, verts, keep_verts, dist):
    '''If keep_verts is used, vertices outside that set can only be merged with vertices in that set. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param keep_verts: list of verts to keep 
    :type keep_verts: list of (bmesh.types.BMVert)
    :param dist: minimum distance 
    :type dist: float
    :return:  targetmap:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def remove_doubles(bm, verts, dist):
    '''Finds groups of vertices closer then dist and merges them together, using the weld verts bmop. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input verts 
    :type verts: list of (bmesh.types.BMVert)
    :param dist: minimum distance 
    :type dist: float
    '''

    pass


def automerge(bm, verts, dist):
    '''Finds groups of vertices closer then dist and merges them together, using the weld verts bmop. The merges must go from a vert not in verts to one in verts. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input verts 
    :type verts: list of (bmesh.types.BMVert)
    :param dist: minimum distance 
    :type dist: float
    '''

    pass


def collapse(bm, edges, uvs):
    '''Collapses connected vertices 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param uvs: also collapse UVs and such 
    :type uvs: bool
    '''

    pass


def pointmerge_facedata(bm, verts, vert_snap):
    '''Merge uv/vcols at a specific vertex. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param vert_snap: snap vertex 
    :type vert_snap: bmesh.types.BMVert
    '''

    pass


def average_vert_facedata(bm, verts):
    '''Merge uv/vcols associated with the input vertices at the bounding box center. (I know, it’s not averaging but the vert_snap_to_bb_center is just too long). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    '''

    pass


def pointmerge(bm, verts, merge_co):
    '''Merge verts together at a point. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices (all verts will be merged into the first). 
    :type verts: list of (bmesh.types.BMVert)
    :param merge_co: Position to merge at. 
    :type merge_co: mathutils.Vector or any sequence of 3 floats
    '''

    pass


def collapse_uvs(bm, edges):
    '''Collapses connected UV vertices. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    '''

    pass


def weld_verts(bm, targetmap):
    '''Welds verts together (kind-of like remove doubles, merge, etc, all of which use or will use this bmop). You pass in mappings from vertices to the vertices they weld with. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param targetmap: Undocumented. 
    :type targetmap: dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace
    '''

    pass


def create_vert(bm, co):
    '''Creates a single vertex; this bmop was necessary for click-create-vertex. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param co: the coordinate of the new vert 
    :type co: mathutils.Vector or any sequence of 3 floats
    :return:  vert: the new verttype list of (bmesh.types.BMVert) 
    '''

    pass


def join_triangles(bm, faces, cmp_seam, cmp_sharp, cmp_uvs, cmp_vcols,
                   cmp_materials, angle_face_threshold, angle_shape_threshold):
    '''Tries to intelligently join triangles according to angle threshold and delimiters. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input geometry. 
    :type faces: list of (bmesh.types.BMFace)
    :param cmp_seam: Undocumented. 
    :type cmp_seam: bool
    :param cmp_sharp: Undocumented. 
    :type cmp_sharp: bool
    :param cmp_uvs: Undocumented. 
    :type cmp_uvs: bool
    :param cmp_vcols: Undocumented. 
    :type cmp_vcols: bool
    :param cmp_materials: Undocumented. 
    :type cmp_materials: bool
    :param angle_face_threshold: Undocumented. 
    :type angle_face_threshold: float
    :param angle_shape_threshold: Undocumented. 
    :type angle_shape_threshold: float
    :return:  faces: joined facestype list of (bmesh.types.BMFace) 
    '''

    pass


def contextual_create(bm, geom, mat_nr, use_smooth):
    '''Three verts become a triangle, four become a quad. Two become a wire edge. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: input geometry. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth to use 
    :type use_smooth: bool
    :return:  faces: newly-made face(s)type list of (bmesh.types.BMFace)edges: newly-made edge(s)type list of (bmesh.types.BMEdge) 
    '''

    pass


def bridge_loops(bm, edges, use_pairs, use_cyclic, use_merge, merge_factor,
                 twist_offset):
    '''Bridge edge loops with faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_pairs: Undocumented. 
    :type use_pairs: bool
    :param use_cyclic: Undocumented. 
    :type use_cyclic: bool
    :param use_merge: Undocumented. 
    :type use_merge: bool
    :param merge_factor: Undocumented. 
    :type merge_factor: float
    :param twist_offset: Undocumented. 
    :type twist_offset: int
    :return:  faces: new facestype list of (bmesh.types.BMFace)edges: new edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def grid_fill(bm, edges, mat_nr, use_smooth, use_interp_simple):
    '''Create faces defined by 2 disconnected edge loops (which share edges). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth state to use 
    :type use_smooth: bool
    :param use_interp_simple: use simple interpolation 
    :type use_interp_simple: bool
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def holes_fill(bm, edges, sides):
    '''Fill boundary edges with faces, copying surrounding customdata. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param sides: number of face sides to fill 
    :type sides: int
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def face_attribute_fill(bm, faces, use_normals, use_data):
    '''Fill in faces with data from adjacent faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param use_normals: copy face winding 
    :type use_normals: bool
    :param use_data: copy face data 
    :type use_data: bool
    :return:  faces_fail: faces that could not be handledtype list of (bmesh.types.BMFace) 
    '''

    pass


def edgeloop_fill(bm, edges, mat_nr, use_smooth):
    '''Create faces defined by one or more non overlapping edge loops. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth state to use 
    :type use_smooth: bool
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def edgenet_fill(bm, edges, mat_nr, use_smooth, sides):
    '''Create faces defined by enclosed edges. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param mat_nr: material to use 
    :type mat_nr: int
    :param use_smooth: smooth state to use 
    :type use_smooth: bool
    :param sides: number of sides 
    :type sides: int
    :return:  faces: new facestype list of (bmesh.types.BMFace) 
    '''

    pass


def edgenet_prepare(bm, edges):
    '''Identifies several useful edge loop cases and modifies them so they’ll become a face when edgenet_fill is called. The cases covered are: 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :return:  edges: new edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def rotate(bm, cent, matrix, verts, space):
    '''Rotate vertices around a center, using a 3x3 rotation matrix. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param cent: center of rotation 
    :type cent: mathutils.Vector or any sequence of 3 floats
    :param matrix: matrix defining rotation 
    :type matrix: mathutils.Matrix
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param space: matrix to define the space (typically object matrix) 
    :type space: mathutils.Matrix
    '''

    pass


def translate(bm, vec, space, verts):
    '''Translate vertices by an offset. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param vec: translation offset 
    :type vec: mathutils.Vector or any sequence of 3 floats
    :param space: matrix to define the space (typically object matrix) 
    :type space: mathutils.Matrix
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    '''

    pass


def scale(bm, vec, space, verts):
    '''Scales vertices by an offset. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param vec: scale factor 
    :type vec: mathutils.Vector or any sequence of 3 floats
    :param space: matrix to define the space (typically object matrix) 
    :type space: mathutils.Matrix
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    '''

    pass


def transform(bm, matrix, space, verts):
    '''Transforms a set of vertices by a matrix. Multiplies the vertex coordinates with the matrix. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param matrix: transform matrix 
    :type matrix: mathutils.Matrix
    :param space: matrix to define the space (typically object matrix) 
    :type space: mathutils.Matrix
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    '''

    pass


def object_load_bmesh(bm, scene, object):
    '''Loads a bmesh into an object/mesh. This is a “private” bmop. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param scene: Undocumented. 
    :type scene: bpy.types.Scene
    :param object: Undocumented. 
    :type object: bpy.types.Object
    '''

    pass


def bmesh_to_mesh(bm, mesh, object, skip_tessface):
    '''Converts a bmesh to a Mesh. This is reserved for exiting editmode. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param mesh: Undocumented. 
    :type mesh: bpy.types.Mesh
    :param object: Undocumented. 
    :type object: bpy.types.Object
    :param skip_tessface: don’t calculate mfaces 
    :type skip_tessface: bool
    '''

    pass


def mesh_to_bmesh(bm, mesh, object, use_shapekey):
    '''Load the contents of a mesh into the bmesh. this bmop is private, it’s reserved exclusively for entering editmode. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param mesh: Undocumented. 
    :type mesh: bpy.types.Mesh
    :param object: Undocumented. 
    :type object: bpy.types.Object
    :param use_shapekey: load active shapekey coordinates into verts 
    :type use_shapekey: bool
    '''

    pass


def extrude_discrete_faces(bm, faces, use_select_history):
    '''Extrudes faces individually. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def extrude_edge_only(bm, edges, use_select_history):
    '''Extrudes Edges into faces, note that this is very simple, there’s no fancy winged extrusion. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input vertices 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  geom: output geometrytype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def extrude_vert_indiv(bm, verts, use_select_history):
    '''Extrudes wire edges from vertices. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  edges: output wire edgestype list of (bmesh.types.BMEdge)verts: output verticestype list of (bmesh.types.BMVert) 
    '''

    pass


def connect_verts(bm, verts, faces_exclude, check_degenerate):
    '''Split faces by adding edges that connect verts. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: Undocumented. 
    :type verts: list of (bmesh.types.BMVert)
    :param faces_exclude: Undocumented. 
    :type faces_exclude: list of (bmesh.types.BMFace)
    :param check_degenerate: prevent splits with overlaps & intersections 
    :type check_degenerate: bool
    :return:  edges:type list of (bmesh.types.BMEdge) 
    '''

    pass


def connect_verts_concave(bm, faces):
    '''Ensures all faces are convex faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: Undocumented. 
    :type faces: list of (bmesh.types.BMFace)
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace) 
    '''

    pass


def connect_verts_nonplanar(bm, angle_limit, faces):
    '''Split faces by connecting edges along non planer faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param angle_limit: total rotation angle (radians) 
    :type angle_limit: float
    :param faces: Undocumented. 
    :type faces: list of (bmesh.types.BMFace)
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace) 
    '''

    pass


def connect_vert_pair(bm, verts, verts_exclude, faces_exclude):
    '''Split faces by adding edges that connect verts. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: Undocumented. 
    :type verts: list of (bmesh.types.BMVert)
    :param verts_exclude: Undocumented. 
    :type verts_exclude: list of (bmesh.types.BMVert)
    :param faces_exclude: Undocumented. 
    :type faces_exclude: list of (bmesh.types.BMFace)
    :return:  edges:type list of (bmesh.types.BMEdge) 
    '''

    pass


def extrude_face_region(bm, geom, edges_exclude, use_keep_orig,
                        use_select_history):
    '''Extrude operator (does not transform) 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: edges and faces 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param edges_exclude: Undocumented. 
    :type edges_exclude: set of vert/edge/face type
    :param use_keep_orig: keep original geometry (requires geom to include edges). 
    :type use_keep_orig: bool
    :param use_select_history: pass to duplicate 
    :type use_select_history: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def dissolve_verts(bm, verts, use_face_split, use_boundary_tear):
    '''Dissolve Verts. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: Undocumented. 
    :type verts: list of (bmesh.types.BMVert)
    :param use_face_split: Undocumented. 
    :type use_face_split: bool
    :param use_boundary_tear: Undocumented. 
    :type use_boundary_tear: bool
    '''

    pass


def dissolve_edges(bm, edges, use_verts, use_face_split):
    '''Dissolve Edges. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: Undocumented. 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_verts: dissolve verts left between only 2 edges. 
    :type use_verts: bool
    :param use_face_split: Undocumented. 
    :type use_face_split: bool
    :return:  region:type list of (bmesh.types.BMFace) 
    '''

    pass


def dissolve_faces(bm, faces, use_verts):
    '''Dissolve Faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: Undocumented. 
    :type faces: list of (bmesh.types.BMFace)
    :param use_verts: dissolve verts left between only 2 edges. 
    :type use_verts: bool
    :return:  region:type list of (bmesh.types.BMFace) 
    '''

    pass


def dissolve_limit(bm, angle_limit, use_dissolve_boundaries, verts, edges,
                   delimit):
    '''Dissolve planar faces and co-linear edges. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param angle_limit: total rotation angle (radians) 
    :type angle_limit: float
    :param use_dissolve_boundaries: Undocumented. 
    :type use_dissolve_boundaries: bool
    :param verts: Undocumented. 
    :type verts: list of (bmesh.types.BMVert)
    :param edges: Undocumented. 
    :type edges: list of (bmesh.types.BMEdge)
    :param delimit: Undocumented. 
    :type delimit: int
    :return:  region:type list of (bmesh.types.BMFace) 
    '''

    pass


def dissolve_degenerate(bm, dist, edges):
    '''Dissolve edges with no length, faces with no area. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param dist: minimum distance to consider degenerate 
    :type dist: float
    :param edges: Undocumented. 
    :type edges: list of (bmesh.types.BMEdge)
    '''

    pass


def triangulate(bm, faces, quad_method, ngon_method):
    '''Triangulate. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: Undocumented. 
    :type faces: list of (bmesh.types.BMFace)
    :param quad_method: Undocumented. 
    :type quad_method: int
    :param ngon_method: Undocumented. 
    :type ngon_method: int
    :return:  edges:type list of (bmesh.types.BMEdge)faces:type list of (bmesh.types.BMFace)face_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceface_map_double: duplicate facestype dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def unsubdivide(bm, verts, iterations):
    '''Reduce detail in geometry containing grids. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param iterations: Undocumented. 
    :type iterations: int
    '''

    pass


def subdivide_edges(bm, edges, smooth, smooth_falloff, fractal, along_normal,
                    cuts, seed, custom_patterns, edge_percents,
                    quad_corner_type, use_grid_fill, use_single_edge,
                    use_only_quads, use_sphere, use_smooth_even):
    '''Advanced operator for subdividing edges with options for face patterns, smoothing and randomization. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: Undocumented. 
    :type edges: list of (bmesh.types.BMEdge)
    :param smooth: Undocumented. 
    :type smooth: float
    :param smooth_falloff: SUBD_FALLOFF_ROOT and friends 
    :type smooth_falloff: int
    :param fractal: Undocumented. 
    :type fractal: float
    :param along_normal: Undocumented. 
    :type along_normal: float
    :param cuts: Undocumented. 
    :type cuts: int
    :param seed: Undocumented. 
    :type seed: int
    :param custom_patterns: uses custom pointers 
    :type custom_patterns: dict mapping vert/edge/face types to unknown internal data, not compatible with python
    :param edge_percents: Undocumented. 
    :type edge_percents: dict mapping vert/edge/face types to float
    :param quad_corner_type: quad corner type, see bmesh_operators.h 
    :type quad_corner_type: int
    :param use_grid_fill: fill in fully-selected faces with a grid 
    :type use_grid_fill: bool
    :param use_single_edge: tessellate the case of one edge selected in a quad or triangle 
    :type use_single_edge: bool
    :param use_only_quads: only subdivide quads (for loopcut) 
    :type use_only_quads: bool
    :param use_sphere: for making new primitives only 
    :type use_sphere: bool
    :param use_smooth_even: maintain even offset when smoothing 
    :type use_smooth_even: bool
    :return:  geom_inner:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_split:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom: contains all output geometrytype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def subdivide_edgering(bm, edges, interp_mode, smooth, cuts, profile_shape,
                       profile_shape_factor):
    '''Take an edge-ring, and subdivide with interpolation options. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input vertices 
    :type edges: list of (bmesh.types.BMEdge)
    :param interp_mode: Undocumented. 
    :type interp_mode: int
    :param smooth: Undocumented. 
    :type smooth: float
    :param cuts: Undocumented. 
    :type cuts: int
    :param profile_shape: Undocumented. 
    :type profile_shape: int
    :param profile_shape_factor: Undocumented. 
    :type profile_shape_factor: float
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def bisect_plane(bm, geom, dist, plane_co, plane_no, use_snap_center,
                 clear_outer, clear_inner):
    '''Bisects the mesh by a plane (cut the mesh in half). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param dist: minimum distance when testing if a vert is exactly on the plane 
    :type dist: float
    :param plane_co: point on the plane 
    :type plane_co: mathutils.Vector or any sequence of 3 floats
    :param plane_no: direction of the plane 
    :type plane_no: mathutils.Vector or any sequence of 3 floats
    :param use_snap_center: snap axis aligned verts to the center 
    :type use_snap_center: bool
    :param clear_outer: when enabled. remove all geometry on the positive side of the plane 
    :type clear_outer: bool
    :param clear_inner: when enabled. remove all geometry on the negative side of the plane 
    :type clear_inner: bool
    :return:  geom_cut: output geometry aligned with the plane (new and existing)type list of (bmesh.types.BMVert, bmesh.types.BMEdge)geom: input and output geometry (result of cut)type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def delete(bm, geom, context):
    '''Utility operator to delete geometry. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param context: enum DEL_VERTS … 
    :type context: int
    '''

    pass


def duplicate(bm, geom, dest, use_select_history):
    '''Utility operator to duplicate geometry, optionally into a destination mesh. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param dest: Undocumented. 
    :type dest: bmesh.types.BMesh
    :param use_select_history: Undocumented. 
    :type use_select_history: bool
    :return:  geom_orig:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)vert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceedge_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceface_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceboundary_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceisovert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def split(bm, geom, dest, use_only_faces):
    '''Disconnect geometry from adjacent edges and faces, optionally into a destination mesh. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param dest: Undocumented. 
    :type dest: bmesh.types.BMesh
    :param use_only_faces: when enabled. don’t duplicate loose verts/edges 
    :type use_only_faces: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)boundary_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFaceisovert_map:type dict mapping vert/edge/face types to bmesh.types.BMVert/bmesh.types.BMEdge/bmesh.types.BMFace 
    '''

    pass


def spin(bm, geom, cent, axis, dvec, angle, space, steps, use_duplicate):
    '''Extrude or duplicate geometry a number of times, rotating and possibly translating after each step 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param cent: rotation center 
    :type cent: mathutils.Vector or any sequence of 3 floats
    :param axis: rotation axis 
    :type axis: mathutils.Vector or any sequence of 3 floats
    :param dvec: translation delta per step 
    :type dvec: mathutils.Vector or any sequence of 3 floats
    :param angle: total rotation angle (radians) 
    :type angle: float
    :param space: matrix to define the space (typically object matrix) 
    :type space: mathutils.Matrix
    :param steps: number of steps 
    :type steps: int
    :param use_duplicate: duplicate or extrude? 
    :type use_duplicate: bool
    :return:  geom_last: result of last steptype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def similar_faces(bm, faces, type, thresh, compare):
    '''Find similar faces (area/material/perimeter, …). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def similar_edges(bm, edges, type, thresh, compare):
    '''Similar Edges Search. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  edges: output edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def similar_verts(bm, verts, type, thresh, compare):
    '''Find similar vertices (normal, face, vertex group, …). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param verts: input vertices 
    :type verts: list of (bmesh.types.BMVert)
    :param type: type of selection 
    :type type: int
    :param thresh: threshold of selection 
    :type thresh: float
    :param compare: comparison method 
    :type compare: int
    :return:  verts: output verticestype list of (bmesh.types.BMVert) 
    '''

    pass


def rotate_uvs(bm, faces, use_ccw):
    '''Cycle the loop UV’s 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    '''

    pass


def reverse_uvs(bm, faces):
    '''Reverse the UV’s 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    '''

    pass


def rotate_colors(bm, faces, use_ccw):
    '''Cycle the loop colors 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param use_ccw: rotate counter-clockwise if true, otherwise clockwise 
    :type use_ccw: bool
    '''

    pass


def reverse_colors(bm, faces):
    '''Reverse the loop colors. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    '''

    pass


def split_edges(bm, edges, verts, use_verts):
    '''Disconnects faces along input edges. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param verts: optional tag verts, use to have greater control of splits 
    :type verts: list of (bmesh.types.BMVert)
    :param use_verts: use ‘verts’ for splitting, else just find verts to split from edges 
    :type use_verts: bool
    :return:  edges: old output disconnected edgestype list of (bmesh.types.BMEdge) 
    '''

    pass


def create_grid(bm, x_segments, y_segments, size, matrix, calc_uvs):
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param x_segments: number of x segments 
    :type x_segments: int
    :param y_segments: number of y segments 
    :type y_segments: int
    :param size: size of the grid 
    :type size: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_uvsphere(bm, u_segments, v_segments, diameter, matrix, calc_uvs):
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param u_segments: number of u segments 
    :type u_segments: int
    :param v_segments: number of v segment 
    :type v_segments: int
    :param diameter: diameter 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_icosphere(bm, subdivisions, diameter, matrix, calc_uvs):
    '''Creates a grid with a variable number of subdivisions 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param subdivisions: how many times to recursively subdivide the sphere 
    :type subdivisions: int
    :param diameter: diameter 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_monkey(bm, matrix, calc_uvs):
    '''Creates a monkey (standard blender primitive). 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_cone(bm, cap_ends, cap_tris, segments, diameter1, diameter2, depth,
                matrix, calc_uvs):
    '''Creates a cone with variable depth at both ends 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param cap_ends: whether or not to fill in the ends with faces 
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons 
    :type cap_tris: bool
    :param segments: Undocumented. 
    :type segments: int
    :param diameter1: diameter of one end 
    :type diameter1: float
    :param diameter2: diameter of the opposite 
    :type diameter2: float
    :param depth: distance between ends 
    :type depth: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_circle(bm, cap_ends, cap_tris, segments, diameter, matrix,
                  calc_uvs):
    '''Creates a Circle. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param cap_ends: whether or not to fill in the ends with faces 
    :type cap_ends: bool
    :param cap_tris: fill ends with triangles instead of ngons 
    :type cap_tris: bool
    :param segments: Undocumented. 
    :type segments: int
    :param diameter: diameter of one end 
    :type diameter: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def create_cube(bm, size, matrix, calc_uvs):
    '''Creates a cube. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param size: size of the cube 
    :type size: float
    :param matrix: matrix to multiply the new geometry with 
    :type matrix: mathutils.Matrix
    :param calc_uvs: calculate default UVs 
    :type calc_uvs: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def bevel(bm, geom, offset, offset_type, segments, profile, vertex_only,
          clamp_overlap, material, loop_slide):
    '''Bevels edges and vertices 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: input edges and vertices 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param offset: amount to offset beveled edge 
    :type offset: float
    :param offset_type: how to measure offset (enum) 
    :type offset_type: int
    :param segments: number of segments in bevel 
    :type segments: int
    :param profile: profile shape, 0->1 (.5=>round) 
    :type profile: float
    :param vertex_only: only bevel vertices, not edges 
    :type vertex_only: bool
    :param clamp_overlap: do not allow beveled edges/vertices to overlap each other 
    :type clamp_overlap: bool
    :param material: material for bevel faces, -1 means get from adjacent faces 
    :type material: int
    :param loop_slide: prefer to slide along edges to having even widths 
    :type loop_slide: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace)edges: output edgestype list of (bmesh.types.BMEdge)verts: output vertstype list of (bmesh.types.BMVert) 
    '''

    pass


def beautify_fill(bm, faces, edges, use_restrict_tag, method):
    '''Rotate edges to create more evenly spaced triangles. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param edges: edges that can be flipped 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_restrict_tag: restrict edge rotation to mixed tagged vertices 
    :type use_restrict_tag: bool
    :param method: method to define what is beautiful 
    :type method: int
    :return:  geom: new flipped faces and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def triangle_fill(bm, use_beauty, use_dissolve, edges, normal):
    '''Fill edges with triangles 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param use_beauty: Undocumented. 
    :type use_beauty: bool
    :param use_dissolve: dissolve resulting faces 
    :type use_dissolve: bool
    :param edges: input edges 
    :type edges: list of (bmesh.types.BMEdge)
    :param normal: optionally pass the fill normal to use 
    :type normal: mathutils.Vector or any sequence of 3 floats
    :return:  geom: new faces and edgestype list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def solidify(bm, geom, thickness):
    '''Turns a mesh into a shell with thickness 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param geom: Undocumented. 
    :type geom: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param thickness: Undocumented. 
    :type thickness: float
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def inset_individual(bm, faces, thickness, depth, use_even_offset,
                     use_interpolate, use_relative_offset):
    '''Insets individual faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param thickness: Undocumented. 
    :type thickness: float
    :param depth: Undocumented. 
    :type depth: float
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_interpolate: Undocumented. 
    :type use_interpolate: bool
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def inset_region(bm, faces, faces_exclude, use_boundary, use_even_offset,
                 use_interpolate, use_relative_offset, use_edge_rail,
                 thickness, depth, use_outset):
    '''Inset or outset face regions. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param faces_exclude: Undocumented. 
    :type faces_exclude: list of (bmesh.types.BMFace)
    :param use_boundary: Undocumented. 
    :type use_boundary: bool
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_interpolate: Undocumented. 
    :type use_interpolate: bool
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :param use_edge_rail: Undocumented. 
    :type use_edge_rail: bool
    :param thickness: Undocumented. 
    :type thickness: float
    :param depth: Undocumented. 
    :type depth: float
    :param use_outset: Undocumented. 
    :type use_outset: bool
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def offset_edgeloops(bm, edges, use_cap_endpoint):
    '''Creates edge loops based on simple edge-outset method. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param edges: input faces 
    :type edges: list of (bmesh.types.BMEdge)
    :param use_cap_endpoint: Undocumented. 
    :type use_cap_endpoint: bool
    :return:  edges: output facestype list of (bmesh.types.BMEdge) 
    '''

    pass


def wireframe(bm, faces, thickness, offset, use_replace, use_boundary,
              use_even_offset, use_crease, crease_weight, use_relative_offset,
              material_offset):
    '''Makes a wire-frame copy of faces. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param thickness: Undocumented. 
    :type thickness: float
    :param offset: Undocumented. 
    :type offset: float
    :param use_replace: Undocumented. 
    :type use_replace: bool
    :param use_boundary: Undocumented. 
    :type use_boundary: bool
    :param use_even_offset: Undocumented. 
    :type use_even_offset: bool
    :param use_crease: Undocumented. 
    :type use_crease: bool
    :param crease_weight: Undocumented. 
    :type crease_weight: float
    :param use_relative_offset: Undocumented. 
    :type use_relative_offset: bool
    :param material_offset: Undocumented. 
    :type material_offset: int
    :return:  faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def poke(bm, faces, offset, center_mode, use_relative_offset):
    '''Splits a face into a triangle fan. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param faces: input faces 
    :type faces: list of (bmesh.types.BMFace)
    :param offset: center vertex offset along normal 
    :type offset: float
    :param center_mode: calculation mode for center vertex 
    :type center_mode: int
    :param use_relative_offset: apply offset 
    :type use_relative_offset: bool
    :return:  verts: output vertstype list of (bmesh.types.BMVert)faces: output facestype list of (bmesh.types.BMFace) 
    '''

    pass


def convex_hull(bm, input, use_existing_faces):
    '''All hull vertices, faces, and edges are added to ‘geom.out’. Any input elements that end up inside the hull (i.e. are not used by an output face) are added to the ‘interior_geom’ slot. The ‘unused_geom’ slot will contain all interior geometry that is completely unused. Lastly, ‘holes_geom’ contains edges and faces that were in the input and are part of the hull. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param input: Undocumented. 
    :type input: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param use_existing_faces: Undocumented. 
    :type use_existing_faces: bool
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_interior:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_unused:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)geom_holes:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass


def symmetrize(bm, input, direction, dist):
    '''All new vertices, edges, and faces are added to the “geom.out” slot. 

    :param bm: The bmesh to operate on. 
    :type bm: bmesh.types.BMesh
    :param input: Undocumented. 
    :type input: list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)
    :param direction: Undocumented. 
    :type direction: int
    :param dist: minimum distance 
    :type dist: float
    :return:  geom:type list of (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace) 
    '''

    pass
