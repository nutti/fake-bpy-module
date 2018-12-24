def area_tri(v1, v2, v3):
    '''Returns the area size of the 2D or 3D triangle defined. 

    :param v1: Point1 
    :type v1: mathutils.Vector
    :param v2: Point2 
    :type v2: mathutils.Vector
    :param v3: Point3 
    :type v3: mathutils.Vector
    '''

    pass


def barycentric_transform(point, tri_a1, tri_a2, tri_a3, tri_b1, tri_b2,
                          tri_b3):
    '''Return a transformed point, the transformation is defined by 2 triangles. 

    :param point: The point to transform. 
    :type point: mathutils.Vector
    :param tri_a1: source triangle vertex. 
    :type tri_a1: mathutils.Vector
    :param tri_a2: source triangle vertex. 
    :type tri_a2: mathutils.Vector
    :param tri_a3: source triangle vertex. 
    :type tri_a3: mathutils.Vector
    :param tri_b1: target triangle vertex. 
    :type tri_b1: mathutils.Vector
    :param tri_b2: target triangle vertex. 
    :type tri_b2: mathutils.Vector
    :param tri_b3: target triangle vertex. 
    :type tri_b3: mathutils.Vector
    :return:  The transformed point 
    '''

    pass


def box_fit_2d(points):
    '''Returns an angle that best fits the points to an axis aligned rectangle 

    :param points: list of 2d points. 
    :type points: list
    :return:  angle 
    '''

    pass


def box_pack_2d(boxes):
    '''Returns the normal of the 3D tri or quad. 

    :param boxes: list of boxes, each box is a list where the first 4 items are [x, y, width, height, …] other items are ignored. 
    :type boxes: list
    :return:  the width and height of the packed bounding box 
    '''

    pass


def convex_hull_2d(points):
    '''Returns a list of indices into the list given 

    :param points: list of 2d points. 
    :type points: list
    :return:  a list of indices 
    '''

    pass


def distance_point_to_plane(pt, plane_co, plane_no):
    '''Returns the signed distance between a point and a plane (negative when below the normal). 

    :param pt: Point 
    :type pt: mathutils.Vector
    :param plane_co: A point on the plane 
    :type plane_co: mathutils.Vector
    :param plane_no: The direction the plane is facing 
    :type plane_no: mathutils.Vector
    '''

    pass


def interpolate_bezier(knot1, handle1, handle2, knot2, resolution):
    '''Interpolate a bezier spline segment. 

    :param knot1: First bezier spline point. 
    :type knot1: mathutils.Vector
    :param handle1: First bezier spline handle. 
    :type handle1: mathutils.Vector
    :param handle2: Second bezier spline handle. 
    :type handle2: mathutils.Vector
    :param knot2: Second bezier spline point. 
    :type knot2: mathutils.Vector
    :param resolution: Number of points to return. 
    :type resolution: int
    :return:  The interpolated points 
    '''

    pass


def intersect_line_line(v1, v2, v3, v4):
    '''Returns a tuple with the points on each line respectively closest to the other. 

    :param v1: First point of the first line 
    :type v1: mathutils.Vector
    :param v2: Second point of the first line 
    :type v2: mathutils.Vector
    :param v3: First point of the second line 
    :type v3: mathutils.Vector
    :param v4: Second point of the second line 
    :type v4: mathutils.Vector
    '''

    pass


def intersect_line_line_2d(lineA_p1, lineA_p2, lineB_p1, lineB_p2):
    '''Takes 2 segments (defined by 4 vectors) and returns a vector for their point of intersection or None. 

    :param lineA_p1: First point of the first line 
    :type lineA_p1: mathutils.Vector
    :param lineA_p2: Second point of the first line 
    :type lineA_p2: mathutils.Vector
    :param lineB_p1: First point of the second line 
    :type lineB_p1: mathutils.Vector
    :param lineB_p2: Second point of the second line 
    :type lineB_p2: mathutils.Vector
    :return:  The point of intersection or None when not found 
    '''

    pass


def intersect_line_plane(line_a, line_b, plane_co, plane_no, no_flip=False):
    '''Calculate the intersection between a line (as 2 vectors) and a plane. Returns a vector for the intersection or None. 

    :param line_a: First point of the first line 
    :type line_a: mathutils.Vector
    :param line_b: Second point of the first line 
    :type line_b: mathutils.Vector
    :param plane_co: A point on the plane 
    :type plane_co: mathutils.Vector
    :param plane_no: The direction the plane is facing 
    :type plane_no: mathutils.Vector
    :return:  The point of intersection or None when not found 
    '''

    pass


def intersect_line_sphere(line_a, line_b, sphere_co, sphere_radius, clip=True):
    '''Takes a line (as 2 points) and a sphere (as a point and a radius) and returns the intersection 

    :param line_a: First point of the line 
    :type line_a: mathutils.Vector
    :param line_b: Second point of the line 
    :type line_b: mathutils.Vector
    :param sphere_co: The center of the sphere 
    :type sphere_co: mathutils.Vector
    :param sphere_radius: Radius of the sphere 
    :type sphere_radius: sphere_radius
    :return:  The intersection points as a pair of vectors or None when there is no intersection 
    '''

    pass


def intersect_line_sphere_2d(line_a,
                             line_b,
                             sphere_co,
                             sphere_radius,
                             clip=True):
    '''Takes a line (as 2 points) and a sphere (as a point and a radius) and returns the intersection 

    :param line_a: First point of the line 
    :type line_a: mathutils.Vector
    :param line_b: Second point of the line 
    :type line_b: mathutils.Vector
    :param sphere_co: The center of the sphere 
    :type sphere_co: mathutils.Vector
    :param sphere_radius: Radius of the sphere 
    :type sphere_radius: sphere_radius
    :return:  The intersection points as a pair of vectors or None when there is no intersection 
    '''

    pass


def intersect_plane_plane(plane_a_co, plane_a_no, plane_b_co, plane_b_no):
    '''Return the intersection between two planes 

    :param plane_a_co: Point on the first plane 
    :type plane_a_co: mathutils.Vector
    :param plane_a_no: Normal of the first plane 
    :type plane_a_no: mathutils.Vector
    :param plane_b_co: Point on the second plane 
    :type plane_b_co: mathutils.Vector
    :param plane_b_no: Normal of the second plane 
    :type plane_b_no: mathutils.Vector
    :return:  The line of the intersection represented as a point and a vector 
    '''

    pass


def intersect_point_line(pt, line_p1, line_p2):
    '''Takes a point and a line and returns a tuple with the closest point on the line and its distance from the first point of the line as a percentage of the length of the line. 

    :param pt: Point 
    :type pt: mathutils.Vector
    :param line_p1: First point of the line 
    :type line_p1: mathutils.Vector
    :param line_p1: Second point of the line 
    :type line_p1: 
    '''

    pass


def intersect_point_quad_2d(pt, quad_p1, quad_p2, quad_p3, quad_p4):
    '''Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad, only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0. Works only with convex quads without singular edges. 

    :param pt: Point 
    :type pt: mathutils.Vector
    :param quad_p1: First point of the quad 
    :type quad_p1: mathutils.Vector
    :param quad_p2: Second point of the quad 
    :type quad_p2: mathutils.Vector
    :param quad_p3: Third point of the quad 
    :type quad_p3: mathutils.Vector
    :param quad_p4: Fourth point of the quad 
    :type quad_p4: mathutils.Vector
    '''

    pass


def intersect_point_tri(pt, tri_p1, tri_p2, tri_p3):
    '''Takes 4 vectors: one is the point and the next 3 define the triangle. 

    :param pt: Point 
    :type pt: mathutils.Vector
    :param tri_p1: First point of the triangle 
    :type tri_p1: mathutils.Vector
    :param tri_p2: Second point of the triangle 
    :type tri_p2: mathutils.Vector
    :param tri_p3: Third point of the triangle 
    :type tri_p3: mathutils.Vector
    :return:  Point on the triangles plane or None if its outside the triangle 
    '''

    pass


def intersect_point_tri_2d(pt, tri_p1, tri_p2, tri_p3):
    '''Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0. 

    :param pt: Point 
    :type pt: mathutils.Vector
    :param tri_p1: First point of the triangle 
    :type tri_p1: mathutils.Vector
    :param tri_p2: Second point of the triangle 
    :type tri_p2: mathutils.Vector
    :param tri_p3: Third point of the triangle 
    :type tri_p3: mathutils.Vector
    '''

    pass


def intersect_ray_tri(v1, v2, v3, ray, orig, clip=True):
    '''Returns the intersection between a ray and a triangle, if possible, returns None otherwise. 

    :param v1: Point1 
    :type v1: mathutils.Vector
    :param v2: Point2 
    :type v2: mathutils.Vector
    :param v3: Point3 
    :type v3: mathutils.Vector
    :param ray: Direction of the projection 
    :type ray: mathutils.Vector
    :param orig: Origin 
    :type orig: mathutils.Vector
    :param clip: When False, don’t restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle. 
    :type clip: boolean
    :return:  The point of intersection or None if no intersection is found 
    '''

    pass


def intersect_sphere_sphere_2d(p_a, radius_a, p_b, radius_b):
    '''Returns 2 points on between intersecting circles. 

    :param p_a: Center of the first circle 
    :type p_a: mathutils.Vector
    :param radius_a: Radius of the first circle 
    :type radius_a: float
    :param p_b: Center of the second circle 
    :type p_b: mathutils.Vector
    :param radius_b: Radius of the second circle 
    :type radius_b: float
    '''

    pass


def normal(vectors):
    '''Returns the normal of a 3D polygon. 

    :param vectors: Vectors to calculate normals with 
    :type vectors: sequence of 3 or more 3d vector
    '''

    pass


def points_in_planes(planes):
    '''Returns a list of points inside all planes given and a list of index values for the planes used. 

    :param planes: List of planes (4D vectors). 
    :type planes: list of mathutils.Vector
    :return:  two lists, once containing the vertices inside the planes, another containing the plane indices used 
    '''

    pass


def tessellate_polygon(veclist_list):
    '''Takes a list of polylines (each point a vector) and returns the point indices for a polyline filled with triangles. 

    :param veclist_list: list of polylines 
    :type veclist_list: 
    '''

    pass


def volume_tetrahedron(v1, v2, v3, v4):
    '''Return the volume formed by a tetrahedron (points can be in any order). 

    :param v1: Point1 
    :type v1: mathutils.Vector
    :param v2: Point2 
    :type v2: mathutils.Vector
    :param v3: Point3 
    :type v3: mathutils.Vector
    :param v4: Point4 
    :type v4: mathutils.Vector
    '''

    pass
