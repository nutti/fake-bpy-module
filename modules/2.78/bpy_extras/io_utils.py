def orientation_helper_factory(name, axis_forward='Y', axis_up='Z'):
    pass


def axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z'):
    pass


def axis_conversion_ensure(operator, forward_attr, up_attr):
    pass


def create_derived_objects(scene, ob):
    pass


def free_derived_objects(ob):
    pass


def unpack_list(list_of_tuples):
    pass


def unpack_face_list(list_of_tuples):
    pass


def path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None):
    pass


def path_reference_copy(copy_set, report='print'):
    pass


def unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.'):
    pass


path_reference_mode = None


class ExportHelper:

    def check(self, context):
        pass

    def invoke(self, context, event):
        pass



class ImportHelper:

    def check(self, context):
        pass

    def invoke(self, context, event):
        pass



