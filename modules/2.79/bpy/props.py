def BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
    pass


def BoolVectorProperty(name="", description="", default=(False, False, False), options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None):
    pass


def CollectionProperty(type=None, name="", description="", options={'ANIMATABLE'}):
    pass


def EnumProperty(items, name="", description="", default=None, options={'ANIMATABLE'}, update=None, get=None, set=None):
    pass


def FloatProperty(name="", description="", default=0.0, min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', update=None, get=None, set=None):
    pass


def FloatVectorProperty(name="", description="", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None):
    pass


def IntProperty(name="", description="", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
    pass


def IntVectorProperty(name="", description="", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None):
    pass


def PointerProperty(type=None, name="", description="", options={'ANIMATABLE'}, poll=None, update=None):
    pass


def RemoveProperty(cls, attr):
    pass


def StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
    pass


