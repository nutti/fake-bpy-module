def cycles_integrator_preset_add(name="",
                                 remove_name=False,
                                 remove_active=False):
    '''Add an Integrator Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def cycles_sampling_preset_add(name="", remove_name=False,
                               remove_active=False):
    '''Add a Sampling Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def opengl(animation=False,
           sequencer=False,
           write_still=False,
           view_context=True):
    '''Take a snapshot of the active viewport 

    :param animation: Animation, Render files from the animation range of this scene 
    :type animation: boolean, (optional)
    :param sequencer: Sequencer, Render using the sequencer’s OpenGL display 
    :type sequencer: boolean, (optional)
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled) 
    :type write_still: boolean, (optional)
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings 
    :type view_context: boolean, (optional)
    '''

    pass


def play_rendered_anim():
    '''Play back rendered frames/movies using an external player 

    '''

    pass


def preset_add(name="", remove_name=False, remove_active=False):
    '''Add or remove a Render Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :type name: string, (optional, never None)
    :param remove_name: remove_name 
    :type remove_name: boolean, (optional)
    :param remove_active: remove_active 
    :type remove_active: boolean, (optional)
    '''

    pass


def render(animation=False,
           write_still=False,
           use_viewport=False,
           layer="",
           scene=""):
    '''Render active scene 

    :param animation: Animation, Render files from the animation range of this scene 
    :type animation: boolean, (optional)
    :param write_still: Write Image, Save rendered the image to the output path (used only when animation is disabled) 
    :type write_still: boolean, (optional)
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport 
    :type use_viewport: boolean, (optional)
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled) 
    :type layer: string, (optional, never None)
    :param scene: Scene, Scene to render, current scene if not specified 
    :type scene: string, (optional, never None)
    '''

    pass


def shutter_curve_preset(shape='SMOOTH'):
    '''Set shutter curve 

    :param shape: Mode 
    :type shape: enum in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)
    '''

    pass


def view_cancel():
    '''Cancel show render view 

    '''

    pass


def view_show():
    '''Toggle show render view 

    '''

    pass
