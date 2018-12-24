AP_LOCATION = None
'''constant value 3 '''

AP_ORIENTATION = None
'''constant value 4 '''

AP_PANNING = None
'''constant value 1 '''

AP_PITCH = None
'''constant value 2 '''

AP_VOLUME = None
'''constant value 0 '''

CHANNELS_INVALID = None
'''constant value 0 '''

CHANNELS_MONO = None
'''constant value 1 '''

CHANNELS_STEREO = None
'''constant value 2 '''

CHANNELS_STEREO_LFE = None
'''constant value 3 '''

CHANNELS_SURROUND4 = None
'''constant value 4 '''

CHANNELS_SURROUND5 = None
'''constant value 5 '''

CHANNELS_SURROUND51 = None
'''constant value 6 '''

CHANNELS_SURROUND61 = None
'''constant value 7 '''

CHANNELS_SURROUND71 = None
'''constant value 8 '''

CODEC_AAC = None
'''constant value 1 '''

CODEC_AC3 = None
'''constant value 2 '''

CODEC_FLAC = None
'''constant value 3 '''

CODEC_INVALID = None
'''constant value 0 '''

CODEC_MP2 = None
'''constant value 4 '''

CODEC_MP3 = None
'''constant value 5 '''

CODEC_OPUS = None
'''constant value 8 '''

CODEC_PCM = None
'''constant value 6 '''

CODEC_VORBIS = None
'''constant value 7 '''

CONTAINER_AC3 = None
'''constant value 1 '''

CONTAINER_FLAC = None
'''constant value 2 '''

CONTAINER_INVALID = None
'''constant value 0 '''

CONTAINER_MATROSKA = None
'''constant value 3 '''

CONTAINER_MP2 = None
'''constant value 4 '''

CONTAINER_MP3 = None
'''constant value 5 '''

CONTAINER_OGG = None
'''constant value 6 '''

CONTAINER_WAV = None
'''constant value 7 '''

DISTANCE_MODEL_EXPONENT = None
'''constant value 5 '''

DISTANCE_MODEL_EXPONENT_CLAMPED = None
'''constant value 6 '''

DISTANCE_MODEL_INVALID = None
'''constant value 0 '''

DISTANCE_MODEL_INVERSE = None
'''constant value 1 '''

DISTANCE_MODEL_INVERSE_CLAMPED = None
'''constant value 2 '''

DISTANCE_MODEL_LINEAR = None
'''constant value 3 '''

DISTANCE_MODEL_LINEAR_CLAMPED = None
'''constant value 4 '''

FORMAT_FLOAT32 = None
'''constant value 36 '''

FORMAT_FLOAT64 = None
'''constant value 40 '''

FORMAT_INVALID = None
'''constant value 0 '''

FORMAT_S16 = None
'''constant value 18 '''

FORMAT_S24 = None
'''constant value 19 '''

FORMAT_S32 = None
'''constant value 20 '''

FORMAT_U8 = None
'''constant value 1 '''

RATE_11025 = None
'''constant value 11025 '''

RATE_16000 = None
'''constant value 16000 '''

RATE_192000 = None
'''constant value 192000 '''

RATE_22050 = None
'''constant value 22050 '''

RATE_32000 = None
'''constant value 32000 '''

RATE_44100 = None
'''constant value 44100 '''

RATE_48000 = None
'''constant value 48000 '''

RATE_8000 = None
'''constant value 8000 '''

RATE_88200 = None
'''constant value 88200 '''

RATE_96000 = None
'''constant value 96000 '''

RATE_INVALID = None
'''constant value 0 '''

STATUS_INVALID = None
'''constant value 0 '''

STATUS_PAUSED = None
'''constant value 2 '''

STATUS_PLAYING = None
'''constant value 1 '''

STATUS_STOPPED = None
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


class DynamicMusic:
    '''Stops playback of the scene. '''

    fadeTime = None
    '''The length in seconds of the crossfade transition '''

    position = None
    '''The playback position of the scene in seconds. '''

    scene = None
    '''The current scene '''

    status = None
    '''Whether the scene is playing, paused or stopped (=invalid). '''

    volume = None
    '''The volume of the scene. '''


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


class PlaybackManager:
    '''Stops playback of the category. '''

    pass


class Sequence:
    '''Writes animation data to a sequence. '''

    channels = None
    '''The channel count of the sequence. '''

    distance_model = None
    '''The distance model of the sequence. '''

    doppler_factor = None
    '''The doppler factor of the sequence. This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity. '''

    fps = None
    '''The listeners’s location in 3D space, a 3D tuple of floats. '''

    muted = None
    '''Whether the whole sequence is muted. '''

    rate = None
    '''The sampling rate of the sequence in Hz. '''

    speed_of_sound = None
    '''The speed of sound of the sequence. The speed of sound in air is typically 343.3 m/s. '''


class SequenceEntry:
    '''Writes animation data to a sequenced entry. '''

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

    muted = None
    '''Whether the entry is muted. '''

    relative = None
    '''Whether the source’s location, velocity and orientation is relative or absolute to the listener. '''

    sound = None
    '''The sound the entry is representing and will be played in the sequence. '''

    volume_maximum = None
    '''The maximum volume of the source. '''

    volume_minimum = None
    '''The minimum volume of the source. '''


class Sound:
    '''Writes the sound to a file. '''

    length = None
    '''The sample specification of the sound as a tuple with rate and channel count. '''

    specs = None
    '''The sample specification of the sound as a tuple with rate and channel count. '''


class Source:
    '''The source object represents the source position of a binaural sound. '''

    azimuth = None
    '''The azimuth angle. '''

    distance = None
    '''The distance value. 0 is min, 1 is max. '''

    elevation = None
    '''The elevation angle. '''


class ThreadPool:
    '''A ThreadPool is used to parallelize convolution efficiently. '''

    pass


class error:
    pass
