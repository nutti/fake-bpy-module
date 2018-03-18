class UILayout:
    active = None
    alert = None
    alignment = None
    enabled = None
    operator_context = None
    scale_x = None
    scale_y = None

    def row(self, align=False):
        pass

    def column(self, align=False):
        pass

    def column_flow(self, columns=0, align=False):
        pass

    def box(self):
        pass

    def split(self, percentage=0.0, align=False):
        pass

    def menu_pie(self):
        pass

    def prop(self, data, property, text="", text_ctxt="", translate=True, icon='NONE', expand=False, slider=False, toggle=False, icon_only=False, event=False, full_event=False, emboss=True, index=-1, icon_value=0):
        pass

    def props_enum(self, data, property):
        pass

    def prop_menu_enum(self, data, property, text="", text_ctxt="", translate=True, icon='NONE'):
        pass

    def prop_enum(self, data, property, value, text="", text_ctxt="", translate=True, icon='NONE'):
        pass

    def prop_search(self, data, property, search_data, search_property, text="", text_ctxt="", translate=True, icon='NONE'):
        pass

    def operator(self, operator, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, icon_value=0):
        pass

    def operator_enum(self, operator, property):
        pass

    def operator_menu_enum(self, operator, property, text="", text_ctxt="", translate=True, icon='NONE'):
        pass

    def label(self, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0):
        pass

    def menu(self, menu, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0):
        pass

    def separator(self):
        pass

    def context_pointer_set(self, name, data):
        pass

    def template_header(self):
        pass

    def template_ID(self, data, property, new="", open="", unlink=""):
        pass

    def template_ID_preview(self, data, property, new="", open="", unlink="", rows=0, cols=0):
        pass

    def template_any_ID(self, data, property, type_property, text="", text_ctxt="", translate=True):
        pass

    def template_path_builder(self, data, property, root, text="", text_ctxt="", translate=True):
        pass

    def template_modifier(self, data):
        pass

    def template_constraint(self, data):
        pass

    def template_preview(self, id, show_buttons=True, parent=None, slot=None, preview_id=""):
        pass

    def template_curve_mapping(self, data, property, type='NONE', levels=False, brush=False, use_negative_slope=False):
        pass

    def template_color_ramp(self, data, property, expand=False):
        pass

    def template_icon_view(self, data, property, show_labels=False, scale=5.0):
        pass

    def template_histogram(self, data, property):
        pass

    def template_waveform(self, data, property):
        pass

    def template_vectorscope(self, data, property):
        pass

    def template_layers(self, data, property, used_layers_data, used_layers_property, active_layer):
        pass

    def template_color_picker(self, data, property, value_slider=False, lock=False, lock_luminosity=False, cubic=False):
        pass

    def template_palette(self, data, property, color=False):
        pass

    def template_image_layers(self, image, image_user):
        pass

    def template_image(self, data, property, image_user, compact=False, multiview=False):
        pass

    def template_image_settings(self, image_settings, color_management=False):
        pass

    def template_image_stereo_3d(self, stereo_3d_format):
        pass

    def template_image_views(self, image_settings):
        pass

    def template_movieclip(self, data, property, compact=False):
        pass

    def template_track(self, data, property):
        pass

    def template_marker(self, data, property, clip_user, track, compact=False):
        pass

    def template_movieclip_information(self, data, property, clip_user):
        pass

    def template_list(self, listtype_name, list_id="", dataptr, propname, active_dataptr, active_propname, item_dyntip_propname="", rows=5, maxrows=5, type='DEFAULT', columns=9):
        pass

    def template_running_jobs(self):
        pass

    def template_operator_search(self):
        pass

    def template_header_3D(self):
        pass

    def template_edit_mode_selection(self):
        pass

    def template_reports_banner(self):
        pass

    def template_node_link(self, ntree, node, socket):
        pass

    def template_node_view(self, ntree, node, socket):
        pass

    def template_texture_user(self):
        pass

    def template_keymap_item_properties(self, item):
        pass

    def template_component_menu(self, data, property, name=""):
        pass

    def introspect(self):
        pass

    def template_colorspace_settings(self, data, property):
        pass

    def template_colormanaged_view_settings(self, data, property):
        pass

    def template_node_socket(self, color=(0.0, 0.0, 0.0, 1.0)):
        pass

    def template_cache_file(self, data, property):
        pass



