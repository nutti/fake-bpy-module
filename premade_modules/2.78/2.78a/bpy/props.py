def BoolProperty(name="",
                 description="",
                 default=False,
                 options={'ANIMATABLE'},
                 subtype='NONE',
                 update=None,
                 get=None,
                 set=None):
    '''Returns a new boolean property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘PIXEL’, ‘UNSIGNED’, ‘PERCENTAGE’, ‘FACTOR’, ‘ANGLE’, ‘TIME’, ‘DISTANCE’, ‘NONE’]. 
    :type subtype: string
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def BoolVectorProperty(name="",
                       description="",
                       default=(False, False, False),
                       options={'ANIMATABLE'},
                       subtype='NONE',
                       size=3,
                       update=None,
                       get=None,
                       set=None):
    '''Returns a new vector boolean property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param default: sequence of booleans the length of size. 
    :type default: sequence
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘COLOR’, ‘TRANSLATION’, ‘DIRECTION’, ‘VELOCITY’, ‘ACCELERATION’, ‘MATRIX’, ‘EULER’, ‘QUATERNION’, ‘AXISANGLE’, ‘XYZ’, ‘COLOR_GAMMA’, ‘LAYER’, ‘NONE’]. 
    :type subtype: string
    :param size: Vector dimensions in [1, 32]. 
    :type size: int
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def CollectionProperty(type=None,
                       name="",
                       description="",
                       options={'ANIMATABLE'}):
    '''Returns a new collection property definition. 

    :param type: A subclass of bpy.types.PropertyGroup. 
    :type type: class
    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    '''

    pass


def EnumProperty(items,
                 name="",
                 description="",
                 default=None,
                 options={'ANIMATABLE'},
                 update=None,
                 get=None,
                 set=None):
    '''Returns a new enumerator property definition. 

    :param items: sequence of enum items formatted: [(identifier, name, description, icon, number), ...].The first three elements of the tuples are mandatory.identifierThe identifier is used for Python access.nameName for the interace.descriptionUsed for documentation and tooltips.iconAn icon string identifier or integer icon value (e.g. returned by bpy.types.UILayout.icon)numberUnique value used as the identifier for this item (stored in file data). Use when the identifier may need to change.When an item only contains 4 items they define (identifier, name, description, number).For dynamic values a callback can be passed which returns a list in the same format as the static list. This function must take 2 arguments (self, context), context may be None.There is a known bug with using a callback, Python must keep a reference to the strings returned or Blender will crash. 
    :type items: sequence of string tuples or a function
    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param default: The default value for this enum, a string from the identifiers used in items. If the ENUM_FLAG option is used this must be a set of such string identifiers instead. WARNING: It shall not be specified (or specified to its default None value) for dynamic enums (i.e. if a callback function is given as items parameter). 
    :type default: string or set
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘ENUM_FLAG’, ‘LIBRARY_EDITABLE’]. 
    :type options: set
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def FloatProperty(name="",
                  description="",
                  default=0.0,
                  min=sys.float_info.min,
                  max=sys.float_info.max,
                  soft_min=sys.float_info.min,
                  soft_max=sys.float_info.max,
                  step=3,
                  precision=2,
                  options={'ANIMATABLE'},
                  subtype='NONE',
                  unit='NONE',
                  update=None,
                  get=None,
                  set=None):
    '''Returns a new float property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead. 
    :type min: float
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead. 
    :type max: float
    :param soft_min: Soft minimum (>= min), user won’t be able to drag the widget below this value in the UI. 
    :type soft_min: float
    :param soft_max: Soft maximum (<= max), user won’t be able to drag the widget above this value in the UI. 
    :type soft_max: float
    :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100). 
    :type step: int
    :param precision: Maximum number of decimal digits to display, in [0, 6]. 
    :type precision: int
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘PIXEL’, ‘UNSIGNED’, ‘PERCENTAGE’, ‘FACTOR’, ‘ANGLE’, ‘TIME’, ‘DISTANCE’, ‘NONE’]. 
    :type subtype: string
    :param unit: Enumerator in [‘NONE’, ‘LENGTH’, ‘AREA’, ‘VOLUME’, ‘ROTATION’, ‘TIME’, ‘VELOCITY’, ‘ACCELERATION’]. 
    :type unit: string
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def FloatVectorProperty(name="",
                        description="",
                        default=(0.0, 0.0, 0.0),
                        min=sys.float_info.min,
                        max=sys.float_info.max,
                        soft_min=sys.float_info.min,
                        soft_max=sys.float_info.max,
                        step=3,
                        precision=2,
                        options={'ANIMATABLE'},
                        subtype='NONE',
                        unit='NONE',
                        size=3,
                        update=None,
                        get=None,
                        set=None):
    '''Returns a new vector float property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param default: sequence of floats the length of size. 
    :type default: sequence
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead. 
    :type min: float
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead. 
    :type max: float
    :param soft_min: Soft minimum (>= min), user won’t be able to drag the widget below this value in the UI. 
    :type soft_min: float
    :param soft_max: Soft maximum (<= max), user won’t be able to drag the widget above this value in the UI. 
    :type soft_max: float
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100). 
    :type step: int
    :param precision: Maximum number of decimal digits to display, in [0, 6]. 
    :type precision: int
    :param subtype: Enumerator in [‘COLOR’, ‘TRANSLATION’, ‘DIRECTION’, ‘VELOCITY’, ‘ACCELERATION’, ‘MATRIX’, ‘EULER’, ‘QUATERNION’, ‘AXISANGLE’, ‘XYZ’, ‘COLOR_GAMMA’, ‘LAYER’, ‘NONE’]. 
    :type subtype: string
    :param unit: Enumerator in [‘NONE’, ‘LENGTH’, ‘AREA’, ‘VOLUME’, ‘ROTATION’, ‘TIME’, ‘VELOCITY’, ‘ACCELERATION’]. 
    :type unit: string
    :param size: Vector dimensions in [1, 32]. 
    :type size: int
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def IntProperty(name="",
                description="",
                default=0,
                min=-2**31,
                max=2**31 - 1,
                soft_min=-2**31,
                soft_max=2**31 - 1,
                step=1,
                options={'ANIMATABLE'},
                subtype='NONE',
                update=None,
                get=None,
                set=None):
    '''Returns a new int property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead. 
    :type min: int
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead. 
    :type max: int
    :param soft_max: Soft maximum (<= max), user won’t be able to drag the widget above this value in the UI. 
    :type soft_max: int
    :param soft_min: Soft minimum (>= min), user won’t be able to drag the widget below this value in the UI. 
    :type soft_min: int
    :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!). 
    :type step: int
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘PIXEL’, ‘UNSIGNED’, ‘PERCENTAGE’, ‘FACTOR’, ‘ANGLE’, ‘TIME’, ‘DISTANCE’, ‘NONE’]. 
    :type subtype: string
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def IntVectorProperty(name="",
                      description="",
                      default=(0, 0, 0),
                      min=-2**31,
                      max=2**31 - 1,
                      soft_min=-2**31,
                      soft_max=2**31 - 1,
                      step=1,
                      options={'ANIMATABLE'},
                      subtype='NONE',
                      size=3,
                      update=None,
                      get=None,
                      set=None):
    '''Returns a new vector int property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param default: sequence of ints the length of size. 
    :type default: sequence
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead. 
    :type min: int
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead. 
    :type max: int
    :param soft_min: Soft minimum (>= min), user won’t be able to drag the widget below this value in the UI. 
    :type soft_min: int
    :param soft_max: Soft maximum (<= max), user won’t be able to drag the widget above this value in the UI. 
    :type soft_max: int
    :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!). 
    :type step: int
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘COLOR’, ‘TRANSLATION’, ‘DIRECTION’, ‘VELOCITY’, ‘ACCELERATION’, ‘MATRIX’, ‘EULER’, ‘QUATERNION’, ‘AXISANGLE’, ‘XYZ’, ‘COLOR_GAMMA’, ‘LAYER’, ‘NONE’]. 
    :type subtype: string
    :param size: Vector dimensions in [1, 32]. 
    :type size: int
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass


def PointerProperty(type=None,
                    name="",
                    description="",
                    options={'ANIMATABLE'},
                    update=None):
    '''Returns a new pointer property definition. 

    :param type: A subclass of bpy.types.PropertyGroup. 
    :type type: class
    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    '''

    pass


def RemoveProperty(cls, attr):
    '''Removes a dynamically defined property. 

    :param cls: The class containing the property (must be a positional argument). 
    :type cls: type
    :param attr: Property name (must be passed as a keyword). 
    :type attr: string
    '''

    pass


def StringProperty(name="",
                   description="",
                   default="",
                   maxlen=0,
                   options={'ANIMATABLE'},
                   subtype='NONE',
                   update=None,
                   get=None,
                   set=None):
    '''Returns a new string property definition. 

    :param name: Name used in the user interface. 
    :type name: string
    :param description: Text used for the tooltip and api documentation. 
    :type description: string
    :param default: initializer string. 
    :type default: string
    :param maxlen: maximum length of the string. 
    :type maxlen: int
    :param options: Enumerator in [‘HIDDEN’, ‘SKIP_SAVE’, ‘ANIMATABLE’, ‘LIBRARY_EDITABLE’, ‘PROPORTIONAL’,’TEXTEDIT_UPDATE’]. 
    :type options: set
    :param subtype: Enumerator in [‘FILE_PATH’, ‘DIR_PATH’, ‘FILE_NAME’, ‘BYTE_STRING’, ‘PASSWORD’, ‘NONE’]. 
    :type subtype: string
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. Warning there are no safety checks to avoid infinite recursion. 
    :type update: function
    :param get: Function to be called when this value is ‘read’, This function must take 1 value (self) and return the value of the property. 
    :type get: function
    :param set: Function to be called when this value is ‘written’, This function must take 2 values (self, value) and return None. 
    :type set: function
    '''

    pass
