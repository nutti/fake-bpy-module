def beautify_fill(angle_limit=3.14159):
    '''Rearrange some faces to try to get less degenerated geometry 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float in [0, 3.14159], (optional)
    '''

    pass


def bevel(offset_type='OFFSET',
          offset=0.0,
          segments=1,
          profile=0.5,
          vertex_only=False,
          clamp_overlap=False,
          loop_slide=True,
          material=-1):
    '''Edge Bevel 

    :param offset_type: Amount Type, What distance Amount measuresOFFSET Offset, Amount is offset of new edges from original.WIDTH Width, Amount is width of new face.DEPTH Depth, Amount is perpendicular distance from original edge to bevel face.PERCENT Percent, Amount is percent of adjacent edge length. 
    :type offset_type: enum in ['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT'], (optional)
    :param offset: Amount 
    :type offset: float in [-1e+06, 1e+06], (optional)
    :param segments: Segments, Segments for curved edge 
    :type segments: int in [1, 1000], (optional)
    :param profile: Profile, Controls profile shape (0.5 = round) 
    :type profile: float in [0.15, 1], (optional)
    :param vertex_only: Vertex Only, Bevel only vertices 
    :type vertex_only: boolean, (optional)
    :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other 
    :type clamp_overlap: boolean, (optional)
    :param loop_slide: Loop Slide, Prefer slide along edge to even widths 
    :type loop_slide: boolean, (optional)
    :param material: Material, Material for bevel faces (-1 means use adjacent faces) 
    :type material: int in [-1, inf], (optional)
    '''

    pass


def bisect(
        plane_co=(0.0, 0.0, 0.0),
        plane_no=(0.0, 0.0, 0.0),
        use_fill=False,
        clear_inner=False,
        clear_outer=False,
        threshold=0.0001,
        xstart=0,
        xend=0,
        ystart=0,
        yend=0,
        cursor=1002):
    '''Cut geometry along a plane (click-drag to define plane) 

    :param plane_co: Plane Point, A point on the plane 
    :type plane_co: float array of 3 items in [-inf, inf], (optional)
    :param plane_no: Plane Normal, The direction the plane points 
    :type plane_no: float array of 3 items in [-1, 1], (optional)
    :param use_fill: Fill, Fill in the cut 
    :type use_fill: boolean, (optional)
    :param clear_inner: Clear Inner, Remove geometry behind the plane 
    :type clear_inner: boolean, (optional)
    :param clear_outer: Clear Outer, Remove geometry in front of the plane 
    :type clear_outer: boolean, (optional)
    :param threshold: Axis Threshold 
    :type threshold: float in [0, 10], (optional)
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


def blend_from_shape(shape='', blend=1.0, add=True):
    '''Blend in shape from a shape key 

    :param shape: Shape, Shape key to use for blending 
    :type shape: enum in [], (optional)
    :param blend: Blend, Blending factor 
    :type blend: float in [-1000, 1000], (optional)
    :param add: Add, Add rather than blend between shapes 
    :type add: boolean, (optional)
    '''

    pass


def bridge_edge_loops(type='SINGLE',
                      use_merge=False,
                      merge_factor=0.5,
                      twist_offset=0,
                      number_cuts=0,
                      interpolation='PATH',
                      smoothness=1.0,
                      profile_shape_factor=0.0,
                      profile_shape='SMOOTH'):
    '''Make faces between two or more edge loops 

    :param type: Connect Loops, Method of bridging multiple loops 
    :type type: enum in ['SINGLE', 'CLOSED', 'PAIRS'], (optional)
    :param use_merge: Merge, Merge rather than creating faces 
    :type use_merge: boolean, (optional)
    :param merge_factor: Merge Factor 
    :type merge_factor: float in [0, 1], (optional)
    :param twist_offset: Twist, Twist offset for closed loops 
    :type twist_offset: int in [-1000, 1000], (optional)
    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [0, 1000], (optional)
    :param interpolation: Interpolation, Interpolation method 
    :type interpolation: enum in ['LINEAR', 'PATH', 'SURFACE'], (optional)
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float in [0, 1000], (optional)
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded 
    :type profile_shape_factor: float in [-1000, 1000], (optional)
    :param profile_shape: Profile Shape, Shape of the profileSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type profile_shape: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)
    '''

    pass


def colors_reverse():
    '''Flip direction of vertex colors inside faces 

    '''

    pass


def colors_rotate(use_ccw=False):
    '''Rotate vertex colors inside faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: boolean, (optional)
    '''

    pass


def convex_hull(delete_unused=True,
                use_existing_faces=True,
                make_holes=False,
                join_triangles=True,
                face_threshold=0.698132,
                shape_threshold=0.698132,
                uvs=False,
                vcols=False,
                seam=False,
                sharp=False,
                materials=False):
    '''Enclose selected vertices in a convex polyhedron 

    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull 
    :type delete_unused: boolean, (optional)
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face 
    :type use_existing_faces: boolean, (optional)
    :param make_holes: Make Holes, Delete selected faces that are used by the hull 
    :type make_holes: boolean, (optional)
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads 
    :type join_triangles: boolean, (optional)
    :param face_threshold: Max Face Angle, Face angle limit 
    :type face_threshold: float in [0, 3.14159], (optional)
    :param shape_threshold: Max Shape Angle, Shape angle limit 
    :type shape_threshold: float in [0, 3.14159], (optional)
    :param uvs: Compare UVs 
    :type uvs: boolean, (optional)
    :param vcols: Compare VCols 
    :type vcols: boolean, (optional)
    :param seam: Compare Seam 
    :type seam: boolean, (optional)
    :param sharp: Compare Sharp 
    :type sharp: boolean, (optional)
    :param materials: Compare Materials 
    :type materials: boolean, (optional)
    '''

    pass


def customdata_custom_splitnormals_add():
    '''Add a custom split normals layer, if none exists yet 

    '''

    pass


def customdata_custom_splitnormals_clear():
    '''Remove the custom split normals layer, if it exists 

    '''

    pass


def customdata_mask_clear():
    '''Clear vertex sculpt masking data from the mesh 

    '''

    pass


def customdata_skin_add():
    '''Add a vertex skin layer 

    '''

    pass


def customdata_skin_clear():
    '''Clear vertex skin layer 

    '''

    pass


def decimate(ratio=1.0,
             use_vertex_group=False,
             vertex_group_factor=1.0,
             invert_vertex_group=False,
             use_symmetry=False,
             symmetry_axis='Y'):
    '''Simplify geometry by collapsing edges 

    :param ratio: Ratio 
    :type ratio: float in [0, 1], (optional)
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence 
    :type use_vertex_group: boolean, (optional)
    :param vertex_group_factor: Weight, Vertex group strength 
    :type vertex_group_factor: float in [0, 1000], (optional)
    :param invert_vertex_group: Invert, Invert vertex group influence 
    :type invert_vertex_group: boolean, (optional)
    :param use_symmetry: Symmetry, Maintain symmetry on an axis 
    :type use_symmetry: boolean, (optional)
    :param symmetry_axis: Axis, Axis of symmetry 
    :type symmetry_axis: enum in ['X', 'Y', 'Z'], (optional)
    '''

    pass


def delete(type='VERT'):
    '''Delete selected vertices, edges or faces 

    :param type: Type, Method used for deleting mesh data 
    :type type: enum in ['VERT', 'EDGE', 'FACE', 'EDGE_FACE', 'ONLY_FACE'], (optional)
    '''

    pass


def delete_edgeloop(use_face_split=True):
    '''Delete an edge loop by merging the faces on each side 

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: boolean, (optional)
    '''

    pass


def delete_loose(use_verts=True, use_edges=True, use_faces=False):
    '''Delete loose vertices, edges or faces 

    :param use_verts: Vertices, Remove loose vertices 
    :type use_verts: boolean, (optional)
    :param use_edges: Edges, Remove loose edges 
    :type use_edges: boolean, (optional)
    :param use_faces: Faces, Remove loose faces 
    :type use_faces: boolean, (optional)
    '''

    pass


def dissolve_degenerate(threshold=0.0001):
    '''Dissolve zero area faces and zero length edges 

    :param threshold: Merge Distance, Minimum distance between elements to merge 
    :type threshold: float in [1e-06, 50], (optional)
    '''

    pass


def dissolve_edges(use_verts=True, use_face_split=False):
    '''Dissolve edges, merging faces 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: boolean, (optional)
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: boolean, (optional)
    '''

    pass


def dissolve_faces(use_verts=False):
    '''Dissolve faces 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: boolean, (optional)
    '''

    pass


def dissolve_limited(angle_limit=0.0872665,
                     use_dissolve_boundaries=False,
                     delimit={'NORMAL'}):
    '''Dissolve selected edges and verts, limited by the angle of surrounding geometry 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float in [0, 3.14159], (optional)
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices inbetween face boundaries 
    :type use_dissolve_boundaries: boolean, (optional)
    :param delimit: Delimit, Delimit dissolve operationNORMAL Normal, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)
    '''

    pass


def dissolve_mode(use_verts=False,
                  use_face_split=False,
                  use_boundary_tear=False):
    '''Dissolve geometry based on the selection mode 

    :param use_verts: Dissolve Verts, Dissolve remaining vertices 
    :type use_verts: boolean, (optional)
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: boolean, (optional)
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces 
    :type use_boundary_tear: boolean, (optional)
    '''

    pass


def dissolve_verts(use_face_split=False, use_boundary_tear=False):
    '''Dissolve verts, merge edges and faces 

    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry 
    :type use_face_split: boolean, (optional)
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces 
    :type use_boundary_tear: boolean, (optional)
    '''

    pass


def drop_named_image(name="Image", filepath="Path", relative_path=True):
    '''Assign Image to active UV Map, or create an UV Map 

    :param name: Name, Image name to assign 
    :type name: string, (optional, never None)
    :param filepath: Filepath, Path to image file 
    :type filepath: string, (optional, never None)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    '''

    pass


def dupli_extrude_cursor(rotate_source=True):
    '''Duplicate and extrude selected vertices, edges or faces towards the mouse cursor 

    :param rotate_source: Rotate Source, Rotate initial selection giving better shape 
    :type rotate_source: boolean, (optional)
    '''

    pass


def duplicate(mode=1):
    '''Duplicate selected vertices, edges or faces 

    :param mode: Mode 
    :type mode: int in [0, inf], (optional)
    '''

    pass


def duplicate_move(MESH_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Duplicate mesh and move 

    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces 
    :type MESH_OT_duplicate: MESH_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def edge_collapse():
    '''Collapse selected edges 

    '''

    pass


def edge_face_add():
    '''Add an edge or face to selected 

    '''

    pass


def edge_rotate(use_ccw=False):
    '''Rotate selected edge or adjoining faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: boolean, (optional)
    '''

    pass


def edge_split():
    '''Split selected edges so that each neighbor face gets its own copy 

    '''

    pass


def edgering_select(extend=False, deselect=False, toggle=False, ring=True):
    '''Select an edge ring 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    :param deselect: Deselect, Remove from the selection 
    :type deselect: boolean, (optional)
    :param toggle: Toggle Select, Toggle the selection 
    :type toggle: boolean, (optional)
    :param ring: Select Ring, Select ring 
    :type ring: boolean, (optional)
    '''

    pass


def edges_select_sharp(sharpness=0.523599):
    '''Select all sharp-enough edges 

    :param sharpness: Sharpness 
    :type sharpness: float in [0.000174533, 3.14159], (optional)
    '''

    pass


def extrude_edges_indiv(mirror=False):
    '''Extrude individual edges only 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    '''

    pass


def extrude_edges_move(MESH_OT_extrude_edges_indiv=None,
                       TRANSFORM_OT_translate=None):
    '''Extrude edges and move result 

    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only 
    :type MESH_OT_extrude_edges_indiv: MESH_OT_extrude_edges_indiv, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude_faces_indiv(mirror=False):
    '''Extrude individual faces only 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    '''

    pass


def extrude_faces_move(MESH_OT_extrude_faces_indiv=None,
                       TRANSFORM_OT_shrink_fatten=None):
    '''Extrude faces and move result 

    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only 
    :type MESH_OT_extrude_faces_indiv: MESH_OT_extrude_faces_indiv, (optional)
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals 
    :type TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten, (optional)
    '''

    pass


def extrude_region(mirror=False):
    '''Extrude region of faces 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    '''

    pass


def extrude_region_move(MESH_OT_extrude_region=None,
                        TRANSFORM_OT_translate=None):
    '''Extrude region and move result 

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces 
    :type MESH_OT_extrude_region: MESH_OT_extrude_region, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude_region_shrink_fatten(MESH_OT_extrude_region=None,
                                 TRANSFORM_OT_shrink_fatten=None):
    '''Extrude region and move result 

    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces 
    :type MESH_OT_extrude_region: MESH_OT_extrude_region, (optional)
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals 
    :type TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten, (optional)
    '''

    pass


def extrude_repeat(offset=2.0, steps=10):
    '''Extrude selected vertices, edges or faces repeatedly 

    :param offset: Offset 
    :type offset: float in [0, inf], (optional)
    :param steps: Steps 
    :type steps: int in [0, 1000000], (optional)
    '''

    pass


def extrude_vertices_move(MESH_OT_extrude_verts_indiv=None,
                          TRANSFORM_OT_translate=None):
    '''Extrude vertices and move result 

    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only 
    :type MESH_OT_extrude_verts_indiv: MESH_OT_extrude_verts_indiv, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude_verts_indiv(mirror=False):
    '''Extrude individual vertices only 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    '''

    pass


def face_make_planar(factor=1.0, repeat=1):
    '''Flatten selected faces 

    :param factor: Factor 
    :type factor: float in [-10, 10], (optional)
    :param repeat: Iterations 
    :type repeat: int in [1, 10000], (optional)
    '''

    pass


def face_split_by_edges():
    '''Weld loose edges into faces (splitting them into new faces) 

    '''

    pass


def faces_mirror_uv(direction='POSITIVE', precision=3):
    '''Copy mirror UV coordinates on the X axis based on a mirrored mesh 

    :param direction: Axis Direction 
    :type direction: enum in ['POSITIVE', 'NEGATIVE'], (optional)
    :param precision: Precision, Tolerance for finding vertex duplicates 
    :type precision: int in [1, 16], (optional)
    '''

    pass


def faces_select_linked_flat(sharpness=0.0174533):
    '''Select linked faces by angle 

    :param sharpness: Sharpness 
    :type sharpness: float in [0.000174533, 3.14159], (optional)
    '''

    pass


def faces_shade_flat():
    '''Display faces flat 

    '''

    pass


def faces_shade_smooth():
    '''Display faces smooth (using vertex normals) 

    '''

    pass


def fill(use_beauty=True):
    '''Fill a selected edge loop with faces 

    :param use_beauty: Beauty, Use best triangulation division 
    :type use_beauty: boolean, (optional)
    '''

    pass


def fill_grid(span=1, offset=0, use_interp_simple=False):
    '''Fill grid from two loops 

    :param span: Span, Number of sides (zero disables) 
    :type span: int in [1, 1000], (optional)
    :param offset: Offset, Number of sides (zero disables) 
    :type offset: int in [-1000, 1000], (optional)
    :param use_interp_simple: Simple Blending 
    :type use_interp_simple: boolean, (optional)
    '''

    pass


def fill_holes(sides=4):
    '''Fill in holes (boundary edge loops) 

    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes) 
    :type sides: int in [0, 1000], (optional)
    '''

    pass


def flip_normals():
    '''Flip the direction of selected faces’ normals (and of their vertices) 

    '''

    pass


def hide(unselected=False):
    '''Hide (un)selected vertices, edges or faces 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: boolean, (optional)
    '''

    pass


def inset(use_boundary=True,
          use_even_offset=True,
          use_relative_offset=False,
          use_edge_rail=False,
          thickness=0.01,
          depth=0.0,
          use_outset=False,
          use_select_inset=False,
          use_individual=False,
          use_interpolate=True):
    '''Inset new faces into selected faces 

    :param use_boundary: Boundary, Inset face boundaries 
    :type use_boundary: boolean, (optional)
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness 
    :type use_even_offset: boolean, (optional)
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry 
    :type use_relative_offset: boolean, (optional)
    :param use_edge_rail: Edge Rail, Inset the region along existing edges 
    :type use_edge_rail: boolean, (optional)
    :param thickness: Thickness 
    :type thickness: float in [0, inf], (optional)
    :param depth: Depth 
    :type depth: float in [-inf, inf], (optional)
    :param use_outset: Outset, Outset rather than inset 
    :type use_outset: boolean, (optional)
    :param use_select_inset: Select Outer, Select the new inset faces 
    :type use_select_inset: boolean, (optional)
    :param use_individual: Individual, Individual Face Inset 
    :type use_individual: boolean, (optional)
    :param use_interpolate: Interpolate, Blend face data across the inset 
    :type use_interpolate: boolean, (optional)
    '''

    pass


def intersect(mode='SELECT_UNSELECT', use_separate=True, threshold=1e-06):
    '''Cut an intersection into faces 

    :param mode: SourceSELECT Self Intersect, Self intersect selected faces.SELECT_UNSELECT Selected/Unselected, Intersect selected with unselected faces. 
    :type mode: enum in ['SELECT', 'SELECT_UNSELECT'], (optional)
    :param use_separate: Separate 
    :type use_separate: boolean, (optional)
    :param threshold: Merge threshold 
    :type threshold: float in [0, 0.01], (optional)
    '''

    pass


def intersect_boolean(operation='DIFFERENCE', use_swap=False, threshold=1e-06):
    '''Cut solid geometry from selected to unselected 

    :param operation: Boolean 
    :type operation: enum in ['INTERSECT', 'UNION', 'DIFFERENCE'], (optional)
    :param use_swap: Swap, Use with difference intersection to swap which side is kept 
    :type use_swap: boolean, (optional)
    :param threshold: Merge threshold 
    :type threshold: float in [0, 0.01], (optional)
    '''

    pass


def knife_project(cut_through=False):
    '''Use other objects outlines & boundaries to project knife cuts 

    :param cut_through: Cut through, Cut through all faces, not just visible ones 
    :type cut_through: boolean, (optional)
    '''

    pass


def knife_tool(use_occlude_geometry=True, only_selected=False):
    '''Cut new topology 

    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry 
    :type use_occlude_geometry: boolean, (optional)
    :param only_selected: Only Selected, Only cut selected geometry 
    :type only_selected: boolean, (optional)
    '''

    pass


def loop_multi_select(ring=False):
    '''Select a loop of connected edges by connection type 

    :param ring: Ring 
    :type ring: boolean, (optional)
    '''

    pass


def loop_select(extend=False, deselect=False, toggle=False, ring=False):
    '''Select a loop of connected edges 

    :param extend: Extend Select, Extend the selection 
    :type extend: boolean, (optional)
    :param deselect: Deselect, Remove from the selection 
    :type deselect: boolean, (optional)
    :param toggle: Toggle Select, Toggle the selection 
    :type toggle: boolean, (optional)
    :param ring: Select Ring, Select ring 
    :type ring: boolean, (optional)
    '''

    pass


def loop_to_region(select_bigger=False):
    '''Select region of faces inside of a selected loop of edges 

    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones 
    :type select_bigger: boolean, (optional)
    '''

    pass


def loopcut(number_cuts=1,
            smoothness=0.0,
            falloff='INVERSE_SQUARE',
            edge_index=-1,
            mesh_select_mode_init=(False, False, False)):
    '''Add a new loop between existing loops 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [1, 1000000], (optional)
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float in [-1000, 1000], (optional)
    :param falloff: Falloff, Falloff type the featherSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)
    :param edge_index: Edge Index 
    :type edge_index: int in [-1, inf], (optional)
    '''

    pass


def loopcut_slide(MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None):
    '''Cut mesh loop and slide it 

    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops 
    :type MESH_OT_loopcut: MESH_OT_loopcut, (optional)
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh 
    :type TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide, (optional)
    '''

    pass


def mark_freestyle_edge(clear=False):
    '''(Un)mark selected edges as Freestyle feature edges 

    :param clear: Clear 
    :type clear: boolean, (optional)
    '''

    pass


def mark_freestyle_face(clear=False):
    '''(Un)mark selected faces for exclusion from Freestyle feature edge detection 

    :param clear: Clear 
    :type clear: boolean, (optional)
    '''

    pass


def mark_seam(clear=False):
    '''(Un)mark selected edges as a seam 

    :param clear: Clear 
    :type clear: boolean, (optional)
    '''

    pass


def mark_sharp(clear=False, use_verts=False):
    '''(Un)mark selected edges as sharp 

    :param clear: Clear 
    :type clear: boolean, (optional)
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp 
    :type use_verts: boolean, (optional)
    '''

    pass


def merge(type='CENTER', uvs=False):
    '''Merge selected vertices 

    :param type: Type, Merge method to use 
    :type type: enum in ['FIRST', 'LAST', 'CENTER', 'CURSOR', 'COLLAPSE'], (optional)
    :param uvs: UVs, Move UVs according to merge 
    :type uvs: boolean, (optional)
    '''

    pass


def navmesh_clear():
    '''Remove navmesh data from this mesh 

    '''

    pass


def navmesh_face_add():
    '''Add a new index and assign it to selected faces 

    '''

    pass


def navmesh_face_copy():
    '''Copy the index from the active face 

    '''

    pass


def navmesh_make():
    '''Create navigation mesh for selected objects 

    '''

    pass


def navmesh_reset():
    '''Assign a new index to every face 

    '''

    pass


def noise(factor=0.1):
    '''Use vertex coordinate as texture coordinate 

    :param factor: Factor 
    :type factor: float in [-10000, 10000], (optional)
    '''

    pass


def normals_make_consistent(inside=False):
    '''Make face and vertex normals point either outside or inside the mesh 

    :param inside: Inside 
    :type inside: boolean, (optional)
    '''

    pass


def offset_edge_loops(use_cap_endpoint=False):
    '''Create offset edge loop from the current selection 

    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points 
    :type use_cap_endpoint: boolean, (optional)
    '''

    pass


def offset_edge_loops_slide(MESH_OT_offset_edge_loops=None,
                            TRANSFORM_OT_edge_slide=None):
    '''Offset edge loop slide 

    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection 
    :type MESH_OT_offset_edge_loops: MESH_OT_offset_edge_loops, (optional)
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh 
    :type TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide, (optional)
    '''

    pass


def poke(offset=0.0, use_relative_offset=False, center_mode='MEAN_WEIGHTED'):
    '''Split a face into a fan 

    :param offset: Poke Offset, Poke Offset 
    :type offset: float in [-1000, 1000], (optional)
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry 
    :type use_relative_offset: boolean, (optional)
    :param center_mode: Poke Center, Poke Face Center CalculationMEAN_WEIGHTED Weighted Mean, Weighted Mean Face Center.MEAN Mean, Mean Face Center.BOUNDS Bounds, Face Bounds Center. 
    :type center_mode: enum in ['MEAN_WEIGHTED', 'MEAN', 'BOUNDS'], (optional)
    '''

    pass


def primitive_circle_add(
        vertices=32,
        radius=1.0,
        fill_type='NOTHING',
        calc_uvs=False,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct a circle mesh 

    :param vertices: Vertices 
    :type vertices: int in [3, 10000000], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param fill_type: Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type fill_type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_cone_add(vertices=32,
                       radius1=1.0,
                       radius2=0.0,
                       depth=2.0,
                       end_fill_type='NGON',
                       calc_uvs=False,
                       view_align=False,
                       enter_editmode=False,
                       location=(0.0, 0.0, 0.0),
                       rotation=(0.0, 0.0, 0.0),
                       layers=(False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False,
                               False, False, False, False, False, False)):
    '''Construct a conic mesh 

    :param vertices: Vertices 
    :type vertices: int in [3, 10000000], (optional)
    :param radius1: Radius 1 
    :type radius1: float in [0, inf], (optional)
    :param radius2: Radius 2 
    :type radius2: float in [0, inf], (optional)
    :param depth: Depth 
    :type depth: float in [0, inf], (optional)
    :param end_fill_type: Base Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type end_fill_type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_cube_add(radius=1.0,
                       calc_uvs=False,
                       view_align=False,
                       enter_editmode=False,
                       location=(0.0, 0.0, 0.0),
                       rotation=(0.0, 0.0, 0.0),
                       layers=(False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False,
                               False, False, False, False, False, False)):
    '''Construct a cube mesh 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_cylinder_add(
        vertices=32,
        radius=1.0,
        depth=2.0,
        end_fill_type='NGON',
        calc_uvs=False,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct a cylinder mesh 

    :param vertices: Vertices 
    :type vertices: int in [3, 10000000], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param depth: Depth 
    :type depth: float in [0, inf], (optional)
    :param end_fill_type: Cap Fill TypeNOTHING Nothing, Don’t fill at all.NGON Ngon, Use ngons.TRIFAN Triangle Fan, Use triangle fans. 
    :type end_fill_type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_grid_add(x_subdivisions=10,
                       y_subdivisions=10,
                       radius=1.0,
                       calc_uvs=False,
                       view_align=False,
                       enter_editmode=False,
                       location=(0.0, 0.0, 0.0),
                       rotation=(0.0, 0.0, 0.0),
                       layers=(False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False,
                               False, False, False, False, False, False)):
    '''Construct a grid mesh 

    :param x_subdivisions: X Subdivisions 
    :type x_subdivisions: int in [2, 10000000], (optional)
    :param y_subdivisions: Y Subdivisions 
    :type y_subdivisions: int in [2, 10000000], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_ico_sphere_add(
        subdivisions=2,
        size=1.0,
        calc_uvs=False,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct an Icosphere mesh 

    :param subdivisions: Subdivisions 
    :type subdivisions: int in [1, 10], (optional)
    :param size: Size 
    :type size: float in [0, inf], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_monkey_add(
        radius=1.0,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct a Suzanne mesh 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_plane_add(
        radius=1.0,
        calc_uvs=False,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct a filled planar mesh with 4 vertices 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def primitive_torus_add(
        rotation=(0.0, 0.0, 0.0),
        view_align=False,
        location=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False),
        major_segments=48,
        minor_segments=12,
        mode='MAJOR_MINOR',
        major_radius=1.0,
        minor_radius=0.25,
        abso_major_rad=1.25,
        abso_minor_rad=0.75):
    '''Add a torus mesh 

    :param rotation: Rotation 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param view_align: Align to View 
    :type view_align: boolean, (optional)
    :param location: Location 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layers 
    :type layers: boolean array of 20 items, (optional)
    :param major_segments: Major Segments, Number of segments for the main ring of the torus 
    :type major_segments: int in [3, 256], (optional)
    :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus 
    :type minor_segments: int in [3, 256], (optional)
    :param mode: Torus DimensionsMAJOR_MINOR Major/Minor, Use the major/minor radii for torus dimensions.EXT_INT Exterior/Interior, Use the exterior/interior radii for torus dimensions. 
    :type mode: enum in ['MAJOR_MINOR', 'EXT_INT'], (optional)
    :param major_radius: Major Radius, Radius from the origin to the center of the cross sections 
    :type major_radius: float in [0.01, 100], (optional)
    :param minor_radius: Minor Radius, Radius of the torus’ cross section 
    :type minor_radius: float in [0.01, 100], (optional)
    :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus 
    :type abso_major_rad: float in [0.01, 100], (optional)
    :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus 
    :type abso_minor_rad: float in [0.01, 100], (optional)
    '''

    pass


def primitive_uv_sphere_add(
        segments=32,
        ring_count=16,
        size=1.0,
        calc_uvs=False,
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False)):
    '''Construct a UV sphere mesh 

    :param segments: Segments 
    :type segments: int in [3, 100000], (optional)
    :param ring_count: Rings 
    :type ring_count: int in [3, 100000], (optional)
    :param size: Size 
    :type size: float in [0, inf], (optional)
    :param calc_uvs: Generate UVs, Generate a default UV map 
    :type calc_uvs: boolean, (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param layers: Layer 
    :type layers: boolean array of 20 items, (optional)
    '''

    pass


def quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY'):
    '''Triangulate selected faces 

    :param quad_method: Quad Method, Method for splitting the quads into trianglesBEAUTY Beauty , Split the quads in nice triangles, slower method.FIXED Fixed, Split the quads on the first and third vertices.FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices. 
    :type quad_method: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional)
    :param ngon_method: Polygon Method, Method for splitting the polygons into trianglesBEAUTY Beauty, Arrange the new triangles evenly (slow).CLIP Clip, Split the polygons with an ear clipping algorithm. 
    :type ngon_method: enum in ['BEAUTY', 'CLIP'], (optional)
    '''

    pass


def region_to_loop():
    '''Select boundary edges around the selected faces 

    '''

    pass


def remove_doubles(threshold=0.0001, use_unselected=False):
    '''Remove duplicate vertices 

    :param threshold: Merge Distance, Minimum distance between elements to merge 
    :type threshold: float in [1e-06, 50], (optional)
    :param use_unselected: Unselected, Merge selected to other unselected vertices 
    :type use_unselected: boolean, (optional)
    '''

    pass


def reveal():
    '''Reveal all hidden vertices, edges and faces 

    '''

    pass


def rip(mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        release_confirm=False,
        use_fill=False):
    '''Disconnect vertex or edges from connected geometry 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_fill: Fill, Fill the ripped region 
    :type use_fill: boolean, (optional)
    '''

    pass


def rip_edge(mirror=False,
             proportional='DISABLED',
             proportional_edit_falloff='SMOOTH',
             proportional_size=1.0,
             release_confirm=False):
    '''Extend vertices along the edge closest to the cursor 

    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    '''

    pass


def rip_edge_move(MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None):
    '''Extend vertices and move the result 

    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor 
    :type MESH_OT_rip_edge: MESH_OT_rip_edge, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def rip_move(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    '''Rip polygons and move the result 

    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry 
    :type MESH_OT_rip: MESH_OT_rip, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def rip_move_fill(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    '''Rip-fill polygons and move the result 

    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry 
    :type MESH_OT_rip: MESH_OT_rip, (optional)
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def screw(steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    '''Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport 

    :param steps: Steps, Steps 
    :type steps: int in [1, 100000], (optional)
    :param turns: Turns, Turns 
    :type turns: int in [1, 100000], (optional)
    :param center: Center, Center in global view space 
    :type center: float array of 3 items in [-inf, inf], (optional)
    :param axis: Axis, Axis in global view space 
    :type axis: float array of 3 items in [-1, 1], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''(De)select all vertices, edges or faces 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_axis(mode='POSITIVE', axis='X_AXIS', threshold=0.0001):
    '''Select all data in the mesh on a single axis 

    :param mode: Axis Mode, Axis side to use when selecting 
    :type mode: enum in ['POSITIVE', 'NEGATIVE', 'ALIGNED'], (optional)
    :param axis: Axis, Select the axis to compare each vertex on 
    :type axis: enum in ['X_AXIS', 'Y_AXIS', 'Z_AXIS'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [1e-06, 50], (optional)
    '''

    pass


def select_face_by_sides(number=4, type='EQUAL', extend=True):
    '''Select vertices or faces by the number of polygon sides 

    :param number: Number of Vertices 
    :type number: int in [3, inf], (optional)
    :param type: Type, Type of comparison to make 
    :type type: enum in ['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL'], (optional)
    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_interior_faces():
    '''Select faces where all edges have more than 2 face users 

    '''

    pass


def select_less(use_face_step=True):
    '''Deselect vertices, edges or faces at the boundary of each selection region 

    :param use_face_step: Face Step, Connected faces (instead of edges) 
    :type use_face_step: boolean, (optional)
    '''

    pass


def select_linked(delimit={'SEAM'}):
    '''Select all vertices linked to the active mesh 

    :param delimit: Delimit, Delimit selected regionNORMAL Normal, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)
    '''

    pass


def select_linked_pick(deselect=False, delimit={'SEAM'}, index=-1):
    '''(De)select all vertices linked to the edge under the mouse cursor 

    :param deselect: Deselect 
    :type deselect: boolean, (optional)
    :param delimit: Delimit, Delimit selected regionNORMAL Normal, Delimit by face directions.MATERIAL Material, Delimit by face material.SEAM Seam, Delimit by edge seams.SHARP Sharp, Delimit by sharp edges.UV UVs, Delimit by UV coordinates. 
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional)
    '''

    pass


def select_loose(extend=False):
    '''Select loose geometry based on the selection mode 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_mirror(axis={'X'}, extend=False):
    '''Select mesh items at mirrored locations 

    :param axis: Axis 
    :type axis: enum set in {'X', 'Y', 'Z'}, (optional)
    :param extend: Extend, Extend the existing selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_mode(use_extend=False,
                use_expand=False,
                type='VERT',
                action='TOGGLE'):
    '''Change selection mode 

    :param use_extend: Extend 
    :type use_extend: boolean, (optional)
    :param use_expand: Expand 
    :type use_expand: boolean, (optional)
    :param type: Type 
    :type type: enum in ['VERT', 'EDGE', 'FACE'], (optional)
    :param action: Action, Selection action to executeDISABLE Disable, Disable selected markers.ENABLE Enable, Enable selected markers.TOGGLE Toggle, Toggle disabled flag for selected markers. 
    :type action: enum in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional)
    '''

    pass


def select_more(use_face_step=True):
    '''Select more vertices, edges or faces connected to initial selection 

    :param use_face_step: Face Step, Connected faces (instead of edges) 
    :type use_face_step: boolean, (optional)
    '''

    pass


def select_next_item():
    '''Select the next element (using selection order) 

    '''

    pass


def select_non_manifold(extend=True,
                        use_wire=True,
                        use_boundary=True,
                        use_multi_face=True,
                        use_non_contiguous=True,
                        use_verts=True):
    '''Select all non-manifold vertices or edges 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    :param use_wire: Wire, Wire edges 
    :type use_wire: boolean, (optional)
    :param use_boundary: Boundaries, Boundary edges 
    :type use_boundary: boolean, (optional)
    :param use_multi_face: Multiple Faces, Edges shared by 3+ faces 
    :type use_multi_face: boolean, (optional)
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions 
    :type use_non_contiguous: boolean, (optional)
    :param use_verts: Vertices, Vertices connecting multiple face regions 
    :type use_verts: boolean, (optional)
    '''

    pass


def select_nth(nth=2, skip=1, offset=0):
    '''Deselect every Nth element starting from the active vertex, edge or face 

    :param nth: Nth Selection 
    :type nth: int in [2, inf], (optional)
    :param skip: Skip 
    :type skip: int in [1, inf], (optional)
    :param offset: Offset 
    :type offset: int in [-inf, inf], (optional)
    '''

    pass


def select_prev_item():
    '''Select the next element (using selection order) 

    '''

    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    '''Randomly select vertices 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float in [0, 100], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: enum in ['SELECT', 'DESELECT'], (optional)
    '''

    pass


def select_similar(type='NORMAL', compare='EQUAL', threshold=0.0):
    '''Select similar vertices, edges or faces by property types 

    :param type: Type 
    :type type: enum in ['NORMAL', 'FACE', 'VGROUP', 'EDGE', 'LENGTH', 'DIR', 'FACE', 'FACE_ANGLE', 'CREASE', 'BEVEL', 'SEAM', 'SHARP', 'FREESTYLE_EDGE', 'MATERIAL', 'IMAGE', 'AREA', 'SIDES', 'PERIMETER', 'NORMAL', 'COPLANAR', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
    :param compare: Compare 
    :type compare: enum in ['EQUAL', 'GREATER', 'LESS'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, 1], (optional)
    '''

    pass


def select_similar_region():
    '''Select similar face regions to the current selection 

    '''

    pass


def select_ungrouped(extend=False):
    '''Select vertices without a group 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def separate(type='SELECTED'):
    '''Separate selected geometry into a new mesh 

    :param type: Type 
    :type type: enum in ['SELECTED', 'MATERIAL', 'LOOSE'], (optional)
    '''

    pass


def shape_propagate_to_all():
    '''Apply selected vertex locations to all other shape keys 

    '''

    pass


def shortest_path_pick(use_face_step=False,
                       use_topology_distance=False,
                       use_fill=False,
                       nth=1,
                       skip=1,
                       offset=0,
                       index=-1):
    '''Select shortest path between two selections 

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) 
    :type use_face_step: boolean, (optional)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance 
    :type use_topology_distance: boolean, (optional)
    :param use_fill: Fill Region, Select all paths between the source/destination elements 
    :type use_fill: boolean, (optional)
    :param nth: Nth Selection 
    :type nth: int in [1, inf], (optional)
    :param skip: Skip 
    :type skip: int in [1, inf], (optional)
    :param offset: Offset 
    :type offset: int in [-inf, inf], (optional)
    '''

    pass


def shortest_path_select(use_face_step=False,
                         use_topology_distance=False,
                         use_fill=False,
                         nth=1,
                         skip=1,
                         offset=0):
    '''Selected vertex path between two vertices 

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings) 
    :type use_face_step: boolean, (optional)
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance 
    :type use_topology_distance: boolean, (optional)
    :param use_fill: Fill Region, Select all paths between the source/destination elements 
    :type use_fill: boolean, (optional)
    :param nth: Nth Selection 
    :type nth: int in [1, inf], (optional)
    :param skip: Skip 
    :type skip: int in [1, inf], (optional)
    :param offset: Offset 
    :type offset: int in [-inf, inf], (optional)
    '''

    pass


def solidify(thickness=0.01):
    '''Create a solid skin by extruding, compensating for sharp angles 

    :param thickness: Thickness 
    :type thickness: float in [-10000, 10000], (optional)
    '''

    pass


def sort_elements(type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0):
    '''The order of selected vertices/edges/faces is modified, based on a given method 

    :param type: Type, Type of re-ordering operation to applyVIEW_ZAXIS View Z Axis, Sort selected elements from farthest to nearest one in current view.VIEW_XAXIS View X Axis, Sort selected elements from left to right one in current view.CURSOR_DISTANCE Cursor Distance, Sort selected elements from nearest to farthest from 3D cursor.MATERIAL Material, Sort selected elements from smallest to greatest material index (faces only!).SELECTED Selected, Move all selected elements in first places, preserving their relative order (WARNING: this will affect unselected elements’ indices as well!).RANDOMIZE Randomize, Randomize order of selected elements.REVERSE Reverse, Reverse current order of selected elements. 
    :type type: enum in ['VIEW_ZAXIS', 'VIEW_XAXIS', 'CURSOR_DISTANCE', 'MATERIAL', 'SELECTED', 'RANDOMIZE', 'REVERSE'], (optional)
    :param elements: Elements, Which elements to affect (vertices, edges and/or faces) 
    :type elements: enum set in {'VERT', 'EDGE', 'FACE'}, (optional)
    :param reverse: Reverse, Reverse the sorting effect 
    :type reverse: boolean, (optional)
    :param seed: Seed, Seed for random-based operations 
    :type seed: int in [0, inf], (optional)
    '''

    pass


def spin(steps=9,
         dupli=False,
         angle=1.5708,
         center=(0.0, 0.0, 0.0),
         axis=(0.0, 0.0, 0.0)):
    '''Extrude selected vertices in a circle around the cursor in indicated viewport 

    :param steps: Steps, Steps 
    :type steps: int in [0, 1000000], (optional)
    :param dupli: Dupli, Make Duplicates 
    :type dupli: boolean, (optional)
    :param angle: Angle, Rotation for each step 
    :type angle: float in [-inf, inf], (optional)
    :param center: Center, Center in global view space 
    :type center: float array of 3 items in [-inf, inf], (optional)
    :param axis: Axis, Axis in global view space 
    :type axis: float array of 3 items in [-1, 1], (optional)
    '''

    pass


def split():
    '''Split off selected geometry from connected unselected geometry 

    '''

    pass


def subdivide(number_cuts=1,
              smoothness=0.0,
              quadtri=False,
              quadcorner='STRAIGHT_CUT',
              fractal=0.0,
              fractal_along_normal=0.0,
              seed=0):
    '''Subdivide selected edges 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [1, 100], (optional)
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float in [0, 1000], (optional)
    :param quadtri: Quad/Tri Mode, Tries to prevent ngons 
    :type quadtri: boolean, (optional)
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent ngons) 
    :type quadcorner: enum in ['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN'], (optional)
    :param fractal: Fractal, Fractal randomness factor 
    :type fractal: float in [0, 1e+06], (optional)
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only 
    :type fractal_along_normal: float in [0, 1], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    '''

    pass


def subdivide_edgering(number_cuts=10,
                       interpolation='PATH',
                       smoothness=1.0,
                       profile_shape_factor=0.0,
                       profile_shape='SMOOTH'):
    '''Undocumented 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [0, 1000], (optional)
    :param interpolation: Interpolation, Interpolation method 
    :type interpolation: enum in ['LINEAR', 'PATH', 'SURFACE'], (optional)
    :param smoothness: Smoothness, Smoothness factor 
    :type smoothness: float in [0, 1000], (optional)
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded 
    :type profile_shape_factor: float in [-1000, 1000], (optional)
    :param profile_shape: Profile Shape, Shape of the profileSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff. 
    :type profile_shape: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional)
    '''

    pass


def symmetrize(direction='NEGATIVE_X', threshold=0.0001):
    '''Enforce symmetry (both form and topological) across an axis 

    :param direction: Direction, Which sides to copy from and to 
    :type direction: enum in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, 10], (optional)
    '''

    pass


def symmetry_snap(direction='NEGATIVE_X',
                  threshold=0.05,
                  factor=0.5,
                  use_center=True):
    '''Snap vertex pairs to their mirrored locations 

    :param direction: Direction, Which sides to copy from and to 
    :type direction: enum in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, 10], (optional)
    :param factor: Factor 
    :type factor: float in [0, 1], (optional)
    :param use_center: Center, Snap mid verts to the axis center 
    :type use_center: boolean, (optional)
    '''

    pass


def tris_convert_to_quads(face_threshold=0.698132,
                          shape_threshold=0.698132,
                          uvs=False,
                          vcols=False,
                          seam=False,
                          sharp=False,
                          materials=False):
    '''Join triangles into quads 

    :param face_threshold: Max Face Angle, Face angle limit 
    :type face_threshold: float in [0, 3.14159], (optional)
    :param shape_threshold: Max Shape Angle, Shape angle limit 
    :type shape_threshold: float in [0, 3.14159], (optional)
    :param uvs: Compare UVs 
    :type uvs: boolean, (optional)
    :param vcols: Compare VCols 
    :type vcols: boolean, (optional)
    :param seam: Compare Seam 
    :type seam: boolean, (optional)
    :param sharp: Compare Sharp 
    :type sharp: boolean, (optional)
    :param materials: Compare Materials 
    :type materials: boolean, (optional)
    '''

    pass


def unsubdivide(iterations=2):
    '''UnSubdivide selected edges & faces 

    :param iterations: Iterations, Number of times to unsubdivide 
    :type iterations: int in [1, 1000], (optional)
    '''

    pass


def uv_texture_add():
    '''Add UV Map 

    '''

    pass


def uv_texture_remove():
    '''Remove UV Map 

    '''

    pass


def uvs_reverse():
    '''Flip direction of UV coordinates inside faces 

    '''

    pass


def uvs_rotate(use_ccw=False):
    '''Rotate UV coordinates inside faces 

    :param use_ccw: Counter Clockwise 
    :type use_ccw: boolean, (optional)
    '''

    pass


def vert_connect():
    '''Connect selected vertices of faces, splitting the face 

    '''

    pass


def vert_connect_concave():
    '''Make all faces convex 

    '''

    pass


def vert_connect_nonplanar(angle_limit=0.0872665):
    '''Split non-planar faces that exceed the angle threshold 

    :param angle_limit: Max Angle, Angle limit 
    :type angle_limit: float in [0, 3.14159], (optional)
    '''

    pass


def vert_connect_path():
    '''Connect vertices by their selection order, creating edges, splitting faces 

    '''

    pass


def vertex_color_add():
    '''Add vertex color layer 

    '''

    pass


def vertex_color_remove():
    '''Remove vertex color layer 

    '''

    pass


def vertices_smooth(factor=0.5, repeat=1, xaxis=True, yaxis=True, zaxis=True):
    '''Flatten angles of selected vertices 

    :param factor: Smoothing, Smoothing factor 
    :type factor: float in [-10, 10], (optional)
    :param repeat: Repeat, Number of times to smooth the mesh 
    :type repeat: int in [1, 1000], (optional)
    :param xaxis: X-Axis, Smooth along the X axis 
    :type xaxis: boolean, (optional)
    :param yaxis: Y-Axis, Smooth along the Y axis 
    :type yaxis: boolean, (optional)
    :param zaxis: Z-Axis, Smooth along the Z axis 
    :type zaxis: boolean, (optional)
    '''

    pass


def vertices_smooth_laplacian(repeat=1,
                              lambda_factor=5e-05,
                              lambda_border=5e-05,
                              use_x=True,
                              use_y=True,
                              use_z=True,
                              preserve_volume=True):
    '''Laplacian smooth of selected vertices 

    :param repeat: Number of iterations to smooth the mesh 
    :type repeat: int in [1, 1000], (optional)
    :param lambda_factor: Lambda factor 
    :type lambda_factor: float in [1e-07, 1000], (optional)
    :param lambda_border: Lambda factor in border 
    :type lambda_border: float in [1e-07, 1000], (optional)
    :param use_x: Smooth X Axis, Smooth object along X axis 
    :type use_x: boolean, (optional)
    :param use_y: Smooth Y Axis, Smooth object along Y axis 
    :type use_y: boolean, (optional)
    :param use_z: Smooth Z Axis, Smooth object along Z axis 
    :type use_z: boolean, (optional)
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth 
    :type preserve_volume: boolean, (optional)
    '''

    pass


def wireframe(use_boundary=True,
              use_even_offset=True,
              use_relative_offset=False,
              use_replace=True,
              thickness=0.01,
              offset=0.01,
              use_crease=False,
              crease_weight=0.01):
    '''Create a solid wire-frame from faces 

    :param use_boundary: Boundary, Inset face boundaries 
    :type use_boundary: boolean, (optional)
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness 
    :type use_even_offset: boolean, (optional)
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry 
    :type use_relative_offset: boolean, (optional)
    :param use_replace: Replace, Remove original faces 
    :type use_replace: boolean, (optional)
    :param thickness: Thickness 
    :type thickness: float in [0, 10000], (optional)
    :param offset: Offset 
    :type offset: float in [0, 10000], (optional)
    :param use_crease: Crease, Crease hub edges for improved subsurf 
    :type use_crease: boolean, (optional)
    :param crease_weight: Crease weight 
    :type crease_weight: float in [0, 1000], (optional)
    '''

    pass
