contexts_C_to_py = None
'''A readonly dict mapping contexts C-identifiers to their py-identifiers. '''

contexts = None
'''constant value bpy.app.translations.contexts(default_real=None, default=*, operator_default=Operator, ui_events_keymaps=UI_Events_KeyMaps, plural=Plural, id_action=Action, id_armature=Armature, id_brush=Brush, id_camera=Camera, id_cachefile=CacheFile, id_collection=Collection, id_curve=Curve, id_fs_linestyle=FreestyleLineStyle, id_gpencil=GPencil, id_id=ID, id_image=Image, id_shapekey=Key, id_lamp=Lamp, id_library=Library, id_lattice=Lattice, id_mask=Mask, …) '''


def locale_explode(locale):
    '''For non-complete locales, missing elements will be None. 

    :param locale: The ISO locale string to explode. 
    :type locale: 
    :return:  A tuple (language, country, variant, language_country, language@variant). 
    '''

    pass


def pgettext(msgid, msgctxt):
    '''Try to translate the given msgid (with optional msgctxt). 

    :param msgid: The string to translate. 
    :type msgid: string
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT). 
    :type msgctxt: string or None
    :return:  The translated string (or msgid if no translation was found). 
    '''

    pass


def pgettext_data(msgid, msgctxt):
    '''Try to translate the given msgid (with optional msgctxt), if new data name’s translation is enabled. 

    :param msgid: The string to translate. 
    :type msgid: string
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT). 
    :type msgctxt: string or None
    :return:  The translated string (or msgid if no translation was found). 
    '''

    pass


def pgettext_iface(msgid, msgctxt):
    '''Try to translate the given msgid (with optional msgctxt), if labels’ translation is enabled. 

    :param msgid: The string to translate. 
    :type msgid: string
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT). 
    :type msgctxt: string or None
    :return:  The translated string (or msgid if no translation was found). 
    '''

    pass


def pgettext_tip(msgid, msgctxt):
    '''Try to translate the given msgid (with optional msgctxt), if tooltips’ translation is enabled. 

    :param msgid: The string to translate. 
    :type msgid: string
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT). 
    :type msgctxt: string or None
    :return:  The translated string (or msgid if no translation was found). 
    '''

    pass


def register(module_name, translations_dict):
    '''Registers an addon’s UI translations. 

    :param module_name: The name identifying the addon. 
    :type module_name: string
    :param translations_dict: A dictionary built like that: {locale: {msg_key: msg_translation, ...}, ...} 
    :type translations_dict: dict
    '''

    pass


def unregister(module_name):
    '''Unregisters an addon’s UI translations. 

    :param module_name: The name identifying the addon. 
    :type module_name: string
    '''

    pass
