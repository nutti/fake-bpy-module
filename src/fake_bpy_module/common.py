import re
from typing import List, Dict

from .utils import (
    check_os,
    remove_unencodable,
    output_log,
    LOG_LEVEL_WARN,
    LOG_LEVEL_DEBUG,
)

REPLACE_DATA_TYPE: Dict[str, str] = {
    "Enumerated constant": "str, int",
    "enum": "str, int",
    "BMEdgeSeq": "BMEdgeSeq of BMEdge",
    "BMFaceSeq": "BMFaceSeq of BMFace",
    "BMLoopSeq": "BMLoopSeq of BMLoop",
    "BMVertSeq": "BMVertSeq of BMVert",
    "BMEditSelSeq": "BMEditSelSeq of BMEditSel",
}

BUILTIN_DATA_TYPE: List[str] = [
    "bool", "str", "bytes", "float", "int",
]

BUILTIN_DATA_TYPE_ALIASES: Dict[str, str] = {
    "string": "str",
    "boolean": "bool",
}

MODIFIER_DATA_TYPE: List[str] = [
    "list", "dict", "set", "tuple",
]

MODIFIER_DATA_TYPE_ALIASES: Dict[str, str] = {
    "List": "list",
    "sequence": "list",
    "array": "list",
}

# True:  XXX of YYY -> Union[List[YYY], XXXX]
# False:  XXX of YYY -> Union[List[YYY]]
LISTOF_FORMAT: Dict[str, bool] = {
    "bpy_prop_collection": True,
    "BMElemSeq": True,
    "BMEdgeSeq": True,
    "BMFaceSeq": True,
    "BMLoopSeq": True,
    "BMVertSeq": True,
    "BMEditSelSeq": True,
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

    data_type = data_type.replace(".", r"\.")

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

    def data_type(self) -> str:
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

    def data_type(self) -> str:
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

    def data_type(self) -> str:
        raise RuntimeError("data_type() is not callable ({})".format(self._data_type))

    def to_string(self) -> str:
        return self._data_type


class BuiltinDataType(DataType):
    def __init__(self, data_type: str, modifier: str=None):
        if not isinstance(data_type, str):
            raise ValueError("Argument 'data_type' must be str ({})".format(data_type))

        if data_type not in BUILTIN_DATA_TYPE:
            raise ValueError("data_type must be {} but {}"
                             .format(BUILTIN_DATA_TYPE, data_type))
        self._data_type: str = data_type
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

    def data_type(self) -> str:
        return self._data_type

    def to_string(self) -> str:
        if self._modifier is None:
            return self._data_type

        return "{}[{}]".format(MODIFIER_DATA_TYPE_TO_TYPING[self._modifier],
                               self._data_type)


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

    def data_type(self) -> str:
        raise RuntimeError("data_type is not callable ({})".format(self._modifier))

    def to_string(self) -> str:
        return self._modifier


class CustomDataType(DataType):
    def __init__(self, data_type: str, modifier: str=None):
        if not isinstance(data_type, str):
            raise ValueError("Argument 'data_type' must be str ({})".format(data_type))

        self._data_type: str = data_type
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

    def data_type(self) -> str:
        return self._data_type

    def to_string(self) -> str:
        if self._modifier is None:
            return "'{}'".format(self._data_type)

        return "{}['{}']".format(MODIFIER_DATA_TYPE_TO_TYPING[self._modifier],
                                 self._data_type)


class MixinDataType(DataType):
    def __init__(self, data_types: List['DataType']):
        if len(data_types) <= 1:
            raise ValueError("length of data_types must be >= 2 but {}"
                             .format(len(data_types)))
        self._data_types: List['DataType'] = data_types

    def type(self) -> str:
        return 'MIXIN'

    def data_types(self) -> List['DataType']:
        return self._data_types

    def to_string(self) -> str:
        s = [dt.to_string() for dt in self._data_types]
        return "typing.Union[{}]".format(", ".join(s))

    def set_data_type(self, index, data_type: 'DataType'):
        self._data_types[index] = data_type


class Info:
    def __init__(self):
        self._type: str = None

    def is_assignable(self, variable, data: dict, key: str, method: str):
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

    def is_data_type_assinable(self, variable, data: dict, key: str, method: str):
        if method == 'NEW':
            if key in data:
                return True
            return False
        elif method == 'APPEND':
            if (key in data) and isinstance(variable, UnknownDataType):
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

    def append_description(self, desc: str):
        if self._description is None:
            self._description = ""
        self._description += desc

    def description(self) -> str:
        return self._description

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
                "type": self._type,
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type.to_string()),
            }
        else:
            data = {
                "type": self._type,
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
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_data_type_assinable(self._data_type, data, "data_type", method):
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

    def append_description(self, desc: str):
        if self._description is None:
            self._description = ""
        self._description += desc

    def description(self) -> str:
        return self._description

    def set_data_type(self, dtype: 'DataType'):
        self._data_type = dtype

    def to_dict(self) -> dict:
        if self._description is None:
            self._description = ""

        if check_os() == "Windows":
            data = {
                "type": self._type,
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type.to_string()),
            }
        else:
            data = {
                "type": self._type,
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
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_data_type_assinable(self._data_type, data, "data_type", method):
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

    def append_description(self, desc: str):
        if self._description is None:
            self._description = ""
        self._description += desc

    def description(self) -> str:
        return self._description

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
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assignable(self._class, data, "class", method):
            self._class = data["class"]
        if self.is_assignable(self._module, data, "module", method):
            self._module = data["module"]
        if self.is_data_type_assinable(self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class FunctionInfo(Info):
    supported_type: List[str] = ["function", "method", "classmethod", "staticmethod"]

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

    def append_description(self, desc: str):
        if self._description is None:
            self._description = ""
        self._description += desc

    def description(self) -> str:
        return self._description

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
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assignable(self._class, data, "class", method):
            self._class = data["class"]
        if self.is_assignable(self._module, data, "module", method):
            self._module = data["module"]

        if "parameters" in data:
            if method == 'NEW':
                if len(self._parameters) == 0:
                    self._parameters = data["parameters"]
            elif method == 'APPEND':
                self._parameters.extend(data["parameters"])
            elif method == 'UPDATE':
                self._parameters = data["parameters"]

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

        if "return" in data:
            if method == 'NEW':
                if self._return is None:
                    self._return = ReturnInfo()
                    self._return.from_dict(data["return"], 'NEW')
            elif method == 'APPEND':
                if self._return is not None:
                    self._return.from_dict(data["return"], 'APPEND')
                else:
                    self._return = ReturnInfo()
                    self._return.from_dict(data["return"], 'NEW')
            elif method == 'UPDATE':
                if self._return is not None:
                    self._return.from_dict(data["return"], 'UPDATE')


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

    def append_description(self, desc: str):
        if self._description is None:
            self._description = ""
        self._description += desc

    def description(self) -> str:
        return self._description

    def methods(self) -> List['FunctionInfo']:
        return self._methods

    def base_classes(self) -> List['DataType']:
        return self._base_classes

    def add_method(self, method: 'FunctionInfo'):
        supported = ["method", "classmethod", "staticmethod"]
        if method.type() not in supported:
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format(supported, method.type()))
        self._methods.append(method)

    def add_methods(self, methods: List['FunctionInfo']):
        supported = ["method", "classmethod", "staticmethod"]
        for m in methods:
            if m.type() not in supported:
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format(supported, m.type()))
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
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assignable(self._module, data, "module", method):
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

    def add_info(self, info: 'Info'):
        self.info_list.append(info)

    def to_dict(self) -> dict:
        result = {"info_list": []}
        for info in self.info_list:
            result["info_list"].append(info.to_dict())
        return result


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

        # strip non-sense string
        strip_pattens = [
            r"\s+type\s*$",
            r"^\s*type\s+",
            r"^type$",
            r"default (True|False|[-0-9.]+)",
            r"default \".*\"",
            r"default \'.*\'",
            r"default \‘.*\’",
            r"default \“.*\”",
            r"default \{.*\}",
            r"default \([-0-9., ]*\)",
            r"\(optional\)",
            r"\(readonly\)",
            r"\(never None\)",
            r"\(optional, never None\)",
            r"\(readonly, never None\)",
            r"in \[.*\]",
            r"in \{.*\}",
            r"of [0-9]+ items",
        ]
        for sp in strip_pattens:
            dtype_str = re.sub(sp, "", dtype_str)

        def only_nonsense_chars(string_to_parse: str) -> bool:
            NONSENSE_CHARS = [",", " ", "(", ")"]
            for c in string_to_parse:
                if c not in NONSENSE_CHARS:
                    return False
            return True

        def parse_builtin_dtype(string_to_parse: str) -> (List[str], str):
            dtype = []
            stripped_string = string_to_parse
            for type_ in BUILTIN_DATA_TYPE:
                if has_data_type(stripped_string, type_):
                    dtype.append(type_)
                    stripped_string = stripped_string.replace(type_, "")
            for (key, value) in BUILTIN_DATA_TYPE_ALIASES.items():
                if has_data_type(stripped_string, key):
                    dtype.append(value)
                    stripped_string = stripped_string.replace(key, "")
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return dtype, stripped_string

        def parse_custom_dtype(string_to_parse: str) -> (List[str], str):
            dtype = []
            stripped_string = string_to_parse
            for entry in self._entry_points:
                if len(stripped_string) == 0:
                    break
                if entry.type not in ["constant", "class"]:
                    continue
                if has_data_type(stripped_string, entry.fullname()):
                    dtype.append(entry.fullname())
                    stripped_string = stripped_string.replace(entry.fullname(), "")
                    if only_nonsense_chars(stripped_string):
                        stripped_string = ""
                    continue
                full_data_type = "{}.{}".format(module_name, stripped_string)
                if has_data_type(full_data_type, entry.fullname()):
                    dtype.append(entry.fullname())
                    stripped_string = stripped_string.replace(entry.name, "")
                    if only_nonsense_chars(stripped_string):
                        stripped_string = ""
                    continue
                full_data_type = full_data_type.replace(" ", "")
                if has_data_type(full_data_type, entry.fullname()):
                    dtype.append(entry.fullname())
                    stripped_string = stripped_string.replace(entry.name, "")
                    if only_nonsense_chars(stripped_string):
                        stripped_string = ""
                    continue
                if has_data_type(stripped_string, entry.name):
                    dtype.append(entry.fullname())
                    stripped_string = stripped_string.replace(entry.name, "")
                    if only_nonsense_chars(stripped_string):
                        stripped_string = ""
                    continue
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return dtype, stripped_string

        # Check "XXX of YYY" format
        def parse_listof_case(string_to_parse: str) -> (List[Dict[str, str]], str):
            listof_case = []
            stripped_string = string_to_parse
            for class_, need_to_add in LISTOF_FORMAT.items():
                regex = r"{} of ([a-zA-z0-9_]+)".format(class_)
                m = re.search(regex, stripped_string)
                if m:
                    case = {}
                    case["modifier"] = "list"
                    case["builtin_dtype"], _ = parse_builtin_dtype(m.groups()[0])
                    case["custom_dtype"] = []
                    case["self_dtype"] = None
                    if not case["builtin_dtype"]:
                        case["custom_dtype"], _ = parse_custom_dtype(m.groups()[0])
                        if not case["custom_dtype"]:
                            continue
                    if need_to_add:
                        case["self_dtype"] = class_
                    stripped_string = stripped_string.replace(m.group(), "")
                    listof_case.append(case)
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return listof_case, stripped_string

        def parse_modifier(string_to_parse: str) -> (List[str], str):
            modifier = None
            stripped_string = string_to_parse
            for type_ in MODIFIER_DATA_TYPE:
                if has_data_type(stripped_string, type_):
                    modifier = type_
                    # remove modifier from stripped_string
                    # TODO: need to clip only modifier string
                    #       (issue ex. hogelist -> hoge)
                    stripped_string = stripped_string.replace(type_, "")
                    break
            if not modifier:
                for (key, value) in MODIFIER_DATA_TYPE_ALIASES.items():
                    if has_data_type(stripped_string, key):
                        modifier = value
                        # remove modifier from stripped_string
                        # TODO: need to clip only modifier string
                        #       (issue ex. hogelist -> hoge)
                        stripped_string = stripped_string.replace(key, "")
                        break
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return modifier, stripped_string


        listof_case, dtype_str = parse_listof_case(dtype_str)
        modifier, dtype_str = parse_modifier(dtype_str)

        # at first we check built-in data type
        builtin_dtypes, dtype_str = parse_builtin_dtype(dtype_str)
        builtin_dtypes = list(set(builtin_dtypes))

        # and then, search from package entry points
        custom_dtypes, dtype_str = parse_custom_dtype(dtype_str)
        if not builtin_dtypes and not custom_dtypes and not modifier and not listof_case:
            output_log(LOG_LEVEL_WARN,
                       "Could not find any data type ({})"
                       .format(remove_unencodable(data_type.to_string())))
        custom_dtypes = list(set(custom_dtypes))

        if dtype_str:
            output_log(LOG_LEVEL_DEBUG,
                       "dtype_str is still exists ({})".format(remove_unencodable(dtype_str)))

        dtype_list = []
        for case in listof_case:
            if case["builtin_dtype"]:
                dtype_list.append(BuiltinDataType(case["builtin_dtype"][0], case["modifier"]))
            elif case["custom_dtype"]:
                dtype_list.append(CustomDataType(case["custom_dtype"][0], case["modifier"]))
            if case["self_dtype"]:
                dtype_list.append(CustomDataType(case["self_dtype"]))

        if modifier is None:
            for d in builtin_dtypes:
                dtype_list.append(BuiltinDataType(d))
            for d in custom_dtypes:
                dtype_list.append(CustomDataType(d))
        else:
            for d in builtin_dtypes:
                if (modifier != "list") and (modifier != "set"):
                    output_log(LOG_LEVEL_WARN,
                               "Modifier '{}' does not support element type inference ({})"
                               .format(modifier, d))
                    dtype_list.append(ModifierDataType(modifier))
                else:
                    dtype_list.append(BuiltinDataType(d, modifier))
            for d in custom_dtypes:
                if (modifier != "list") and (modifier != "set"):
                    output_log(LOG_LEVEL_WARN,
                               "Modifier '{}' does not support element type inference ({})"
                               .format(modifier, d))
                    dtype_list.append(ModifierDataType(modifier))
                else:
                    dtype_list.append(CustomDataType(d, modifier))
            if not builtin_dtypes and not custom_dtypes:
                dtype_list.append(ModifierDataType(modifier))

        if len(dtype_list) == 1:
            return dtype_list[0]
        elif len(dtype_list) >= 2:
            return MixinDataType(dtype_list)
        else:
            return UnknownDataType()

    def get_base_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        sp = data_type.split(".")
        return sp[-1]

    def get_module_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        module_names = data_type.split(".")[:-1]

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
            return ""

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

    def get_generation_data_type(self, data_type: str,
                                 target_module: str) -> str:
        mod_names_full_1 = self.get_module_name(data_type)
        mod_names_full_2 = target_module

        if mod_names_full_1 is None or mod_names_full_2 is None:
            return data_type      # TODO: should return better data_type

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

        # [Case 1] No match => Use data_type
        #   data_type: bpy.types.Mesh
        #   target_module: bgl
        #       => bpy.types.Mesh
        if match_level == 0:
            final_data_type = self._ensure_correct_data_type(data_type)
        else:
            rest_level_1 = len(mod_names_1) - match_level
            rest_level_2 = len(mod_names_2) - match_level

            # [Case 2] Match exactly => Use data_type without module
            #   data_type: bgl.Buffer
            #   target_module: bgl
            #       => Buffer
            if rest_level_1 == 0 and rest_level_2 == 0:
                final_data_type = self.get_base_name(data_type)
            # [Case 3] Match partially (Same level) => Use data_type
            #   data_type: bpy.types.Mesh
            #   target_module: bpy.ops
            #       => bpy.types.Mesh
            elif rest_level_1 >= 1 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type)
            # [Case 4] Match partially (Upper level) => Use data_type
            #   data_type: mathutils.Vector
            #   target_module: mathutils.noise
            #       => mathutils.Vector
            elif rest_level_1 == 0 and rest_level_2 >= 1:
                final_data_type = self._ensure_correct_data_type(data_type)
            # [Case 5] Match partially (Lower level) => Use data_type
            #   data_type: mathutils.noise.cell
            #   target_module: mathutils
            #       => mathutils.noise.cell
            elif rest_level_1 >= 1 and rest_level_2 == 0:
                final_data_type = self._ensure_correct_data_type(data_type)
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
