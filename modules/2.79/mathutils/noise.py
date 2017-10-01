STDPERLIN = None


def cell(position):
    pass


def cell_vector(position):
    pass


def fractal(position, H, lacunarity, octaves, noise_basis=STDPERLIN):
    pass


def hetero_terrain(position, H, lacunarity, octaves, offset, noise_basis=STDPERLIN):
    pass


def hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=STDPERLIN):
    pass


def multi_fractal(position, H, lacunarity, octaves, noise_basis=STDPERLIN):
    pass


def noise(position, noise_basis=STDPERLIN):
    pass


def noise_vector(position, noise_basis=STDPERLIN):
    pass


def random():
    pass


def random_unit_vector(size=3):
    pass


def ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis=STDPERLIN):
    pass


def seed_set(seed):
    pass


def turbulence(position, octaves, hard, noise_basis=STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0):
    pass


def turbulence_vector(position, octaves, hard, noise_basis=STDPERLIN, amplitude_scale=0.5, frequency_scale=2.0):
    pass


def variable_lacunarity(position, distortion, noise_type1=STDPERLIN, noise_type2=STDPERLIN):
    pass


def voronoi(position, distance_metric=noise.distance_metrics.DISTANCE, exponent=2.5):
    pass


