import re
from typing import List, Dict

from .utils import (
    check_os,
    remove_unencodable,
    output_log,
    LOG_LEVEL_WARN,
)

REPLACE_DATA_TYPE: Dict[str, str] = {
    "Enumerated constant": "str, int",
    "enum": "str, int",
    # TODO: should handle by using __iter__() method and so on...
    "BMEdgeSeq": "list of BMEdge",
    "BMFaceSeq": "list of BMFace",
    "BMLoopSeq": "list of BMLoop",
    "BMVertSeq": "list of BMVert",
    "BMEditSelSeq": "list of BMEditSel",
}

BUILTIN_DATA_TYPE: List[str] = [
    "bool", "str", "bytes", "float", "int",
]

BUILTIN_DATA_TYPE_ALIASES: Dict[str, str] = {
    "string": "str",
    "boolean": "bool",
}

MODIFIER_DATA_TYPE: List[str] = [
    "list", "dict", "set",
]

MODIFIER_DATA_TYPE_ALIASES: Dict[str, str] = {
    "List": "list",
    "bpy_prop_collection": "list",
    "BMElemSeq": "list",
    "sequence": "list",
}

MODIFIER_DATA_TYPE_TO_TYPING: Dict[str, str] = {
    "list": "typing.List",
    "dict": "typing.Dict",
    "set": "typing.Set",
}


def has_data_type(str_: str, data_type: str) -> bool:
    ALLOWED_CHAR_BEFORE = [" ", "("]
    ALLOWED_CHAR_AFTER = [" ", ",", ")"]

    start_index = 0
    end_index = len(str_)

    for m in re.finditer(data_type, str_):
        si = m.start(0)
        ei = m.end(0)
        # example: "int"
        if (si == start_index) and (ei == end_index):
            return True
        # example: "int or float"
        if (si == start_index) and ((ei != end_index) and (str_[ei] in ALLOWED_CHAR_AFTER)):
            return True
        # example: "list of int"
        if ((si != start_index) and (str_[si-1] in ALLOWED_CHAR_BEFORE)) and (ei == end_index):
            return True
        # example: "list of int or float"
        if ((si != start_index) and (str_[si-1] in ALLOWED_CHAR_BEFORE)) and ((ei != end_index) and (str_[ei] in ALLOWED_CHAR_AFTER)):
            return True

    return False


FROM_DICT_METHOD: List[str] = [
    'NONE',
    'NEW',
    'APPEND',
    'UPDATE',
]


class DataType:
    def type(self) -> str:
        raise NotImplementedError()

    def has_modifier(self) -> bool:
        raise NotImplementedError()

    def modifier(self) -> str:
        raise NotImplementedError()

    def data_types(self) -> List[str]:
        raise NotImplementedError()

    def to_string(self) -> str:
        raise NotImplementedError()


class UnknownDataType(DataType):
    def __init__(self):
        pass

    def type(self) -> str:
        return 'UNKNOWN'

    def has_modifier(self) -> bool:
        raise RuntimeError("has_modifier() is not callable")

    def modifier(self) -> str:
        raise RuntimeError("module() is not callable")

    def data_types(self) -> List[str]:
        raise RuntimeError("data_type() is not callable")

    def to_string(self) -> str:
        return ""


class IntermidiateDataType(DataType):
    def __init__(self, data_type: str):
        self._data_type: str = data_type

    def type(self) -> str:
        return 'INTERMIDIATE'

    def has_modifier(self) -> bool:
        raise RuntimeError("has_modifier() is not callable ({})".format(self._data_type))

    def modifier(self) -> str:
        raise RuntimeError("module() is not callable ({})".format(self._data_type))

    def data_types(self) -> List[str]:
        raise RuntimeError("data_type() is not callable ({})".format(self._data_type))

    def to_string(self) -> str:
        return self._data_type


class BuiltinDataType(DataType):
    def __init__(self, data_types: List[str], modifier: str=None):
        if len(data_types) == 0:
            raise ValueError("length of data_types must be >= 1 but {}"
                             .format(len(data_types)))
        for dtype in data_types:
            if dtype not in BUILTIN_DATA_TYPE:
                raise ValueError("data_type must be {} but {}"
                                 .format(BUILTIN_DATA_TYPE, dtype))
        self._data_types: List[str] = data_types
        if (modifier is not None) and (modifier not in MODIFIER_DATA_TYPE):
            raise ValueError("modifier must be {} but {}"
                             .format(MODIFIER_DATA_TYPE, modifier))
        self._modifier: str = modifier

    def type(self) -> str:
        return 'BUILTIN'

    def has_modifier(self) -> bool:
        return self._modifier is not None

    def modifier(self) -> str:
        return self._modifier

    def data_types(self) -> List[str]:
        return self._data_types

    def to_string(self) -> str:
        if self._modifier is None:
            if len(self._data_types) == 1:
                return self._data_types[0]
            return "typing.Union[{}]".format(", ".join(self._data_types))

        if len(self._data_types) == 1:
            return "{}[{}]"\
                   .format(MODIFIER_DATA_TYPE_TO_TYPING[self._modifier],
                                   self._data_types[0])
        else:
            return "{}[typing.Union[{}]]"\
                   .format(MODIFIER_DATA_TYPE_TO_TYPING[self._modifier],
                           ", ".join(self._data_types))


class ModifierDataType(DataType):
    def __init__(self, modifier: str):
        if (modifier is None) or (modifier not in MODIFIER_DATA_TYPE):
            raise ValueError("modifier must be {} but {}"
                             .format(MODIFIER_DATA_TYPE, modifier))
        self._modifier: str = modifier

    def type(self) -> str:
        return 'MODIFIER'

    def has_modifier(self) -> bool:
        raise RuntimeError("has_modifier() is not callable ({})".format(self._modifier))

    def modifier(self) -> str:
        return self._modifier

    def data_types(self) -> List[str]:
        raise RuntimeError("data_type is not callable ({})".format(self._modifier))

    def to_string(self) -> str:
        return self._modifier


class CustomDataType(DataType):
    def __init__(self, data_types: List[str], modifier: str=None):
        # TODO: support more than 2 data_types
        if len(data_types) != 1:
            raise ValueError("length of data_types must be {} but {}"
                             .format(1, len(data_types)))
        self._data_types: List[str] = data_types
        if (modifier is not None) and (modifier not in MODIFIER_DATA_TYPE):
            raise ValueError("modifier must be {} but {}"
                             .format(MODIFIER_DATA_TYPE, modifier))
        self._modifier: str = modifier

    def type(self) -> str:
        return 'CUSTOM'

    def has_modifier(self) -> bool:
        return self._modifier is not None

    def modifier(self) -> str:
        return self._modifier

    def data_types(self) -> List[str]:
        return self._data_types

    def to_string(self) -> str:
        if self._modifier is None:
            return "'{}'".format(self._data_types[0])

        return "{}['{}']"\
               .format(MODIFIER_DATA_TYPE_TO_TYPING[self._modifier],
                               self._data_types[0])


class Info:
    def __init__(self):
        self._type: str = None

    def is_assinable(self, variable, data: dict, key: str, method: str):
        if method == 'NEW':
            if key in data:
                return True
            return False
        elif method == 'APPEND':
            if (key in data) and (variable is None):
                return True
            return False
        elif method == 'UPDATE':
            if key in data:
                return True
            return False
        else:
            raise RuntimeError("Unsupported method: {}".format(method))

    def name(self) -> str:
        raise NotImplementedError()

    def module(self) -> str:
        raise NotImplementedError()

    def type(self) -> str:
        if self._type is None:
            raise RuntimeError("'type' is empty")
        return self._type

    def to_dict(self) -> dict:
        raise NotImplementedError()

    def from_dict(self, data: dict, method: str=False):
        raise NotImplementedError()


class ParameterDetailInfo(Info):
    def __init__(self):
        super(ParameterDetailInfo, self).__init__()
        self._type: str = "parameter"
        self._name: str = None
        self._description: str = None
        self._data_type: 'DataType' = UnknownDataType()

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def set_description(self, desc: str):
        self._description = desc

    def set_data_type(self, dtype: 'DataType'):
        self._data_type = dtype

    def data_type(self) -> 'DataType':
        return self._data_type

    def to_dict(self) -> dict:
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._description is None:
            self._description = ""

        if check_os() == "Windows":
            data = {
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type.to_string()),
            }
        else:
            data = {
                "name": self._name,
                "description": self._description,
                "data_type": self._data_type.to_string(),
            }

        return data

    def from_dict(self, data: dict, method: str='NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "parameter":
            raise RuntimeError("Unsupported type: {}".format(data["type"]))

        self._type = data["type"]
        if self.is_assinable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assinable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assinable(self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class ReturnInfo(Info):
    def __init__(self):
        super(ReturnInfo, self).__init__()
        self._type: str = "return"
        self._description: str = None
        self._data_type: 'DataType' = UnknownDataType()

    def data_type(self) -> 'DataType':
        return self._data_type

    def set_description(self, desc: str):
        self._description = desc

    def set_data_type(self, dtype: 'DataType'):
        self._data_type = dtype

    def to_dict(self) -> dict:
        if self._description is None:
            self._description = ""

        if check_os() == "Windows":
            data = {
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type.to_string()),
            }
        else:
            data = {
                "description": self._description,
                "data_type": self._data_type.to_string(),
            }

        return data

    def from_dict(self, data: dict, method: str='NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "return":
            raise RuntimeError("Unsupported type: {}".format(data["type"]))

        self._type = data["type"]
        if self.is_assinable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assinable(self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class VariableInfo(Info):
    supported_type: List[str] = ["constant", "attribute"]

    def __init__(self, type_: str):
        super(VariableInfo, self).__init__()
        if type_ not in self.supported_type:
            raise RuntimeError("VariableInfo must be type {} but {}"
                               .format(self.supported_type, type_))
        self._type: str = type_
        self._name: str = None
        self._description: str = None
        self._class: str = None
        self._module: str = None
        self._data_type: 'DataType' = UnknownDataType()

    def name(self) -> str:
        return self._name

    def data_type(self) -> 'DataType':
        return self._data_type

    def set_name(self, name: str):
        self._name = name

    def set_description(self, desc: str):
        self._description = desc

    def set_class(self, class_: str):
        self._class = class_

    def module(self) -> str:
        return self._module

    def set_module(self, module_: str):
        self._module = module_

    def set_data_type(self, data_type: 'DataType'):
        self._data_type = data_type

    def to_dict(self) -> dict:
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._description is None:
            self._description = ""

        if self._class is None:
            self._class = ""

        if self._module is None:
            self._module = ""

        if check_os() == "Windows":
            data = {
                "type": self._type,
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "class": remove_unencodable(self._class),
                "module": remove_unencodable(self._module),
                "data_type": remove_unencodable(self._data_type.to_string()),
            }
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "class": self._class,
                "module": self._module,
                "data_type": self._data_type.to_string(),
            }

        return data

    def from_dict(self, data: dict, method: str='NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] not in self.supported_type:
            raise RuntimeError("Unsupported type: {}".format(data["type"]))

        self._type = data["type"]
        if self.is_assinable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assinable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assinable(self._class, data, "class", method):
            self._class = data["class"]
        if self.is_assinable(self._module, data, "module", method):
            self._module = data["module"]
        if self.is_assinable(self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class FunctionInfo(Info):
    supported_type: List[str] = ["function", "method"]

    def __init__(self, type_: str):
        super(FunctionInfo, self).__init__()
        if type_ not in self.supported_type:
            raise RuntimeError("FunctionInfo must be type {} but {}"
                               .format(self.supported_type, type_))
        self._type: str = type_
        self._name: str = None
        self._parameters: List[str] = []
        self._parameter_details: List['ParameterDetailInfo'] = []
        self._return: 'ReturnInfo' = None
        self._class: str = None
        self._module: str = None
        self._description: str = None

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def equal_to_fullname(self, fullname: str) -> bool:
        return self._name == fullname

    def parameters(self) -> List[str]:
        return self._parameters

    def parameter(self, idx: int) -> str:
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        return self._parameters[idx]

    def parameter_details(self) -> List['ParameterDetailInfo']:
        return self._parameter_details

    def return_(self) -> 'ReturnInfo':
        return self._return

    def set_parameters(self, params: List[str]):
        self._parameters = []
        self.add_parameters(params)

    def set_parameter(self, idx: int, param: str):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        self._parameters[idx] = param

    def add_parameter(self, param: str):
        if param in self._parameters:
            output_log(LOG_LEVEL_WARN,
                       "Parameter {} is already registered in ({}), so skip to add this parameter."
                       .format(param, " | ".join(self._parameters)))
            return
        self._parameters.append(param)

    def add_parameters(self, params: List[str]):
        for p in params:
            self.add_parameter(p)

    def remove_parameter(self, idx: int):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        del self._parameters[idx]

    def add_parameter_detail(self, param: 'ParameterDetailInfo'):
        if param.type() != "parameter":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("parameter", param.type()))
        self._parameter_details.append(param)

    def add_parameter_details(self, params: List['ParameterDetailInfo']):
        for p in params:
            if p.type() != "parameter":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("parameter", p.type()))
            self.add_parameter_detail(p)

    def set_parameter_details(self, params: List['ParameterDetailInfo']):
        self._parameter_details = []
        self.add_parameter_details(params)

    def set_class(self, class_: str):
        self._class = class_

    def module(self) -> str:
        return self._module

    def set_module(self, module_: str):
        self._module = module_

    def set_return(self, return_: 'ReturnInfo'):
        self._return = return_

    def set_description(self, desc: str):
        self._description = desc

    def to_dict(self) -> dict:
        if self._type not in self.supported_type:
            raise RuntimeError("'type' must be ({})"
                               .format(self.supported_type))

        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._return is None:
            self._return = ReturnInfo()

        if self._class is None:
            self._class = ""

        if self._module is None:
            self._module = ""

        if self._description is None:
            self._description = ""

        # remove 'self' parameter
        try:
            self._parameters.remove("self")
        except ValueError:
            pass

        if check_os() == "Windows":
            data = {
                "type": self._type,
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "return": self._return.to_dict(),
                "class": remove_unencodable(self._class),
                "module": remove_unencodable(self._module),
                "parameters": [p for p in self._parameters],
                "parameter_details": [p.to_dict()
                                      for p in self._parameter_details],
            }
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "return": self._return.to_dict(),
                "class": self._class,
                "module": self._module,
                "parameters": [p for p in self._parameters],
                "parameter_details": [p.to_dict()
                                      for p in self._parameter_details],
            }

        return data

    def from_dict(self, data: dict, method: str='NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] not in self.supported_type:
            raise RuntimeError("Unsupported type: {}".format(data["type"]))

        self._type = data["type"]
        if self.is_assinable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assinable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assinable(self._class, data, "class", method):
            self._class = data["class"]
        if self.is_assinable(self._module, data, "module", method):
            self._module = data["module"]
        if self.is_assinable(self._parameters, data, "parameters", method):
            self._parameters = data["parameters"]
        if self.is_assinable(self._return, data, "return", method):
            self._return = ReturnInfo()
            self._return.from_dict(data["return"], method)

        if "parameter_details" in data:
            if method == 'NEW':
                for pd in data["parameter_details"]:
                    new_pd = ParameterDetailInfo()
                    new_pd.from_dict(pd, 'NEW')
                    self._parameter_details.append(new_pd)
            elif method == 'APPEND':
                for pd in data["parameter_details"]:
                    for update_pd in self._parameter_details:
                        if update_pd.name() == pd["name"]:
                            update_pd.from_dict(pd, 'APPEND')
                            break
                    else:
                        new_pd = ParameterDetailInfo()
                        new_pd.from_dict(pd, 'NEW')
                        self._parameter_details.append(new_pd)
            elif method == 'UPDATE':
                for pd in data["parameter_details"]:
                    for update_pd in self._parameter_details:
                        if update_pd.name() == pd["name"]:
                            update_pd.from_dict(pd, 'UPDATE')
                            break
                    else:
                        raise RuntimeError("{} is not found".format(pd["name"]))


class ClassInfo(Info):
    def __init__(self):
        super(ClassInfo, self).__init__()
        self._type: str = "class"
        self._name: str = None
        self._description: str = None
        self._module: str = None
        self._methods: List['FunctionInfo'] = []
        self._attributes: List['VariableInfo'] = []
        self._base_classes: List['DataType'] = []

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def module(self) -> str:
        return self._module

    def attributes(self) -> List['VariableInfo']:
        return self._attributes

    def set_module(self, module_: str):
        self._module = module_

    def set_description(self, desc: str):
        self._description = desc

    def methods(self) -> List['FunctionInfo']:
        return self._methods

    def base_classes(self) -> List['DataType']:
        return self._base_classes

    def add_method(self, method: 'FunctionInfo'):
        if method.type() != "method":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("method", method.type()))
        self._methods.append(method)

    def add_methods(self, methods: List['FunctionInfo']):
        for m in methods:
            if m.type() != "method":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("method", m.type()))
            self.add_method(m)

    def set_methods(self, methods: List['FunctionInfo']):
        self._methods = []
        self.add_methods(methods)

    def add_attribute(self, attr: 'VariableInfo'):
        if attr.type() != "attribute":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("attribute", attr.type()))
        self._attributes.append(attr)

    def add_attributes(self, attrs: List['VariableInfo']):
        for a in attrs:
            if a.type() != "attribute":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("attribute", a.type()))
            self.add_attribute(a)

    def set_attributes(self, attrs: List['VariableInfo']):
        self._attributes = []
        self.add_attributes(attrs)

    def add_base_class(self, class_: 'DataType'):
        self._base_classes.append(class_)

    def add_base_classes(self, classes: List['DataType']):
        for c in classes:
            self.add_base_class(c)

    def set_base_class(self, index: int, class_: 'DataType'):
        self._base_classes[index] = class_

    def to_dict(self) -> dict:
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._module is None:
            self._module = ""

        if self._description is None:
            self._description = ""

        if check_os() == "Windows":
            data = {
                "type": self._type,
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "module": remove_unencodable(self._module),
                "methods": [m.to_dict() for m in self._methods],
                "attributes": [a.to_dict() for a in self._attributes],
                "base_classes": [remove_unencodable(c.to_string())
                                 for c in self._base_classes]
            }
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "module": self._module,
                "methods": [m.to_dict() for m in self._methods],
                "attributes": [a.to_dict() for a in self._attributes],
                "base_classes": [c.to_string() for c in self._base_classes]
            }

        return data

    def from_dict(self, data: dict, method: str='NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "class":
            raise RuntimeError("Unsupported type: {}".format(data["type"]))

        self._type = data["type"]
        if self.is_assinable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assinable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assinable(self._module, data, "module", method):
            self._module = data["module"]

        if "methods" in data:
            if method == 'NEW':
                for m in data["methods"]:
                    new_m = FunctionInfo("method")
                    new_m.from_dict(m, 'NEW')
                    self._methods.append(new_m)
            elif method == 'APPEND':
                for m in data["methods"]:
                    for update_m in self._methods:
                        if update_m.name() == m["name"]:
                            update_m.from_dict(m, 'APPEND')
                            break
                    else:
                        new_m = FunctionInfo("method")
                        new_m.from_dict(m, 'NEW')
                        self._methods.append(new_m)
            elif method == 'UPDATE':
                for m in data["methods"]:
                    for update_m in self._methods:
                        if update_m.name() == m["name"]:
                            update_m.from_dict(m, 'UPDATE')
                            break
                    else:
                        raise RuntimeError("Method '{}' is not found at class '{}.{}'"
                                           .format(m["name"], self._module, self._name))
            else:
                raise RuntimeError("Unsupported method: {}".format(method))

        if "attributes" in data:
            if method == 'NEW':
                for a in data["attributes"]:
                    new_a = VariableInfo("attribute")
                    new_a.from_dict(a, 'NEW')
                    self._attributes.append(new_a)
            elif method == 'APPEND':
                for a in data["attributes"]:
                    for update_a in self._attributes:
                        if update_a.name() == a["name"]:
                            update_a.from_dict(a, 'APPEND')
                            break
                    else:
                        new_a = VariableInfo("attribute")
                        new_a.from_dict(a, 'NEW')
                        self._attributes.append(new_a)
            elif method == 'UPDATE':
                for a in data["attributes"]:
                    for update_a in self._attributes:
                        if update_a.name() == a["name"]:
                            update_a.from_dict(a, 'UPDATE')
                            break
                    else:
                        raise RuntimeError("{} is not found".format(a["name"]))
            else:
                raise RuntimeError("Unsupported method: {}".format(method))

        if "base_classes" in data:
            if method == 'NEW':
                for c in data["base_classes"]:
                    new_c = IntermidiateDataType(c)
                    self._base_classes.append(new_c)
            else:
                raise RuntimeError("Unsupported method: {}".format(method))


class SectionInfo:
    def __init__(self):
        self.info_list: List['Info'] = []


class ModuleStructure:
    def __init__(self):
        self._name: str = None
        self._children: List['ModuleStructure'] = []

    @property
    def name(self) -> str:
        # this is a root of structure. name of root is None
        if self._name is None:
            raise RuntimeError("name must not call when self._name is None")
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def add_child(self, child: 'ModuleStructure'):
        self._children.append(child)

    def children(self) -> List['ModuleStructure']:
        return self._children

    def to_dict(self) -> dict:
        def to_dict_internal(c: List[dict], psc: List['ModuleStructure']):
            for p in psc:
                nd = {"name": p.name, "children": []}
                to_dict_internal(nd["children"], p.children())
                c.append(nd)

        result = {"name": self._name, "children": []}
        to_dict_internal(result["children"], self._children)

        return result


class DataTypeRefiner:

    def __init__(self, package_structure: 'ModuleStructure', entry_points: List['EntryPoint']):
        self._package_structure: 'ModuleStructure' = package_structure
        self._entry_points: List['EntryPoint'] = entry_points

    def is_builtin_data_type(self, data_type: str) -> bool:
        return data_type in BUILTIN_DATA_TYPE

    def is_modifier_data_type(self, data_type: str) -> bool:
        return data_type in MODIFIER_DATA_TYPE

    def make_annotate_data_type(self, data_type: str) -> str:
        if self.is_builtin_data_type(data_type):
            return data_type
        if self.is_modifier_data_type(data_type):
            return data_type

        return "'{}'".format(data_type)

    def decompose_refined_data_type(self, data_type: str):
        if data_type is None:
            return None, None

        # example: typing.List['Action'] -> List, Action
        p = re.compile(r"^typing\.(List|Set|Dict)\['(.+)'\]$")
        m = p.match(data_type)
        if m:
            return m.group(1), m.group(2)

        # example: typing.List[int] -> List, int
        p = re.compile(r"^typing\.(List|Set|Dict)\[(.+)\]$")
        m = p.match(data_type)
        if m:
            return m.group(1), m.group(2)

        # example: 'Action' -> Action
        p = re.compile(r"^'(.+)'$")
        m = p.match(data_type)
        if m:
            return None, m.group(1)

        # example: int -> int
        return None, data_type

    def get_refined_data_type(self, data_type: 'DataType', module_name: str) -> 'DataType':
        if data_type.type() == 'UNKNOWN':
            return UnknownDataType()

        if data_type.type() != 'INTERMIDIATE':
            output_log(LOG_LEVEL_WARN, "data_type should be 'INTERMIDIATE' but {}".format(data_type.type()))

        # convert to aliased data type string
        dtype_str = data_type.to_string()
        for (key, value) in REPLACE_DATA_TYPE.items():
            if has_data_type(dtype_str, key):
                dtype_str = dtype_str.replace(key, value)

        # get modifier
        modifier = None
        for type_ in MODIFIER_DATA_TYPE:
            if has_data_type(dtype_str, type_):
                modifier = type_
                # remove modifier from dtype_str
                # TODO: need to clip only modifier string
                dtype_str = dtype_str.replace(type_, "")
                break
        if not modifier:
            for (key, value) in MODIFIER_DATA_TYPE_ALIASES.items():
                if has_data_type(dtype_str, key):
                    modifier = value
                    # remove modifier from dtype_str
                    # TODO: need to clip only modifier string
                    dtype_str = dtype_str.replace(key, "")
                    break

        # at first we check built-in data type
        dtype = []
        has_builtin_dtype = False
        for type_ in BUILTIN_DATA_TYPE:
            if has_data_type(dtype_str, type_):
                dtype.append(type_)
                has_builtin_dtype = True
        for (key, value) in BUILTIN_DATA_TYPE_ALIASES.items():
            if has_data_type(dtype_str, key):
                dtype.append(value)
                has_builtin_dtype = True
        dtype = list(set(dtype))

        # and then, search from package entry points
        # TODO: Need to check _entry_point if dtype has some value, but
        #       it raises performance problem.
        has_custom_dtype = False
        if not has_builtin_dtype:
            for entry in self._entry_points:
                if entry.type not in ["constant", "class"]:
                    continue
                if has_data_type(dtype_str, entry.fullname()):
                    dtype.append(entry.fullname())
                    has_custom_dtype = True
                    break
                full_data_type = "{}.{}".format(module_name, dtype_str)
                if has_data_type(full_data_type, entry.fullname()):
                    dtype.append(entry.fullname())
                    has_custom_dtype = True
                    break
                full_data_type = full_data_type.replace(" ", "")
                if has_data_type(full_data_type, entry.fullname()):
                    dtype.append(entry.fullname())
                    has_custom_dtype = True
                    break
                if has_data_type(dtype_str, entry.name):
                    dtype.append(entry.fullname())
                    has_custom_dtype = True
                    break
        if not has_builtin_dtype and not has_custom_dtype:
            output_log(LOG_LEVEL_WARN,
                       "Could not find any data type ({})"
                       .format(remove_unencodable(data_type.to_string())))

        if modifier is None:
            if has_builtin_dtype:
                return BuiltinDataType(dtype)
            elif has_custom_dtype:
                return CustomDataType(dtype)
            else:
                return UnknownDataType()
        else:
            if has_builtin_dtype:
                if (modifier != "list") and (modifier != "set"):
                    output_log(LOG_LEVEL_WARN,
                               "Modifier '{}' does not support element type inference ({})"
                               .format(modifier, data_type.to_string()))
                    return ModifierDataType(modifier)
                return BuiltinDataType(dtype, modifier)
            elif has_custom_dtype:
                if (modifier != "list") and (modifier != "set"):
                    output_log(LOG_LEVEL_WARN,
                               "Modifier '{}' does not support element type inference ({})"
                               .format(modifier, data_type.to_string()))
                    return ModifierDataType(modifier)
                return CustomDataType(dtype, modifier)
            else:
                return ModifierDataType(modifier)

    def get_base_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        sp = data_type.split(".")
        return sp[-1]

    def get_module_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        module_names = data_type.split(".")

        def search(mod_names, structure: 'ModuleStructure', dtype: str, is_first_level: bool=False):
            if len(mod_names) == 0:
                return dtype
            for s in structure.children():
                if s.name != mod_names[0]:
                    continue
                if is_first_level:
                    return search(mod_names[1:], s, s.name)
                else:
                    return search(mod_names[1:], s, dtype + "." + s.name)
            return dtype

        relative_type = search(module_names, self._package_structure,
                               "", True)

        return relative_type if relative_type != "" else None

    def _ensure_correct_data_type(self, data_type: str) -> str:
        mod_name = self.get_module_name(data_type)
        base_name = self.get_base_name(data_type)

        ensured = "{}.{}".format(mod_name, base_name)
        if ensured != data_type:
            raise RuntimeError("Invalid data type: ({} vs {})"
                               .format(data_type, ensured))

        return ensured

    def get_generation_data_type(self, data_type_1: List[str],
                                      data_type_2: str) -> List[str]:
        final_data_types = []
        for dtype in data_type_1:
            final_data_types.append(
                self._get_generation_data_type(dtype, data_type_2))
        return final_data_types

    def _get_generation_data_type(self, data_type_1: str,
                                 data_type_2: str) -> str:
        mod_names_full_1 = self.get_module_name(data_type_1)
        mod_names_full_2 = self.get_module_name(data_type_2)
        if mod_names_full_1 is None or mod_names_full_2 is None:
            return data_type_1      # TODO: should return better data_type

        mod_names_1 = mod_names_full_1.split(".")
        mod_names_2 = mod_names_full_2.split(".")

        for i, (m1, m2) in enumerate(zip(mod_names_1, mod_names_2)):
            if m1 != m2:
                match_level = i
                break
        else:
            if len(mod_names_1) >= len(mod_names_2):
                match_level = len(mod_names_2)
            else:
                match_level = len(mod_names_1)

        # [Case 1] No match => Use data_type_1
        #   data_type_1: bpy.types.Mesh
        #   data_type_2: bgl.glCallLists()
        #       => bpy.types.Mesh
        if match_level == 0:
            final_data_type = self._ensure_correct_data_type(data_type_1)
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => Use data_type_1 without module
            #   data_type_1: bgl.Buffer
            #   data_type_2: bgl.glCallLists()
            #       => Buffer
            if rest_level_1 == 0 and rest_level_2 == 0:
                final_data_type = self.get_base_name(data_type_1)
            # [Case 3] Match partially (Same level) => Use data_type_1
            #   data_type_1: bpy.types.Mesh
            #   data_type_2: bpy.ops.automerge()
            #       => bpy.types.Mesh
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type_1)
            # [Case 4] Match partially (Upper level) => Use data_type_1
            #   data_type_1: mathutils.Vector
            #   data_type_2: mathutils.noise.cell
            #       => mathutils.Vector
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type_1)
            # [Case 5] Match partially (Lower level) => Use relative data_type_1
            #   data_type_1: mathutils.noise.cell
            #   data_type_2: mathutils.Vector
            #       => noise.cell
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                final_data_type = ".".join(mod_names_1[match_level:])
                final_data_type += "." + self.get_base_name(data_type_1)
            else:
                raise RuntimeError("Should not reach this condition. ({} vs {})"
                                   .format(rest_level_1, rest_level_2))

        return final_data_type


class EntryPoint:
    def __init__(self):
        self._type: str = None
        self._name: str = None
        self._module: str = None

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def module(self) -> str:
        return self._module

    @module.setter
    def module(self, value: str):
        self._module = value

    def fullname(self) -> str:
        return "{}.{}".format(self._module, self._name)
