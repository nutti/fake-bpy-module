def add(radius=1.0, type='EMPTY', view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def add_named(linked=False, name=""):
    pass


def align(bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={}):
    pass


def anim_transforms_to_deltas():
    pass


def armature_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def bake(type='COMBINED', pass_filter={}, filepath="", width=512, height=512, margin=16, use_selected_to_active=False, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer=""):
    pass


def bake_image():
    pass


def camera_add(view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def constraint_add(type=''):
    pass


def constraint_add_with_targets(type=''):
    pass


def constraints_clear():
    pass


def constraints_copy():
    pass


def convert(target='MESH', keep_original=False):
    pass


def correctivesmooth_bind(modifier=""):
    pass


def data_transfer(use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0):
    pass


def datalayout_transfer(modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE'):
    pass


def delete(use_global=False):
    pass


def drop_named_image(filepath="", relative_path=True, name="", view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def drop_named_material(name="Material"):
    pass


def dupli_offset_from_cursor():
    pass


def duplicate(linked=False, mode='TRANSLATION'):
    pass


def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def duplicate_move_linked(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def duplicates_make_real(use_base_parent=False, use_hierarchy=False):
    pass


def editmode_toggle():
    pass


def effector_add(type='FORCE', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def empty_add(type='PLAIN_AXES', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def explode_refresh(modifier=""):
    pass


def forcefield_toggle():
    pass


def game_physics_copy():
    pass


def game_property_clear():
    pass


def game_property_copy(operation='COPY', property=''):
    pass


def game_property_move(index=0, direction='UP'):
    pass


def game_property_new(type='FLOAT', name=""):
    pass


def game_property_remove(index=0):
    pass


def group_add():
    pass


def group_instance_add(name="Group", group='', view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def group_link(group=''):
    pass


def group_remove():
    pass


def group_unlink():
    pass


def grouped_select():
    pass


def hide_render_clear():
    pass


def hide_render_clear_all():
    pass


def hide_render_set(unselected=False):
    pass


def hide_view_clear():
    pass


def hide_view_set(unselected=False):
    pass


def hook_add_newob():
    pass


def hook_add_selob(use_bone=False):
    pass


def hook_assign(modifier=''):
    pass


def hook_recenter(modifier=''):
    pass


def hook_remove(modifier=''):
    pass


def hook_reset(modifier=''):
    pass


def hook_select(modifier=''):
    pass


def isolate_type_render():
    pass


def join():
    pass


def join_shapes():
    pass


def join_uvs():
    pass


def lamp_add(type='POINT', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def laplaciandeform_bind(modifier=""):
    pass


def location_clear(clear_delta=False):
    pass


def lod_add():
    pass


def lod_by_name():
    pass


def lod_clear_all():
    pass


def lod_generate(count=3, target=0.1, package=False):
    pass


def lod_remove(index=1):
    pass


def logic_bricks_copy():
    pass


def make_dupli_face():
    pass


def make_links_data(type='OBDATA'):
    pass


def make_links_scene(scene=''):
    pass


def make_local(type='SELECT_OBJECT'):
    pass


def make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=False, texture=False, animation=False):
    pass


def material_slot_add():
    pass


def material_slot_assign():
    pass


def material_slot_copy():
    pass


def material_slot_deselect():
    pass


def material_slot_move(direction='UP'):
    pass


def material_slot_remove():
    pass


def material_slot_select():
    pass


def meshdeform_bind(modifier=""):
    pass


def metaball_add(type='BALL', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def mode_set(mode='OBJECT', toggle=False):
    pass


def modifier_add(type='SUBSURF'):
    pass


def modifier_apply(apply_as='DATA', modifier=""):
    pass


def modifier_convert(modifier=""):
    pass


def modifier_copy(modifier=""):
    pass


def modifier_move_down(modifier=""):
    pass


def modifier_move_up(modifier=""):
    pass


def modifier_remove(modifier=""):
    pass


def move_to_layer(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def multires_base_apply(modifier=""):
    pass


def multires_external_pack():
    pass


def multires_external_save(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=True, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', modifier=""):
    pass


def multires_higher_levels_delete(modifier=""):
    pass


def multires_reshape(modifier=""):
    pass


def multires_subdivide(modifier=""):
    pass


def ocean_bake(modifier="", free=False):
    pass


def origin_clear():
    pass


def origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN'):
    pass


def parent_clear(type='CLEAR'):
    pass


def parent_no_inverse_set():
    pass


def parent_set(type='OBJECT', xmirror=False, keep_transform=False):
    pass


def particle_system_add():
    pass


def particle_system_remove():
    pass


def paths_calculate(start_frame=1, end_frame=250):
    pass


def paths_clear(only_selected=False):
    pass


def paths_update():
    pass


def posemode_toggle():
    pass


def proxy_make(object='DEFAULT'):
    pass


def quick_explode(style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True):
    pass


def quick_fluid(style='BASIC', initial_velocity=(0.0, 0.0, 0.0), show_flows=False, start_baking=False):
    pass


def quick_fur(density='MEDIUM', view_percentage=10, length=0.1):
    pass


def quick_smoke(style='SMOKE', show_flows=False):
    pass


def randomize_transform(random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0)):
    pass


def rotation_clear(clear_delta=False):
    pass


def scale_clear(clear_delta=False):
    pass


def select_all(action='TOGGLE'):
    pass


def select_by_layer(match='EXACT', extend=False, layers=1):
    pass


def select_by_type(extend=False, type='MESH'):
    pass


def select_camera(extend=False):
    pass


def select_grouped(extend=False, type='CHILDREN_RECURSIVE'):
    pass


def select_hierarchy(direction='PARENT', extend=False):
    pass


def select_less():
    pass


def select_linked(extend=False, type='OBDATA'):
    pass


def select_mirror(extend=False):
    pass


def select_more():
    pass


def select_pattern(pattern="*", case_sensitive=False, extend=True):
    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    pass


def select_same_group(group=""):
    pass


def shade_flat():
    pass


def shade_smooth():
    pass


def shape_key_add(from_mix=True):
    pass


def shape_key_clear():
    pass


def shape_key_mirror(use_topology=False):
    pass


def shape_key_move(type='TOP'):
    pass


def shape_key_remove(all=False):
    pass


def shape_key_retime():
    pass


def shape_key_transfer(mode='OFFSET', use_clamp=False):
    pass


def skin_armature_create(modifier=""):
    pass


def skin_loose_mark_clear(action='MARK'):
    pass


def skin_radii_equalize():
    pass


def skin_root_mark():
    pass


def slow_parent_clear():
    pass


def slow_parent_set():
    pass


def speaker_add(view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def subdivision_set(level=1, relative=False):
    pass


def surfacedeform_bind(modifier=""):
    pass


def text_add(radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    pass


def track_clear(type='CLEAR'):
    pass


def track_set(type='DAMPTRACK'):
    pass


def transform_apply(location=False, rotation=False, scale=False):
    pass


def transforms_to_deltas(mode='ALL', reset_values=True):
    pass


def unlink_data():
    pass


def vertex_group_add():
    pass


def vertex_group_assign():
    pass


def vertex_group_assign_new():
    pass


def vertex_group_clean(group_select_mode='', limit=0.0, keep_single=False):
    pass


def vertex_group_copy():
    pass


def vertex_group_copy_to_linked():
    pass


def vertex_group_copy_to_selected():
    pass


def vertex_group_deselect():
    pass


def vertex_group_fix(dist=0.0, strength=1.0, accuracy=1.0):
    pass


def vertex_group_invert(group_select_mode='', auto_assign=True, auto_remove=True):
    pass


def vertex_group_levels(group_select_mode='', offset=0.0, gain=1.0):
    pass


def vertex_group_limit_total(group_select_mode='', limit=4):
    pass


def vertex_group_lock(action='TOGGLE'):
    pass


def vertex_group_mirror(mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False):
    pass


def vertex_group_move(direction='UP'):
    pass


def vertex_group_normalize():
    pass


def vertex_group_normalize_all(group_select_mode='', lock_active=True):
    pass


def vertex_group_quantize(group_select_mode='', steps=4):
    pass


def vertex_group_remove(all=False, all_unlocked=False):
    pass


def vertex_group_remove_from(use_all_groups=False, use_all_verts=False):
    pass


def vertex_group_select():
    pass


def vertex_group_set_active(group=''):
    pass


def vertex_group_smooth(group_select_mode='', factor=0.5, repeat=1, expand=0.0, source='ALL'):
    pass


def vertex_group_sort(sort_type='NAME'):
    pass


def vertex_parent_set():
    pass


def vertex_weight_copy():
    pass


def vertex_weight_delete(weight_group=-1):
    pass


def vertex_weight_normalize_active_vertex():
    pass


def vertex_weight_paste(weight_group=-1):
    pass


def vertex_weight_set_active(weight_group=-1):
    pass


def visual_transform_apply():
    pass


