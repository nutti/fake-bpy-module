def glAccum(op, value):
    pass


def glAlphaFunc(func, ref):
    pass


def glAreTexturesResident(n, textures, residences):
    pass


def glBegin(mode):
    pass


def glBindTexture(target, texture):
    pass


def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    pass


def glBlendFunc(sfactor, dfactor):
    pass


def glCallList(list):
    pass


def glCallLists(n, type, lists):
    pass


def glClear(mask):
    pass


def glClearAccum(red, green, blue, alpha):
    pass


def glClearColor(red, green, blue, alpha):
    pass


def glClearDepth(depth):
    pass


def glClearIndex(c):
    pass


def glClearStencil(s):
    pass


def glClipPlane (plane, equation):
    pass


def glColor (red, green, blue, alpha):
    pass


def glColorMask(red, green, blue, alpha):
    pass


def glColorMaterial(face, mode):
    pass


def glCopyPixels(x, y, width, height, type):
    pass


def glCullFace(mode):
    pass


def glDeleteLists(list, range):
    pass


def glDeleteTextures(n, textures):
    pass


def glDepthFunc(func):
    pass


def glDepthMask(flag):
    pass


def glDepthRange(zNear, zFar):
    pass


def glDisable(cap):
    pass


def glDrawBuffer(mode):
    pass


def glDrawPixels(width, height, format, type, pixels):
    pass


def glEdgeFlag (flag):
    pass


def glEnable(cap):
    pass


def glEnd():
    pass


def glEndList():
    pass


def glEvalCoord (u, v):
    pass


def glEvalMesh (mode, i1, i2):
    pass


def glEvalPoint (i, j):
    pass


def glFeedbackBuffer (size, type, buffer):
    pass


def glFinish():
    pass


def glFlush():
    pass


def glFog (pname, param):
    pass


def glFrontFace(mode):
    pass


def glFrustum(left, right, bottom, top, zNear, zFar):
    pass


def glGenLists(range):
    pass


def glGenTextures(n, textures):
    pass


def glGet (pname, param):
    pass


def glGetClipPlane(plane, equation):
    pass


def glGetError():
    pass


def glGetLight (light, pname, params):
    pass


def glGetMap (target, query, v):
    pass


def glGetMaterial (face, pname, params):
    pass


def glGetPixelMap (map, values):
    pass


def glGetPolygonStipple(mask):
    pass


def glGetString(name):
    pass


def glGetTexEnv (target, pname, params):
    pass


def glGetTexGen (coord, pname, params):
    pass


def glGetTexImage(target, level, format, type, pixels):
    pass


def glGetTexLevelParameter (target, level, pname, params):
    pass


def glGetTexParameter (target, pname, params):
    pass


def glHint(target, mode):
    pass


def glIndex(c):
    pass


def glIndexMask(mask):
    pass


def glInitNames():
    pass


def glIsEnabled(cap):
    pass


def glIsList(list):
    pass


def glIsTexture(texture):
    pass


def glLight (light, pname, param):
    pass


def glLightModel (pname, param):
    pass


def glLineStipple(factor, pattern):
    pass


def glLineWidth(width):
    pass


def glListBase(base):
    pass


def glLoadIdentity():
    pass


def glLoadMatrix (m):
    pass


def glLoadName(name):
    pass


def glLogicOp(opcode):
    pass


def glMap1 (target, u1, u2, stride, order, points):
    pass


def glMap2 (target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
    pass


def glMapGrid (un, u1, u2, vn, v1, v2):
    pass


def glMaterial (face, pname, params):
    pass


def glMatrixMode(mode):
    pass


def glMultMatrix (m):
    pass


def glNewList(list, mode):
    pass


def glNormal3 (nx, ny, nz, v):
    pass


def glOrtho(left, right, bottom, top, zNear, zFar):
    pass


def glPassThrough(token):
    pass


def glPixelMap (map, mapsize, values):
    pass


def glPixelStore (pname, param):
    pass


def glPixelTransfer (pname, param):
    pass


def glPixelZoom(xfactor, yfactor):
    pass


def glPointSize(size):
    pass


def glPolygonMode(face, mode):
    pass


def glPolygonOffset(factor, units):
    pass


def glPolygonStipple(mask):
    pass


def glPopAttrib():
    pass


def glPopClientAttrib():
    pass


def glPopMatrix():
    pass


def glPopName():
    pass


def glPrioritizeTextures(n, textures, priorities):
    pass


def glPushAttrib(mask):
    pass


def glPushClientAttrib(mask):
    pass


def glPushMatrix():
    pass


def glPushName(name):
    pass


def glRasterPos (x, y, z, w):
    pass


def glReadBuffer(mode):
    pass


def glReadPixels(x, y, width, height, format, type, pixels):
    pass


def glRect (x1, y1, x2, y2, v1, v2):
    pass


def glRenderMode(mode):
    pass


def glRotate (angle, x, y, z):
    pass


def glScale (x, y, z):
    pass


def glScissor(x, y, width, height):
    pass


def glSelectBuffer(size, buffer):
    pass


def glShadeModel(mode):
    pass


def glStencilFunc(func, ref, mask):
    pass


def glStencilMask(mask):
    pass


def glStencilOp(fail, zfail, zpass):
    pass


def glTexCoord (s, t, r, q, v):
    pass


def glTexEnv  (target, pname, param):
    pass


def glTexGen (coord, pname, param):
    pass


def glTexImage1D(target, level, internalformat, width, border, format, type, pixels):
    pass


def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
    pass


def glTexParameter (target, pname, param):
    pass


def glTranslate (x, y, z):
    pass


def glVertex (x, y, z, w, v):
    pass


def glViewport(x, y, width, height):
    pass


def gluPerspective(fovY, aspect, zNear, zFar):
    pass


def gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz):
    pass


def gluOrtho2D(left, right, bottom, top):
    pass


def gluPickMatrix(x, y, width, height, viewport):
    pass


def gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport, winx, winy, winz):
    pass


def gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport, objx, objy, objz):
    pass


def glUseProgram(program):
    pass


def glValidateProgram(program):
    pass


def glLinkProgram(program):
    pass


def glActiveTexture(texture):
    pass


def glAttachShader(program, shader):
    pass


def glCompileShader(shader):
    pass


def glCreateProgram():
    pass


def glCreateShader(shaderType):
    pass


def glDeleteProgram(program):
    pass


def glDeleteShader(shader):
    pass


def glDetachShader(program, shader):
    pass


def glGetAttachedShaders(program, maxCount, count, shaders):
    pass


def glGetProgramInfoLog(program, maxLength, length, infoLog):
    pass


def glGetShaderInfoLog(program, maxLength, length, infoLog):
    pass


def glGetProgramiv(program, pname, params):
    pass


def glIsShader(shader):
    pass


def glIsProgram(program):
    pass


def glGetShaderSource(shader, bufSize, length, source):
    pass


def glShaderSource(shader, shader_string):
    pass


class Buffer:
    dimensions = None

    def to_list(self):
        pass

    def __init__(self, type, dimensions, template=None):
        pass



