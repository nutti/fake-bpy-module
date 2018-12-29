from . import noise
from . import bvhtree
from . import kdtree
from . import geometry
from . import interpolate


class Color:
    '''This object gives access to Colors in Blender. '''

    b = None
    '''Blue color channel. 

    :type:  float 
    '''

    g = None
    '''Green color channel. 

    :type:  float 
    '''

    h = None
    '''HSV Hue component in [0, 1]. 

    :type:  float 
    '''

    hsv = None
    '''HSV Values in [0, 1]. 

    :type:  float triplet 
    '''

    is_frozen = None
    '''True when this object has been frozen (read-only). 

    :type:  boolean 
    '''

    is_wrapped = None
    '''True when this object wraps external data (read-only). 

    :type:  boolean 
    '''

    owner = None
    '''The item this is wrapping or None (read-only). '''

    r = None
    '''Red color channel. 

    :type:  float 
    '''

    s = None
    '''HSV Saturation component in [0, 1]. 

    :type:  float 
    '''

    v = None
    '''HSV Value component in [0, 1]. 

    :type:  float 
    '''

    def copy(self):
        '''Returns a copy of this color. 

        :rtype: Color 
        :return:  A copy of the color. 
        '''
        pass

    def freeze(self):
        '''After this the object can be hashed, used in dictionaries & sets. 

        :return:  An instance of this object. 
        '''
        pass

    def __init__(self, val):
        '''

        '''
        pass


class Euler:
    '''This object gives access to Eulers in Blender. '''

    is_frozen = None
    '''True when this object has been frozen (read-only). 

    :type:  boolean 
    '''

    is_wrapped = None
    '''True when this object wraps external data (read-only). 

    :type:  boolean 
    '''

    order = None
    '''Euler rotation order. 

    :type:  string in [‘XYZ’, ‘XZY’, ‘YXZ’, ‘YZX’, ‘ZXY’, ‘ZYX’] 
    '''

    owner = None
    '''The item this is wrapping or None (read-only). '''

    x = None
    '''Euler axis angle in radians. 

    :type:  float 
    '''

    y = None
    '''Euler axis angle in radians. 

    :type:  float 
    '''

    z = None
    '''Euler axis angle in radians. 

    :type:  float 
    '''

    def copy(self):
        '''Returns a copy of this euler. 

        :rtype: Euler 
        :return:  A copy of the euler. 
        '''
        pass

    def freeze(self):
        '''After this the object can be hashed, used in dictionaries & sets. 

        :return:  An instance of this object. 
        '''
        pass

    def make_compatible(self, other):
        '''Make this euler compatible with another, so interpolating between them works as intended. 

        '''
        pass

    def rotate(self, other):
        '''Rotates the euler by another mathutils value. 

        :param other: rotation component of mathutils value 
        :type other: Euler, Quaternion or Matrix
        '''
        pass

    def rotate_axis(self, axis, angle):
        '''Rotates the euler a certain amount and returning a unique euler rotation (no 720 degree pitches). 

        :param axis: single character in [‘X, ‘Y’, ‘Z’]. 
        :type axis: string
        :param angle: angle in radians. 
        :type angle: float
        '''
        pass

    def to_matrix(self):
        '''Return a matrix representation of the euler. 

        :rtype: Matrix 
        :return:  A 3x3 rotation matrix representation of the euler. 
        '''
        pass

    def to_quaternion(self):
        '''Return a quaternion representation of the euler. 

        :rtype: Quaternion 
        :return:  Quaternion representation of the euler. 
        '''
        pass

    def zero(self):
        '''Set all values to zero. 

        '''
        pass

    def __init__(self, val):
        '''

        '''
        pass


class Matrix:
    '''This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4. '''

    col = None
    '''Access the matrix by columns, 3x3 and 4x4 only, (read-only). 

    :type:  Matrix Access 
    '''

    is_frozen = None
    '''True when this object has been frozen (read-only). 

    :type:  boolean 
    '''

    is_negative = None
    '''True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only). 

    :type:  bool 
    '''

    is_orthogonal = None
    '''True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only). 

    :type:  bool 
    '''

    is_orthogonal_axis_vectors = None
    '''True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only). 

    :type:  bool 
    '''

    is_wrapped = None
    '''True when this object wraps external data (read-only). 

    :type:  boolean 
    '''

    median_scale = None
    '''The average scale applied to each axis (read-only). 

    :type:  float 
    '''

    owner = None
    '''The item this is wrapping or None (read-only). '''

    row = None
    '''Access the matrix by rows (default), (read-only). 

    :type:  Matrix Access 
    '''

    translation = None
    '''The translation component of the matrix. 

    :type:  Vector 
    '''

    def adjugate(self):
        '''Set the matrix to its adjugate. 

        '''
        pass

    def adjugated(self):
        '''Return an adjugated copy of the matrix. 

        :rtype: Matrix 
        :return:  the adjugated matrix. 
        '''
        pass

    def copy(self):
        '''Returns a copy of this matrix. 

        :rtype: Matrix 
        :return:  an instance of itself 
        '''
        pass

    def decompose(self):
        '''Return the translation, rotation, and scale components of this matrix. 

        :rtype: (Vector, Quaternion, Vector) 
        :return:  tuple of translation, rotation, and scale 
        '''
        pass

    def determinant(self):
        '''Return the determinant of a matrix. 

        :rtype: float 
        :return:  Return the determinant of a matrix. 
        '''
        pass

    def freeze(self):
        '''After this the object can be hashed, used in dictionaries & sets. 

        :return:  An instance of this object. 
        '''
        pass

    def identity(self):
        '''Set the matrix to the identity matrix. 

        '''
        pass

    def invert(self, fallback=None):
        '''Set the matrix to its inverse. 

        :param fallback: Set the matrix to this value when the inverse cannot be calculated (instead of raising a ValueError exception). 
        :type fallback: Matrix
        '''
        pass

    def invert_safe(self):
        '''Set the matrix to its inverse, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, set to the identity matrix instead. 

        '''
        pass

    def inverted(self, fallback=None):
        '''Return an inverted copy of the matrix. 

        :param fallback: return this when the inverse can’t be calculated (instead of raising a ValueError). 
        :type fallback: any
        :rtype: Matrix 
        :return:  the inverted matrix or fallback when given. 
        '''
        pass

    def inverted_safe(self):
        '''Return an inverted copy of the matrix, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, return the identity matrix instead. 

        :rtype: Matrix 
        :return:  the inverted matrix. 
        '''
        pass

    def lerp(self, other, factor):
        '''Returns the interpolation of two matrices. Uses polar decomposition, see “Matrix Animation and Polar Decomposition”, Shoemake and Duff, 1992. 

        :param other: value to interpolate with. 
        :type other: Matrix
        :param factor: The interpolation value in [0.0, 1.0]. 
        :type factor: float
        :rtype: Matrix 
        :return:  The interpolated matrix. 
        '''
        pass

    def normalize(self):
        '''Normalize each of the matrix columns. 

        '''
        pass

    def normalized(self):
        '''Return a column normalized matrix 

        :rtype: Matrix 
        :return:  a column normalized matrix 
        '''
        pass

    def resize_4x4(self):
        '''Resize the matrix to 4x4. 

        '''
        pass

    def rotate(self, other):
        '''Rotates the matrix by another mathutils value. 

        :param other: rotation component of mathutils value 
        :type other: Euler, Quaternion or Matrix
        '''
        pass

    def to_3x3(self):
        '''Return a 3x3 copy of this matrix. 

        :rtype: Matrix 
        :return:  a new matrix. 
        '''
        pass

    def to_4x4(self):
        '''Return a 4x4 copy of this matrix. 

        :rtype: Matrix 
        :return:  a new matrix. 
        '''
        pass

    def to_euler(self, order, euler_compat):
        '''Return an Euler representation of the rotation matrix (3x3 or 4x4 matrix only). 

        :param order: Optional rotation order argument in [‘XYZ’, ‘XZY’, ‘YXZ’, ‘YZX’, ‘ZXY’, ‘ZYX’]. 
        :type order: string
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves. 
        :type euler_compat: Euler
        :rtype: Euler 
        :return:  Euler representation of the matrix. 
        '''
        pass

    def to_quaternion(self):
        '''Return a quaternion representation of the rotation matrix. 

        :rtype: Quaternion 
        :return:  Quaternion representation of the rotation matrix. 
        '''
        pass

    def to_scale(self):
        '''Return the scale part of a 3x3 or 4x4 matrix. 

        :rtype: Vector 
        :return:  Return the scale of a matrix. 
        '''
        pass

    def to_translation(self):
        '''Return the translation part of a 4 row matrix. 

        :rtype: Vector 
        :return:  Return the translation of a matrix. 
        '''
        pass

    def transpose(self):
        '''Set the matrix to its transpose. 

        '''
        pass

    def transposed(self):
        '''Return a new, transposed matrix. 

        :rtype: Matrix 
        :return:  a transposed matrix 
        '''
        pass

    def zero(self):
        '''Set all the matrix values to zero. 

        :rtype: Matrix 
        '''
        pass

    def __init__(self, val):
        '''

        '''
        pass


class Quaternion:
    '''The constructor takes arguments in various forms: '''

    angle = None
    '''Angle of the quaternion. 

    :type:  float 
    '''

    axis = None
    '''Quaternion axis as a vector. 

    :type:  Vector 
    '''

    is_frozen = None
    '''True when this object has been frozen (read-only). 

    :type:  boolean 
    '''

    is_wrapped = None
    '''True when this object wraps external data (read-only). 

    :type:  boolean 
    '''

    magnitude = None
    '''Size of the quaternion (read-only). 

    :type:  float 
    '''

    owner = None
    '''The item this is wrapping or None (read-only). '''

    w = None
    '''Quaternion axis value. 

    :type:  float 
    '''

    x = None
    '''Quaternion axis value. 

    :type:  float 
    '''

    y = None
    '''Quaternion axis value. 

    :type:  float 
    '''

    z = None
    '''Quaternion axis value. 

    :type:  float 
    '''

    def conjugate(self):
        '''Set the quaternion to its conjugate (negate x, y, z). 

        '''
        pass

    def conjugated(self):
        '''Return a new conjugated quaternion. 

        :rtype: Quaternion 
        :return:  a new quaternion. 
        '''
        pass

    def copy(self):
        '''Returns a copy of this quaternion. 

        :rtype: Quaternion 
        :return:  A copy of the quaternion. 
        '''
        pass

    def cross(self, other):
        '''Return the cross product of this quaternion and another. 

        :param other: The other quaternion to perform the cross product with. 
        :type other: Quaternion
        :rtype: Quaternion 
        :return:  The cross product. 
        '''
        pass

    def dot(self, other):
        '''Return the dot product of this quaternion and another. 

        :param other: The other quaternion to perform the dot product with. 
        :type other: Quaternion
        :rtype: Quaternion 
        :return:  The dot product. 
        '''
        pass

    def freeze(self):
        '''After this the object can be hashed, used in dictionaries & sets. 

        :return:  An instance of this object. 
        '''
        pass

    def identity(self):
        '''Set the quaternion to an identity quaternion. 

        :rtype: Quaternion 
        '''
        pass

    def invert(self):
        '''Set the quaternion to its inverse. 

        '''
        pass

    def inverted(self):
        '''Return a new, inverted quaternion. 

        :rtype: Quaternion 
        :return:  the inverted value. 
        '''
        pass

    def negate(self):
        '''Set the quaternion to its negative. 

        :rtype: Quaternion 
        '''
        pass

    def normalize(self):
        '''Normalize the quaternion. 

        '''
        pass

    def normalized(self):
        '''Return a new normalized quaternion. 

        :rtype: Quaternion 
        :return:  a normalized copy. 
        '''
        pass

    def rotate(self, other):
        '''Rotates the quaternion by another mathutils value. 

        :param other: rotation component of mathutils value 
        :type other: Euler, Quaternion or Matrix
        '''
        pass

    def rotation_difference(self, other):
        '''Returns a quaternion representing the rotational difference. 

        :param other: second quaternion. 
        :type other: Quaternion
        :rtype: Quaternion 
        :return:  the rotational difference between the two quat rotations. 
        '''
        pass

    def slerp(self, other, factor):
        '''Returns the interpolation of two quaternions. 

        :param other: value to interpolate with. 
        :type other: Quaternion
        :param factor: The interpolation value in [0.0, 1.0]. 
        :type factor: float
        :rtype: Quaternion 
        :return:  The interpolated rotation. 
        '''
        pass

    def to_axis_angle(self):
        '''Return the axis, angle representation of the quaternion. 

        :rtype: (Vector, float) pair 
        :return:  axis, angle. 
        '''
        pass

    def to_euler(self, order, euler_compat):
        '''Return Euler representation of the quaternion. 

        :param order: Optional rotation order argument in [‘XYZ’, ‘XZY’, ‘YXZ’, ‘YZX’, ‘ZXY’, ‘ZYX’]. 
        :type order: string
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves. 
        :type euler_compat: Euler
        :rtype: Euler 
        :return:  Euler representation of the quaternion. 
        '''
        pass

    def to_exponential_map(self):
        '''To convert back to a quaternion, pass it to the Quaternion constructor. 

        :rtype: Vector of size 3 
        :return:  exponential map. 
        '''
        pass

    def to_matrix(self):
        '''Return a matrix representation of the quaternion. 

        :rtype: Matrix 
        :return:  A 3x3 rotation matrix representation of the quaternion. 
        '''
        pass

    def __init__(self, val):
        '''

        '''
        pass


class Vector:
    '''This object gives access to Vectors in Blender. '''

    is_frozen = None
    '''True when this object has been frozen (read-only). 

    :type:  boolean 
    '''

    is_wrapped = None
    '''True when this object wraps external data (read-only). 

    :type:  boolean 
    '''

    length = None
    '''Vector Length. 

    :type:  float 
    '''

    length_squared = None
    '''Vector length squared (v.dot(v)). 

    :type:  float 
    '''

    magnitude = None
    '''Vector Length. 

    :type:  float 
    '''

    owner = None
    '''The item this is wrapping or None (read-only). '''

    w = None
    '''Vector W axis (4D Vectors only). 

    :type:  float 
    '''

    ww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    www = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wwzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wxzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wywx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wywy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wywz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wyzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    wzzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    x = None
    '''Vector X axis. 

    :type:  float 
    '''

    xw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xwzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xxzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xywx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xywy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xywz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xyzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    xzzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    y = None
    '''Vector Y axis. 

    :type:  float 
    '''

    yw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    ywzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yxzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yywx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yywy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yywz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yyzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    yzzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    z = None
    '''Vector Z axis (3D Vectors only). 

    :type:  float 
    '''

    zw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zwzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zxzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zywx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zywy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zywz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zyzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzww = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzwx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzwy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzwz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzxw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzxx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzxy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzxz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzyw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzyx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzyy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzyz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzzw = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzzx = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzzy = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    zzzz = None
    '''Undocumented contribute <https://developer.blender.org/T51061> '''

    def angle(self, other, fallback=None):
        '''Return the angle between two vectors. 

        :param other: another vector to compare the angle with 
        :type other: Vector
        :param fallback: return this when the angle can’t be calculated (zero length vector), (instead of raising a ValueError). 
        :type fallback: any
        :rtype: float 
        :return:  angle in radians or fallback when given 
        '''
        pass

    def angle_signed(self, other, fallback):
        '''Return the signed angle between two 2D vectors (clockwise is positive). 

        :param other: another vector to compare the angle with 
        :type other: Vector
        :param fallback: return this when the angle can’t be calculated (zero length vector), (instead of raising a ValueError). 
        :type fallback: any
        :rtype: float 
        :return:  angle in radians or fallback when given 
        '''
        pass

    def copy(self):
        '''Returns a copy of this vector. 

        :rtype: Vector 
        :return:  A copy of the vector. 
        '''
        pass

    def cross(self, other):
        '''Return the cross product of this vector and another. 

        :param other: The other vector to perform the cross product with. 
        :type other: Vector
        :rtype: Vector or float when 2D vectors are used 
        :return:  The cross product. 
        '''
        pass

    def dot(self, other):
        '''Return the dot product of this vector and another. 

        :param other: The other vector to perform the dot product with. 
        :type other: Vector
        :rtype: Vector 
        :return:  The dot product. 
        '''
        pass

    def freeze(self):
        '''After this the object can be hashed, used in dictionaries & sets. 

        :return:  An instance of this object. 
        '''
        pass

    def lerp(self, other, factor):
        '''Returns the interpolation of two vectors. 

        :param other: value to interpolate with. 
        :type other: Vector
        :param factor: The interpolation value in [0.0, 1.0]. 
        :type factor: float
        :rtype: Vector 
        :return:  The interpolated vector. 
        '''
        pass

    def negate(self):
        '''Set all values to their negative. 

        '''
        pass

    def normalize(self):
        '''Normalize the vector, making the length of the vector always 1.0. 

        '''
        pass

    def normalized(self):
        '''Return a new, normalized vector. 

        :rtype: Vector 
        :return:  a normalized copy of the vector 
        '''
        pass

    def orthogonal(self):
        '''Return a perpendicular vector. 

        :rtype: Vector 
        :return:  a new vector 90 degrees from this vector. 
        '''
        pass

    def project(self, other):
        '''Return the projection of this vector onto the other. 

        :param other: second vector. 
        :type other: Vector
        :rtype: Vector 
        :return:  the parallel projection vector 
        '''
        pass

    def reflect(self, mirror):
        '''Return the reflection vector from the mirror argument. 

        :param mirror: This vector could be a normal from the reflecting surface. 
        :type mirror: Vector
        :rtype: Vector 
        :return:  The reflected vector matching the size of this vector. 
        '''
        pass

    def resize(self, size=3):
        '''Resize the vector to have size number of elements. 

        '''
        pass

    def resize_2d(self):
        '''Resize the vector to 2D (x, y). 

        '''
        pass

    def resize_3d(self):
        '''Resize the vector to 3D (x, y, z). 

        '''
        pass

    def resize_4d(self):
        '''Resize the vector to 4D (x, y, z, w). 

        '''
        pass

    def resized(self, size=3):
        '''Return a resized copy of the vector with size number of elements. 

        :rtype: Vector 
        :return:  a new vector 
        '''
        pass

    def rotate(self, other):
        '''Rotate the vector by a rotation value. 

        :param other: rotation component of mathutils value 
        :type other: Euler, Quaternion or Matrix
        '''
        pass

    def rotation_difference(self, other):
        '''Returns a quaternion representing the rotational difference between this vector and another. 

        :param other: second vector. 
        :type other: Vector
        :rtype: Quaternion 
        :return:  the rotational difference between the two vectors. 
        '''
        pass

    def slerp(self, other, factor, fallback=None):
        '''Returns the interpolation of two non-zero vectors (spherical coordinates). 

        :param other: value to interpolate with. 
        :type other: Vector
        :param factor: The interpolation value typically in [0.0, 1.0]. 
        :type factor: float
        :param fallback: return this when the vector can’t be calculated (zero length vector or direct opposites), (instead of raising a ValueError). 
        :type fallback: any
        :rtype: Vector 
        :return:  The interpolated vector. 
        '''
        pass

    def to_2d(self):
        '''Return a 2d copy of the vector. 

        :rtype: Vector 
        :return:  a new vector 
        '''
        pass

    def to_3d(self):
        '''Return a 3d copy of the vector. 

        :rtype: Vector 
        :return:  a new vector 
        '''
        pass

    def to_4d(self):
        '''Return a 4d copy of the vector. 

        :rtype: Vector 
        :return:  a new vector 
        '''
        pass

    def to_track_quat(self, track, up):
        '''Return a quaternion rotation from the vector and the track and up axis. 

        :param track: Track axis in [‘X’, ‘Y’, ‘Z’, ‘-X’, ‘-Y’, ‘-Z’]. 
        :type track: string
        :param up: Up axis in [‘X’, ‘Y’, ‘Z’]. 
        :type up: string
        :rtype: Quaternion 
        :return:  rotation from the vector and the track and up axis. 
        '''
        pass

    def to_tuple(self, precision=-1):
        '''Return this vector as a tuple with. 

        :param precision: The number to round the value to in [-1, 21]. 
        :type precision: int
        :rtype: tuple 
        :return:  the values of the vector rounded by precision 
        '''
        pass

    def zero(self):
        '''Set all values to zero. 

        '''
        pass

    def __init__(self, val):
        '''

        '''
        pass
