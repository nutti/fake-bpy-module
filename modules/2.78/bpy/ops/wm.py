def addon_disable(module=""):
    pass


def addon_enable(module=""):
    pass


def addon_expand(module=""):
    pass


def addon_install(overwrite=True, target='DEFAULT', filepath="", filter_folder=True, filter_python=True, filter_glob="*.py;*.zip"):
    pass


def addon_refresh():
    pass


def addon_remove(module=""):
    pass


def alembic_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', start=1, end=1, xsamples=1, gsamples=1, sh_open=0.0, sh_close=1.0, selected=False, renderable_only=True, visible_layers_only=False, flatten=False, uvs=True, packuv=True, normals=True, vcolors=False, face_sets=False, subdiv_schema=False, apply_subdiv=False, compression_type='OGAWA', global_scale=1.0):
    pass


def alembic_import(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', scale=1.0, set_frame_range=True, validate_meshes=False, is_sequence=False):
    pass


def appconfig_activate(filepath=""):
    pass


def appconfig_default():
    pass


def append(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=False, autoselect=True, active_layer=True, instance_groups=False, set_fake=False, use_recursive=True):
    pass


def blenderplayer_start():
    pass


def call_menu(name=""):
    pass


def call_menu_pie(name=""):
    pass


def collada_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', apply_modifiers=False, export_mesh_type=0, export_mesh_type_selection='view', selected=False, include_children=False, include_armatures=False, include_shapekeys=True, deform_bones_only=False, active_uv_only=False, include_uv_textures=False, include_material_textures=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_transformation_type=0, export_transformation_type_selection='matrix', open_sim=False):
    pass


def collada_import(filepath="", filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', import_units=False, fix_orientation=False, find_chains=False, auto_connect=False, min_chain_length=0):
    pass


def context_collection_boolean_set(data_path_iter="", data_path_item="", type='TOGGLE'):
    pass


def context_cycle_array(data_path="", reverse=False):
    pass


def context_cycle_enum(data_path="", reverse=False, wrap=False):
    pass


def context_cycle_int(data_path="", reverse=False, wrap=False):
    pass


def context_menu_enum(data_path=""):
    pass


def context_modal_mouse(data_path_iter="", data_path_item="", header_text="", input_scale=0.01, invert=False, initial_x=0):
    pass


def context_pie_enum(data_path=""):
    pass


def context_scale_float(data_path="", value=1.0):
    pass


def context_scale_int(data_path="", value=1.0, always_step=True):
    pass


def context_set_boolean(data_path="", value=True):
    pass


def context_set_enum(data_path="", value=""):
    pass


def context_set_float(data_path="", value=0.0, relative=False):
    pass


def context_set_id(data_path="", value=""):
    pass


def context_set_int(data_path="", value=0, relative=False):
    pass


def context_set_string(data_path="", value=""):
    pass


def context_set_value(data_path="", value=""):
    pass


def context_toggle(data_path=""):
    pass


def context_toggle_enum(data_path="", value_1="", value_2=""):
    pass


def copy_prev_settings():
    pass


def debug_menu(debug_value=0):
    pass


def dependency_relations():
    pass


def doc_view(doc_id=""):
    pass


def doc_view_manual(doc_id=""):
    pass


def doc_view_manual_ui_context():
    pass


def interaction_preset_add(name="", remove_active=False):
    pass


def interface_theme_preset_add(name="", remove_active=False):
    pass


def keyconfig_activate(filepath=""):
    pass


def keyconfig_export(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True):
    pass


def keyconfig_import(filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True, keep_original=True):
    pass


def keyconfig_preset_add(name="", remove_active=False):
    pass


def keyconfig_remove():
    pass


def keyconfig_test():
    pass


def keyitem_add():
    pass


def keyitem_remove(item_id=0):
    pass


def keyitem_restore(item_id=0):
    pass


def keymap_restore(all=False):
    pass


def lib_reload(library="", filepath="", directory="", filename="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    pass


def lib_relocate(library="", filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    pass


def link(filepath="", directory="", filename="", files=None, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', link=True, autoselect=True, active_layer=True, instance_groups=True):
    pass


def memory_statistics():
    pass


def open_mainfile(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', load_ui=True, use_scripts=True):
    pass


def operator_cheat_sheet():
    pass


def operator_defaults():
    pass


def operator_pie_enum(data_path="", prop_string=""):
    pass


def operator_preset_add(name="", remove_active=False, operator=""):
    pass


def path_open(filepath=""):
    pass


def previews_batch_clear(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
    pass


def previews_batch_generate(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_groups=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
    pass


def previews_clear(id_type={'GROUP', 'IMAGE', 'LAMP', 'MATERIAL', 'OBJECT', 'SCENE', 'TEXTURE', 'WORLD'}):
    pass


def previews_ensure():
    pass


def properties_add(data_path=""):
    pass


def properties_context_change(context=""):
    pass


def properties_edit(data_path="", property="", value="", min=-10000, max=10000.0, use_soft_limits=False, soft_min=-10000, soft_max=10000.0, description=""):
    pass


def properties_remove(data_path="", property=""):
    pass


def quit_blender():
    pass


def radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False):
    pass


def read_factory_settings():
    pass


def read_history():
    pass


def read_homefile(filepath="", load_ui=True):
    pass


def recover_auto_save(filepath="", filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=False, filter_blenlib=False, filemode=8, display_type='LIST_LONG', sort_method='FILE_SORT_TIME'):
    pass


def recover_last_session():
    pass


def redraw_timer(type='DRAW', iterations=10, time_limit=0.0):
    pass


def revert_mainfile(use_scripts=True):
    pass


def save_as_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=True, copy=False, use_mesh_compat=False):
    pass


def save_homefile():
    pass


def save_mainfile(filepath="", check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=False):
    pass


def save_userpref():
    pass


def search_menu():
    pass


def set_stereo_3d(display_mode='ANAGLYPH', anaglyph_type='RED_CYAN', interlace_type='ROW_INTERLEAVED', use_interlace_swap=False, use_sidebyside_crosseyed=False):
    pass


def splash():
    pass


def sysinfo(filepath=""):
    pass


def theme_install(overwrite=True, filepath="", filter_folder=True, filter_glob="*.xml"):
    pass


def url_open(url=""):
    pass


def userpref_autoexec_path_add():
    pass


def userpref_autoexec_path_remove(index=0):
    pass


def window_close():
    pass


def window_duplicate():
    pass


def window_fullscreen_toggle():
    pass


