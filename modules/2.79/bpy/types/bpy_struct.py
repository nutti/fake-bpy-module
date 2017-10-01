class bpy_struct:
    id_data = None

    def as_pointer(self):
        pass

    def driver_add(self, path, index=-1):
        pass

    def driver_remove(self, path, index=-1):
        pass

    def get(self, key, default=None):
        pass

    def is_property_hidden(self, property):
        pass

    def is_property_readonly(self, property):
        pass

    def is_property_set(self, property):
        pass

    def items(self):
        pass

    def keyframe_delete(self, data_path, index=-1, frame=bpy.context.scene.frame_current, group=""):
        pass

    def keyframe_insert(self, data_path, index=-1, frame=bpy.context.scene.frame_current, group=""):
        pass

    def keys(self):
        pass

    def path_from_id(self, property=""):
        pass

    def path_resolve(self, path, coerce=True):
        pass

    def property_unset(self, property):
        pass

    def type_recast(self):
        pass

    def values(self):
        pass



