def beautify_fill(angle_limit=3.14159):
    pass


def bevel(offset_type='OFFSET', offset=0.0, segments=1, profile=0.5, vertex_only=False, clamp_overlap=False, loop_slide=True, material=-1):
    pass


def bisect(plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
    pass


def blend_from_shape(shape='', blend=1.0, add=True):
    pass


def bridge_edge_loops(type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
    pass


def colors_reverse():
    pass


def colors_rotate(use_ccw=False):
    pass


def convex_hull(delete_unused=True, use_existing_faces=True, make_holes=False, join_triangles=True, face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
    pass


def customdata_custom_splitnormals_add():
    pass


def customdata_custom_splitnormals_clear():
    pass


def customdata_mask_clear():
    pass


def customdata_skin_add():
    pass


def customdata_skin_clear():
    pass


def decimate(ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y'):
    pass


def delete(type='VERT'):
    pass


def delete_edgeloop(use_face_split=True):
    pass


def delete_loose(use_verts=True, use_edges=True, use_faces=False):
    pass


def dissolve_degenerate(threshold=0.0001):
    pass


def dissolve_edges(use_verts=True, use_face_split=False):
    pass


def dissolve_faces(use_verts=False):
    pass


def dissolve_limited(angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'}):
    pass


def dissolve_mode(use_verts=False, use_face_split=False, use_boundary_tear=False):
    pass


def dissolve_verts(use_face_split=False, use_boundary_tear=False):
    pass


def drop_named_image(name="Image", filepath="Path", relative_path=True):
    pass


def dupli_extrude_cursor(rotate_source=True):
    pass


def duplicate(mode=1):
    pass


def duplicate_move(MESH_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def edge_collapse():
    pass


def edge_face_add():
    pass


def edge_rotate(use_ccw=False):
    pass


def edge_split():
    pass


def edgering_select(extend=False, deselect=False, toggle=False, ring=True):
    pass


def edges_select_sharp(sharpness=0.523599):
    pass


def extrude_edges_indiv(mirror=False):
    pass


def extrude_edges_move(MESH_OT_extrude_edges_indiv=None, TRANSFORM_OT_translate=None):
    pass


def extrude_faces_indiv(mirror=False):
    pass


def extrude_faces_move(MESH_OT_extrude_faces_indiv=None, TRANSFORM_OT_shrink_fatten=None):
    pass


def extrude_region(mirror=False):
    pass


def extrude_region_move(MESH_OT_extrude_region=None, TRANSFORM_OT_translate=None):
    pass


def extrude_region_shrink_fatten(MESH_OT_extrude_region=None, TRANSFORM_OT_shrink_fatten=None):
    pass


def extrude_repeat(offset=2.0, steps=10):
    pass


def extrude_vertices_move(MESH_OT_extrude_verts_indiv=None, TRANSFORM_OT_translate=None):
    pass


def extrude_verts_indiv(mirror=False):
    pass


def face_make_planar(factor=1.0, repeat=1):
    pass


def face_split_by_edges():
    pass


def faces_mirror_uv(direction='POSITIVE', precision=3):
    pass


def faces_select_linked_flat(sharpness=0.0174533):
    pass


def faces_shade_flat():
    pass


def faces_shade_smooth():
    pass


def fill(use_beauty=True):
    pass


def fill_grid(span=1, offset=0, use_interp_simple=False):
    pass


def fill_holes(sides=4):
    pass


def flip_normals():
    pass


def hide(unselected=False):
    pass


def inset(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.01, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True):
    pass


def intersect(mode='SELECT_UNSELECT', separate_mode='CUT', threshold=1e-06):
    pass


def intersect_boolean(operation='DIFFERENCE', use_swap=False, threshold=1e-06):
    pass


def knife_project(cut_through=False):
    pass


def knife_tool(use_occlude_geometry=True, only_selected=False):
    pass


def loop_multi_select(ring=False):
    pass


def loop_select(extend=False, deselect=False, toggle=False, ring=False):
    pass


def loop_to_region(select_bigger=False):
    pass


def loopcut(number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', edge_index=-1, mesh_select_mode_init=(False, False, False)):
    pass


def loopcut_slide(MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None):
    pass


def mark_freestyle_edge(clear=False):
    pass


def mark_freestyle_face(clear=False):
    pass


def mark_seam(clear=False):
    pass


def mark_sharp(clear=False, use_verts=False):
    pass


def merge(type='CENTER', uvs=False):
    pass


def navmesh_clear():
    pass


def navmesh_face_add():
    pass


def navmesh_face_copy():
    pass


def navmesh_make():
    pass


def navmesh_reset():
    pass


def noise(factor=0.1):
    pass


def normals_make_consistent(inside=False):
    pass


def offset_edge_loops(use_cap_endpoint=False):
    pass


def offset_edge_loops_slide(MESH_OT_offset_edge_loops=None, TRANSFORM_OT_edge_slide=None):
    pass


def poke(offset=0.0, use_relative_offset=False, center_mode='MEAN_WEIGHTED'):
    pass


def primitive_circle_add(vertices=32, radius=1.0, fill_type='NOTHING', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_cone_add(vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_cube_add(radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_cylinder_add(vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_grid_add(x_subdivisions=10, y_subdivisions=10, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_ico_sphere_add(subdivisions=2, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_monkey_add(radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_plane_add(radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def primitive_torus_add(rotation=(0.0, 0.0, 0.0), view_align=False, location=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs=False):
    pass


def primitive_uv_sphere_add(segments=32, ring_count=16, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY'):
    pass


def region_to_loop():
    pass


def remove_doubles(threshold=0.0001, use_unselected=False):
    pass


def reveal():
    pass


def rip(mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False, use_accurate=False, use_fill=False):
    pass


def rip_edge(mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False, use_accurate=False):
    pass


def rip_edge_move(MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None):
    pass


def rip_move(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    pass


def rip_move_fill(MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    pass


def screw(steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    pass


def select_all(action='TOGGLE'):
    pass


def select_axis(mode='POSITIVE', axis='X_AXIS', threshold=0.0001):
    pass


def select_face_by_sides(number=4, type='EQUAL', extend=True):
    pass


def select_interior_faces():
    pass


def select_less(use_face_step=True):
    pass


def select_linked(delimit={'SEAM'}):
    pass


def select_linked_pick(deselect=False, delimit={'SEAM'}, index=-1):
    pass


def select_loose(extend=False):
    pass


def select_mirror(axis={'X'}, extend=False):
    pass


def select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE'):
    pass


def select_more(use_face_step=True):
    pass


def select_next_item():
    pass


def select_non_manifold(extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True):
    pass


def select_nth(nth=2, skip=1, offset=0):
    pass


def select_prev_item():
    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    pass


def select_similar(type='NORMAL', compare='EQUAL', threshold=0.0):
    pass


def select_similar_region():
    pass


def select_ungrouped(extend=False):
    pass


def separate(type='SELECTED'):
    pass


def set_normals_from_faces():
    pass


def shape_propagate_to_all():
    pass


def shortest_path_pick(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0, index=-1):
    pass


def shortest_path_select(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0):
    pass


def solidify(thickness=0.01):
    pass


def sort_elements(type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0):
    pass


def spin(steps=9, dupli=False, angle=1.5708, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    pass


def split():
    pass


def subdivide(number_cuts=1, smoothness=0.0, quadtri=False, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0):
    pass


def subdivide_edgering(number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
    pass


def symmetrize(direction='NEGATIVE_X', threshold=0.0001):
    pass


def symmetry_snap(direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True):
    pass


def tris_convert_to_quads(face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
    pass


def unsubdivide(iterations=2):
    pass


def uv_texture_add():
    pass


def uv_texture_remove():
    pass


def uvs_reverse():
    pass


def uvs_rotate(use_ccw=False):
    pass


def vert_connect():
    pass


def vert_connect_concave():
    pass


def vert_connect_nonplanar(angle_limit=0.0872665):
    pass


def vert_connect_path():
    pass


def vertex_color_add():
    pass


def vertex_color_remove():
    pass


def vertices_smooth(factor=0.5, repeat=1, xaxis=True, yaxis=True, zaxis=True):
    pass


def vertices_smooth_laplacian(repeat=1, lambda_factor=5e-05, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True):
    pass


def wireframe(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01):
    pass


