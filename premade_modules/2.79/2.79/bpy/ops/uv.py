def align(axis='ALIGN_AUTO'):
    '''Align selected UV vertices to an axis 

    :param axis: Axis, Axis to align UV locations onALIGN_S Straighten, Align UVs along the line defined by the endpoints.ALIGN_T Straighten X, Align UVs along the line defined by the endpoints along the X axis.ALIGN_U Straighten Y, Align UVs along the line defined by the endpoints along the Y axis.ALIGN_AUTO Align Auto, Automatically choose the axis on which there is most alignment already.ALIGN_X Align X, Align UVs on X axis.ALIGN_Y Align Y, Align UVs on Y axis. 
    :type axis: enum in ['ALIGN_S', 'ALIGN_T', 'ALIGN_U', 'ALIGN_AUTO', 'ALIGN_X', 'ALIGN_Y'], (optional)
    '''

    pass


def average_islands_scale():
    '''Average the size of separate UV islands, based on their area in 3D space 

    '''

    pass


def circle_select(x=0, y=0, radius=1, gesture_mode=0):
    '''Select UV vertices using circle selection 

    :param x: X 
    :type x: int in [-inf, inf], (optional)
    :param y: Y 
    :type y: int in [-inf, inf], (optional)
    :param radius: Radius 
    :type radius: int in [1, inf], (optional)
    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int in [-inf, inf], (optional)
    '''

    pass


def cube_project(cube_size=1.0,
                 correct_aspect=True,
                 clip_to_bounds=False,
                 scale_to_bounds=False):
    '''Project the UV vertices of the mesh over the six faces of a cube 

    :param cube_size: Cube Size, Size of the cube to project on 
    :type cube_size: float in [0, inf], (optional)
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type correct_aspect: boolean, (optional)
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping 
    :type clip_to_bounds: boolean, (optional)
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping 
    :type scale_to_bounds: boolean, (optional)
    '''

    pass


def cursor_set(location=(0.0, 0.0)):
    '''Set 2D cursor location 

    :param location: Location, Cursor location in normalized (0.0-1.0) coordinates 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def cylinder_project(direction='VIEW_ON_EQUATOR',
                     align='POLAR_ZX',
                     radius=1.0,
                     correct_aspect=True,
                     clip_to_bounds=False,
                     scale_to_bounds=False):
    '''Project the UV vertices of the mesh over the curved wall of a cylinder 

    :param direction: Direction, Direction of the sphere or cylinderVIEW_ON_EQUATOR View on Equator, 3D view is on the equator.VIEW_ON_POLES View on Poles, 3D view is on the poles.ALIGN_TO_OBJECT Align to Object, Align according to object transform. 
    :type direction: enum in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional)
    :param align: Align, How to determine rotation around the polePOLAR_ZX Polar ZX, Polar 0 is X.POLAR_ZY Polar ZY, Polar 0 is Y. 
    :type align: enum in ['POLAR_ZX', 'POLAR_ZY'], (optional)
    :param radius: Radius, Radius of the sphere or cylinder 
    :type radius: float in [0, inf], (optional)
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type correct_aspect: boolean, (optional)
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping 
    :type clip_to_bounds: boolean, (optional)
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping 
    :type scale_to_bounds: boolean, (optional)
    '''

    pass


def export_layout(filepath="",
                  check_existing=True,
                  export_all=False,
                  modified=False,
                  mode='PNG',
                  size=(1024, 1024),
                  opacity=0.25,
                  tessellated=False):
    '''Export UV layout to file 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param export_all: All UVs, Export all UVs in this mesh (not just visible ones) 
    :type export_all: boolean, (optional)
    :param modified: Modified, Exports UVs from the modified mesh 
    :type modified: boolean, (optional)
    :param mode: Format, File format to export the UV layout toSVG Scalable Vector Graphic (.svg), Export the UV layout to a vector SVG file.EPS Encapsulate PostScript (.eps), Export the UV layout to a vector EPS file.PNG PNG Image (.png), Export the UV layout to a bitmap image. 
    :type mode: enum in ['SVG', 'EPS', 'PNG'], (optional)
    :param size: size, Dimensions of the exported file 
    :type size: int array of 2 items in [8, 32768], (optional)
    :param opacity: Fill Opacity, Set amount of opacity for exported UV layout 
    :type opacity: float in [0, 1], (optional)
    :param tessellated: Tessellated UVs, Export tessellated UVs instead of polygons ones 
    :type tessellated: boolean, (optional)
    '''

    pass


def follow_active_quads(mode='LENGTH_AVERAGE'):
    '''Follow UVs from active quads along continuous face loops 

    :param mode: Edge Length Mode, Method to space UV edge loopsEVEN Even, Space all UVs evenly.LENGTH Length, Average space UVs edge length of each loop.LENGTH_AVERAGE Length Average, Average space UVs edge length of each loop. 
    :type mode: enum in ['EVEN', 'LENGTH', 'LENGTH_AVERAGE'], (optional)
    '''

    pass


def hide(unselected=False):
    '''Hide (un)selected UV vertices 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: boolean, (optional)
    '''

    pass


def lightmap_pack(PREF_CONTEXT='SEL_FACES',
                  PREF_PACK_IN_ONE=True,
                  PREF_NEW_UVLAYER=False,
                  PREF_APPLY_IMAGE=False,
                  PREF_IMG_PX_SIZE=512,
                  PREF_BOX_DIV=12,
                  PREF_MARGIN_DIV=0.1):
    '''Pack each faces UV’s into the UV bounds 

    :param PREF_CONTEXT: SelectionSEL_FACES Selected Faces, Space all UVs evenly.ALL_FACES All Faces, Average space UVs edge length of each loop.ALL_OBJECTS Selected Mesh Object, Average space UVs edge length of each loop. 
    :type PREF_CONTEXT: enum in ['SEL_FACES', 'ALL_FACES', 'ALL_OBJECTS'], (optional)
    :param PREF_PACK_IN_ONE: Share Tex Space, Objects Share texture space, map all objects into 1 uvmap 
    :type PREF_PACK_IN_ONE: boolean, (optional)
    :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed 
    :type PREF_NEW_UVLAYER: boolean, (optional)
    :param PREF_APPLY_IMAGE: New Image, Assign new images for every mesh (only one if shared tex space enabled) 
    :type PREF_APPLY_IMAGE: boolean, (optional)
    :param PREF_IMG_PX_SIZE: Image Size, Width and Height for the new image 
    :type PREF_IMG_PX_SIZE: int in [64, 5000], (optional)
    :param PREF_BOX_DIV: Pack Quality, Pre Packing before the complex boxpack 
    :type PREF_BOX_DIV: int in [1, 48], (optional)
    :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV 
    :type PREF_MARGIN_DIV: float in [0.001, 1], (optional)
    '''

    pass


def mark_seam(clear=False):
    '''Mark selected UV edges as seams 

    :param clear: Clear Seams, Clear instead of marking seams 
    :type clear: boolean, (optional)
    '''

    pass


def minimize_stretch(fill_holes=True, blend=0.0, iterations=0):
    '''Reduce UV stretching by relaxing angles 

    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry 
    :type fill_holes: boolean, (optional)
    :param blend: Blend, Blend factor between stretch minimized and original 
    :type blend: float in [0, 1], (optional)
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively 
    :type iterations: int in [0, inf], (optional)
    '''

    pass


def pack_islands(rotate=True, margin=0.001):
    '''Transform all islands so that they fill up the UV space as much as possible 

    :param rotate: Rotate, Rotate islands for best fit 
    :type rotate: boolean, (optional)
    :param margin: Margin, Space between islands 
    :type margin: float in [0, 1], (optional)
    '''

    pass


def pin(clear=False):
    '''Set/clear selected UV vertices as anchored between multiple unwrap operations 

    :param clear: Clear, Clear pinning for the selection instead of setting it 
    :type clear: boolean, (optional)
    '''

    pass


def project_from_view(orthographic=False,
                      camera_bounds=True,
                      correct_aspect=True,
                      clip_to_bounds=False,
                      scale_to_bounds=False):
    '''Project the UV vertices of the mesh as seen in current 3D view 

    :param orthographic: Orthographic, Use orthographic projection 
    :type orthographic: boolean, (optional)
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account 
    :type camera_bounds: boolean, (optional)
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type correct_aspect: boolean, (optional)
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping 
    :type clip_to_bounds: boolean, (optional)
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping 
    :type scale_to_bounds: boolean, (optional)
    '''

    pass


def remove_doubles(threshold=0.02, use_unselected=False):
    '''Selected UV vertices that are within a radius of each other are welded together 

    :param threshold: Merge Distance, Maximum distance between welded vertices 
    :type threshold: float in [0, 10], (optional)
    :param use_unselected: Unselected, Merge selected to other unselected vertices 
    :type use_unselected: boolean, (optional)
    '''

    pass


def reset():
    '''Reset UV projection 

    '''

    pass


def reveal():
    '''Reveal all hidden UV vertices 

    '''

    pass


def seams_from_islands(mark_seams=True, mark_sharp=False):
    '''Set mesh seams according to island setup in the UV editor 

    :param mark_seams: Mark Seams, Mark boundary edges as seams 
    :type mark_seams: boolean, (optional)
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp 
    :type mark_sharp: boolean, (optional)
    '''

    pass


def select(extend=False, location=(0.0, 0.0)):
    '''Select UV vertices 

    :param extend: Extend, Extend selection rather than clearing the existing selection 
    :type extend: boolean, (optional)
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all UV vertices 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_border(pinned=False,
                  gesture_mode=0,
                  xmin=0,
                  xmax=0,
                  ymin=0,
                  ymax=0,
                  extend=True):
    '''Select UV vertices using border selection 

    :param pinned: Pinned, Border select pinned UVs only 
    :type pinned: boolean, (optional)
    :param gesture_mode: Gesture Mode 
    :type gesture_mode: int in [-inf, inf], (optional)
    :param xmin: X Min 
    :type xmin: int in [-inf, inf], (optional)
    :param xmax: X Max 
    :type xmax: int in [-inf, inf], (optional)
    :param ymin: Y Min 
    :type ymin: int in [-inf, inf], (optional)
    :param ymax: Y Max 
    :type ymax: int in [-inf, inf], (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_lasso(path=None, deselect=False, extend=True):
    '''Select UVs using lasso selection 

    :param path: Path 
    :type path: bpy_prop_collection of OperatorMousePath, (optional)
    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: boolean, (optional)
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Deselect UV vertices at the boundary of each selection region 

    '''

    pass


def select_linked(extend=False):
    '''Select all UV vertices linked to the active UV map 

    :param extend: Extend, Extend selection rather than clearing the existing selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_linked_pick(extend=False, location=(0.0, 0.0)):
    '''Select all UV vertices linked under the mouse 

    :param extend: Extend, Extend selection rather than clearing the existing selection 
    :type extend: boolean, (optional)
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_loop(extend=False, location=(0.0, 0.0)):
    '''Select a loop of connected UV vertices 

    :param extend: Extend, Extend selection rather than clearing the existing selection 
    :type extend: boolean, (optional)
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds 
    :type location: float array of 2 items in [-inf, inf], (optional)
    '''

    pass


def select_more():
    '''Select more UV vertices connected to initial selection 

    '''

    pass


def select_pinned():
    '''Select all pinned UV vertices 

    '''

    pass


def select_split():
    '''Select only entirely selected faces 

    '''

    pass


def smart_project(angle_limit=66.0,
                  island_margin=0.0,
                  user_area_weight=0.0,
                  use_aspect=True,
                  stretch_to_bounds=True):
    '''This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces) 

    :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion 
    :type angle_limit: float in [1, 89], (optional)
    :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands 
    :type island_margin: float in [0, 1], (optional)
    :param user_area_weight: Area Weight, Weight projections vector by faces with larger areas 
    :type user_area_weight: float in [0, 1], (optional)
    :param use_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type use_aspect: boolean, (optional)
    :param stretch_to_bounds: Stretch to UV Bounds, Stretch the final output to texture bounds 
    :type stretch_to_bounds: boolean, (optional)
    '''

    pass


def snap_cursor(target='PIXELS'):
    '''Snap cursor to target type 

    :param target: Target, Target to snap the selected UVs to 
    :type target: enum in ['PIXELS', 'SELECTED'], (optional)
    '''

    pass


def snap_selected(target='PIXELS'):
    '''Snap selected UV vertices to target type 

    :param target: Target, Target to snap the selected UVs to 
    :type target: enum in ['PIXELS', 'CURSOR', 'CURSOR_OFFSET', 'ADJACENT_UNSELECTED'], (optional)
    '''

    pass


def sphere_project(direction='VIEW_ON_EQUATOR',
                   align='POLAR_ZX',
                   correct_aspect=True,
                   clip_to_bounds=False,
                   scale_to_bounds=False):
    '''Project the UV vertices of the mesh over the curved surface of a sphere 

    :param direction: Direction, Direction of the sphere or cylinderVIEW_ON_EQUATOR View on Equator, 3D view is on the equator.VIEW_ON_POLES View on Poles, 3D view is on the poles.ALIGN_TO_OBJECT Align to Object, Align according to object transform. 
    :type direction: enum in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional)
    :param align: Align, How to determine rotation around the polePOLAR_ZX Polar ZX, Polar 0 is X.POLAR_ZY Polar ZY, Polar 0 is Y. 
    :type align: enum in ['POLAR_ZX', 'POLAR_ZY'], (optional)
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type correct_aspect: boolean, (optional)
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping 
    :type clip_to_bounds: boolean, (optional)
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping 
    :type scale_to_bounds: boolean, (optional)
    '''

    pass


def stitch(use_limit=False,
           snap_islands=True,
           limit=0.01,
           static_island=0,
           midpoint_snap=False,
           clear_seams=True,
           mode='VERTEX',
           stored_mode='VERTEX',
           selection=None):
    '''Stitch selected UV vertices by proximity 

    :param use_limit: Use Limit, Stitch UVs within a specified limit distance 
    :type use_limit: boolean, (optional)
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too) 
    :type snap_islands: boolean, (optional)
    :param limit: Limit, Limit distance in normalized coordinates 
    :type limit: float in [0, inf], (optional)
    :param static_island: Static Island, Island that stays in place when stitching islands 
    :type static_island: int in [0, inf], (optional)
    :param midpoint_snap: Snap At Midpoint, UVs are stitched at midpoint instead of at static island 
    :type midpoint_snap: boolean, (optional)
    :param clear_seams: Clear Seams, Clear seams of stitched edges 
    :type clear_seams: boolean, (optional)
    :param mode: Operation Mode, Use vertex or edge stitching 
    :type mode: enum in ['VERTEX', 'EDGE'], (optional)
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching 
    :type stored_mode: enum in ['VERTEX', 'EDGE'], (optional)
    :param selection: Selection 
    :type selection: bpy_prop_collection of SelectedUvElement, (optional)
    '''

    pass


def tile_set(tile=(0, 0)):
    '''Set UV image tile coordinates 

    :param tile: Tile, Tile coordinate 
    :type tile: int array of 2 items in [0, inf], (optional)
    '''

    pass


def unwrap(method='ANGLE_BASED',
           fill_holes=True,
           correct_aspect=True,
           use_subsurf_data=False,
           margin=0.001):
    '''Unwrap the mesh of the object being edited 

    :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower) 
    :type method: enum in ['ANGLE_BASED', 'CONFORMAL'], (optional)
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry 
    :type fill_holes: boolean, (optional)
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account 
    :type correct_aspect: boolean, (optional)
    :param use_subsurf_data: Use Subsurf Modifier, Map UVs taking vertex position after Subdivision Surface modifier has been applied 
    :type use_subsurf_data: boolean, (optional)
    :param margin: Margin, Space between islands 
    :type margin: float in [0, 1], (optional)
    '''

    pass


def weld():
    '''Weld selected UV vertices together 

    '''

    pass
