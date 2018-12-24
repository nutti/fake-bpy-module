categories = None
'''constant value bpy.utils.units.categories(NONE=NONE, LENGTH=LENGTH, AREA=AREA, VOLUME=VOLUME, MASS=MASS, ROTATION=ROTATION, TIME=TIME, VELOCITY=VELOCITY, ACCELERATION=ACCELERATION, CAMERA=CAMERA) '''

systems = None
'''constant value bpy.utils.units.systems(NONE=NONE, METRIC=METRIC, IMPERIAL=IMPERIAL) '''


def to_string(unit_system,
              unit_category,
              value,
              precision=3,
              split_unit=False,
              compatible_unit=False):
    '''Convert a given input float value into a string with units. 

    :param unit_system: The unit system, from bpy.utils.units.systems. 
    :type unit_system: string
    :param unit_category: The category of data we are converting (length, area, rotation, etc.), from bpy.utils.units.categories. 
    :type unit_category: string
    :param value: The value to convert to a string. 
    :type value: float
    :param precision: Number of digits after the comma. 
    :type precision: int
    :param split_unit: Whether to use several units if needed (1m1cm), or always only one (1.01m). 
    :type split_unit: bool
    :param compatible_unit: Whether to use keyboard-friendly units (1m2) or nicer utf-8 ones (1m²). 
    :type compatible_unit: bool
    :return:  The converted string. 
    '''

    pass


def to_value(unit_system, unit_category, str_input, str_ref_unit=None):
    '''Convert a given input string into a float value. 

    :param unit_system: The unit system, from bpy.utils.units.systems. 
    :type unit_system: string
    :param unit_category: The category of data we are converting (length, area, rotation, etc.), from bpy.utils.units.categories. 
    :type unit_category: string
    :param str_input: The string to convert to a float value. 
    :type str_input: string
    :param str_ref_unit: A reference string from which to extract a default unit, if none is found in str_input. 
    :type str_ref_unit: string or None
    :return:  The converted/interpreted value. 
    '''

    pass
