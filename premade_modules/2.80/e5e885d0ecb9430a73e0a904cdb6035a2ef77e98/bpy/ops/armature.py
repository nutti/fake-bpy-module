def align():
    '''Align selected bones to the active bone (or to their parent) 

    '''

    pass


def armature_layers(
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False)):
    '''Change the visible armature layers 

    :param layers: Layer, Armature layers to make visible 
    :type layers: boolean array of 32 items, (optional)
    '''

    pass


def autoside_names(type='XAXIS'):
    '''Automatically renames the selected bones according to which side of the target axis they fall on 

    :param type: Axis, Axis tag names withXAXIS X-Axis, Left/Right.YAXIS Y-Axis, Front/Back.ZAXIS Z-Axis, Top/Bottom. 
    :type type: enum in ['XAXIS', 'YAXIS', 'ZAXIS'], (optional)
    '''

    pass


def bone_layers(
        layers=(False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False)):
    '''Change the layers that the selected bones belong to 

    :param layers: Layer, Armature layers that bone belongs to 
    :type layers: boolean array of 32 items, (optional)
    '''

    pass


def bone_primitive_add(name="Bone"):
    '''Add a new bone located at the 3D-Cursor 

    :param name: Name, Name of the newly created bone 
    :type name: string, (optional, never None)
    '''

    pass


def calculate_roll(type='POS_X', axis_flip=False, axis_only=False):
    '''Automatically fix alignment of select bones’ axes 

    :param type: Type 
    :type type: enum in ['POS_X', 'POS_Z', 'GLOBAL_POS_X', 'GLOBAL_POS_Y', 'GLOBAL_POS_Z', 'NEG_X', 'NEG_Z', 'GLOBAL_NEG_X', 'GLOBAL_NEG_Y', 'GLOBAL_NEG_Z', 'ACTIVE', 'VIEW', 'CURSOR'], (optional)
    :param axis_flip: Flip Axis, Negate the alignment axis 
    :type axis_flip: boolean, (optional)
    :param axis_only: Shortest Rotation, Ignore the axis direction, use the shortest rotation to align 
    :type axis_only: boolean, (optional)
    '''

    pass


def click_extrude():
    '''Create a new bone going from the last selected joint to the mouse position 

    '''

    pass


def delete():
    '''Remove selected bones from the armature 

    '''

    pass


def dissolve():
    '''Dissolve selected bones from the armature 

    '''

    pass


def duplicate(do_flip_names=False):
    '''Make copies of the selected bones within the same armature 

    :param do_flip_names: Flip Names, Try to flip names of the bones, if possible, instead of adding a number extension 
    :type do_flip_names: boolean, (optional)
    '''

    pass


def duplicate_move(ARMATURE_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Make copies of the selected bones within the same armature and move them 

    :param ARMATURE_OT_duplicate: Duplicate Selected Bone(s), Make copies of the selected bones within the same armature 
    :type ARMATURE_OT_duplicate: ARMATURE_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude(forked=False):
    '''Create new bones from the selected joints 

    :param forked: Forked 
    :type forked: boolean, (optional)
    '''

    pass


def extrude_forked(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None):
    '''Create new bones from the selected joints and move them 

    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints 
    :type ARMATURE_OT_extrude: ARMATURE_OT_extrude, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def extrude_move(ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None):
    '''Create new bones from the selected joints and move them 

    :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints 
    :type ARMATURE_OT_extrude: ARMATURE_OT_extrude, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def fill():
    '''Add bone between selected joint(s) and/or 3D-Cursor 

    '''

    pass


def flip_names(do_strip_numbers=False):
    '''Flips (and corrects) the axis suffixes of the names of selected bones 

    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names (WARNING: may result in incoherent naming in some cases) 
    :type do_strip_numbers: boolean, (optional)
    '''

    pass


def hide(unselected=False):
    '''Tag selected bones to not be visible in Edit Mode 

    :param unselected: Unselected, Hide unselected rather than selected 
    :type unselected: boolean, (optional)
    '''

    pass


def layers_show_all(all=True):
    '''Make all armature layers visible 

    :param all: All Layers, Enable all layers or just the first 16 (top row) 
    :type all: boolean, (optional)
    '''

    pass


def merge(type='WITHIN_CHAIN'):
    '''Merge continuous chains of selected bones 

    :param type: Type 
    :type type: enum in ['WITHIN_CHAIN'], (optional)
    '''

    pass


def parent_clear(type='CLEAR'):
    '''Remove the parent-child relationship between selected bones and their parents 

    :param type: ClearType, What way to clear parenting 
    :type type: enum in ['CLEAR', 'DISCONNECT'], (optional)
    '''

    pass


def parent_set(type='CONNECTED'):
    '''Set the active bone as the parent of the selected bones 

    :param type: ParentType, Type of parenting 
    :type type: enum in ['CONNECTED', 'OFFSET'], (optional)
    '''

    pass


def reveal(select=True):
    '''Reveal all bones hidden in Edit Mode 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def roll_clear(roll=0.0):
    '''Clear roll for selected bones 

    :param roll: Roll 
    :type roll: float in [-6.28319, 6.28319], (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Toggle selection status of all bones 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_hierarchy(direction='PARENT', extend=False):
    '''Select immediate parent/children of selected bones 

    :param direction: Direction 
    :type direction: enum in ['PARENT', 'CHILD'], (optional)
    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Deselect those bones at the boundary of each selection region 

    '''

    pass


def select_linked(deselect=False):
    '''Select bones related to selected ones by parent/child relationships 

    :param deselect: Deselect 
    :type deselect: boolean, (optional)
    '''

    pass


def select_mirror(only_active=False, extend=False):
    '''Mirror the bone selection 

    :param only_active: Active Only, Only operate on the active bone 
    :type only_active: boolean, (optional)
    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_more():
    '''Select those bones connected to the initial selection 

    '''

    pass


def select_similar(type='LENGTH', threshold=0.1):
    '''Select similar bones by property types 

    :param type: Type 
    :type type: enum in ['CHILDREN', 'CHILDREN_IMMEDIATE', 'SIBLINGS', 'LENGTH', 'DIRECTION', 'PREFIX', 'SUFFIX', 'LAYER', 'GROUP', 'SHAPE'], (optional)
    :param threshold: Threshold 
    :type threshold: float in [0, 1], (optional)
    '''

    pass


def separate():
    '''Isolate selected bones into a separate armature 

    '''

    pass


def shortest_path_pick():
    '''Select shortest path between two bones 

    '''

    pass


def split():
    '''Split off selected bones from connected unselected bones 

    '''

    pass


def subdivide(number_cuts=1):
    '''Break selected bones into chains of smaller bones 

    :param number_cuts: Number of Cuts 
    :type number_cuts: int in [1, 1000], (optional)
    '''

    pass


def switch_direction():
    '''Change the direction that a chain of bones points in (head <-> tail swap) 

    '''

    pass


def symmetrize(direction='NEGATIVE_X'):
    '''Enforce symmetry, make copies of the selection or use existing 

    :param direction: Direction, Which sides to copy from and to (when both are selected) 
    :type direction: enum in ['NEGATIVE_X', 'POSITIVE_X'], (optional)
    '''

    pass
