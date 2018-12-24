def add_simple_uvs():
    '''Add cube map uvs on mesh 

    '''

    pass


def add_texture_paint_slot(type='BASE_COLOR',
                           name="Untitled",
                           width=1024,
                           height=1024,
                           color=(0.0, 0.0, 0.0, 1.0),
                           alpha=True,
                           generated_type='BLANK',
                           float=False):
    '''Add a texture paint slot 

    :param type: Type, Merge method to use 
    :type type: enum in ['BASE_COLOR', 'SPECULAR', 'ROUGHNESS', 'METALLIC', 'NORMAL', 'BUMP', 'DISPLACEMENT'], (optional)
    :param name: Name, Image data-block name 
    :type name: string, (optional, never None)
    :param width: Width, Image width 
    :type width: int in [1, inf], (optional)
    :param height: Height, Image height 
    :type height: int in [1, inf], (optional)
    :param color: Color, Default fill color 
    :type color: float array of 4 items in [0, inf], (optional)
    :param alpha: Alpha, Create an image with an alpha channel 
    :type alpha: boolean, (optional)
    :param generated_type: Generated Type, Fill the image with a grid for UV map testingBLANK Blank, Generate a blank image.UV_GRID UV Grid, Generated grid to test UV mappings.COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings. 
    :type generated_type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth 
    :type float: boolean, (optional)
    '''

    pass


def brush_colors_flip():
    '''Toggle foreground and background brush colors 

    '''

    pass


def brush_select(sculpt_tool='DRAW',
                 vertex_tool='DRAW',
                 weight_tool='DRAW',
                 image_tool='DRAW',
                 gpencil_tool='DRAW',
                 toggle=False,
                 create_missing=False):
    '''Select a paint mode’s brush by tool type 

    :param sculpt_tool: sculpt_tool 
    :type sculpt_tool: enum in ['DRAW', 'CLAY', 'CLAY_STRIPS', 'LAYER', 'INFLATE', 'BLOB', 'CREASE', 'SMOOTH', 'FLATTEN', 'FILL', 'SCRAPE', 'PINCH', 'GRAB', 'SNAKE_HOOK', 'THUMB', 'NUDGE', 'ROTATE', 'MASK', 'SIMPLIFY'], (optional)
    :param vertex_tool: vertex_tool 
    :type vertex_tool: enum in ['DRAW', 'BLUR', 'AVERAGE', 'SMEAR'], (optional)
    :param weight_tool: weight_tool 
    :type weight_tool: enum in ['DRAW', 'BLUR', 'AVERAGE', 'SMEAR'], (optional)
    :param image_tool: image_tool 
    :type image_tool: enum in ['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK'], (optional)
    :param gpencil_tool: gpencil_toolDRAW Draw, The brush is of type used for drawing strokes.FILL Fill, The brush is of type used for filling areas.ERASE Erase, The brush is used for erasing strokes. 
    :type gpencil_tool: enum in ['DRAW', 'FILL', 'ERASE'], (optional)
    :param toggle: Toggle, Toggle between two brushes rather than cycling 
    :type toggle: boolean, (optional)
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush 
    :type create_missing: boolean, (optional)
    '''

    pass


def face_select_all(action='TOGGLE'):
    '''Change selection for all faces 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def face_select_hide(unselected=False):
    '''Hide selected faces 

    :param unselected: Unselected, Hide unselected rather than selected objects 
    :type unselected: boolean, (optional)
    '''

    pass


def face_select_linked():
    '''Select linked faces 

    '''

    pass


def face_select_linked_pick(deselect=False):
    '''Select linked faces under the cursor 

    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    '''

    pass


def face_select_reveal(select=True):
    '''Reveal hidden faces 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def grab_clone(delta=(0.0, 0.0)):
    '''Move the clone source image 

    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates 
    :type delta: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def hide_show(action='HIDE',
              area='INSIDE',
              xmin=0,
              xmax=0,
              ymin=0,
              ymax=0,
              wait_for_input=True):
    '''Hide/show some vertices 

    :param action: Action, Whether to hide or show verticesHIDE Hide, Hide vertices.SHOW Show, Show vertices. 
    :type action: enum in ['HIDE', 'SHOW'], (optional)
    :param area: Area, Which vertices to hide or showOUTSIDE Outside, Hide or show vertices outside the selection.INSIDE Inside, Hide or show vertices inside the selection.ALL All, Hide or show all vertices.MASKED Masked, Hide or show vertices that are masked (minimum mask value of 0.5). 
    :type area: enum in ['OUTSIDE', 'INSIDE', 'ALL', 'MASKED'], (optional)
    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param wait_for_input: Wait for Input 
    :type wait_for_input: boolean, (optional)
    '''

    pass


def image_from_view(filepath=""):
    '''Make an image from the current 3D view for re-projection 

    :param filepath: File Path, Name of the file 
    :type filepath: string, (optional, never None)
    '''

    pass


def image_paint(stroke=None, mode='NORMAL'):
    '''Paint a stroke into the image 

    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Normal, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)
    '''

    pass


def mask_flood_fill(mode='VALUE', value=0.0):
    '''Fill the whole mask with a given value, or invert its values 

    :param mode: ModeVALUE Value, Set mask to the level specified by the ‘value’ property.VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted ‘value’ property.INVERT Invert, Invert the mask. 
    :type mode: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
    :param value: Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked 
    :type value: float in [0, 1], (optional)
    '''

    pass


def mask_lasso_gesture(path=None, mode='VALUE', value=1.0):
    '''Add mask within the lasso as you move the brush 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param mode: ModeVALUE Value, Set mask to the level specified by the ‘value’ property.VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted ‘value’ property.INVERT Invert, Invert the mask. 
    :type mode: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
    :param value: Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked 
    :type value: float in [0, 1], (optional)
    '''

    pass


def project_image(image=''):
    '''Project an edited render from the active camera back onto the object 

    :param image: Image 
    :type image: enum in [], (optional)
    '''

    pass


def sample_color(location=(0, 0), merged=False, palette=False):
    '''Use the mouse to sample a color in the image 

    :param location: Location 
    :type location: int array of 2 items in [0, inf], (optional)
    :param merged: Sample Merged, Sample the output display color 
    :type merged: boolean, (optional)
    :param palette: Add to Palette 
    :type palette: boolean, (optional)
    '''

    pass


def texture_paint_toggle():
    '''Toggle texture paint mode in 3D view 

    '''

    pass


def vert_select_all(action='TOGGLE'):
    '''Change selection for all vertices 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def vert_select_ungrouped(extend=False):
    '''Select vertices without a group 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def vertex_color_brightness_contrast(brightness=0.0, contrast=0.0):
    '''Adjust vertex color brightness/contrast 

    :param brightness: Brightness 
    :type brightness: float in [-100, 100], (optional)
    :param contrast: Contrast 
    :type contrast: float in [-100, 100], (optional)
    '''

    pass


def vertex_color_dirt(blur_strength=1.0,
                      blur_iterations=1,
                      clean_angle=3.14159,
                      dirt_angle=0.0,
                      dirt_only=False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param blur_strength: Blur Strength, Blur strength per iteration 
    :type blur_strength: float in [0.01, 1], (optional)
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more) 
    :type blur_iterations: int in [0, 40], (optional)
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range 
    :type clean_angle: float in [0, 3.14159], (optional)
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range 
    :type dirt_angle: float in [0, 3.14159], (optional)
    :param dirt_only: Dirt Only, Don’t calculate cleans for convex areas 
    :type dirt_only: boolean, (optional)
    '''

    pass


def vertex_color_from_weight():
    '''Convert active weight into gray scale vertex colors 

    '''

    pass


def vertex_color_hsv(h=0.5, s=1.0, v=1.0):
    '''Adjust vertex color HSV values 

    :param h: Hue 
    :type h: float in [0, 1], (optional)
    :param s: Saturation 
    :type s: float in [0, 2], (optional)
    :param v: Value 
    :type v: float in [0, 2], (optional)
    '''

    pass


def vertex_color_invert():
    '''Invert RGB values 

    '''

    pass


def vertex_color_levels(offset=0.0, gain=1.0):
    '''Adjust levels of vertex colors 

    :param offset: Offset, Value to add to colors 
    :type offset: float in [-1, 1], (optional)
    :param gain: Gain, Value to multiply colors by 
    :type gain: float in [0, inf], (optional)
    '''

    pass


def vertex_color_set():
    '''Fill the active vertex color layer with the current paint color 

    '''

    pass


def vertex_color_smooth():
    '''Smooth colors across vertices 

    '''

    pass


def vertex_paint(stroke=None, mode='NORMAL'):
    '''Paint a stroke in the active vertex color layer 

    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Normal, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)
    '''

    pass


def vertex_paint_toggle():
    '''Toggle the vertex paint mode in 3D view 

    '''

    pass


def weight_from_bones(type='AUTOMATIC'):
    '''Set the weights of the groups matching the attached armature’s selected bones, using the distance between the vertices and the bones 

    :param type: Type, Method to use for assigning weightsAUTOMATIC Automatic, Automatic weights from bones.ENVELOPES From Envelopes, Weights from envelopes with user defined radius. 
    :type type: enum in ['AUTOMATIC', 'ENVELOPES'], (optional)
    '''

    pass


def weight_gradient(type='LINEAR',
                    xstart=0,
                    xend=0,
                    ystart=0,
                    yend=0,
                    cursor=1002):
    '''Draw a line to apply a weight gradient to selected vertices 

    :param type: Type 
    :type type: enum in ['LINEAR', 'RADIAL'], (optional)
    :param xstart: X Start 
    :type xstart: int in [-inf, inf], (optional)
    :param xend: X End 
    :type xend: int in [-inf, inf], (optional)
    :param ystart: Y Start 
    :type ystart: int in [-inf, inf], (optional)
    :param yend: Y End 
    :type yend: int in [-inf, inf], (optional)
    :param cursor: Cursor, Mouse cursor style to use during the modal operator 
    :type cursor: int in [0, inf], (optional)
    '''

    pass


def weight_paint(stroke=None, mode='NORMAL'):
    '''Paint a stroke in the current vertex group’s weights 

    :param stroke: Stroke 
    :type stroke: bpy_prop_collection of OperatorStrokeElement, (optional)
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Normal, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)
    '''

    pass


def weight_paint_toggle():
    '''Toggle weight paint mode in 3D view 

    '''

    pass


def weight_sample():
    '''Use the mouse to sample a weight in the 3D view 

    '''

    pass


def weight_sample_group(group='DEFAULT'):
    '''Select one of the vertex groups available under current mouse position 

    :param group: Keying Set, The Keying Set to use 
    :type group: enum in ['DEFAULT'], (optional)
    '''

    pass


def weight_set():
    '''Fill the active vertex group with the current paint weight 

    '''

    pass
