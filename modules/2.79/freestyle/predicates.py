class AndBP1D:

    pass


class AndUP1D:

    pass


class ContourUP1D:

    def __call__(self, inter):
        pass



class DensityLowerThanUP1D:

    def __init__(self, threshold, sigma=2.0):
        pass

    def __call__(self, inter):
        pass



class EqualToChainingTimeStampUP1D:

    def __init__(self, ts):
        pass

    def __call__(self, inter):
        pass



class EqualToTimeStampUP1D:

    def __init__(self, ts):
        pass

    def __call__(self, inter):
        pass



class ExternalContourUP1D:

    def __call__(self, inter):
        pass



class FalseBP1D:

    def __call__(self, inter1, inter2):
        pass



class FalseUP0D:

    def __call__(self, it):
        pass



class FalseUP1D:

    def __call__(self, inter):
        pass



class Length2DBP1D:

    def __call__(self, inter1, inter2):
        pass



class MaterialBP1D:

    pass


class NotBP1D:

    pass


class NotUP1D:

    pass


class ObjectNamesUP1D:

    pass


class OrBP1D:

    pass


class OrUP1D:

    pass


class QuantitativeInvisibilityRangeUP1D:

    pass


class QuantitativeInvisibilityUP1D:

    def __init__(self, qi=0):
        pass

    def __call__(self, inter):
        pass



class SameShapeIdBP1D:

    def __call__(self, inter1, inter2):
        pass



class ShapeUP1D:

    def __init__(self, first, second=0):
        pass

    def __call__(self, inter):
        pass



class TrueBP1D:

    def __call__(self, inter1, inter2):
        pass



class TrueUP0D:

    def __call__(self, it):
        pass



class TrueUP1D:

    def __call__(self, inter):
        pass



class ViewMapGradientNormBP1D:

    def __init__(self, level, integration_type=IntegrationType.MEAN, sampling=2.0):
        pass

    def __call__(self, inter1, inter2):
        pass



class WithinImageBoundaryUP1D:

    def __init__(self, xmin, ymin, xmax, ymax):
        pass

    def __call__(self, inter):
        pass



class pyBackTVertexUP0D:

    pass


class pyClosedCurveUP1D:

    pass


class pyDensityFunctorUP1D:

    pass


class pyDensityUP1D:

    pass


class pyDensityVariableSigmaUP1D:

    pass


class pyHighDensityAnisotropyUP1D:

    pass


class pyHighDirectionalViewMapDensityUP1D:

    pass


class pyHighSteerableViewMapDensityUP1D:

    pass


class pyHighViewMapDensityUP1D:

    pass


class pyHighViewMapGradientNormUP1D:

    pass


class pyHigherCurvature2DAngleUP0D:

    pass


class pyHigherLengthUP1D:

    pass


class pyHigherNumberOfTurnsUP1D:

    pass


class pyIsInOccludersListUP1D:

    pass


class pyIsOccludedByIdListUP1D:

    pass


class pyIsOccludedByItselfUP1D:

    pass


class pyIsOccludedByUP1D:

    pass


class pyLengthBP1D:

    pass


class pyLowDirectionalViewMapDensityUP1D:

    pass


class pyLowSteerableViewMapDensityUP1D:

    pass


class pyNFirstUP1D:

    pass


class pyNatureBP1D:

    pass


class pyNatureUP1D:

    pass


class pyParameterUP0D:

    pass


class pyParameterUP0DGoodOne:

    pass


class pyProjectedXBP1D:

    pass


class pyProjectedYBP1D:

    pass


class pyShapeIdListUP1D:

    pass


class pyShapeIdUP1D:

    pass


class pyShuffleBP1D:

    pass


class pySilhouetteFirstBP1D:

    pass


class pyUEqualsUP0D:

    pass


class pyVertexNatureUP0D:

    pass


class pyViewMapGradientNormBP1D:

    pass


class pyZBP1D:

    pass


class pyZDiscontinuityBP1D:

    pass


class pyZSmallerUP1D:

    pass


