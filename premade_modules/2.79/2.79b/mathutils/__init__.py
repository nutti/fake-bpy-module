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
        :return:  A 3x3 roation matrix representation of the euler. 
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
    '''Access the matix by colums, 3x3 and 4x4 only, (read-only). 

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
    '''Access the matix by rows (default), (read-only). 

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
        '''Return the translation, rotation and scale components of this matrix. 

        :rtype: (Vector, Quaternion, Vector) 
        :return:  trans, rot, scale triple. 
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
        '''Returns the interpolation of two matrices. 

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
    '''Undocumented '''

    www = None
    '''Undocumented '''

    wwww = None
    '''Undocumented '''

    wwwx = None
    '''Undocumented '''

    wwwy = None
    '''Undocumented '''

    wwwz = None
    '''Undocumented '''

    wwx = None
    '''Undocumented '''

    wwxw = None
    '''Undocumented '''

    wwxx = None
    '''Undocumented '''

    wwxy = None
    '''Undocumented '''

    wwxz = None
    '''Undocumented '''

    wwy = None
    '''Undocumented '''

    wwyw = None
    '''Undocumented '''

    wwyx = None
    '''Undocumented '''

    wwyy = None
    '''Undocumented '''

    wwyz = None
    '''Undocumented '''

    wwz = None
    '''Undocumented '''

    wwzw = None
    '''Undocumented '''

    wwzx = None
    '''Undocumented '''

    wwzy = None
    '''Undocumented '''

    wwzz = None
    '''Undocumented '''

    wx = None
    '''Undocumented '''

    wxw = None
    '''Undocumented '''

    wxww = None
    '''Undocumented '''

    wxwx = None
    '''Undocumented '''

    wxwy = None
    '''Undocumented '''

    wxwz = None
    '''Undocumented '''

    wxx = None
    '''Undocumented '''

    wxxw = None
    '''Undocumented '''

    wxxx = None
    '''Undocumented '''

    wxxy = None
    '''Undocumented '''

    wxxz = None
    '''Undocumented '''

    wxy = None
    '''Undocumented '''

    wxyw = None
    '''Undocumented '''

    wxyx = None
    '''Undocumented '''

    wxyy = None
    '''Undocumented '''

    wxyz = None
    '''Undocumented '''

    wxz = None
    '''Undocumented '''

    wxzw = None
    '''Undocumented '''

    wxzx = None
    '''Undocumented '''

    wxzy = None
    '''Undocumented '''

    wxzz = None
    '''Undocumented '''

    wy = None
    '''Undocumented '''

    wyw = None
    '''Undocumented '''

    wyww = None
    '''Undocumented '''

    wywx = None
    '''Undocumented '''

    wywy = None
    '''Undocumented '''

    wywz = None
    '''Undocumented '''

    wyx = None
    '''Undocumented '''

    wyxw = None
    '''Undocumented '''

    wyxx = None
    '''Undocumented '''

    wyxy = None
    '''Undocumented '''

    wyxz = None
    '''Undocumented '''

    wyy = None
    '''Undocumented '''

    wyyw = None
    '''Undocumented '''

    wyyx = None
    '''Undocumented '''

    wyyy = None
    '''Undocumented '''

    wyyz = None
    '''Undocumented '''

    wyz = None
    '''Undocumented '''

    wyzw = None
    '''Undocumented '''

    wyzx = None
    '''Undocumented '''

    wyzy = None
    '''Undocumented '''

    wyzz = None
    '''Undocumented '''

    wz = None
    '''Undocumented '''

    wzw = None
    '''Undocumented '''

    wzww = None
    '''Undocumented '''

    wzwx = None
    '''Undocumented '''

    wzwy = None
    '''Undocumented '''

    wzwz = None
    '''Undocumented '''

    wzx = None
    '''Undocumented '''

    wzxw = None
    '''Undocumented '''

    wzxx = None
    '''Undocumented '''

    wzxy = None
    '''Undocumented '''

    wzxz = None
    '''Undocumented '''

    wzy = None
    '''Undocumented '''

    wzyw = None
    '''Undocumented '''

    wzyx = None
    '''Undocumented '''

    wzyy = None
    '''Undocumented '''

    wzyz = None
    '''Undocumented '''

    wzz = None
    '''Undocumented '''

    wzzw = None
    '''Undocumented '''

    wzzx = None
    '''Undocumented '''

    wzzy = None
    '''Undocumented '''

    wzzz = None
    '''Undocumented '''

    x = None
    '''Vector X axis. 

    :type:  float 
    '''

    xw = None
    '''Undocumented '''

    xww = None
    '''Undocumented '''

    xwww = None
    '''Undocumented '''

    xwwx = None
    '''Undocumented '''

    xwwy = None
    '''Undocumented '''

    xwwz = None
    '''Undocumented '''

    xwx = None
    '''Undocumented '''

    xwxw = None
    '''Undocumented '''

    xwxx = None
    '''Undocumented '''

    xwxy = None
    '''Undocumented '''

    xwxz = None
    '''Undocumented '''

    xwy = None
    '''Undocumented '''

    xwyw = None
    '''Undocumented '''

    xwyx = None
    '''Undocumented '''

    xwyy = None
    '''Undocumented '''

    xwyz = None
    '''Undocumented '''

    xwz = None
    '''Undocumented '''

    xwzw = None
    '''Undocumented '''

    xwzx = None
    '''Undocumented '''

    xwzy = None
    '''Undocumented '''

    xwzz = None
    '''Undocumented '''

    xx = None
    '''Undocumented '''

    xxw = None
    '''Undocumented '''

    xxww = None
    '''Undocumented '''

    xxwx = None
    '''Undocumented '''

    xxwy = None
    '''Undocumented '''

    xxwz = None
    '''Undocumented '''

    xxx = None
    '''Undocumented '''

    xxxw = None
    '''Undocumented '''

    xxxx = None
    '''Undocumented '''

    xxxy = None
    '''Undocumented '''

    xxxz = None
    '''Undocumented '''

    xxy = None
    '''Undocumented '''

    xxyw = None
    '''Undocumented '''

    xxyx = None
    '''Undocumented '''

    xxyy = None
    '''Undocumented '''

    xxyz = None
    '''Undocumented '''

    xxz = None
    '''Undocumented '''

    xxzw = None
    '''Undocumented '''

    xxzx = None
    '''Undocumented '''

    xxzy = None
    '''Undocumented '''

    xxzz = None
    '''Undocumented '''

    xy = None
    '''Undocumented '''

    xyw = None
    '''Undocumented '''

    xyww = None
    '''Undocumented '''

    xywx = None
    '''Undocumented '''

    xywy = None
    '''Undocumented '''

    xywz = None
    '''Undocumented '''

    xyx = None
    '''Undocumented '''

    xyxw = None
    '''Undocumented '''

    xyxx = None
    '''Undocumented '''

    xyxy = None
    '''Undocumented '''

    xyxz = None
    '''Undocumented '''

    xyy = None
    '''Undocumented '''

    xyyw = None
    '''Undocumented '''

    xyyx = None
    '''Undocumented '''

    xyyy = None
    '''Undocumented '''

    xyyz = None
    '''Undocumented '''

    xyz = None
    '''Undocumented '''

    xyzw = None
    '''Undocumented '''

    xyzx = None
    '''Undocumented '''

    xyzy = None
    '''Undocumented '''

    xyzz = None
    '''Undocumented '''

    xz = None
    '''Undocumented '''

    xzw = None
    '''Undocumented '''

    xzww = None
    '''Undocumented '''

    xzwx = None
    '''Undocumented '''

    xzwy = None
    '''Undocumented '''

    xzwz = None
    '''Undocumented '''

    xzx = None
    '''Undocumented '''

    xzxw = None
    '''Undocumented '''

    xzxx = None
    '''Undocumented '''

    xzxy = None
    '''Undocumented '''

    xzxz = None
    '''Undocumented '''

    xzy = None
    '''Undocumented '''

    xzyw = None
    '''Undocumented '''

    xzyx = None
    '''Undocumented '''

    xzyy = None
    '''Undocumented '''

    xzyz = None
    '''Undocumented '''

    xzz = None
    '''Undocumented '''

    xzzw = None
    '''Undocumented '''

    xzzx = None
    '''Undocumented '''

    xzzy = None
    '''Undocumented '''

    xzzz = None
    '''Undocumented '''

    y = None
    '''Vector Y axis. 

    :type:  float 
    '''

    yw = None
    '''Undocumented '''

    yww = None
    '''Undocumented '''

    ywww = None
    '''Undocumented '''

    ywwx = None
    '''Undocumented '''

    ywwy = None
    '''Undocumented '''

    ywwz = None
    '''Undocumented '''

    ywx = None
    '''Undocumented '''

    ywxw = None
    '''Undocumented '''

    ywxx = None
    '''Undocumented '''

    ywxy = None
    '''Undocumented '''

    ywxz = None
    '''Undocumented '''

    ywy = None
    '''Undocumented '''

    ywyw = None
    '''Undocumented '''

    ywyx = None
    '''Undocumented '''

    ywyy = None
    '''Undocumented '''

    ywyz = None
    '''Undocumented '''

    ywz = None
    '''Undocumented '''

    ywzw = None
    '''Undocumented '''

    ywzx = None
    '''Undocumented '''

    ywzy = None
    '''Undocumented '''

    ywzz = None
    '''Undocumented '''

    yx = None
    '''Undocumented '''

    yxw = None
    '''Undocumented '''

    yxww = None
    '''Undocumented '''

    yxwx = None
    '''Undocumented '''

    yxwy = None
    '''Undocumented '''

    yxwz = None
    '''Undocumented '''

    yxx = None
    '''Undocumented '''

    yxxw = None
    '''Undocumented '''

    yxxx = None
    '''Undocumented '''

    yxxy = None
    '''Undocumented '''

    yxxz = None
    '''Undocumented '''

    yxy = None
    '''Undocumented '''

    yxyw = None
    '''Undocumented '''

    yxyx = None
    '''Undocumented '''

    yxyy = None
    '''Undocumented '''

    yxyz = None
    '''Undocumented '''

    yxz = None
    '''Undocumented '''

    yxzw = None
    '''Undocumented '''

    yxzx = None
    '''Undocumented '''

    yxzy = None
    '''Undocumented '''

    yxzz = None
    '''Undocumented '''

    yy = None
    '''Undocumented '''

    yyw = None
    '''Undocumented '''

    yyww = None
    '''Undocumented '''

    yywx = None
    '''Undocumented '''

    yywy = None
    '''Undocumented '''

    yywz = None
    '''Undocumented '''

    yyx = None
    '''Undocumented '''

    yyxw = None
    '''Undocumented '''

    yyxx = None
    '''Undocumented '''

    yyxy = None
    '''Undocumented '''

    yyxz = None
    '''Undocumented '''

    yyy = None
    '''Undocumented '''

    yyyw = None
    '''Undocumented '''

    yyyx = None
    '''Undocumented '''

    yyyy = None
    '''Undocumented '''

    yyyz = None
    '''Undocumented '''

    yyz = None
    '''Undocumented '''

    yyzw = None
    '''Undocumented '''

    yyzx = None
    '''Undocumented '''

    yyzy = None
    '''Undocumented '''

    yyzz = None
    '''Undocumented '''

    yz = None
    '''Undocumented '''

    yzw = None
    '''Undocumented '''

    yzww = None
    '''Undocumented '''

    yzwx = None
    '''Undocumented '''

    yzwy = None
    '''Undocumented '''

    yzwz = None
    '''Undocumented '''

    yzx = None
    '''Undocumented '''

    yzxw = None
    '''Undocumented '''

    yzxx = None
    '''Undocumented '''

    yzxy = None
    '''Undocumented '''

    yzxz = None
    '''Undocumented '''

    yzy = None
    '''Undocumented '''

    yzyw = None
    '''Undocumented '''

    yzyx = None
    '''Undocumented '''

    yzyy = None
    '''Undocumented '''

    yzyz = None
    '''Undocumented '''

    yzz = None
    '''Undocumented '''

    yzzw = None
    '''Undocumented '''

    yzzx = None
    '''Undocumented '''

    yzzy = None
    '''Undocumented '''

    yzzz = None
    '''Undocumented '''

    z = None
    '''Vector Z axis (3D Vectors only). 

    :type:  float 
    '''

    zw = None
    '''Undocumented '''

    zww = None
    '''Undocumented '''

    zwww = None
    '''Undocumented '''

    zwwx = None
    '''Undocumented '''

    zwwy = None
    '''Undocumented '''

    zwwz = None
    '''Undocumented '''

    zwx = None
    '''Undocumented '''

    zwxw = None
    '''Undocumented '''

    zwxx = None
    '''Undocumented '''

    zwxy = None
    '''Undocumented '''

    zwxz = None
    '''Undocumented '''

    zwy = None
    '''Undocumented '''

    zwyw = None
    '''Undocumented '''

    zwyx = None
    '''Undocumented '''

    zwyy = None
    '''Undocumented '''

    zwyz = None
    '''Undocumented '''

    zwz = None
    '''Undocumented '''

    zwzw = None
    '''Undocumented '''

    zwzx = None
    '''Undocumented '''

    zwzy = None
    '''Undocumented '''

    zwzz = None
    '''Undocumented '''

    zx = None
    '''Undocumented '''

    zxw = None
    '''Undocumented '''

    zxww = None
    '''Undocumented '''

    zxwx = None
    '''Undocumented '''

    zxwy = None
    '''Undocumented '''

    zxwz = None
    '''Undocumented '''

    zxx = None
    '''Undocumented '''

    zxxw = None
    '''Undocumented '''

    zxxx = None
    '''Undocumented '''

    zxxy = None
    '''Undocumented '''

    zxxz = None
    '''Undocumented '''

    zxy = None
    '''Undocumented '''

    zxyw = None
    '''Undocumented '''

    zxyx = None
    '''Undocumented '''

    zxyy = None
    '''Undocumented '''

    zxyz = None
    '''Undocumented '''

    zxz = None
    '''Undocumented '''

    zxzw = None
    '''Undocumented '''

    zxzx = None
    '''Undocumented '''

    zxzy = None
    '''Undocumented '''

    zxzz = None
    '''Undocumented '''

    zy = None
    '''Undocumented '''

    zyw = None
    '''Undocumented '''

    zyww = None
    '''Undocumented '''

    zywx = None
    '''Undocumented '''

    zywy = None
    '''Undocumented '''

    zywz = None
    '''Undocumented '''

    zyx = None
    '''Undocumented '''

    zyxw = None
    '''Undocumented '''

    zyxx = None
    '''Undocumented '''

    zyxy = None
    '''Undocumented '''

    zyxz = None
    '''Undocumented '''

    zyy = None
    '''Undocumented '''

    zyyw = None
    '''Undocumented '''

    zyyx = None
    '''Undocumented '''

    zyyy = None
    '''Undocumented '''

    zyyz = None
    '''Undocumented '''

    zyz = None
    '''Undocumented '''

    zyzw = None
    '''Undocumented '''

    zyzx = None
    '''Undocumented '''

    zyzy = None
    '''Undocumented '''

    zyzz = None
    '''Undocumented '''

    zz = None
    '''Undocumented '''

    zzw = None
    '''Undocumented '''

    zzww = None
    '''Undocumented '''

    zzwx = None
    '''Undocumented '''

    zzwy = None
    '''Undocumented '''

    zzwz = None
    '''Undocumented '''

    zzx = None
    '''Undocumented '''

    zzxw = None
    '''Undocumented '''

    zzxx = None
    '''Undocumented '''

    zzxy = None
    '''Undocumented '''

    zzxz = None
    '''Undocumented '''

    zzy = None
    '''Undocumented '''

    zzyw = None
    '''Undocumented '''

    zzyx = None
    '''Undocumented '''

    zzyy = None
    '''Undocumented '''

    zzyz = None
    '''Undocumented '''

    zzz = None
    '''Undocumented '''

    zzzw = None
    '''Undocumented '''

    zzzx = None
    '''Undocumented '''

    zzzy = None
    '''Undocumented '''

    zzzz = None
    '''Undocumented '''

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
