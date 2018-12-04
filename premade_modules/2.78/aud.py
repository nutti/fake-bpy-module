AUD_DEVICE_JACK = None
'''constant value 3 '''

AUD_DEVICE_NULL = None
'''constant value 0 '''

AUD_DEVICE_OPENAL = None
'''constant value 1 '''

AUD_DEVICE_SDL = None
'''constant value 2 '''

AUD_DISTANCE_MODEL_EXPONENT = None
'''constant value 5 '''

AUD_DISTANCE_MODEL_EXPONENT_CLAMPED = None
'''constant value 6 '''

AUD_DISTANCE_MODEL_INVALID = None
'''constant value 0 '''

AUD_DISTANCE_MODEL_INVERSE = None
'''constant value 1 '''

AUD_DISTANCE_MODEL_INVERSE_CLAMPED = None
'''constant value 2 '''

AUD_DISTANCE_MODEL_LINEAR = None
'''constant value 3 '''

AUD_DISTANCE_MODEL_LINEAR_CLAMPED = None
'''constant value 4 '''

AUD_FORMAT_FLOAT32 = None
'''constant value 36 '''

AUD_FORMAT_FLOAT64 = None
'''constant value 40 '''

AUD_FORMAT_INVALID = None
'''constant value 0 '''

AUD_FORMAT_S16 = None
'''constant value 18 '''

AUD_FORMAT_S24 = None
'''constant value 19 '''

AUD_FORMAT_S32 = None
'''constant value 20 '''

AUD_FORMAT_U8 = None
'''constant value 1 '''

AUD_STATUS_INVALID = None
'''constant value 0 '''

AUD_STATUS_PAUSED = None
'''constant value 2 '''

AUD_STATUS_PLAYING = None
'''constant value 1 '''

AUD_STATUS_STOPPED = None
'''constant value 3 '''


class Device:
    '''Unlocks the device after a lock call, see lock() for details. '''

    channels = None
    '''The channel count of the device. '''

    distance_model = None
    '''The distance model of the device. '''

    doppler_factor = None
    '''The doppler factor of the device. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity. '''

    format = None
    '''The native sample format of the device. '''

    listener_location = None
    '''The listeners’s location in 3D space, a 3D tuple of floats. '''

    listener_orientation = None
    '''The listener’s orientation in 3D space as quaternion, a 4 float tuple. '''

    listener_velocity = None
    '''The listener’s velocity in 3D space, a 3D tuple of floats. '''

    rate = None
    '''The sampling rate of the device in Hz. '''

    speed_of_sound = None
    '''The speed of sound of the device. The speed of sound in air is typically 343.3 m/s. '''

    volume = None
    '''The overall volume of the device. '''


class Factory:
    '''Changes the volume of a factory. '''

    pass


class Handle:
    '''Stops playback. '''

    attenuation = None
    '''This factor is used for distance based attenuation of the source. '''

    cone_angle_inner = None
    '''The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the location of the source and with infinite height, heading in the direction of the source’s orientation. In the inner cone the volume is normal. Outside the outer cone the volume will be cone_volume_outer and in the area between the volume will be interpolated linearly. '''

    cone_angle_outer = None
    '''The opening angle of the outer cone of the source. '''

    cone_volume_outer = None
    '''The volume outside the outer cone of the source. '''

    distance_maximum = None
    '''The maximum distance of the source. If the listener is further away the source volume will be 0. '''

    distance_reference = None
    '''The reference distance of the source. At this distance the volume will be exactly volume. '''

    keep = None
    '''Whether the sound should be kept paused in the device when its end is reached. This can be used to seek the sound to some position and start playback again. '''

    location = None
    '''The source’s location in 3D space, a 3D tuple of floats. '''

    loop_count = None
    '''The (remaining) loop count of the sound. A negative value indicates infinity. '''

    orientation = None
    '''The source’s orientation in 3D space as quaternion, a 4 float tuple. '''

    pitch = None
    '''The pitch of the sound. '''

    position = None
    '''The playback position of the sound in seconds. '''

    relative = None
    '''Whether the source’s location, velocity and orientation is relative or absolute to the listener. '''

    status = None
    '''Whether the sound is playing, paused or stopped (=invalid). '''

    velocity = None
    '''The source’s velocity in 3D space, a 3D tuple of floats. '''

    volume = None
    '''The volume of the sound. '''

    volume_maximum = None
    '''The maximum volume of the source. '''

    volume_minimum = None
    '''The minimum volume of the source. '''


class error:
    pass
