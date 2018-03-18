class KeyingSetInfo:
    bl_description = None
    bl_idname = None
    bl_label = None
    bl_options = None

    def poll(self, context):
        pass

    def iterator(self, context, ks):
        pass

    def generate(self, context, ks, data):
        pass



