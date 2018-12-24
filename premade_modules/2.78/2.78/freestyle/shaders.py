class BackboneStretcherShader:
    '''[Geometry shader] '''

    def __init__(self, amount=2.0):
        '''Builds a BackboneStretcherShader object. 

        :param amount: The stretching amount value. 
        :type amount: float
        '''
        pass

    def shade(self, stroke):
        '''Stretches the stroke at its two extremities and following the respective directions: v(1)v(0) and v(n-1)v(n). 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class BezierCurveShader:
    '''[Geometry shader] '''

    def __init__(self, error=4.0):
        '''Builds a BezierCurveShader object. 

        :param error: The error we’re allowing for the approximation. This error is the max distance allowed between the new curve and the original geometry. 
        :type error: float
        '''
        pass

    def shade(self, stroke):
        '''Transforms the stroke backbone geometry so that it corresponds to a Bezier Curve approximation of the original backbone geometry. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class BlenderTextureShader:
    '''[Texture shader] '''

    def __init__(self, texture):
        '''Builds a BlenderTextureShader object. 

        :param texture: A line style texture slot or a shader node tree to define a set of textures. 
        :type texture: bpy.types.LineStyleTextureSlot or bpy.types.ShaderNodeTree
        '''
        pass

    def shade(self, stroke):
        '''Assigns a blender texture slot to the stroke shading in order to simulate marks. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class CalligraphicShader:
    '''[Thickness Shader] '''

    def __init__(self, thickness_min, thickness_max, orientation, clamp):
        '''Builds a CalligraphicShader object. 

        :param thickness_min: The minimum thickness in the direction perpendicular to the main direction. 
        :type thickness_min: float
        :param thickness_max: The maximum thickness in the main direction. 
        :type thickness_max: float
        :param orientation: The 2D vector giving the main direction. 
        :type orientation: mathutils.Vector
        :param clamp: If true, the strokes are drawn in black when the stroke direction is between -90 and 90 degrees with respect to the main direction and drawn in white otherwise. If false, the strokes are always drawn in black. 
        :type clamp: bool
        '''
        pass

    def shade(self, stroke):
        '''Assigns thicknesses to the stroke vertices so that the stroke looks like made with a calligraphic tool, i.e. the stroke will be the thickest in a main direction, and the thinest in the direction perpendicular to this one, and an interpolation inbetween. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class ColorNoiseShader:
    '''[Color shader] '''

    def __init__(self, amplitude, period):
        '''Builds a ColorNoiseShader object. 

        :param amplitude: The amplitude of the noise signal. 
        :type amplitude: float
        :param period: The period of the noise signal. 
        :type period: float
        '''
        pass

    def shade(self, stroke):
        '''Shader to add noise to the stroke colors. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class ConstantColorShader:
    '''[Color shader] '''

    def __init__(self, red, green, blue, alpha=1.0):
        '''Builds a ConstantColorShader object. 

        :param red: The red component. 
        :type red: float
        :param green: The green component. 
        :type green: float
        :param blue: The blue component. 
        :type blue: float
        :param alpha: The alpha value. 
        :type alpha: float
        '''
        pass

    def shade(self, stroke):
        '''Assigns a constant color to every vertex of the Stroke. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class ConstantThicknessShader:
    '''[Thickness shader] '''

    def __init__(self, thickness):
        '''Builds a ConstantThicknessShader object. 

        :param thickness: The thickness that must be assigned to the stroke. 
        :type thickness: float
        '''
        pass

    def shade(self, stroke):
        '''Assigns an absolute constant thickness to every vertex of the Stroke. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class ConstrainedIncreasingThicknessShader:
    '''[Thickness shader] '''

    def __init__(self, thickness_min, thickness_max, ratio):
        '''Builds a ConstrainedIncreasingThicknessShader object. 

        :param thickness_min: The minimum thickness. 
        :type thickness_min: float
        :param thickness_max: The maximum thickness. 
        :type thickness_max: float
        :param ratio: The thickness/length ratio that we don’t want to exceed. 
        :type ratio: float
        '''
        pass

    def shade(self, stroke):
        '''Same as the IncreasingThicknessShader, but here we allow the user to control the thickness/length ratio so that we don’t get fat short lines. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class GuidingLinesShader:
    '''[Geometry shader] '''

    def __init__(self, offset):
        '''Builds a GuidingLinesShader object. 

        :param offset: The line that replaces the stroke is initially in the middle of the initial stroke bounding box. offset is the value of the displacement which is applied to this line along its normal. 
        :type offset: float
        '''
        pass

    def shade(self, stroke):
        '''Shader to modify the Stroke geometry so that it corresponds to its main direction line. This shader must be used together with the splitting operator using the curvature criterion. Indeed, the precision of the approximation will depend on the size of the stroke’s pieces. The bigger the pieces are, the rougher the approximation is. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class IncreasingColorShader:
    '''[Color shader] '''

    def __init__(self, red_min, green_min, blue_min, alpha_min, red_max,
                 green_max, blue_max, alpha_max):
        '''Builds an IncreasingColorShader object. 

        :param red_min: The first color red component. 
        :type red_min: float
        :param green_min: The first color green component. 
        :type green_min: float
        :param blue_min: The first color blue component. 
        :type blue_min: float
        :param alpha_min: The first color alpha value. 
        :type alpha_min: float
        :param red_max: The second color red component. 
        :type red_max: float
        :param green_max: The second color green component. 
        :type green_max: float
        :param blue_max: The second color blue component. 
        :type blue_max: float
        :param alpha_max: The second color alpha value. 
        :type alpha_max: float
        '''
        pass

    def shade(self, stroke):
        '''Assigns a varying color to the stroke. The user specifies two colors A and B. The stroke color will change linearly from A to B between the first and the last vertex. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class IncreasingThicknessShader:
    '''[Thickness shader] '''

    def __init__(self, thickness_A, thickness_B):
        '''Builds an IncreasingThicknessShader object. 

        :param thickness_A: The first thickness value. 
        :type thickness_A: float
        :param thickness_B: The second thickness value. 
        :type thickness_B: float
        '''
        pass

    def shade(self, stroke):
        '''Assigns thicknesses values such as the thickness increases from a thickness value A to a thickness value B between the first vertex to the midpoint vertex and then decreases from B to a A between this midpoint vertex and the last vertex. The thickness is linearly interpolated from A to B. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class PolygonalizationShader:
    '''[Geometry shader] '''

    def __init__(self, error):
        '''Builds a PolygonalizationShader object. 

        :param error: The error we want our polygonal approximation to have with respect to the original geometry. The smaller, the closer the new stroke is to the orinal one. This error corresponds to the maximum distance between the new stroke and the old one. 
        :type error: float
        '''
        pass

    def shade(self, stroke):
        '''Modifies the Stroke geometry so that it looks more “polygonal”. The basic idea is to start from the minimal stroke approximation consisting in a line joining the first vertex to the last one and to subdivide using the original stroke vertices until a certain error is reached. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class RoundCapShader:
    def round_cap_thickness(self, x):
        '''

        '''
        pass

    def shade(self, stroke):
        '''

        '''
        pass


class SamplingShader:
    '''[Geometry shader] '''

    def __init__(self, sampling):
        '''Builds a SamplingShader object. 

        :param sampling: The sampling to use for the stroke resampling. 
        :type sampling: float
        '''
        pass

    def shade(self, stroke):
        '''Resamples the stroke. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class SmoothingShader:
    '''[Geometry shader] '''

    def __init__(self,
                 num_iterations=100,
                 factor_point=0.1,
                 factor_curvature=0.0,
                 factor_curvature_difference=0.2,
                 aniso_point=0.0,
                 aniso_normal=0.0,
                 aniso_curvature=0.0,
                 carricature_factor=1.0):
        '''Builds a SmoothingShader object. 

        :param num_iterations: The number of iterations. 
        :type num_iterations: int
        :param factor_point: 0.1 
        :type factor_point: float
        :param factor_curvature: 0.0 
        :type factor_curvature: float
        :param factor_curvature_difference: 0.2 
        :type factor_curvature_difference: float
        :param aniso_point: 0.0 
        :type aniso_point: float
        :param aniso_normal: 0.0 
        :type aniso_normal: float
        :param aniso_curvature: 0.0 
        :type aniso_curvature: float
        :param carricature_factor: 1.0 
        :type carricature_factor: float
        '''
        pass

    def shade(self, stroke):
        '''Smoothes the stroke by moving the vertices to make the stroke smoother. Uses curvature flow to converge towards a curve of constant curvature. The diffusion method we use is anisotropic to prevent the diffusion across corners. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class SpatialNoiseShader:
    '''[Geometry shader] '''

    def __init__(self, amount, scale, num_octaves, smooth, pure_random):
        '''Builds a SpatialNoiseShader object. 

        :param amount: The amplitude of the noise. 
        :type amount: float
        :param scale: The noise frequency. 
        :type scale: float
        :param num_octaves: The number of octaves 
        :type num_octaves: int
        :param smooth: True if you want the noise to be smooth. 
        :type smooth: bool
        :param pure_random: True if you don’t want any coherence. 
        :type pure_random: bool
        '''
        pass

    def shade(self, stroke):
        '''Spatial Noise stroke shader. Moves the vertices to make the stroke more noisy. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class SquareCapShader:
    def shade(self, stroke):
        '''

        '''
        pass


class StrokeTextureStepShader:
    '''[Texture shader] '''

    def __init__(self, step):
        '''Builds a StrokeTextureStepShader object. 

        :param step: The spacing along the stroke. 
        :type step: float
        '''
        pass

    def shade(self, stroke):
        '''Assigns a spacing factor to the texture coordinates of the Stroke. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class ThicknessNoiseShader:
    '''[Thickness shader] '''

    def __init__(self, amplitude, period):
        '''Builds a ThicknessNoiseShader object. 

        :param amplitude: The amplitude of the noise signal. 
        :type amplitude: float
        :param period: The period of the noise signal. 
        :type period: float
        '''
        pass

    def shade(self, stroke):
        '''Adds some noise to the stroke thickness. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class TipRemoverShader:
    '''[Geometry shader] '''

    def __init__(self, tip_length):
        '''Builds a TipRemoverShader object. 

        :param tip_length: The length of the piece of stroke we want to remove at each extremity. 
        :type tip_length: float
        '''
        pass

    def shade(self, stroke):
        '''Removes the stroke’s extremities. 

        :param stroke: A Stroke object. 
        :type stroke: freestyle.types.Stroke
        '''
        pass


class py2DCurvatureColorShader:
    '''Assigns a color (greyscale) to the stroke based on the curvature. A higher curvature will yield a brighter color. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyBackboneStretcherNoCuspShader:
    '''Stretches the stroke’s backbone, excluding cusp vertices (end junctions). '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyBackboneStretcherShader:
    '''Stretches the stroke’s backbone by a given length (in pixels). '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyBluePrintCirclesShader:
    '''Draws the silhouette of the object as a circle. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyBluePrintDirectedSquaresShader:
    '''Replaces the stroke with a directed square. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyBluePrintEllipsesShader:
    def shade(self, stroke):
        '''

        '''
        pass


class pyBluePrintSquaresShader:
    def shade(self, stroke):
        '''

        '''
        pass


class pyConstantColorShader:
    '''Assigns a constant color to the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyConstantThicknessShader:
    '''Assigns a constant thickness along the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyConstrainedIncreasingThicknessShader:
    '''Increasingly thickens the stroke, constrained by a ratio of the stroke’s length. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyDecreasingThicknessShader:
    '''Inverse of pyIncreasingThicknessShader, decreasingly thickens the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyDepthDiscontinuityThicknessShader:
    '''Assigns a thickness to the stroke based on the stroke’s distance to the camera (Z-value). '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyDiffusion2Shader:
    '''Iteratively adds an offset to the position of each stroke vertex in the direction perpendicular to the stroke direction at the point. The offset is scaled by the 2D curvature (i.e. how quickly the stroke curve is) at the point. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyFXSVaryingThicknessWithDensityShader:
    '''Assigns thickness to a stroke based on the density of the diffuse map. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyGuidingLineShader:
    def shade(self, stroke):
        '''

        '''
        pass


class pyHLRShader:
    '''Controls visibility based upon the quantitative invisibility (QI) based on hidden line removal (HLR). '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyImportance2DThicknessShader:
    '''Assigns thickness based on distance to a given point in 2D space. the thickness is inverted, so the vertices closest to the specified point have the lowest thickness. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyImportance3DThicknessShader:
    '''Assigns thickness based on distance to a given point in 3D space. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyIncreasingColorShader:
    '''Fades from one color to another along the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyIncreasingThicknessShader:
    '''Increasingly thickens the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyInterpolateColorShader:
    '''Fades from one color to another and back. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyLengthDependingBackboneStretcherShader:
    '''Stretches the stroke’s backbone proportional to the stroke’s length NOTE: you’ll probably want an l somewhere between (0.5 - 0). A value that is too high may yield unexpected results. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyMaterialColorShader:
    '''Assigns the color of the underlying material to the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyModulateAlphaShader:
    '''Limits the stroke’s alpha between a min and max value. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyNonLinearVaryingThicknessShader:
    '''Assigns thickness to a stroke based on an exponential function. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyPerlinNoise1DShader:
    '''Displaces the stroke using the curvilinear abscissa. This means that lines with the same length and sampling interval will be identically distorded. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyPerlinNoise2DShader:
    '''More information on the noise shaders can be found at: freestyleintegration.wordpress.com/2011/09/25/development-updates-on-september-25/ '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyRandomColorShader:
    '''Assigns a color to the stroke based on given seed. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pySLERPThicknessShader:
    '''Assigns thickness to a stroke based on spherical linear interpolation. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pySamplingShader:
    '''Resamples the stroke, which gives the stroke the amount of vertices specified. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pySinusDisplacementShader:
    '''Displaces the stroke in the shape of a sine wave. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyTVertexRemoverShader:
    '''Removes t-vertices from the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyTVertexThickenerShader:
    '''Thickens TVertices (visual intersections between two edges). '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyTimeColorShader:
    '''Assigns a greyscale value that increases for every vertex. The brightness will increase along the stroke. '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyTipRemoverShader:
    '''Undocumented '''

    def shade(self, stroke):
        '''

        '''
        pass


class pyZDependingThicknessShader:
    '''Assigns thickness based on an object’s local Z depth (point closest to camera is 1, point furthest from camera is zero). '''

    def shade(self, stroke):
        '''

        '''
        pass
