STDPERLIN = None

STDPERLIN = None


def cell(position):
    '''Returns cell noise value at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :return:  The cell noise value. 
    '''

    pass


def cell_vector(position):
    '''Returns cell noise vector at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :return:  The cell noise vector. 
    '''

    pass


def fractal(position, H, lacunarity, octaves, noise_basis=STDPERLIN):
    '''Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param H: The fractal increment factor. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The fractal Brownian motion noise value. 
    '''

    pass


def hetero_terrain(position,
                   H,
                   lacunarity,
                   octaves,
                   offset,
                   noise_basis=STDPERLIN):
    '''Returns the heterogeneous terrain value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The heterogeneous terrain value. 
    '''

    pass


def hybrid_multi_fractal(position,
                         H,
                         lacunarity,
                         octaves,
                         offset,
                         gain,
                         noise_basis=STDPERLIN):
    '''Returns hybrid multifractal value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param gain: Scaling applied to the values. 
    :type gain: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The hybrid multifractal value. 
    '''

    pass


def multi_fractal(position, H, lacunarity, octaves, noise_basis=STDPERLIN):
    '''Returns multifractal noise value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param H: The fractal increment factor. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The multifractal noise value. 
    '''

    pass


def noise(position, noise_basis=STDPERLIN):
    '''Returns noise value from the noise basis at the position specified. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The noise value. 
    '''

    pass


def noise_vector(position, noise_basis=STDPERLIN):
    '''Returns the noise vector from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The noise vector. 
    '''

    pass


def random():
    '''Returns a random number in the range [0, 1]. 

    :return:  The random number. 
    '''

    pass


def random_unit_vector(size=3):
    '''Returns a unit vector with random entries. 

    :param size: The size of the vector to be produced. 
    :type size: Int
    :return:  The random unit vector. 
    '''

    pass


def ridged_multi_fractal(position,
                         H,
                         lacunarity,
                         octaves,
                         offset,
                         gain,
                         noise_basis=STDPERLIN):
    '''Returns ridged multifractal value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param H: The fractal dimension of the roughest areas. 
    :type H: float
    :param lacunarity: The gap between successive frequencies. 
    :type lacunarity: float
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param offset: The height of the terrain above ‘sea level’. 
    :type offset: float
    :param gain: Scaling applied to the values. 
    :type gain: float
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in noise.types or int
    :return:  The ridged multifractal value. 
    '''

    pass


def seed_set(seed):
    '''Sets the random seed used for random_unit_vector, random_vector and random. 

    :param seed: Seed used for the random generator. When seed is zero, the current time will be used instead. 
    :type seed: Int
    '''

    pass


def turbulence(position,
               octaves,
               hard,
               noise_basis=STDPERLIN,
               amplitude_scale=0.5,
               frequency_scale=2.0):
    '''Returns the turbulence value from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions). 
    :type hard: :boolean
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in mathutils.noise.types or int
    :param amplitude_scale: The amplitude scaling factor. 
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor 
    :type frequency_scale: Value in noise.types or int
    :return:  The turbulence value. 
    '''

    pass


def turbulence_vector(position,
                      octaves,
                      hard,
                      noise_basis=STDPERLIN,
                      amplitude_scale=0.5,
                      frequency_scale=2.0):
    '''Returns the turbulence vector from the noise basis at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param octaves: The number of different noise frequencies used. 
    :type octaves: int
    :param hard: Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions). 
    :type hard: :boolean
    :param noise_basis: The type of noise to be evaluated. 
    :type noise_basis: Value in mathutils.noise.types or int
    :param amplitude_scale: The amplitude scaling factor. 
    :type amplitude_scale: float
    :param frequency_scale: The frequency scaling factor 
    :type frequency_scale: Value in noise.types or int
    :return:  The turbulence vector. 
    '''

    pass


def variable_lacunarity(position,
                        distortion,
                        noise_type1=STDPERLIN,
                        noise_type2=STDPERLIN):
    '''Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param distortion: The amount of distortion. 
    :type distortion: float
    :param noise_type1: The type of noise to be distorted. 
    :type noise_type1: Value in noise.types or int
    :param noise_type2: The type of noise used to distort noise_type1. 
    :type noise_type2: Value in noise.types or int
    :return:  The variable lacunarity noise value. 
    '''

    pass


def voronoi(position,
            distance_metric=noise.distance_metrics.DISTANCE,
            exponent=2.5):
    '''Returns a list of distances to the four closest features and their locations. 

    :param position: The position to evaluate the selected noise function at. 
    :type position: mathutils.Vector
    :param distance_metric: Method of measuring distance. 
    :type distance_metric: Value in noise.distance_metrics or int
    :param exponent: The exponent for Minkowski distance metric. 
    :type exponent: float
    :return:  A list of distances to the four closest features and their locations. 
    '''

    pass


STDPERLIN = None

STDPERLIN = None

STDPERLIN = None

STDPERLIN = None
