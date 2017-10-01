class AdjacencyIterator:
    is_incoming = None
    object = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, vertex, restrict_to_selection=True, restrict_to_unvisited=True):
        pass



class BBox:

    def __init__(self):
        pass



class BinaryPredicate0D:
    name = None

    def __init__(self):
        pass

    def __call__(self, inter1, inter2):
        pass



class BinaryPredicate1D:
    name = None

    def __init__(self):
        pass

    def __call__(self, inter1, inter2):
        pass



class Chain:

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, id):
        pass

    def push_viewedge_back(self, viewedge, orientation):
        pass

    def push_viewedge_front(self, viewedge, orientation):
        pass



class ChainingIterator:
    is_incrementing = None
    next_vertex = None
    object = None

    def __init__(self, restrict_to_selection=True, restrict_to_unvisited=True, begin=None, orientation=True):
        pass

    def __init__(self, brother):
        pass

    def init(self):
        pass

    def traverse(self, it):
        pass



class Curve:
    is_empty = None
    segments_size = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, id):
        pass

    def push_vertex_back(self, vertex):
        pass

    def push_vertex_front(self, vertex):
        pass



class CurvePoint:
    fedge = None
    first_svertex = None
    second_svertex = None
    t2d = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, first_vertex, second_vertex, t2d):
        pass

    def __init__(self, first_point, second_point, t2d):
        pass



class CurvePointIterator:
    object = None
    t = None
    u = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, step=0.0):
        pass



class FEdge:
    first_svertex = None
    id = None
    is_smooth = None
    nature = None
    next_fedge = None
    previous_fedge = None
    second_svertex = None
    viewedge = None

    def FEdge(self):
        pass

    def FEdge(self, brother):
        pass

    def FEdge(self, first_vertex, second_vertex):
        pass



class FEdgeSharp:
    face_mark_left = None
    face_mark_right = None
    material_index_left = None
    material_index_right = None
    material_left = None
    material_right = None
    normal_left = None
    normal_right = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, first_vertex, second_vertex):
        pass



class FEdgeSmooth:
    face_mark = None
    material = None
    material_index = None
    normal = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, first_vertex, second_vertex):
        pass



class Id:
    first = None
    second = None

    def __init__(self, first=0, second=0):
        pass

    def __init__(self, brother):
        pass



class IntegrationType:

    pass


class Interface0D:
    id = None
    name = None
    nature = None
    point_2d = None
    point_3d = None
    projected_x = None
    projected_y = None
    projected_z = None

    def __init__(self):
        pass

    def get_fedge(self, inter):
        pass



class Interface0DIterator:
    at_last = None
    object = None
    t = None
    u = None

    def __init__(self, brother):
        pass

    def __init__(self, it):
        pass



class Interface1D:
    id = None
    length_2d = None
    name = None
    nature = None
    time_stamp = None

    def __init__(self):
        pass

    def points_begin(self, t=0.0):
        pass

    def points_end(self, t=0.0):
        pass

    def vertices_begin(self):
        pass

    def vertices_end(self):
        pass



class Iterator:
    is_begin = None
    is_end = None
    name = None

    def __init__(self):
        pass

    def decrement(self):
        pass

    def increment(self):
        pass



class Material:
    ambient = None
    diffuse = None
    emission = None
    line = None
    priority = None
    shininess = None
    specular = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, line, diffuse, ambient, specular, emission, shininess, priority):
        pass



class MediumType:

    pass


class Nature:

    pass


class Noise:

    def __init__(self, seed = -1):
        pass

    def smoothNoise1(self, v):
        pass

    def smoothNoise2(self, v):
        pass

    def smoothNoise3(self, v):
        pass

    def turbulence1(self, v, freq, amp, oct=4):
        pass

    def turbulence2(self, v, freq, amp, oct=4):
        pass

    def turbulence3(self, v, freq, amp, oct=4):
        pass



class NonTVertex:
    svertex = None

    def __init__(self):
        pass

    def __init__(self, svertex):
        pass



class Operators:

    pass


class SShape:
    bbox = None
    edges = None
    id = None
    name = None
    vertices = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def add_edge(self, edge):
        pass

    def add_vertex(self, vertex):
        pass

    def compute_bbox(self):
        pass



class SVertex:
    curvatures = None
    id = None
    normals = None
    normals_size = None
    point_2d = None
    point_3d = None
    viewvertex = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, point_3d, id):
        pass

    def add_fedge(self, fedge):
        pass

    def add_normal(self, normal):
        pass



class SVertexIterator:
    object = None
    t = None
    u = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, vertex, begin, previous_edge, next_edge, t):
        pass



class Stroke:
    id = None
    length_2d = None
    medium_type = None
    texture_id = None
    tips = None

    def Stroke(self):
        pass

    def Stroke(self, brother):
        pass

    def compute_sampling(self, n):
        pass

    def insert_vertex(self, vertex, next):
        pass

    def remove_all_vertices(self):
        pass

    def remove_vertex(self, vertex):
        pass

    def resample(self, n):
        pass

    def resample(self, sampling):
        pass

    def stroke_vertices_begin(self, t=0.0):
        pass

    def stroke_vertices_end(self):
        pass

    def stroke_vertices_size(self):
        pass

    def update_length(self):
        pass



class StrokeAttribute:
    alpha = None
    color = None
    thickness = None
    visible = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, red, green, blue, alpha, thickness_right, thickness_left):
        pass

    def __init__(self, attribute1, attribute2, t):
        pass

    def get_attribute_real(self, name):
        pass

    def get_attribute_vec2(self, name):
        pass

    def get_attribute_vec3(self, name):
        pass

    def has_attribute_real(self, name):
        pass

    def has_attribute_vec2(self, name):
        pass

    def has_attribute_vec3(self, name):
        pass

    def set_attribute_real(self, name, value):
        pass

    def set_attribute_vec2(self, name, value):
        pass

    def set_attribute_vec3(self, name, value):
        pass



class StrokeShader:
    name = None

    def __init__(self):
        pass

    def shade(self, stroke):
        pass



class StrokeVertex:
    attribute = None
    curvilinear_abscissa = None
    point = None
    stroke_length = None
    u = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, first_vertex, second_vertex, t3d):
        pass

    def __init__(self, point):
        pass

    def __init__(self, svertex):
        pass

    def __init__(self, svertex, attribute):
        pass



class StrokeVertexIterator:
    at_last = None
    object = None
    t = None
    u = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def decremented(self):
        pass

    def incremented(self):
        pass

    def reversed(self):
        pass



class TVertex:
    back_svertex = None
    front_svertex = None
    id = None

    def __init__(self):
        pass

    def get_mate(self, viewedge):
        pass

    def get_svertex(self, fedge):
        pass



class UnaryFunction0D:
    name = None



class UnaryFunction0DDouble:

    def __init__(self):
        pass



class UnaryFunction0DEdgeNature:

    def __init__(self):
        pass



class UnaryFunction0DFloat:

    def __init__(self):
        pass



class UnaryFunction0DId:

    def __init__(self):
        pass



class UnaryFunction0DMaterial:

    def __init__(self):
        pass



class UnaryFunction0DUnsigned:

    def __init__(self):
        pass



class UnaryFunction0DVec2f:

    def __init__(self):
        pass



class UnaryFunction0DVec3f:

    def __init__(self):
        pass



class UnaryFunction0DVectorViewShape:

    def __init__(self):
        pass



class UnaryFunction0DViewShape:

    def __init__(self):
        pass



class UnaryFunction1D:
    name = None



class UnaryFunction1DDouble:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DEdgeNature:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DFloat:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DUnsigned:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DVec2f:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DVec3f:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DVectorViewShape:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryFunction1DVoid:
    integration_type = None

    def __init__(self):
        pass

    def __init__(self, integration_type):
        pass



class UnaryPredicate0D:
    name = None

    def __init__(self):
        pass

    def __call__(self, it):
        pass



class UnaryPredicate1D:
    name = None

    def __init__(self):
        pass

    def __call__(self, inter):
        pass



class ViewEdge:
    chaining_time_stamp = None
    first_fedge = None
    first_viewvertex = None
    id = None
    is_closed = None
    last_fedge = None
    last_viewvertex = None
    nature = None
    occludee = None
    qi = None
    viewshape = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def update_fedges(self):
        pass



class ViewEdgeIterator:
    begin = None
    current_edge = None
    object = None
    orientation = None

    def __init__(self, begin=None, orientation=True):
        pass

    def __init__(self, brother):
        pass

    def change_orientation(self):
        pass



class ViewMap:
    scene_bbox = None

    def __init__(self):
        pass

    def get_closest_fedge(self, x, y):
        pass

    def get_closest_viewedge(self, x, y):
        pass



class ViewShape:
    edges = None
    id = None
    library_path = None
    name = None
    sshape = None
    vertices = None

    def __init__(self):
        pass

    def __init__(self, brother):
        pass

    def __init__(self, sshape):
        pass

    def add_edge(self, edge):
        pass

    def add_vertex(self, vertex):
        pass



class ViewVertex:
    nature = None

    def edges_begin(self):
        pass

    def edges_end(self):
        pass

    def edges_iterator(self, edge):
        pass



class orientedViewEdgeIterator:
    object = None

    def __init__(self):
        pass

    def __init__(self, iBrother):
        pass



