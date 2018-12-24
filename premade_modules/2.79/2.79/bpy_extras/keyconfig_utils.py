def addon_keymap_register(wm, keymaps_description):
    '''

    '''

    pass


def addon_keymap_unregister(wm, keymaps_description):
    '''

    '''

    pass


def keyconfig_export(wm, kc, filepath):
    '''

    '''

    pass


def keyconfig_merge(kc1, kc2):
    '''note: kc1 takes priority over kc2 

    '''

    pass


def keyconfig_test(kc):
    '''

    '''

    pass


def km_exists_in(km, export_keymaps):
    '''

    '''

    pass


keymaps_description_doc = None
'''constant value ‘nkeymaps_description is a tuple (((keymap_description), (tuple of keymap_item_descriptions))).nkeymap_description is a tuple (name, space_type, region_type, is_modal).nkeymap_item_description is a tuple ({kw_args_for_keymap_new}, (tuple of properties)).nkw_args_for_keymap_new is a mapping which keywords match parameters of keymap.new() function.ntuple of properties is a tuple of pairs (prop_name, prop_value) (properties being those of called operator).nnExample:nnKEYMAPS = (n # First, keymap identifiers (last bool is True for modal km).n ((‘Sequencer, ‘SEQUENCE_EDITOR, ‘WINDOW, False), (n # Then a tuple of keymap items, defined by a dict of kwargs for the km new func, and a tuple of tuples (name, val)n # for ops properties, if needing non-default values.n ({“idname”: export_strips.SEQExportStrip.bl_idname, “type”: ‘P, “value”: ‘PRESS, “shift”: True, “ctrl”: True},n ()),n )),n)n '''
