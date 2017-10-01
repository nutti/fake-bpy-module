def getCurrentScene():
    pass


def integrate(func, it, it_end, integration_type):
    pass


def angle_x_normal(it):
    pass


def bound(lower, x, higher):
    pass


def bounding_box(stroke):
    pass


def curvature_from_stroke_vertex(svert):
    pass


def find_matching_vertex(id, it):
    pass


def get_chain_length(ve, orientation):
    pass


def get_object_name(stroke):
    pass


def get_strokes():
    pass


def get_test_stroke():
    pass


def is_poly_clockwise(stroke):
    pass


def iter_distance_along_stroke(stroke):
    pass


def iter_distance_from_camera(stroke, range_min, range_max, normfac):
    pass


def iter_distance_from_object(stroke, location, range_min, range_max, normfac):
    pass


def iter_material_value(stroke, func, attribute):
    pass


def iter_t2d_along_stroke(stroke):
    pass


def material_from_fedge(fe):
    pass


def normal_at_I0D(it):
    pass


def pairwise(iterable, types={}):
    pass


def rgb_to_bw(r, g, b):
    pass


def simplify(points, tolerance):
    pass


def stroke_curvature(it):
    pass


def stroke_normal(stroke):
    pass


def tripplewise(iterable):
    pass


class BoundingBox:

    def inside(self, other):
        pass



class StrokeCollector:

    def shade(self, stroke):
        pass



