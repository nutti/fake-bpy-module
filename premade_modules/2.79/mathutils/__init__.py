STDPERLIN = None


class Color:
    b = None
    g = None
    h = None
    hsv = None
    is_frozen = None
    is_wrapped = None
    owner = None
    r = None
    s = None
    v = None

    def copy(self):
        pass

    def freeze(self):
        pass

    def __init__(self, val):
        pass



class Euler:
    is_frozen = None
    is_wrapped = None
    order = None
    owner = None
    x = None
    y = None
    z = None

    def copy(self):
        pass

    def freeze(self):
        pass

    def make_compatible(self, other):
        pass

    def rotate(self, other):
        pass

    def rotate_axis(self, axis, angle):
        pass

    def to_matrix(self):
        pass

    def to_quaternion(self):
        pass

    def zero(self):
        pass

    def __init__(self, val):
        pass



class Matrix:
    col = None
    is_frozen = None
    is_negative = None
    is_orthogonal = None
    is_orthogonal_axis_vectors = None
    is_wrapped = None
    median_scale = None
    owner = None
    row = None
    translation = None

    def adjugate(self):
        pass

    def adjugated(self):
        pass

    def copy(self):
        pass

    def decompose(self):
        pass

    def determinant(self):
        pass

    def freeze(self):
        pass

    def identity(self):
        pass

    def invert(self, fallback=None):
        pass

    def invert_safe(self):
        pass

    def inverted(self, fallback=None):
        pass

    def inverted_safe(self):
        pass

    def lerp(self, other, factor):
        pass

    def normalize(self):
        pass

    def normalized(self):
        pass

    def resize_4x4(self):
        pass

    def rotate(self, other):
        pass

    def to_3x3(self):
        pass

    def to_4x4(self):
        pass

    def to_euler(self, order, euler_compat):
        pass

    def to_quaternion(self):
        pass

    def to_scale(self):
        pass

    def to_translation(self):
        pass

    def transpose(self):
        pass

    def transposed(self):
        pass

    def zero(self):
        pass

    def __init__(self, val):
        pass



class Quaternion:
    angle = None
    axis = None
    is_frozen = None
    is_wrapped = None
    magnitude = None
    owner = None
    w = None
    x = None
    y = None
    z = None

    def conjugate(self):
        pass

    def conjugated(self):
        pass

    def copy(self):
        pass

    def cross(self, other):
        pass

    def dot(self, other):
        pass

    def freeze(self):
        pass

    def identity(self):
        pass

    def invert(self):
        pass

    def inverted(self):
        pass

    def negate(self):
        pass

    def normalize(self):
        pass

    def normalized(self):
        pass

    def rotate(self, other):
        pass

    def rotation_difference(self, other):
        pass

    def slerp(self, other, factor):
        pass

    def to_axis_angle(self):
        pass

    def to_euler(self, order, euler_compat):
        pass

    def to_exponential_map(self):
        pass

    def to_matrix(self):
        pass

    def __init__(self, val):
        pass



class Vector:
    is_frozen = None
    is_wrapped = None
    length = None
    length_squared = None
    magnitude = None
    owner = None
    w = None
    ww = None
    www = None
    wwww = None
    wwwx = None
    wwwy = None
    wwwz = None
    wwx = None
    wwxw = None
    wwxx = None
    wwxy = None
    wwxz = None
    wwy = None
    wwyw = None
    wwyx = None
    wwyy = None
    wwyz = None
    wwz = None
    wwzw = None
    wwzx = None
    wwzy = None
    wwzz = None
    wx = None
    wxw = None
    wxww = None
    wxwx = None
    wxwy = None
    wxwz = None
    wxx = None
    wxxw = None
    wxxx = None
    wxxy = None
    wxxz = None
    wxy = None
    wxyw = None
    wxyx = None
    wxyy = None
    wxyz = None
    wxz = None
    wxzw = None
    wxzx = None
    wxzy = None
    wxzz = None
    wy = None
    wyw = None
    wyww = None
    wywx = None
    wywy = None
    wywz = None
    wyx = None
    wyxw = None
    wyxx = None
    wyxy = None
    wyxz = None
    wyy = None
    wyyw = None
    wyyx = None
    wyyy = None
    wyyz = None
    wyz = None
    wyzw = None
    wyzx = None
    wyzy = None
    wyzz = None
    wz = None
    wzw = None
    wzww = None
    wzwx = None
    wzwy = None
    wzwz = None
    wzx = None
    wzxw = None
    wzxx = None
    wzxy = None
    wzxz = None
    wzy = None
    wzyw = None
    wzyx = None
    wzyy = None
    wzyz = None
    wzz = None
    wzzw = None
    wzzx = None
    wzzy = None
    wzzz = None
    x = None
    xw = None
    xww = None
    xwww = None
    xwwx = None
    xwwy = None
    xwwz = None
    xwx = None
    xwxw = None
    xwxx = None
    xwxy = None
    xwxz = None
    xwy = None
    xwyw = None
    xwyx = None
    xwyy = None
    xwyz = None
    xwz = None
    xwzw = None
    xwzx = None
    xwzy = None
    xwzz = None
    xx = None
    xxw = None
    xxww = None
    xxwx = None
    xxwy = None
    xxwz = None
    xxx = None
    xxxw = None
    xxxx = None
    xxxy = None
    xxxz = None
    xxy = None
    xxyw = None
    xxyx = None
    xxyy = None
    xxyz = None
    xxz = None
    xxzw = None
    xxzx = None
    xxzy = None
    xxzz = None
    xy = None
    xyw = None
    xyww = None
    xywx = None
    xywy = None
    xywz = None
    xyx = None
    xyxw = None
    xyxx = None
    xyxy = None
    xyxz = None
    xyy = None
    xyyw = None
    xyyx = None
    xyyy = None
    xyyz = None
    xyz = None
    xyzw = None
    xyzx = None
    xyzy = None
    xyzz = None
    xz = None
    xzw = None
    xzww = None
    xzwx = None
    xzwy = None
    xzwz = None
    xzx = None
    xzxw = None
    xzxx = None
    xzxy = None
    xzxz = None
    xzy = None
    xzyw = None
    xzyx = None
    xzyy = None
    xzyz = None
    xzz = None
    xzzw = None
    xzzx = None
    xzzy = None
    xzzz = None
    y = None
    yw = None
    yww = None
    ywww = None
    ywwx = None
    ywwy = None
    ywwz = None
    ywx = None
    ywxw = None
    ywxx = None
    ywxy = None
    ywxz = None
    ywy = None
    ywyw = None
    ywyx = None
    ywyy = None
    ywyz = None
    ywz = None
    ywzw = None
    ywzx = None
    ywzy = None
    ywzz = None
    yx = None
    yxw = None
    yxww = None
    yxwx = None
    yxwy = None
    yxwz = None
    yxx = None
    yxxw = None
    yxxx = None
    yxxy = None
    yxxz = None
    yxy = None
    yxyw = None
    yxyx = None
    yxyy = None
    yxyz = None
    yxz = None
    yxzw = None
    yxzx = None
    yxzy = None
    yxzz = None
    yy = None
    yyw = None
    yyww = None
    yywx = None
    yywy = None
    yywz = None
    yyx = None
    yyxw = None
    yyxx = None
    yyxy = None
    yyxz = None
    yyy = None
    yyyw = None
    yyyx = None
    yyyy = None
    yyyz = None
    yyz = None
    yyzw = None
    yyzx = None
    yyzy = None
    yyzz = None
    yz = None
    yzw = None
    yzww = None
    yzwx = None
    yzwy = None
    yzwz = None
    yzx = None
    yzxw = None
    yzxx = None
    yzxy = None
    yzxz = None
    yzy = None
    yzyw = None
    yzyx = None
    yzyy = None
    yzyz = None
    yzz = None
    yzzw = None
    yzzx = None
    yzzy = None
    yzzz = None
    z = None
    zw = None
    zww = None
    zwww = None
    zwwx = None
    zwwy = None
    zwwz = None
    zwx = None
    zwxw = None
    zwxx = None
    zwxy = None
    zwxz = None
    zwy = None
    zwyw = None
    zwyx = None
    zwyy = None
    zwyz = None
    zwz = None
    zwzw = None
    zwzx = None
    zwzy = None
    zwzz = None
    zx = None
    zxw = None
    zxww = None
    zxwx = None
    zxwy = None
    zxwz = None
    zxx = None
    zxxw = None
    zxxx = None
    zxxy = None
    zxxz = None
    zxy = None
    zxyw = None
    zxyx = None
    zxyy = None
    zxyz = None
    zxz = None
    zxzw = None
    zxzx = None
    zxzy = None
    zxzz = None
    zy = None
    zyw = None
    zyww = None
    zywx = None
    zywy = None
    zywz = None
    zyx = None
    zyxw = None
    zyxx = None
    zyxy = None
    zyxz = None
    zyy = None
    zyyw = None
    zyyx = None
    zyyy = None
    zyyz = None
    zyz = None
    zyzw = None
    zyzx = None
    zyzy = None
    zyzz = None
    zz = None
    zzw = None
    zzww = None
    zzwx = None
    zzwy = None
    zzwz = None
    zzx = None
    zzxw = None
    zzxx = None
    zzxy = None
    zzxz = None
    zzy = None
    zzyw = None
    zzyx = None
    zzyy = None
    zzyz = None
    zzz = None
    zzzw = None
    zzzx = None
    zzzy = None
    zzzz = None

    def angle(self, other, fallback=None):
        pass

    def angle_signed(self, other, fallback):
        pass

    def copy(self):
        pass

    def cross(self, other):
        pass

    def dot(self, other):
        pass

    def freeze(self):
        pass

    def lerp(self, other, factor):
        pass

    def negate(self):
        pass

    def normalize(self):
        pass

    def normalized(self):
        pass

    def orthogonal(self):
        pass

    def project(self, other):
        pass

    def reflect(self, mirror):
        pass

    def resize(self, size=3):
        pass

    def resize_2d(self):
        pass

    def resize_3d(self):
        pass

    def resize_4d(self):
        pass

    def resized(self, size=3):
        pass

    def rotate(self, other):
        pass

    def rotation_difference(self, other):
        pass

    def slerp(self, other, factor, fallback=None):
        pass

    def to_2d(self):
        pass

    def to_3d(self):
        pass

    def to_4d(self):
        pass

    def to_track_quat(self, track, up):
        pass

    def to_tuple(self, precision=-1):
        pass

    def zero(self):
        pass

    def __init__(self, val):
        pass



