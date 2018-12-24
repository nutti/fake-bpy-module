def assign_default_button():
    '''Set this property’s current value as the new default 

    '''

    pass


def button_execute(skip_depressed=False):
    '''Presses active button 

    :param skip_depressed: Skip Depressed 
    :type skip_depressed: boolean, (optional)
    '''

    pass


def copy_data_path_button(full_path=False):
    '''Copy the RNA data path for this property to the clipboard 

    :param full_path: full_path, Copy full data path 
    :type full_path: boolean, (optional)
    '''

    pass


def copy_python_command_button():
    '''Copy the Python command matching this button 

    '''

    pass


def copy_to_selected_button(all=True):
    '''Copy property from this object to selected objects or bones 

    :param all: All, Copy to selected all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def drop_color(color=(0.0, 0.0, 0.0), gamma=False):
    '''Drop colors to buttons 

    :param color: Color, Source color 
    :type color: float array of 3 items in [0, inf], (optional)
    :param gamma: Gamma Corrected, The source color is gamma corrected 
    :type gamma: boolean, (optional)
    '''

    pass


def editsource():
    '''Edit UI source code of the active button 

    '''

    pass


def edittranslation_init():
    '''Edit i18n in current language for the active button 

    '''

    pass


def eyedropper_color():
    '''Sample a color from the Blender Window to store in a property 

    '''

    pass


def eyedropper_color_crypto():
    '''Pick a color from Cryptomatte node Pick output image 

    '''

    pass


def eyedropper_colorband():
    '''Sample a color band 

    '''

    pass


def eyedropper_colorband_point():
    '''Point-sample a color band 

    '''

    pass


def eyedropper_depth():
    '''Sample depth from the 3D view 

    '''

    pass


def eyedropper_driver(mapping_type='SINGLE_MANY'):
    '''Pick a property to use as a driver target 

    :param mapping_type: Mapping Type, Method used to match target and driven propertiesSINGLE_MANY All from Target, Drive all components of this property using the target picked.DIRECT Single from Target, Drive this component of this property using the target picked.MATCH Match Indices, Create drivers for each pair of corresponding elements.NONE_ALL Manually Create Later, Create drivers for all properties without assigning any targets yet.NONE_SINGLE Manually Create Later (Single), Create driver for this property only and without assigning any targets yet. 
    :type mapping_type: enum in ['SINGLE_MANY', 'DIRECT', 'MATCH', 'NONE_ALL', 'NONE_SINGLE'], (optional)
    '''

    pass


def eyedropper_id():
    '''Sample a data-block from the 3D View to store in a property 

    '''

    pass


def jump_to_target_button():
    '''Switch to the target object or bone 

    '''

    pass


def override_remove_button(all=True):
    '''Remove an override operation 

    :param all: All, Reset to default values all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def override_type_set_button(all=True, type='REPLACE'):
    '''Create an override operation, or set the type of an existing one 

    :param all: All, Reset to default values all elements of the array 
    :type all: boolean, (optional)
    :param type: Type, Type of override operationNOOP NoOp, ‘No-Operation’, place holder preventing automatic override to ever affect the property.REPLACE Replace, Completely replace value from linked data by local one.DIFFERENCE Difference, Store difference to linked data value.FACTOR Factor, Store factor to linked data value (useful e.g. for scale). 
    :type type: enum in ['NOOP', 'REPLACE', 'DIFFERENCE', 'FACTOR'], (optional)
    '''

    pass


def reloadtranslation():
    '''Force a full reload of UI translation 

    '''

    pass


def reports_to_textblock():
    '''Write the reports 

    '''

    pass


def reset_default_button(all=True):
    '''Reset this property’s value to its default value 

    :param all: All, Reset to default values all elements of the array 
    :type all: boolean, (optional)
    '''

    pass


def reset_default_theme():
    '''Reset to the default theme colors 

    '''

    pass


def unset_property_button():
    '''Clear the property and use default or generated value in operators 

    '''

    pass
