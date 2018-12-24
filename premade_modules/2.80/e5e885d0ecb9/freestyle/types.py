class AdjacencyIterator:
    '''Class for representing adjacency iterators used in the chaining process. An AdjacencyIterator is created in the increment() and decrement() methods of a ChainingIterator and passed to the traverse() method of the ChainingIterator. '''

    is_incoming = None
    '''True if the current ViewEdge is coming towards the iteration vertex, and False otherwise. 

    :type:  bool 
    '''

    object = None
    '''The ViewEdge object currently pointed to by this iterator. 

    :type:  ViewEdge 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An AdjacencyIterator object. 
        :type brother: AdjacencyIterator
        '''
        pass

    def __init__(self,
                 vertex,
                 restrict_to_selection=True,
                 restrict_to_unvisited=True):
        '''Builds a AdjacencyIterator object. 

        :param vertex: The vertex which is the next crossing. 
        :type vertex: ViewVertex
        :param restrict_to_selection: Indicates whether to force the chaining to stay within the set of selected ViewEdges or not. 
        :type restrict_to_selection: bool
        :param restrict_to_unvisited: Indicates whether a ViewEdge that has already been chained must be ignored ot not. 
        :type restrict_to_unvisited: bool
        '''
        pass


class BBox:
    '''Class for representing a bounding box. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class BinaryPredicate0D:
    '''Base class for binary predicates working on Interface0D objects. A BinaryPredicate0D is typically an ordering relation between two Interface0D objects. The predicate evaluates a relation between the two Interface0D instances and returns a boolean value (true or false). It is used by invoking the __call__() method. '''

    name = None
    '''The name of the binary 0D predicate. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __call__(self, inter1, inter2):
        '''Must be overload by inherited classes. It evaluates a relation between two Interface0D objects. 

        :param inter1: The first Interface0D object. 
        :type inter1: Interface0D
        :param inter2: The second Interface0D object. 
        :type inter2: Interface0D
        :rtype: bool 
        :return:  True or false. 
        '''
        pass


class BinaryPredicate1D:
    '''Base class for binary predicates working on Interface1D objects. A BinaryPredicate1D is typically an ordering relation between two Interface1D objects. The predicate evaluates a relation between the two Interface1D instances and returns a boolean value (true or false). It is used by invoking the __call__() method. '''

    name = None
    '''The name of the binary 1D predicate. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __call__(self, inter1, inter2):
        '''Must be overload by inherited classes. It evaluates a relation between two Interface1D objects. 

        :param inter1: The first Interface1D object. 
        :type inter1: Interface1D
        :param inter2: The second Interface1D object. 
        :type inter2: Interface1D
        :rtype: bool 
        :return:  True or false. 
        '''
        pass


class Chain:
    '''Class to represent a 1D elements issued from the chaining process. A Chain is the last step before the Stroke and is used in the Splitting and Creation processes. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A Chain object. 
        :type brother: Chain
        '''
        pass

    def __init__(self, id):
        '''Builds a chain from its Id. 

        :param id: An Id object. 
        :type id: Id
        '''
        pass

    def push_viewedge_back(self, viewedge, orientation):
        '''Adds a ViewEdge at the end of the Chain. 

        :param viewedge: The ViewEdge that must be added. 
        :type viewedge: ViewEdge
        :param orientation: The orientation with which the ViewEdge must be processed. 
        :type orientation: bool
        '''
        pass

    def push_viewedge_front(self, viewedge, orientation):
        '''Adds a ViewEdge at the beginning of the Chain. 

        :param viewedge: The ViewEdge that must be added. 
        :type viewedge: ViewEdge
        :param orientation: The orientation with which the ViewEdge must be processed. 
        :type orientation: bool
        '''
        pass


class ChainingIterator:
    '''Base class for chaining iterators. This class is designed to be overloaded in order to describe chaining rules. It makes the description of chaining rules easier. The two main methods that need to overloaded are traverse() and init(). traverse() tells which ViewEdge to follow, among the adjacent ones. If you specify restriction rules (such as “Chain only ViewEdges of the selection”), they will be included in the adjacency iterator (i.e, the adjacent iterator will only stop on “valid” edges). '''

    is_incrementing = None
    '''True if the current iteration is an incrementation. 

    :type:  bool 
    '''

    next_vertex = None
    '''The ViewVertex that is the next crossing. 

    :type:  ViewVertex 
    '''

    object = None
    '''The ViewEdge object currently pointed by this iterator. 

    :type:  ViewEdge 
    '''

    def __init__(self,
                 restrict_to_selection=True,
                 restrict_to_unvisited=True,
                 begin=None,
                 orientation=True):
        '''Builds a Chaining Iterator from the first ViewEdge used for iteration and its orientation. 

        :param restrict_to_selection: Indicates whether to force the chaining to stay within the set of selected ViewEdges or not. 
        :type restrict_to_selection: bool
        :param restrict_to_unvisited: Indicates whether a ViewEdge that has already been chained must be ignored ot not. 
        :type restrict_to_unvisited: bool
        :param begin: The ViewEdge from which to start the chain. 
        :type begin: ViewEdge or None
        :param orientation: The direction to follow to explore the graph. If true, the direction indicated by the first ViewEdge is used. 
        :type orientation: bool
        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: 
        :type brother: ChainingIterator
        '''
        pass

    def init(self):
        '''Initializes the iterator context. This method is called each time a new chain is started. It can be used to reset some history information that you might want to keep. 

        '''
        pass

    def traverse(self, it):
        '''This method iterates over the potential next ViewEdges and returns the one that will be followed next. Returns the next ViewEdge to follow or None when the end of the chain is reached. 

        :param it: The iterator over the ViewEdges adjacent to the end vertex of the current ViewEdge. The adjacency iterator reflects the restriction rules by only iterating over the valid ViewEdges. 
        :type it: AdjacencyIterator
        :rtype: ViewEdge or None 
        :return:  Returns the next ViewEdge to follow, or None if chaining ends. 
        '''
        pass


class Curve:
    '''Base class for curves made of CurvePoints. SVertex is the type of the initial curve vertices. A Chain is a specialization of a Curve. '''

    is_empty = None
    '''True if the Curve doesn’t have any Vertex yet. 

    :type:  bool 
    '''

    segments_size = None
    '''The number of segments in the polyline constituting the Curve. 

    :type:  int 
    '''

    def __init__(self):
        '''Default Constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy Constructor. 

        :param brother: A Curve object. 
        :type brother: Curve
        '''
        pass

    def __init__(self, id):
        '''Builds a Curve from its Id. 

        :param id: An Id object. 
        :type id: Id
        '''
        pass

    def push_vertex_back(self, vertex):
        '''Adds a single vertex at the end of the Curve. 

        :param vertex: A vertex object. 
        :type vertex: SVertex or CurvePoint
        '''
        pass

    def push_vertex_front(self, vertex):
        '''Adds a single vertex at the front of the Curve. 

        :param vertex: A vertex object. 
        :type vertex: SVertex or CurvePoint
        '''
        pass


class CurvePoint:
    '''Class to represent a point of a curve. A CurvePoint can be any point of a 1D curve (it doesn’t have to be a vertex of the curve). Any Interface1D is built upon ViewEdges, themselves built upon FEdges. Therefore, a curve is basically a polyline made of a list of SVertex objects. Thus, a CurvePoint is built by linearly interpolating two SVertex instances. CurvePoint can be used as virtual points while querying 0D information along a curve at a given resolution. '''

    fedge = None
    '''Gets the FEdge for the two SVertices that given CurvePoints consists out of. A shortcut for CurvePoint.first_svertex.get_fedge(CurvePoint.second_svertex). 

    :type:  FEdge 
    '''

    first_svertex = None
    '''The first SVertex upon which the CurvePoint is built. 

    :type:  SVertex 
    '''

    second_svertex = None
    '''The second SVertex upon which the CurvePoint is built. 

    :type:  SVertex 
    '''

    t2d = None
    '''The 2D interpolation parameter. 

    :type:  float 
    '''

    def __init__(self):
        '''Defult constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A CurvePoint object. 
        :type brother: CurvePoint
        '''
        pass

    def __init__(self, first_vertex, second_vertex, t2d):
        '''Builds a CurvePoint from two SVertex objects and an interpolation parameter. 

        :param first_vertex: The first SVertex. 
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex. 
        :type second_vertex: SVertex
        :param t2d: A 2D interpolation parameter used to linearly interpolate first_vertex and second_vertex. 
        :type t2d: float
        '''
        pass

    def __init__(self, first_point, second_point, t2d):
        '''Builds a CurvePoint from two CurvePoint objects and an interpolation parameter. 

        :param first_point: The first CurvePoint. 
        :type first_point: CurvePoint
        :param second_point: The second CurvePoint. 
        :type second_point: CurvePoint
        :param t2d: The 2D interpolation parameter used to linearly interpolate first_point and second_point. 
        :type t2d: float
        '''
        pass


class CurvePointIterator:
    '''Class representing an iterator on a curve. Allows an iterating outside initial vertices. A CurvePoint is instanciated and returned through the .object attribute. '''

    object = None
    '''The CurvePoint object currently pointed by this iterator. 

    :type:  CurvePoint 
    '''

    t = None
    '''The curvilinear abscissa of the current point. 

    :type:  float 
    '''

    u = None
    '''The point parameter at the current point in the stroke (0 <= u <= 1). 

    :type:  float 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A CurvePointIterator object. 
        :type brother: CurvePointIterator
        '''
        pass

    def __init__(self, step=0.0):
        '''Builds a CurvePointIterator object. 

        :param step: A resampling resolution with which the curve is resampled. If zero, no resampling is done (i.e., the iterator iterates over initial vertices). 
        :type step: float
        '''
        pass


class FEdge:
    '''Base Class for feature edges. This FEdge can represent a silhouette, a crease, a ridge/valley, a border or a suggestive contour. For silhouettes, the FEdge is oriented so that the visible face lies on the left of the edge. For borders, the FEdge is oriented so that the face lies on the left of the edge. An FEdge can represent an initial edge of the mesh or runs across a face of the initial mesh depending on the smoothness or sharpness of the mesh. This class is specialized into a smooth and a sharp version since their properties slightly vary from one to the other. '''

    first_svertex = None
    '''The first SVertex constituting this FEdge. 

    :type:  SVertex 
    '''

    id = None
    '''The Id of this FEdge. 

    :type:  Id 
    '''

    is_smooth = None
    '''True if this FEdge is a smooth FEdge. 

    :type:  bool 
    '''

    nature = None
    '''The nature of this FEdge. 

    :type:  Nature 
    '''

    next_fedge = None
    '''The FEdge following this one in the ViewEdge. The value is None if this FEdge is the last of the ViewEdge. 

    :type:  FEdge 
    '''

    previous_fedge = None
    '''The FEdge preceding this one in the ViewEdge. The value is None if this FEdge is the first one of the ViewEdge. 

    :type:  FEdge 
    '''

    second_svertex = None
    '''The second SVertex constituting this FEdge. 

    :type:  SVertex 
    '''

    viewedge = None
    '''The ViewEdge to which this FEdge belongs to. 

    :type:  ViewEdge 
    '''

    def FEdge(self):
        '''Default constructor. 

        '''
        pass

    def FEdge(self, brother):
        '''Copy constructor. 

        :param brother: An FEdge object. 
        :type brother: FEdge
        '''
        pass

    def FEdge(self, first_vertex, second_vertex):
        '''Builds an FEdge going from the first vertex to the second. 

        :param first_vertex: The first SVertex. 
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex. 
        :type second_vertex: SVertex
        '''
        pass


class FEdgeSharp:
    '''Class defining a sharp FEdge. A Sharp FEdge corresponds to an initial edge of the input mesh. It can be a silhouette, a crease or a border. If it is a crease edge, then it is borded by two faces of the mesh. Face a lies on its right whereas Face b lies on its left. If it is a border edge, then it doesn’t have any face on its right, and thus Face a is None. '''

    face_mark_left = None
    '''The face mark of the face lying on the left of the FEdge. 

    :type:  bool 
    '''

    face_mark_right = None
    '''The face mark of the face lying on the right of the FEdge. If this FEdge is a border, it has no face on the right and thus this property is set to false. 

    :type:  bool 
    '''

    material_index_left = None
    '''The index of the material of the face lying on the left of the FEdge. 

    :type:  int 
    '''

    material_index_right = None
    '''The index of the material of the face lying on the right of the FEdge. If this FEdge is a border, it has no Face on its right and therefore no material. 

    :type:  int 
    '''

    material_left = None
    '''The material of the face lying on the left of the FEdge. 

    :type:  Material 
    '''

    material_right = None
    '''The material of the face lying on the right of the FEdge. If this FEdge is a border, it has no Face on its right and therefore no material. 

    :type:  Material 
    '''

    normal_left = None
    '''The normal to the face lying on the left of the FEdge. 

    :type:  mathutils.Vector 
    '''

    normal_right = None
    '''The normal to the face lying on the right of the FEdge. If this FEdge is a border, it has no Face on its right and therefore no normal. 

    :type:  mathutils.Vector 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An FEdgeSharp object. 
        :type brother: FEdgeSharp
        '''
        pass

    def __init__(self, first_vertex, second_vertex):
        '''Builds an FEdgeSharp going from the first vertex to the second. 

        :param first_vertex: The first SVertex object. 
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex object. 
        :type second_vertex: SVertex
        '''
        pass


class FEdgeSmooth:
    '''Class defining a smooth edge. This kind of edge typically runs across a face of the input mesh. It can be a silhouette, a ridge or valley, a suggestive contour. '''

    face_mark = None
    '''The face mark of the face that this FEdge is running across. 

    :type:  bool 
    '''

    material = None
    '''The material of the face that this FEdge is running across. 

    :type:  Material 
    '''

    material_index = None
    '''The index of the material of the face that this FEdge is running across. 

    :type:  int 
    '''

    normal = None
    '''The normal of the face that this FEdge is running across. 

    :type:  mathutils.Vector 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An FEdgeSmooth object. 
        :type brother: FEdgeSmooth
        '''
        pass

    def __init__(self, first_vertex, second_vertex):
        '''Builds an FEdgeSmooth going from the first to the second. 

        :param first_vertex: The first SVertex object. 
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex object. 
        :type second_vertex: SVertex
        '''
        pass


class Id:
    '''Class for representing an object Id. '''

    first = None
    '''The first number constituting the Id. 

    :type:  int 
    '''

    second = None
    '''The second number constituting the Id. 

    :type:  int 
    '''

    def __init__(self, first=0, second=0):
        '''Build the Id from two numbers. 

        :param first: The first number. 
        :type first: int
        :param second: The second number. 
        :type second: int
        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An Id object. 
        :type brother: Id
        '''
        pass


class IntegrationType:
    '''Different integration methods that can be invoked to integrate into a single value the set of values obtained from each 0D element of an 1D element: '''

    pass


class Interface0D:
    '''Base class for any 0D element. '''

    id = None
    '''The Id of this 0D element. 

    :type:  Id 
    '''

    name = None
    '''The string of the name of this 0D element. 

    :type:  str 
    '''

    nature = None
    '''The nature of this 0D element. 

    :type:  Nature 
    '''

    point_2d = None
    '''The 2D point of this 0D element. 

    :type:  mathutils.Vector 
    '''

    point_3d = None
    '''The 3D point of this 0D element. 

    :type:  mathutils.Vector 
    '''

    projected_x = None
    '''The X coordinate of the projected 3D point of this 0D element. 

    :type:  float 
    '''

    projected_y = None
    '''The Y coordinate of the projected 3D point of this 0D element. 

    :type:  float 
    '''

    projected_z = None
    '''The Z coordinate of the projected 3D point of this 0D element. 

    :type:  float 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def get_fedge(self, inter):
        '''Returns the FEdge that lies between this 0D element and the 0D element given as the argument. 

        :param inter: A 0D element. 
        :type inter: Interface0D
        :rtype: FEdge 
        :return:  The FEdge lying between the two 0D elements. 
        '''
        pass


class Interface0DIterator:
    '''Class defining an iterator over Interface0D elements. An instance of this iterator is always obtained from a 1D element. '''

    at_last = None
    '''True if the interator points to the last valid element. For its counterpart (pointing to the first valid element), use it.is_begin. 

    :type:  bool 
    '''

    object = None
    '''The 0D object currently pointed to by this iterator. Note that the object may be an instance of an Interface0D subclass. For example if the iterator has been created from the vertices_begin() method of the Stroke class, the .object property refers to a StrokeVertex object. 

    :type:  Interface0D or one of its subclasses. 
    '''

    t = None
    '''The curvilinear abscissa of the current point. 

    :type:  float 
    '''

    u = None
    '''The point parameter at the current point in the 1D element (0 <= u <= 1). 

    :type:  float 
    '''

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An Interface0DIterator object. 
        :type brother: Interface0DIterator
        '''
        pass

    def __init__(self, it):
        '''Construct a nested Interface0DIterator that can be the argument of a Function0D. 

        :param it: An iterator object to be nested. 
        :type it: SVertexIterator, CurvePointIterator, or StrokeVertexIterator
        '''
        pass


class Interface1D:
    '''Base class for any 1D element. '''

    id = None
    '''The Id of this Interface1D. 

    :type:  Id 
    '''

    length_2d = None
    '''The 2D length of this Interface1D. 

    :type:  float 
    '''

    name = None
    '''The string of the name of the 1D element. 

    :type:  str 
    '''

    nature = None
    '''The nature of this Interface1D. 

    :type:  Nature 
    '''

    time_stamp = None
    '''The time stamp of the 1D element, mainly used for selection. 

    :type:  int 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def points_begin(self, t=0.0):
        '''Returns an iterator over the Interface1D points, pointing to the first point. The difference with vertices_begin() is that here we can iterate over points of the 1D element at a any given sampling. Indeed, for each iteration, a virtual point is created. 

        :param t: A sampling with which we want to iterate over points of this 1D element. 
        :type t: float
        :rtype: Interface0DIterator 
        :return:  An Interface0DIterator pointing to the first point. 
        '''
        pass

    def points_end(self, t=0.0):
        '''Returns an iterator over the Interface1D points, pointing after the last point. The difference with vertices_end() is that here we can iterate over points of the 1D element at a given sampling. Indeed, for each iteration, a virtual point is created. 

        :param t: A sampling with which we want to iterate over points of this 1D element. 
        :type t: float
        :rtype: Interface0DIterator 
        :return:  An Interface0DIterator pointing after the last point. 
        '''
        pass

    def vertices_begin(self):
        '''Returns an iterator over the Interface1D vertices, pointing to the first vertex. 

        :rtype: Interface0DIterator 
        :return:  An Interface0DIterator pointing to the first vertex. 
        '''
        pass

    def vertices_end(self):
        '''Returns an iterator over the Interface1D vertices, pointing after the last vertex. 

        :rtype: Interface0DIterator 
        :return:  An Interface0DIterator pointing after the last vertex. 
        '''
        pass


class Iterator:
    '''Base class to define iterators. '''

    is_begin = None
    '''True if the interator points the first element. 

    :type:  bool 
    '''

    is_end = None
    '''True if the interator points the last element. 

    :type:  bool 
    '''

    name = None
    '''The string of the name of this iterator. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def decrement(self):
        '''Makes the iterator point the previous element. 

        '''
        pass

    def increment(self):
        '''Makes the iterator point the next element. 

        '''
        pass


class Material:
    '''Class defining a material. '''

    ambient = None
    '''RGBA components of the ambient color of the material. 

    :type:  mathutils.Color 
    '''

    diffuse = None
    '''RGBA components of the diffuse color of the material. 

    :type:  mathutils.Vector 
    '''

    emission = None
    '''RGBA components of the emissive color of the material. 

    :type:  mathutils.Color 
    '''

    line = None
    '''RGBA components of the line color of the material. 

    :type:  mathutils.Vector 
    '''

    priority = None
    '''Line color priority of the material. 

    :type:  int 
    '''

    shininess = None
    '''Shininess coefficient of the material. 

    :type:  float 
    '''

    specular = None
    '''RGBA components of the specular color of the material. 

    :type:  mathutils.Vector 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A Material object. 
        :type brother: Material
        '''
        pass

    def __init__(self, line, diffuse, ambient, specular, emission, shininess,
                 priority):
        '''Builds a Material from its line, diffuse, ambient, specular, emissive colors, a shininess coefficient and line color priority. 

        :param line: The line color. 
        :type line: mathutils.Vector, list or tuple of 4 float values
        :param diffuse: The diffuse color. 
        :type diffuse: mathutils.Vector, list or tuple of 4 float values
        :param ambient: The ambient color. 
        :type ambient: mathutils.Vector, list or tuple of 4 float values
        :param specular: The specular color. 
        :type specular: mathutils.Vector, list or tuple of 4 float values
        :param emission: The emissive color. 
        :type emission: mathutils.Vector, list or tuple of 4 float values
        :param shininess: The shininess coefficient. 
        :type shininess: float
        :param priority: The line color priority. 
        :type priority: int
        '''
        pass


class MediumType:
    '''The different blending modes available to similate the interaction media-medium: '''

    pass


class Nature:
    '''Edge natures: '''

    pass


class Noise:
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    def __init__(self, seed=-1):
        '''Builds a Noise object. Seed is an optional argument. The seed value is used as a seed for random number generation if it is equal to or greater than zero; otherwise, time is used as a seed. 

        :param seed: Seed for random number generation. 
        :type seed: int
        '''
        pass

    def smoothNoise1(self, v):
        '''Returns a smooth noise value for a 1D element. 

        :param v: One-dimensional sample point. 
        :type v: float
        :rtype: float 
        :return:  A smooth noise value. 
        '''
        pass

    def smoothNoise2(self, v):
        '''Returns a smooth noise value for a 2D element. 

        :param v: Two-dimensional sample point. 
        :type v: mathutils.Vector, list or tuple of 2 real numbers
        :rtype: float 
        :return:  A smooth noise value. 
        '''
        pass

    def smoothNoise3(self, v):
        '''Returns a smooth noise value for a 3D element. 

        :param v: Three-dimensional sample point. 
        :type v: mathutils.Vector, list or tuple of 3 real numbers
        :rtype: float 
        :return:  A smooth noise value. 
        '''
        pass

    def turbulence1(self, v, freq, amp, oct=4):
        '''Returns a noise value for a 1D element. 

        :param v: One-dimensional sample point. 
        :type v: float
        :param freq: Noise frequency. 
        :type freq: float
        :param amp: Amplitude. 
        :type amp: float
        :param oct: Number of octaves. 
        :type oct: int
        :rtype: float 
        :return:  A noise value. 
        '''
        pass

    def turbulence2(self, v, freq, amp, oct=4):
        '''Returns a noise value for a 2D element. 

        :param v: Two-dimensional sample point. 
        :type v: mathutils.Vector, list or tuple of 2 real numbers
        :param freq: Noise frequency. 
        :type freq: float
        :param amp: Amplitude. 
        :type amp: float
        :param oct: Number of octaves. 
        :type oct: int
        :rtype: float 
        :return:  A noise value. 
        '''
        pass

    def turbulence3(self, v, freq, amp, oct=4):
        '''Returns a noise value for a 3D element. 

        :param v: Three-dimensional sample point. 
        :type v: mathutils.Vector, list or tuple of 3 real numbers
        :param freq: Noise frequency. 
        :type freq: float
        :param amp: Amplitude. 
        :type amp: float
        :param oct: Number of octaves. 
        :type oct: int
        :rtype: float 
        :return:  A noise value. 
        '''
        pass


class NonTVertex:
    '''View vertex for corners, cusps, etc. associated to a single SVertex. Can be associated to 2 or more view edges. '''

    svertex = None
    '''The SVertex on top of which this NonTVertex is built. 

    :type:  SVertex 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, svertex):
        '''Build a NonTVertex from a SVertex. 

        :param svertex: An SVertex object. 
        :type svertex: SVertex
        '''
        pass


class Operators:
    '''Class defining the operators used in a style module. There are five types of operators: Selection, chaining, splitting, sorting and creation. All these operators are user controlled through functors, predicates and shaders that are taken as arguments. '''

    pass


class SShape:
    '''Class to define a feature shape. It is the gathering of feature elements from an identified input shape. '''

    bbox = None
    '''The bounding box of the SShape. 

    :type:  BBox 
    '''

    edges = None
    '''The list of edges constituting this SShape. 

    :type:  List of FEdge objects 
    '''

    id = None
    '''The Id of this SShape. 

    :type:  Id 
    '''

    name = None
    '''The name of the SShape. 

    :type:  str 
    '''

    vertices = None
    '''The list of vertices constituting this SShape. 

    :type:  List of SVertex objects 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An SShape object. 
        :type brother: SShape
        '''
        pass

    def add_edge(self, edge):
        '''Adds an FEdge to the list of FEdges. 

        :param edge: An FEdge object. 
        :type edge: FEdge
        '''
        pass

    def add_vertex(self, vertex):
        '''Adds an SVertex to the list of SVertex of this Shape. The SShape attribute of the SVertex is also set to this SShape. 

        :param vertex: An SVertex object. 
        :type vertex: SVertex
        '''
        pass

    def compute_bbox(self):
        '''Compute the bbox of the SShape. 

        '''
        pass


class SVertex:
    '''Class to define a vertex of the embedding. '''

    curvatures = None
    '''Curvature information expressed in the form of a seven-element tuple (K1, e1, K2, e2, Kr, er, dKr), where K1 and K2 are scalar values representing the first (maximum) and second (minimum) principal curvatures at this SVertex, respectively; e1 and e2 are three-dimensional vectors representing the first and second principal directions, i.e. the directions of the normal plane where the curvature takes its maximum and minimum values, respectively; and Kr, er and dKr are the radial curvature, radial direction, and the derivative of the radial curvature at this SVertex, respectively. 

    :type:  tuple 
    '''

    id = None
    '''The Id of this SVertex. 

    :type:  Id 
    '''

    normals = None
    '''The normals for this Vertex as a list. In a sharp surface, an SVertex has exactly one normal. In a smooth surface, an SVertex can have any number of normals. 

    :type:  list of mathutils.Vector objects 
    '''

    normals_size = None
    '''The number of different normals for this SVertex. 

    :type:  int 
    '''

    point_2d = None
    '''The projected 3D coordinates of the SVertex. 

    :type:  mathutils.Vector 
    '''

    point_3d = None
    '''The 3D coordinates of the SVertex. 

    :type:  mathutils.Vector 
    '''

    viewvertex = None
    '''If this SVertex is also a ViewVertex, this property refers to the ViewVertex, and None otherwise. 

    :type:  ViewVertex 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A SVertex object. 
        :type brother: SVertex
        '''
        pass

    def __init__(self, point_3d, id):
        '''Builds a SVertex from 3D coordinates and an Id. 

        :param point_3d: A three-dimensional vector. 
        :type point_3d: mathutils.Vector
        :param id: An Id object. 
        :type id: Id
        '''
        pass

    def add_fedge(self, fedge):
        '''Add an FEdge to the list of edges emanating from this SVertex. 

        :param fedge: An FEdge. 
        :type fedge: FEdge
        '''
        pass

    def add_normal(self, normal):
        '''Adds a normal to the SVertex’s set of normals. If the same normal is already in the set, nothing changes. 

        :param normal: A three-dimensional vector. 
        :type normal: mathutils.Vector, list or tuple of 3 real numbers
        '''
        pass


class SVertexIterator:
    '''Class representing an iterator over SVertex of a ViewEdge. An instance of an SVertexIterator can be obtained from a ViewEdge by calling verticesBegin() or verticesEnd(). '''

    object = None
    '''The SVertex object currently pointed by this iterator. 

    :type:  SVertex 
    '''

    t = None
    '''The curvilinear abscissa of the current point. 

    :type:  float 
    '''

    u = None
    '''The point parameter at the current point in the 1D element (0 <= u <= 1). 

    :type:  float 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: An SVertexIterator object. 
        :type brother: SVertexIterator
        '''
        pass

    def __init__(self, vertex, begin, previous_edge, next_edge, t):
        '''Build an SVertexIterator that starts iteration from an SVertex object v. 

        :param vertex: The SVertex from which the iterator starts iteration. 
        :type vertex: SVertex
        :param begin: The first SVertex of a ViewEdge. 
        :type begin: SVertex
        :param previous_edge: The previous FEdge coming to vertex. 
        :type previous_edge: FEdge
        :param next_edge: The next FEdge going out from vertex. 
        :type next_edge: FEdge
        :param t: The curvilinear abscissa at vertex. 
        :type t: float
        '''
        pass


class Stroke:
    '''Class to define a stroke. A stroke is made of a set of 2D vertices (StrokeVertex), regularly spaced out. This set of vertices defines the stroke’s backbone geometry. Each of these stroke vertices defines the stroke’s shape and appearance at this vertex position. '''

    id = None
    '''The Id of this Stroke. 

    :type:  Id 
    '''

    length_2d = None
    '''The 2D length of the Stroke. 

    :type:  float 
    '''

    medium_type = None
    '''The MediumType used for this Stroke. 

    :type:  MediumType 
    '''

    texture_id = None
    '''The ID of the texture used to simulate th marks system for this Stroke. 

    :type:  int 
    '''

    tips = None
    '''True if this Stroke uses a texture with tips, and false otherwise. 

    :type:  bool 
    '''

    def Stroke(self):
        '''Default constructor 

        '''
        pass

    def Stroke(self, brother):
        '''Copy constructor 

        '''
        pass

    def compute_sampling(self, n):
        '''Compute the sampling needed to get N vertices. If the specified number of vertices is less than the actual number of vertices, the actual sampling value is returned. (To remove Vertices, use the RemoveVertex() method of this class.) 

        :param n: The number of stroke vertices we eventually want in our Stroke. 
        :type n: int
        :rtype: float 
        :return:  The sampling that must be used in the Resample(float) method. 
        '''
        pass

    def insert_vertex(self, vertex, next):
        '''Inserts the StrokeVertex given as argument into the Stroke before the point specified by next. The length and curvilinear abscissa are updated consequently. 

        :param vertex: The StrokeVertex to insert in the Stroke. 
        :type vertex: StrokeVertex
        :param next: A StrokeVertexIterator pointing to the StrokeVertex before which vertex must be inserted. 
        :type next: StrokeVertexIterator
        '''
        pass

    def remove_all_vertices(self):
        '''Removes all vertices from the Stroke. 

        '''
        pass

    def remove_vertex(self, vertex):
        '''Removes the StrokeVertex given as argument from the Stroke. The length and curvilinear abscissa are updated consequently. 

        :param vertex: the StrokeVertex to remove from the Stroke. 
        :type vertex: StrokeVertex
        '''
        pass

    def resample(self, n):
        '''Resamples the stroke so that it eventually has N points. That means it is going to add N-vertices_size, where vertices_size is the number of points we already have. If vertices_size >= N, no resampling is done. 

        :param n: The number of vertices we eventually want in our stroke. 
        :type n: int
        '''
        pass

    def resample(self, sampling):
        '''Resamples the stroke with a given sampling. If the sampling is smaller than the actual sampling value, no resampling is done. 

        :param sampling: The new sampling value. 
        :type sampling: float
        '''
        pass

    def stroke_vertices_begin(self, t=0.0):
        '''Returns a StrokeVertexIterator pointing on the first StrokeVertex of the Stroke. One can specify a sampling value to resample the Stroke on the fly if needed. 

        :param t: The resampling value with which we want our Stroke to be resampled. If 0 is specified, no resampling is done. 
        :type t: float
        :rtype: StrokeVertexIterator 
        :return:  A StrokeVertexIterator pointing on the first StrokeVertex. 
        '''
        pass

    def stroke_vertices_end(self):
        '''Returns a StrokeVertexIterator pointing after the last StrokeVertex of the Stroke. 

        :rtype: StrokeVertexIterator 
        :return:  A StrokeVertexIterator pointing after the last StrokeVertex. 
        '''
        pass

    def stroke_vertices_size(self):
        '''Returns the number of StrokeVertex constituting the Stroke. 

        :rtype: int 
        :return:  The number of stroke vertices. 
        '''
        pass

    def update_length(self):
        '''Updates the 2D length of the Stroke. 

        '''
        pass


class StrokeAttribute:
    '''Class to define a set of attributes associated with a StrokeVertex. The attribute set stores the color, alpha and thickness values for a Stroke Vertex. '''

    alpha = None
    '''Alpha component of the stroke color. 

    :type:  float 
    '''

    color = None
    '''RGB components of the stroke color. 

    :type:  mathutils.Color 
    '''

    thickness = None
    '''Right and left components of the stroke thickness. The right (left) component is the thickness on the right (left) of the vertex when following the stroke. 

    :type:  mathutils.Vector 
    '''

    visible = None
    '''The visibility flag. True if the StrokeVertex is visible. 

    :type:  bool 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A StrokeAttribute object. 
        :type brother: StrokeAttribute
        '''
        pass

    def __init__(self, red, green, blue, alpha, thickness_right,
                 thickness_left):
        '''Build a stroke vertex attribute from a set of parameters. 

        :param red: Red component of a stroke color. 
        :type red: float
        :param green: Green component of a stroke color. 
        :type green: float
        :param blue: Blue component of a stroke color. 
        :type blue: float
        :param alpha: Alpha component of a stroke color. 
        :type alpha: float
        :param thickness_right: Stroke thickness on the right. 
        :type thickness_right: float
        :param thickness_left: Stroke thickness on the left. 
        :type thickness_left: float
        '''
        pass

    def __init__(self, attribute1, attribute2, t):
        '''Interpolation constructor. Build a StrokeAttribute from two StrokeAttribute objects and an interpolation parameter. 

        :param attribute1: The first StrokeAttribute object. 
        :type attribute1: StrokeAttribute
        :param attribute2: The second StrokeAttribute object. 
        :type attribute2: StrokeAttribute
        :param t: The interpolation parameter (0 <= t <= 1). 
        :type t: float
        '''
        pass

    def get_attribute_real(self, name):
        '''Returns an attribute of float type. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: float 
        :return:  The attribute value. 
        '''
        pass

    def get_attribute_vec2(self, name):
        '''Returns an attribute of two-dimensional vector type. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: mathutils.Vector 
        :return:  The attribute value. 
        '''
        pass

    def get_attribute_vec3(self, name):
        '''Returns an attribute of three-dimensional vector type. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: mathutils.Vector 
        :return:  The attribute value. 
        '''
        pass

    def has_attribute_real(self, name):
        '''Checks whether the attribute name of float type is available. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: bool 
        :return:  True if the attribute is availbale. 
        '''
        pass

    def has_attribute_vec2(self, name):
        '''Checks whether the attribute name of two-dimensional vector type is available. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: bool 
        :return:  True if the attribute is availbale. 
        '''
        pass

    def has_attribute_vec3(self, name):
        '''Checks whether the attribute name of three-dimensional vector type is available. 

        :param name: The name of the attribute. 
        :type name: str
        :rtype: bool 
        :return:  True if the attribute is availbale. 
        '''
        pass

    def set_attribute_real(self, name, value):
        '''Adds a user-defined attribute of float type. If there is no attribute of the given name, it is added. Otherwise, the new value replaces the old one. 

        :param name: The name of the attribute. 
        :type name: str
        :param value: The attribute value. 
        :type value: float
        '''
        pass

    def set_attribute_vec2(self, name, value):
        '''Adds a user-defined attribute of two-dimensional vector type. If there is no attribute of the given name, it is added. Otherwise, the new value replaces the old one. 

        :param name: The name of the attribute. 
        :type name: str
        :param value: The attribute value. 
        :type value: mathutils.Vector, list or tuple of 2 real numbers
        '''
        pass

    def set_attribute_vec3(self, name, value):
        '''Adds a user-defined attribute of three-dimensional vector type. If there is no attribute of the given name, it is added. Otherwise, the new value replaces the old one. 

        :param name: The name of the attribute. 
        :type name: str
        :param value: The attribute value. 
        :type value: mathutils.Vector, list or tuple of 3 real numbers
        '''
        pass


class StrokeShader:
    '''Base class for stroke shaders. Any stroke shader must inherit from this class and overload the shade() method. A StrokeShader is designed to modify stroke attributes such as thickness, color, geometry, texture, blending mode, and so on. The basic way for this operation is to iterate over the stroke vertices of the Stroke and to modify the StrokeAttribute of each vertex. Here is a code example of such an iteration: '''

    name = None
    '''The name of the stroke shader. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def shade(self, stroke):
        '''The shading method. Must be overloaded by inherited classes. 

        :param stroke: A Stroke object. 
        :type stroke: Stroke
        '''
        pass


class StrokeVertex:
    '''Class to define a stroke vertex. '''

    attribute = None
    '''StrokeAttribute for this StrokeVertex. 

    :type:  StrokeAttribute 
    '''

    curvilinear_abscissa = None
    '''Curvilinear abscissa of this StrokeVertex in the Stroke. 

    :type:  float 
    '''

    point = None
    '''2D point coordinates. 

    :type:  mathutils.Vector 
    '''

    stroke_length = None
    '''Stroke length (it is only a value retained by the StrokeVertex, and it won’t change the real stroke length). 

    :type:  float 
    '''

    u = None
    '''Curvilinear abscissa of this StrokeVertex in the Stroke. 

    :type:  float 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A StrokeVertex object. 
        :type brother: StrokeVertex
        '''
        pass

    def __init__(self, first_vertex, second_vertex, t3d):
        '''Build a stroke vertex from 2 stroke vertices and an interpolation parameter. 

        :param first_vertex: The first StrokeVertex. 
        :type first_vertex: StrokeVertex
        :param second_vertex: The second StrokeVertex. 
        :type second_vertex: StrokeVertex
        :param t3d: An interpolation parameter. 
        :type t3d: float
        '''
        pass

    def __init__(self, point):
        '''Build a stroke vertex from a CurvePoint 

        :param point: A CurvePoint object. 
        :type point: CurvePoint
        '''
        pass

    def __init__(self, svertex):
        '''Build a stroke vertex from a SVertex 

        :param svertex: An SVertex object. 
        :type svertex: SVertex
        '''
        pass

    def __init__(self, svertex, attribute):
        '''Build a stroke vertex from an SVertex and a StrokeAttribute object. 

        :param svertex: An SVertex object. 
        :type svertex: SVertex
        :param attribute: A StrokeAttribute object. 
        :type attribute: StrokeAttribute
        '''
        pass


class StrokeVertexIterator:
    '''Class defining an iterator designed to iterate over the StrokeVertex of a Stroke. An instance of a StrokeVertexIterator can be obtained from a Stroke by calling iter(), stroke_vertices_begin() or stroke_vertices_begin(). It is iterating over the same vertices as an Interface0DIterator. The difference resides in the object access: an Interface0DIterator only allows access to an Interface0D while one might need to access the specialized StrokeVertex type. In this case, one should use a StrokeVertexIterator. To call functions of the UnaryFuntion0D type, a StrokeVertexIterator can be converted to an Interface0DIterator by by calling Interface0DIterator(it). '''

    at_last = None
    '''True if the interator points to the last valid element. For its counterpart (pointing to the first valid element), use it.is_begin. 

    :type:  bool 
    '''

    object = None
    '''The StrokeVertex object currently pointed to by this iterator. 

    :type:  StrokeVertex 
    '''

    t = None
    '''The curvilinear abscissa of the current point. 

    :type:  float 
    '''

    u = None
    '''The point parameter at the current point in the stroke (0 <= u <= 1). 

    :type:  float 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A StrokeVertexIterator object. 
        :type brother: StrokeVertexIterator
        '''
        pass

    def decremented(self):
        '''Returns a copy of a decremented StrokeVertexIterator. 

        :rtype: StrokeVertexIterator 
        :return:  A StrokeVertexIterator pointing the previous StrokeVertex. 
        '''
        pass

    def incremented(self):
        '''Returns a copy of an incremented StrokeVertexIterator. 

        :rtype: StrokeVertexIterator 
        :return:  A StrokeVertexIterator pointing the next StrokeVertex. 
        '''
        pass

    def reversed(self):
        '''Returns a StrokeVertexIterator that traverses stroke vertices in the reversed order. 

        :rtype: StrokeVertexIterator 
        :return:  A StrokeVertexIterator traversing stroke vertices backward. 
        '''
        pass


class TVertex:
    '''Class to define a T vertex, i.e. an intersection between two edges. It points towards two SVertex and four ViewEdges. Among the ViewEdges, two are front and the other two are back. Basically a front edge hides part of a back edge. So, among the back edges, one is of invisibility N and the other of invisibility N+1. '''

    back_svertex = None
    '''The SVertex that is further away from the viewpoint. 

    :type:  SVertex 
    '''

    front_svertex = None
    '''The SVertex that is closer to the viewpoint. 

    :type:  SVertex 
    '''

    id = None
    '''The Id of this TVertex. 

    :type:  Id 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def get_mate(self, viewedge):
        '''Returns the mate edge of the ViewEdge given as argument. If the ViewEdge is frontEdgeA, frontEdgeB is returned. If the ViewEdge is frontEdgeB, frontEdgeA is returned. Same for back edges. 

        :param viewedge: A ViewEdge object. 
        :type viewedge: ViewEdge
        :rtype: ViewEdge 
        :return:  The mate edge of the given ViewEdge. 
        '''
        pass

    def get_svertex(self, fedge):
        '''Returns the SVertex (among the 2) belonging to the given FEdge. 

        :param fedge: An FEdge object. 
        :type fedge: FEdge
        :rtype: SVertex 
        :return:  The SVertex belonging to the given FEdge. 
        '''
        pass


class UnaryFunction0D:
    '''Base class for Unary Functions (functors) working on Interface0DIterator. A unary function will be used by invoking __call__() on an Interface0DIterator. In Python, several different subclasses of UnaryFunction0D are used depending on the types of functors’ return values. For example, you would inherit from a UnaryFunction0DDouble if you wish to define a function that returns a double value. Available UnaryFunction0D subclasses are: '''

    name = None
    '''The name of the unary 0D function. 

    :type:  str 
    '''


class UnaryFunction0DDouble:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a float value. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DEdgeNature:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a Nature object. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DFloat:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a float value. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DId:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return an Id object. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DMaterial:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a Material object. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DUnsigned:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return an int value. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DVec2f:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a 2D vector. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DVec3f:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a 3D vector. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DVectorViewShape:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a list of ViewShape objects. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction0DViewShape:
    '''Base class for unary functions (functors) that work on Interface0DIterator and return a ViewShape object. '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass


class UnaryFunction1D:
    '''Base class for Unary Functions (functors) working on Interface1D. A unary function will be used by invoking __call__() on an Interface1D. In Python, several different subclasses of UnaryFunction1D are used depending on the types of functors’ return values. For example, you would inherit from a UnaryFunction1DDouble if you wish to define a function that returns a double value. Available UnaryFunction1D subclasses are: '''

    name = None
    '''The name of the unary 1D function. 

    :type:  str 
    '''


class UnaryFunction1DDouble:
    '''Base class for unary functions (functors) that work on Interface1D and return a float value. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DEdgeNature:
    '''Base class for unary functions (functors) that work on Interface1D and return a Nature object. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DFloat:
    '''Base class for unary functions (functors) that work on Interface1D and return a float value. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DUnsigned:
    '''Base class for unary functions (functors) that work on Interface1D and return an int value. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DVec2f:
    '''Base class for unary functions (functors) that work on Interface1D and return a 2D vector. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DVec3f:
    '''Base class for unary functions (functors) that work on Interface1D and return a 3D vector. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DVectorViewShape:
    '''Base class for unary functions (functors) that work on Interface1D and return a list of ViewShape objects. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryFunction1DVoid:
    '''Base class for unary functions (functors) working on Interface1D. '''

    integration_type = None
    '''The integration method. 

    :type:  IntegrationType 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, integration_type):
        '''Builds a unary 1D function using the integration method given as argument. 

        :param integration_type: An integration method. 
        :type integration_type: IntegrationType
        '''
        pass


class UnaryPredicate0D:
    '''Base class for unary predicates that work on Interface0DIterator. A UnaryPredicate0D is a functor that evaluates a condition on an Interface0DIterator and returns true or false depending on whether this condition is satisfied or not. The UnaryPredicate0D is used by invoking its __call__() method. Any inherited class must overload the __call__() method. '''

    name = None
    '''The name of the unary 0D predicate. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __call__(self, it):
        '''Must be overload by inherited classes. 

        :param it: The Interface0DIterator pointing onto the Interface0D at which we wish to evaluate the predicate. 
        :type it: Interface0DIterator
        :rtype: bool 
        :return:  True if the condition is satisfied, false otherwise. 
        '''
        pass


class UnaryPredicate1D:
    '''Base class for unary predicates that work on Interface1D. A UnaryPredicate1D is a functor that evaluates a condition on a Interface1D and returns true or false depending on whether this condition is satisfied or not. The UnaryPredicate1D is used by invoking its __call__() method. Any inherited class must overload the __call__() method. '''

    name = None
    '''The name of the unary 1D predicate. 

    :type:  str 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __call__(self, inter):
        '''Must be overload by inherited classes. 

        :param inter: The Interface1D on which we wish to evaluate the predicate. 
        :type inter: Interface1D
        :rtype: bool 
        :return:  True if the condition is satisfied, false otherwise. 
        '''
        pass


class ViewEdge:
    '''Class defining a ViewEdge. A ViewEdge in an edge of the image graph. it connects two ViewVertex objects. It is made by connecting a set of FEdges. '''

    chaining_time_stamp = None
    '''The time stamp of this ViewEdge. 

    :type:  int 
    '''

    first_fedge = None
    '''The first FEdge that constitutes this ViewEdge. 

    :type:  FEdge 
    '''

    first_viewvertex = None
    '''The first ViewVertex. 

    :type:  ViewVertex 
    '''

    id = None
    '''The Id of this ViewEdge. 

    :type:  Id 
    '''

    is_closed = None
    '''True if this ViewEdge forms a closed loop. 

    :type:  bool 
    '''

    last_fedge = None
    '''The last FEdge that constitutes this ViewEdge. 

    :type:  FEdge 
    '''

    last_viewvertex = None
    '''The second ViewVertex. 

    :type:  ViewVertex 
    '''

    nature = None
    '''The nature of this ViewEdge. 

    :type:  Nature 
    '''

    occludee = None
    '''The shape that is occluded by the ViewShape to which this ViewEdge belongs to. If no object is occluded, this property is set to None. 

    :type:  ViewShape 
    '''

    qi = None
    '''The quantitative invisibility. 

    :type:  int 
    '''

    viewshape = None
    '''The ViewShape to which this ViewEdge belongs to. 

    :type:  ViewShape 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A ViewEdge object. 
        :type brother: ViewEdge
        '''
        pass

    def update_fedges(self):
        '''Sets Viewedge to this for all embedded fedges. 

        '''
        pass


class ViewEdgeIterator:
    '''Base class for iterators over ViewEdges of the ViewMap Graph. Basically the increment() operator of this class should be able to take the decision of “where” (on which ViewEdge) to go when pointing on a given ViewEdge. '''

    begin = None
    '''The first ViewEdge used for the iteration. 

    :type:  ViewEdge 
    '''

    current_edge = None
    '''The ViewEdge object currently pointed by this iterator. 

    :type:  ViewEdge 
    '''

    object = None
    '''The ViewEdge object currently pointed by this iterator. 

    :type:  ViewEdge 
    '''

    orientation = None
    '''The orientation of the pointed ViewEdge in the iteration. If true, the iterator looks for the next ViewEdge among those ViewEdges that surround the ending ViewVertex of the “begin” ViewEdge. If false, the iterator searches over the ViewEdges surrounding the ending ViewVertex of the “begin” ViewEdge. 

    :type:  bool 
    '''

    def __init__(self, begin=None, orientation=True):
        '''Builds a ViewEdgeIterator from a starting ViewEdge and its orientation. 

        :param begin: The ViewEdge from where to start the iteration. 
        :type begin: ViewEdge or None
        :param orientation: If true, we’ll look for the next ViewEdge among the ViewEdges that surround the ending ViewVertex of begin. If false, we’ll search over the ViewEdges surrounding the ending ViewVertex of begin. 
        :type orientation: bool
        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A ViewEdgeIterator object. 
        :type brother: ViewEdgeIterator
        '''
        pass

    def change_orientation(self):
        '''Changes the current orientation. 

        '''
        pass


class ViewMap:
    '''Class defining the ViewMap. '''

    scene_bbox = None
    '''The 3D bounding box of the scene. 

    :type:  BBox 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def get_closest_fedge(self, x, y):
        '''Gets the FEdge nearest to the 2D point specified as arguments. 

        :param x: X coordinate of a 2D point. 
        :type x: float
        :param y: Y coordinate of a 2D point. 
        :type y: float
        :rtype: FEdge 
        :return:  The FEdge nearest to the specified 2D point. 
        '''
        pass

    def get_closest_viewedge(self, x, y):
        '''Gets the ViewEdge nearest to the 2D point specified as arguments. 

        :param x: X coordinate of a 2D point. 
        :type x: float
        :param y: Y coordinate of a 2D point. 
        :type y: float
        :rtype: ViewEdge 
        :return:  The ViewEdge nearest to the specified 2D point. 
        '''
        pass


class ViewShape:
    '''Class gathering the elements of the ViewMap (i.e., ViewVertex and ViewEdge) that are issued from the same input shape. '''

    edges = None
    '''The list of ViewEdge objects contained in this ViewShape. 

    :type:  List of ViewEdge objects 
    '''

    id = None
    '''The Id of this ViewShape. 

    :type:  Id 
    '''

    library_path = None
    '''The library path of the ViewShape. 

    :type:  str, or None if the ViewShape is not part of a library 
    '''

    name = None
    '''The name of the ViewShape. 

    :type:  str 
    '''

    sshape = None
    '''The SShape on top of which this ViewShape is built. 

    :type:  SShape 
    '''

    vertices = None
    '''The list of ViewVertex objects contained in this ViewShape. 

    :type:  List of ViewVertex objects 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, brother):
        '''Copy constructor. 

        :param brother: A ViewShape object. 
        :type brother: ViewShape
        '''
        pass

    def __init__(self, sshape):
        '''Builds a ViewShape from an SShape. 

        :param sshape: An SShape object. 
        :type sshape: SShape
        '''
        pass

    def add_edge(self, edge):
        '''Adds a ViewEdge to the list of ViewEdge objects. 

        :param edge: A ViewEdge object. 
        :type edge: ViewEdge
        '''
        pass

    def add_vertex(self, vertex):
        '''Adds a ViewVertex to the list of the ViewVertex objects. 

        :param vertex: A ViewVertex object. 
        :type vertex: ViewVertex
        '''
        pass


class ViewVertex:
    '''Class to define a view vertex. A view vertex is a feature vertex corresponding to a point of the image graph, where the characteristics of an edge (e.g., nature and visibility) might change. A ViewVertex can be of two kinds: A TVertex when it corresponds to the intersection between two ViewEdges or a NonTVertex when it corresponds to a vertex of the initial input mesh (it is the case for vertices such as corners for example). Thus, this class can be specialized into two classes, the TVertex class and the NonTVertex class. '''

    nature = None
    '''The nature of this ViewVertex. 

    :type:  Nature 
    '''

    def edges_begin(self):
        '''Returns an iterator over the ViewEdges that goes to or comes from this ViewVertex pointing to the first ViewEdge of the list. The orientedViewEdgeIterator allows to iterate in CCW order over these ViewEdges and to get the orientation for each ViewEdge (incoming/outgoing). 

        :rtype: orientedViewEdgeIterator 
        :return:  An orientedViewEdgeIterator pointing to the first ViewEdge. 
        '''
        pass

    def edges_end(self):
        '''Returns an orientedViewEdgeIterator over the ViewEdges around this ViewVertex, pointing after the last ViewEdge. 

        :rtype: orientedViewEdgeIterator 
        :return:  An orientedViewEdgeIterator pointing after the last ViewEdge. 
        '''
        pass

    def edges_iterator(self, edge):
        '''Returns an orientedViewEdgeIterator pointing to the ViewEdge given as argument. 

        :param edge: A ViewEdge object. 
        :type edge: ViewEdge
        :rtype: orientedViewEdgeIterator 
        :return:  An orientedViewEdgeIterator pointing to the given ViewEdge. 
        '''
        pass


class orientedViewEdgeIterator:
    '''Class representing an iterator over oriented ViewEdges around a ViewVertex. This iterator allows a CCW iteration (in the image plane). An instance of an orientedViewEdgeIterator can only be obtained from a ViewVertex by calling edges_begin() or edges_end(). '''

    object = None
    '''The oriented ViewEdge (i.e., a tuple of the pointed ViewEdge and a boolean value) currently pointed to by this iterator. If the boolean value is true, the ViewEdge is incoming. 

    :type:  (ViewEdge, bool) 
    '''

    def __init__(self):
        '''Default constructor. 

        '''
        pass

    def __init__(self, iBrother):
        '''Copy constructor. 

        :param iBrother: An orientedViewEdgeIterator object. 
        :type iBrother: orientedViewEdgeIterator
        '''
        pass
