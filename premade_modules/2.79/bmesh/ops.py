def smooth_vert(bm, verts, factor, mirror_clip_x, mirror_clip_y, mirror_clip_z, clip_dist, use_axis_x, use_axis_y, use_axis_z):
    pass


def smooth_laplacian_vert(bm, verts, lambda_factor, lambda_border, use_x, use_y, use_z, preserve_volume):
    pass


def recalc_face_normals(bm, faces):
    pass


def planar_faces(bm, faces, iterations, factor):
    pass


def region_extend(bm, geom, use_contract, use_faces, use_face_step):
    pass


def rotate_edges(bm, edges, use_ccw):
    pass


def reverse_faces(bm, faces, flip_multires):
    pass


def bisect_edges(bm, edges, cuts, edge_percents):
    pass


def mirror(bm, geom, matrix, merge_dist, axis, mirror_u, mirror_v):
    pass


def find_doubles(bm, verts, keep_verts, dist):
    pass


def remove_doubles(bm, verts, dist):
    pass


def automerge(bm, verts, dist):
    pass


def collapse(bm, edges, uvs):
    pass


def pointmerge_facedata(bm, verts, vert_snap):
    pass


def average_vert_facedata(bm, verts):
    pass


def pointmerge(bm, verts, merge_co):
    pass


def collapse_uvs(bm, edges):
    pass


def weld_verts(bm, targetmap):
    pass


def create_vert(bm, co):
    pass


def join_triangles(bm, faces, cmp_seam, cmp_sharp, cmp_uvs, cmp_vcols, cmp_materials, angle_face_threshold, angle_shape_threshold):
    pass


def contextual_create(bm, geom, mat_nr, use_smooth):
    pass


def bridge_loops(bm, edges, use_pairs, use_cyclic, use_merge, merge_factor, twist_offset):
    pass


def grid_fill(bm, edges, mat_nr, use_smooth, use_interp_simple):
    pass


def holes_fill(bm, edges, sides):
    pass


def face_attribute_fill(bm, faces, use_normals, use_data):
    pass


def edgeloop_fill(bm, edges, mat_nr, use_smooth):
    pass


def edgenet_fill(bm, edges, mat_nr, use_smooth, sides):
    pass


def edgenet_prepare(bm, edges):
    pass


def rotate(bm, cent, matrix, verts, space):
    pass


def translate(bm, vec, space, verts):
    pass


def scale(bm, vec, space, verts):
    pass


def transform(bm, matrix, space, verts):
    pass


def object_load_bmesh(bm, scene, object):
    pass


def bmesh_to_mesh(bm, mesh, object, skip_tessface):
    pass


def mesh_to_bmesh(bm, mesh, object, use_shapekey):
    pass


def extrude_discrete_faces(bm, faces, use_select_history):
    pass


def extrude_edge_only(bm, edges, use_select_history):
    pass


def extrude_vert_indiv(bm, verts, use_select_history):
    pass


def connect_verts(bm, verts, faces_exclude, check_degenerate):
    pass


def connect_verts_concave(bm, faces):
    pass


def connect_verts_nonplanar(bm, angle_limit, faces):
    pass


def connect_vert_pair(bm, verts, verts_exclude, faces_exclude):
    pass


def extrude_face_region(bm, geom, edges_exclude, use_keep_orig, use_select_history):
    pass


def dissolve_verts(bm, verts, use_face_split, use_boundary_tear):
    pass


def dissolve_edges(bm, edges, use_verts, use_face_split):
    pass


def dissolve_faces(bm, faces, use_verts):
    pass


def dissolve_limit(bm, angle_limit, use_dissolve_boundaries, verts, edges, delimit):
    pass


def dissolve_degenerate(bm, dist, edges):
    pass


def triangulate(bm, faces, quad_method, ngon_method):
    pass


def unsubdivide(bm, verts, iterations):
    pass


def subdivide_edges(bm, edges, smooth, smooth_falloff, fractal, along_normal, cuts, seed, custom_patterns, edge_percents, quad_corner_type, use_grid_fill, use_single_edge, use_only_quads, use_sphere, use_smooth_even):
    pass


def subdivide_edgering(bm, edges, interp_mode, smooth, cuts, profile_shape, profile_shape_factor):
    pass


def bisect_plane(bm, geom, dist, plane_co, plane_no, use_snap_center, clear_outer, clear_inner):
    pass


def delete(bm, geom, context):
    pass


def duplicate(bm, geom, dest, use_select_history):
    pass


def split(bm, geom, dest, use_only_faces):
    pass


def spin(bm, geom, cent, axis, dvec, angle, space, steps, use_duplicate):
    pass


def similar_faces(bm, faces, type, thresh, compare):
    pass


def similar_edges(bm, edges, type, thresh, compare):
    pass


def similar_verts(bm, verts, type, thresh, compare):
    pass


def rotate_uvs(bm, faces, use_ccw):
    pass


def reverse_uvs(bm, faces):
    pass


def rotate_colors(bm, faces, use_ccw):
    pass


def reverse_colors(bm, faces):
    pass


def split_edges(bm, edges, verts, use_verts):
    pass


def create_grid(bm, x_segments, y_segments, size, matrix, calc_uvs):
    pass


def create_uvsphere(bm, u_segments, v_segments, diameter, matrix, calc_uvs):
    pass


def create_icosphere(bm, subdivisions, diameter, matrix, calc_uvs):
    pass


def create_monkey(bm, matrix, calc_uvs):
    pass


def create_cone(bm, cap_ends, cap_tris, segments, diameter1, diameter2, depth, matrix, calc_uvs):
    pass


def create_circle(bm, cap_ends, cap_tris, segments, diameter, matrix, calc_uvs):
    pass


def create_cube(bm, size, matrix, calc_uvs):
    pass


def bevel(bm, geom, offset, offset_type, segments, profile, vertex_only, clamp_overlap, material, loop_slide):
    pass


def beautify_fill(bm, faces, edges, use_restrict_tag, method):
    pass


def triangle_fill(bm, use_beauty, use_dissolve, edges, normal):
    pass


def solidify(bm, geom, thickness):
    pass


def inset_individual(bm, faces, thickness, depth, use_even_offset, use_interpolate, use_relative_offset):
    pass


def inset_region(bm, faces, faces_exclude, use_boundary, use_even_offset, use_interpolate, use_relative_offset, use_edge_rail, thickness, depth, use_outset):
    pass


def offset_edgeloops(bm, edges, use_cap_endpoint):
    pass


def wireframe(bm, faces, thickness, offset, use_replace, use_boundary, use_even_offset, use_crease, crease_weight, use_relative_offset, material_offset):
    pass


def poke(bm, faces, offset, center_mode, use_relative_offset):
    pass


def convex_hull(bm, input, use_existing_faces):
    pass


def symmetrize(bm, input, direction, dist):
    pass


