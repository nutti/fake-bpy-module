class BMesh:
    edges = None
    faces = None
    is_valid = None
    is_wrapped = None
    loops = None
    select_history = None
    select_mode = None
    verts = None

    def calc_tessface(self):
        pass

    def calc_volume(self, signed=False):
        pass

    def clear(self):
        pass

    def copy(self):
        pass

    def free(self):
        pass

    def from_mesh(self, mesh, face_normals=True, use_shape_key=False, shape_key_index=0):
        pass

    def from_object(self, object, scene, deform=True, render=False, cage=False, face_normals=True):
        pass

    def normal_update(self):
        pass

    def select_flush(self, select):
        pass

    def select_flush_mode(self):
        pass

    def to_mesh(self, mesh):
        pass

    def transform(self, matrix, filter=None):
        pass



class BMVert:
    co = None
    hide = None
    index = None
    is_boundary = None
    is_manifold = None
    is_valid = None
    is_wire = None
    link_edges = None
    link_faces = None
    link_loops = None
    normal = None
    select = None
    tag = None

    def calc_edge_angle(self, fallback=None):
        pass

    def calc_shell_factor(self):
        pass

    def copy_from(self, other):
        pass

    def copy_from_face_interp(self, face):
        pass

    def copy_from_vert_interp(self, vert_pair, fac):
        pass

    def hide_set(self, hide):
        pass

    def normal_update(self):
        pass

    def select_set(self, select):
        pass



class BMEdge:
    hide = None
    index = None
    is_boundary = None
    is_contiguous = None
    is_convex = None
    is_manifold = None
    is_valid = None
    is_wire = None
    link_faces = None
    link_loops = None
    seam = None
    select = None
    smooth = None
    tag = None
    verts = None

    def calc_face_angle(self, fallback=None):
        pass

    def calc_face_angle_signed(self, fallback=None):
        pass

    def calc_length(self):
        pass

    def calc_tangent(self, loop):
        pass

    def copy_from(self, other):
        pass

    def hide_set(self, hide):
        pass

    def normal_update(self):
        pass

    def other_vert(self, vert):
        pass

    def select_set(self, select):
        pass



class BMFace:
    edges = None
    hide = None
    index = None
    is_valid = None
    loops = None
    material_index = None
    normal = None
    select = None
    smooth = None
    tag = None
    verts = None

    def calc_area(self):
        pass

    def calc_center_bounds(self):
        pass

    def calc_center_median(self):
        pass

    def calc_center_median_weighted(self):
        pass

    def calc_perimeter(self):
        pass

    def calc_tangent_edge(self):
        pass

    def calc_tangent_edge_diagonal(self):
        pass

    def calc_tangent_edge_pair(self):
        pass

    def calc_tangent_vert_diagonal(self):
        pass

    def copy(self, verts=True, edges=True):
        pass

    def copy_from(self, other):
        pass

    def copy_from_face_interp(self, face, vert=True):
        pass

    def hide_set(self, hide):
        pass

    def normal_flip(self):
        pass

    def normal_update(self):
        pass

    def select_set(self, select):
        pass



class BMLoop:
    edge = None
    face = None
    index = None
    is_convex = None
    is_valid = None
    link_loop_next = None
    link_loop_prev = None
    link_loop_radial_next = None
    link_loop_radial_prev = None
    link_loops = None
    tag = None
    vert = None

    def calc_angle(self):
        pass

    def calc_normal(self):
        pass

    def calc_tangent(self):
        pass

    def copy_from(self, other):
        pass

    def copy_from_face_interp(self, face, vert=True, multires=True):
        pass



class BMElemSeq:

    def index_update(self):
        pass



class BMVertSeq:
    layers = None

    def ensure_lookup_table(self):
        pass

    def index_update(self):
        pass

    def new(self, co=(0.0, 0.0, 0.0), example=None):
        pass

    def remove(self, vert):
        pass

    def sort(self, key=None, reverse=False):
        pass



class BMEdgeSeq:
    layers = None

    def ensure_lookup_table(self):
        pass

    def get(self, verts, fallback=None):
        pass

    def index_update(self):
        pass

    def new(self, verts, example=None):
        pass

    def remove(self, edge):
        pass

    def sort(self, key=None, reverse=False):
        pass



class BMFaceSeq:
    active = None
    layers = None

    def ensure_lookup_table(self):
        pass

    def get(self, verts, fallback=None):
        pass

    def index_update(self):
        pass

    def new(self, verts, example=None):
        pass

    def remove(self, face):
        pass

    def sort(self, key=None, reverse=False):
        pass



class BMLoopSeq:
    layers = None



class BMIter:

    pass


class BMEditSelSeq:
    active = None

    def add(self, element):
        pass

    def clear(self):
        pass

    def discard(self, element):
        pass

    def remove(self, element):
        pass

    def validate(self):
        pass



class BMEditSelIter:

    pass


class BMLayerAccessVert:
    bevel_weight = None
    deform = None
    float = None
    int = None
    paint_mask = None
    shape = None
    skin = None
    string = None



class BMLayerAccessEdge:
    bevel_weight = None
    crease = None
    float = None
    freestyle = None
    int = None
    string = None



class BMLayerAccessFace:
    float = None
    freestyle = None
    int = None
    string = None
    tex = None



class BMLayerAccessLoop:
    color = None
    float = None
    int = None
    string = None
    uv = None



class BMLayerCollection:
    active = None
    is_singleton = None

    def get(self, key, default=None):
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def new(self, name):
        pass

    def remove(self, layer):
        pass

    def values(self):
        pass

    def verify(self):
        pass



class BMLayerItem:
    name = None

    def copy_from(self, other):
        pass



class BMLoopUV:
    pin_uv = None
    select = None
    select_edge = None
    uv = None



class BMDeformVert:

    def clear(self):
        pass

    def get(self, key, default=None):
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass



