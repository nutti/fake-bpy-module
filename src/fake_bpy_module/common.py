import copy
import re
from typing import List, Dict, Set, Tuple
import typing

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
    "listlist", "tupletuple",
    "listtuple", "listcallable",
    "Generic",
    "typing.Iterator",
    "typing.Callable",
    "typing.Any",
    "typing.Sequence",
]

CUSTOM_MODIFIER_MODIFIER_DATA_TYPE: List[str] = [
    "bpy.types.bpy_prop_collection",
    "bpy.types.bpy_prop_array",
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

# Key is string, and value is XXX -> Dict[str, XXX]
DICT_WITH_STRKEY_FORMAT: List[str] = {
    "bpy_prop_collection",
}

MODIFIER_DATA_TYPE_TO_TYPING: Dict[str, str] = {
    "list": "typing.List",
    "dict": "typing.Dict",
    "set": "typing.Set",
    "tuple": "typing.Tuple",
    "Generic": "typing.Generic",
    "typing.Iterator": "typing.Iterator",
    "typing.Callable": "typing.Callable",
    "typing.Sequence": "typing.Sequence",
    "typing.Any": "typing.Any",
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
        if (si == start_index) and \
                ((ei != end_index) and (str_[ei] in ALLOWED_CHAR_AFTER)):
            return True
        # example: "list of int"
        if ((si != start_index) and (str_[si-1] in ALLOWED_CHAR_BEFORE)) and \
                (ei == end_index):
            return True
        # example: "list of int or float"
        if ((si != start_index) and (str_[si-1] in ALLOWED_CHAR_BEFORE)) and \
                ((ei != end_index) and (str_[ei] in ALLOWED_CHAR_AFTER)):
            return True

    return False


FROM_DICT_METHOD: List[str] = [
    'NONE',
    'NEW',
    'APPEND',
    'UPDATE',
]


class DataTypeMetadata:
    def __init__(self):
        self.variable_kind = None
        self.readonly: bool = False
        self.never_none: bool = False       # Add typing.Optional if false
        self.optional: bool = False         # Default value is needed if true
        self.default_value = None

    def __str__(self):
        flags = []
        if self.readonly:
            flags.append('READONLY')
        if self.never_none:
            flags.append('NEVER_NONE')
        if self.optional:
            flags.append('OPTIONAL')

        return f"Kind: {self.variable_kind}, Flags: {flags}, " \
               f"Default Value: {self.default_value}"


class DataType:
    def __init__(self):
        self._metadata: DataTypeMetadata = DataTypeMetadata()
        self._is_optional: bool = False

    @staticmethod
    def output_typing_optional(func):
        def wrapper(self, *args, **kwargs):
            inner_str: str = func(self, *args, **kwargs)
            metadata: DataTypeMetadata = self.get_metadata()
            if metadata.variable_kind == 'FUNC_ARG' and \
               not metadata.never_none:
                inner_str = f"typing.Optional[{inner_str}]"
            return inner_str
        return wrapper

    def get_metadata(self) -> DataTypeMetadata:
        return self._metadata

    def set_metadata(self, metadata: DataTypeMetadata):
        self._metadata = metadata

    def set_is_optional(self, is_optional: bool):
        self._is_optional = is_optional

    def is_optional(self) -> bool:
        return self._is_optional

    def type(self) -> str:
        raise NotImplementedError()

    def has_modifier(self) -> bool:
        raise NotImplementedError()

    def modifier(self) -> 'ModifierDataType':
        raise NotImplementedError()

    def data_type(self) -> str:
        raise NotImplementedError()

    def to_string(self) -> str:
        raise NotImplementedError()


class UnknownDataType(DataType):

    def type(self) -> str:
        return 'UNKNOWN'

    def has_modifier(self) -> bool:
        raise RuntimeError("has_modifier() is not callable")

    def modifier(self) -> 'ModifierDataType':
        raise RuntimeError("module() is not callable")

    def data_type(self) -> str:
        raise RuntimeError("data_type() is not callable")

    def to_string(self) -> str:
        return ""


class IntermidiateDataType(DataType):
    def __init__(self, data_type: str):
        super().__init__()

        self._data_type: str = data_type

    def type(self) -> str:
        return 'INTERMIDIATE'

    def has_modifier(self) -> bool:
        raise RuntimeError(
            f"has_modifier() is not callable ({self._data_type})")

    def modifier(self) -> 'ModifierDataType':
        raise RuntimeError(f"module() is not callable ({self._data_type})")

    def data_type(self) -> str:
        raise RuntimeError(f"data_type() is not callable ({self._data_type})")

    def to_string(self) -> str:
        return self._data_type


class BuiltinDataType(DataType):
    def __init__(
            self, data_type: str, modifier: 'ModifierDataType' = None,
            modifier_add_info=None):
        super().__init__()

        assert (modifier is None) or (not isinstance(modifier, str))

        if not isinstance(data_type, str):
            raise ValueError(f"Argument 'data_type' must be str ({data_type})")

        if data_type not in BUILTIN_DATA_TYPE:
            raise ValueError(
                f"data_type must be {BUILTIN_DATA_TYPE} but {data_type}")
        self._data_type: str = data_type
        self._modifier: 'ModifierDataType' = modifier
        self._modifier_add_info = modifier_add_info

    def type(self) -> str:
        return 'BUILTIN'

    def has_modifier(self) -> bool:
        return self._modifier is not None

    def modifier(self) -> 'ModifierDataType':
        return self._modifier

    def modifier_add_info(self):
        return self._modifier_add_info

    def data_type(self) -> str:
        return self._data_type

    @DataType.output_typing_optional
    def to_string(self) -> str:
        if self._modifier is None:
            return self._data_type

        if self._modifier.modifier_data_type() == "dict":
            if self._modifier_add_info is not None:
                if self._modifier_add_info["dict_key"] in BUILTIN_DATA_TYPE:
                    return f"{self._modifier.to_string()}[" \
                        f"{self._modifier_add_info['dict_key']}, " \
                        f"{self._data_type}]"
                return f"{self._modifier.to_string()}[" \
                    f"'{self._modifier_add_info['dict_key']}', " \
                    f"{self._data_type}]"
        elif self._modifier.modifier_data_type() == "tuple":
            if self._modifier_add_info is not None:
                elms_strs = [elm.to_string()
                             for elm in self._modifier_add_info['tuple_elms']]
                return f"{self._modifier.to_string()}[" \
                    f"{', '.join(elms_strs)}]"
        elif self._modifier.modifier_data_type() == "tupletuple":
            if self._modifier_add_info is not None:
                inner_str = []
                for elms in self._modifier_add_info["tuple_elms"]:
                    inner_str.append(f"typing.Tuple[{', '.join(elms)}]")
                return f"typing.Tuple[{', '.join(inner_str)}]"
        elif self._modifier.modifier_data_type() == "listlist":
            return f"typing.List[typing.List[{self._data_type}]]"
        elif self._modifier.modifier_data_type() == 'listtuple':
            if self._modifier_add_info is not None:
                return "typing.List[typing.Tuple[" \
                    f"{', '.join(self._modifier_add_info['tuple_elms'])}]]"

        return f"{self._modifier.to_string()}[{self._data_type}]"


class ModifierDataType(DataType):
    def __init__(self, modifier: str):
        super().__init__()

        if (modifier is None) or (modifier not in MODIFIER_DATA_TYPE):
            raise ValueError(
                f"modifier must be {MODIFIER_DATA_TYPE} but {modifier}")
        self._modifier: str = modifier

    def type(self) -> str:
        return 'MODIFIER'

    def has_modifier(self) -> bool:
        raise RuntimeError(
            f"has_modifier() is not callable ({self._modifier})")

    def modifier(self) -> 'ModifierDataType':
        raise RuntimeError(f"modifier() is not callable ({self._modifier})")

    def data_type(self) -> str:
        raise RuntimeError(f"data_type is not callable ({self._modifier})")

    def modifier_data_type(self) -> str:
        return self._modifier

    @DataType.output_typing_optional
    def to_string(self) -> str:
        return MODIFIER_DATA_TYPE_TO_TYPING[self._modifier]


class CustomDataType(DataType):
    def __init__(
            self, data_type: str, modifier: 'ModifierDataType' = None,
            modifier_add_info=None, skip_refine=False):
        super().__init__()

        assert (modifier is None) or (not isinstance(modifier, str))

        if not isinstance(data_type, str):
            raise ValueError(f"Argument 'data_type' must be str ({data_type})")

        self._data_type: str = data_type
        self._modifier: 'ModifierDataType' = modifier
        self._modifier_add_info = modifier_add_info
        self._skip_refine = skip_refine

    def type(self) -> str:
        return 'CUSTOM'

    def skip_refine(self):
        return self._skip_refine

    def has_modifier(self) -> bool:
        return self._modifier is not None

    def modifier(self) -> 'ModifierDataType':
        return self._modifier

    def modifier_add_info(self):
        return self._modifier_add_info

    def data_type(self) -> str:
        return self._data_type

    @DataType.output_typing_optional
    def to_string(self) -> str:
        if self._modifier is None:
            return f"'{self._data_type}'"

        if self._modifier.modifier_data_type() == "dict":
            if self._modifier_add_info is not None:
                if self._modifier_add_info["dict_key"] in BUILTIN_DATA_TYPE:
                    return f"{self._modifier.to_string()}" \
                        f"[{self._modifier_add_info['dict_key']}, " \
                        f"'{self._data_type}']"
                return f"{self._modifier.to_string()}['" \
                    f"{self._modifier_add_info['dict_key']}', " \
                    f"'{self._data_type}']"
        elif self._modifier.modifier_data_type() == "tuple":
            if self._modifier_add_info is not None:
                elms_strs = [elm.to_string()
                             for elm in self._modifier_add_info['tuple_elms']]
                return f"{self._modifier.to_string()}[" \
                    f"{', '.join(elms_strs)}]"
        elif self._modifier.modifier_data_type() == "listlist":
            return f"typing.List[typing.List['{self._data_type}']]"
        elif self._modifier.modifier_data_type() == "listcallable":
            return "typing.List[typing.Callable[['" \
                f"{','.join(self._modifier_add_info['arguments'])}'], None]]"

        return f"{self._modifier.to_string()}['{self._data_type}']"


class CustomModifierDataType(ModifierDataType):
    # pylint: disable=W0231
    def __init__(self, modifier: str):
        self._is_optional: bool = False
        self._metadata: DataTypeMetadata = DataTypeMetadata()

        if (modifier is None) or \
                (modifier not in CUSTOM_MODIFIER_MODIFIER_DATA_TYPE):
            raise ValueError(
                f"modifier must be {CUSTOM_MODIFIER_MODIFIER_DATA_TYPE} but "
                f"{modifier}")
        self._modifier: str = modifier
        self._output_modifier_name = modifier

    def type(self) -> str:
        return 'CUSTOM_MODIFIER'

    def has_modifier(self) -> bool:
        raise RuntimeError(
            f"has_modifier() is not callable ({self._modifier})")

    def modifier(self) -> 'ModifierDataType':
        raise RuntimeError(f"modifier() is not callable ({self._modifier})")

    def data_type(self) -> str:
        raise RuntimeError(f"data_type() is not callable ({self._modifier})")

    def modifier_data_type(self) -> str:
        return self._modifier

    def output_modifier_name(self) -> str:
        return self._output_modifier_name

    def set_output_modifier_name(self, modifier_name: str):
        self._output_modifier_name = modifier_name

    @DataType.output_typing_optional
    def to_string(self) -> str:
        return self._output_modifier_name


class MixinDataType(DataType):
    def __init__(self, data_types: List['DataType']):
        super().__init__()

        if len(data_types) <= 1:
            raise ValueError(
                f"length of data_types must be >= 2 but {len(data_types)}")
        self._data_types: List['DataType'] = data_types

    def type(self) -> str:
        return 'MIXIN'

    def data_type(self) -> str:
        raise RuntimeError("data_type() is not callable")

    def has_modifier(self) -> bool:
        raise RuntimeError("has_modifier() is not callable")

    def modifier(self) -> 'ModifierDataType':
        raise RuntimeError("modifier() is not callable")

    def data_types(self) -> List['DataType']:
        return self._data_types

    @DataType.output_typing_optional
    def to_string(self) -> str:
        s = [dt.to_string() for dt in self._data_types]
        return f"typing.Union[{', '.join(s)}]"

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
        if method == 'APPEND':
            if (key in data) and (variable is None):
                return True
            return False
        if method == 'UPDATE':
            if key in data:
                return True
            return False

        raise RuntimeError(f"Unsupported method: {method}")

    def is_data_type_assinable(
            self, variable, data: dict, key: str, method: str):
        if method == 'NEW':
            if key in data:
                return True
            return False
        if method == 'APPEND':
            if (key in data) and isinstance(variable, UnknownDataType):
                return True
            return False
        if method == 'UPDATE':
            if key in data:
                return True
            return False

        raise RuntimeError(f"Unsupported method: {method}")

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

    def from_dict(self, data: dict, method: str = False):
        raise NotImplementedError()


class ParameterDetailInfo(Info):
    def __init__(self):
        super().__init__()
        self._type: str = "parameter"
        self._name: str = None
        self._description: str = None
        self._data_type: 'DataType' = UnknownDataType()

    def name(self) -> str:
        return self._name

    def module(self) -> str:
        raise RuntimeError("module() is not callable")

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
            default_value = self._data_type.get_metadata().default_value
            if default_value is not None:
                data["default_value"] = remove_unencodable(default_value)
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "data_type": self._data_type.to_string(),
            }
            default_value = self._data_type.get_metadata().default_value
            if default_value is not None:
                data["default_value"] = remove_unencodable(default_value)

        return data

    def from_dict(self, data: dict, method: str = 'NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "parameter":
            raise RuntimeError(f"Unsupported type: {data['type']}")

        self._type = data["type"]
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_data_type_assinable(
                self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class ReturnInfo(Info):
    def __init__(self):
        super().__init__()
        self._type: str = "return"
        self._description: str = None
        self._data_type: 'DataType' = UnknownDataType()

    def name(self) -> str:
        raise RuntimeError("name() is not callable")

    def module(self) -> str:
        raise RuntimeError("module() is not callable")

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

    def from_dict(self, data: dict, method: str = 'NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "return":
            raise RuntimeError(f"Unsupported type: {data['type']}")

        self._type = data["type"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_data_type_assinable(
                self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class VariableInfo(Info):
    supported_type: List[str] = ["constant", "attribute"]

    def __init__(self, type_: str):
        super().__init__()
        if type_ not in self.supported_type:
            raise RuntimeError(
                f"VariableInfo must be type {self.supported_type} "
                f"but {type_}")
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

    def from_dict(self, data: dict, method: str = 'NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] not in self.supported_type:
            raise RuntimeError(f"Unsupported type: {data['type']}")

        self._type = data["type"]
        if self.is_assignable(self._name, data, "name", method):
            self._name = data["name"]
        if self.is_assignable(self._description, data, "description", method):
            self._description = data["description"]
        if self.is_assignable(self._class, data, "class", method):
            self._class = data["class"]
        if self.is_assignable(self._module, data, "module", method):
            self._module = data["module"]
        if self.is_data_type_assinable(
                self._data_type, data, "data_type", method):
            self._data_type = IntermidiateDataType(data["data_type"])


class FunctionInfo(Info):
    supported_type: List[str] = [
        "function", "method", "classmethod", "staticmethod"]

    def __init__(self, type_: str):
        super().__init__()
        if type_ not in self.supported_type:
            raise RuntimeError(
                f"FunctionInfo must be type {self.supported_type} but {type_}")
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

    def add_parameter(self, param: str, pos: int = -1):
        if param in self._parameters:
            output_log(
                LOG_LEVEL_WARN,
                f"Parameter {param} is already registered in "
                f"({' | '.join(self._parameters)}, so skip to add this "
                f"parameter. (module: {self._module}, name: {self._name})")
            return
        if pos == -1:
            self._parameters.append(param)
        else:
            self._parameters.insert(pos, param)

    def add_parameters(self, params: List[str]):
        for p in params:
            self.add_parameter(p)

    def remove_parameter(self, idx: int):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        del self._parameters[idx]

    def add_parameter_detail(
            self, param: 'ParameterDetailInfo', pos: int = -1):
        if param.type() != "parameter":
            raise RuntimeError(
                f"Expected Info.type() is parameter but {param.type()}.")
        if pos == -1:
            self._parameter_details.append(param)
        else:
            self._parameter_details.insert(pos, param)

    def add_parameter_details(self, params: List['ParameterDetailInfo']):
        for p in params:
            if p.type() != "parameter":
                raise RuntimeError(
                    f"Expected Info.type() is parameter but {p.type()}.")
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
            raise RuntimeError(f"'type' must be ({self.supported_type})")

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
                "parameters": list(self._parameters),
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
                "parameters": list(self._parameters),
                "parameter_details": [p.to_dict()
                                      for p in self._parameter_details],
            }

        return data

    def from_dict(self, data: dict, method: str = 'NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] not in self.supported_type:
            raise RuntimeError(f"Unsupported type: {data['type']}")

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
                        raise RuntimeError(f"{pd['name']} is not found")

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
        super().__init__()
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
            raise RuntimeError(
                f"Expected Info.type() is {supported} but {method.type()}.")
        self._methods.append(method)

    def add_methods(self, methods: List['FunctionInfo']):
        supported = ["method", "classmethod", "staticmethod"]
        for m in methods:
            if m.type() not in supported:
                raise RuntimeError(
                    f"Expected Info.type() is {supported} but {m.type()}.")
            self.add_method(m)

    def set_methods(self, methods: List['FunctionInfo']):
        self._methods = []
        self.add_methods(methods)

    def add_attribute(self, attr: 'VariableInfo'):
        if attr.type() != "attribute":
            raise RuntimeError(
                f"Expected Info.type() is attribute but {attr.type()}.")
        self._attributes.append(attr)

    def add_attributes(self, attrs: List['VariableInfo']):
        for a in attrs:
            if a.type() != "attribute":
                raise RuntimeError(
                    f"Expected Info.type() is attribute but {a.type()}.")
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

    def from_dict(self, data: dict, method: str = 'NONE'):
        if "type" not in data:
            raise RuntimeError("data must have type")
        if data["type"] != "class":
            raise RuntimeError(f"Unsupported type: {data['type']}")

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
                        raise RuntimeError(
                            f"Method '{m['name']}' is not found at class "
                            f"'{self._module}.{self._name}'")
            else:
                raise RuntimeError(f"Unsupported method: {method}")

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
                        raise RuntimeError(f"{a['name']} is not found")
            else:
                raise RuntimeError(f"Unsupported method: {method}")

        if "base_classes" in data:
            if method == 'NEW':
                for c in data["base_classes"]:
                    new_c = IntermidiateDataType(c)
                    self._base_classes.append(new_c)
            else:
                raise RuntimeError(f"Unsupported method: {method}")


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

    def __init__(
            self, package_structure: 'ModuleStructure',
            entry_points: List['EntryPoint']):
        self._package_structure: 'ModuleStructure' = package_structure
        self._entry_points: List['EntryPoint'] = entry_points

        self._entry_points_cache: Dict[str, Set] = {}
        self._entry_points_cache["uniq_full_names"] = {
            e.fullname() for e in self._entry_points}
        self._entry_points_cache["uniq_module_names"] = {
            e.module for e in self._entry_points}

    def _parse_custom_data_type(
            self, string_to_parse: str, uniq_full_names: Set[str],
            uniq_module_names: Set[str], module_name: str) -> str:
        dtype_str = string_to_parse
        if dtype_str in uniq_full_names:
            return dtype_str
        dtype_str = f"{module_name}.{string_to_parse}"
        if dtype_str in uniq_full_names:
            return dtype_str

        for mod in list(uniq_module_names):
            dtype_str = f"{mod}.{string_to_parse}"
            if dtype_str in uniq_full_names:
                return dtype_str

        return None

    def _build_metadata(
            self, dtype_str: str, module_name: str, parameter_str: str,
            variable_kind: str) -> Tuple[DataTypeMetadata, str]:
        metadata = DataTypeMetadata()

        metadata.variable_kind = variable_kind

        # Get default value from parameter string.
        if parameter_str is not None:
            m = re.match(r"^([a-zA-Z0-9_]+?)=(.*)", parameter_str)
            if m:
                metadata.default_value = m.group(2)

        if module_name.startswith("bpy."):
            m = re.search(r"\(([a-zA-Z, ]+?)\)$", dtype_str)
            if not m:
                return metadata, dtype_str

            # Get parameter option.
            data = [e.strip().lower() for e in m.group(1).split(",")]
            has_unknown_metadata = False
            for d in data:
                if d == "optional":
                    metadata.optional = True
                elif d == "readonly":
                    metadata.readonly = True
                elif d == "never none":
                    metadata.never_none = True
                else:
                    has_unknown_metadata = True
                    output_log(
                        LOG_LEVEL_WARN,
                        f"Unknown metadata '{d}' is found from {dtype_str}")

            # If there is unknown parameter options, we don't strip them from
            # original string.
            if has_unknown_metadata:
                return metadata, dtype_str

            # Strip the unused string to speed up the later parsing process.
            stripped = re.sub(r"\(([a-zA-Z, ]+?)\)$", "", dtype_str)
            output_log(LOG_LEVEL_DEBUG,
                       f"Data type is stripped: {dtype_str} -> {stripped}")

            return metadata, stripped

        # From this, we assumed non-bpy module.

        metadata.never_none = True
        m = re.search(r"or None$", dtype_str)
        if not m:
            return metadata, dtype_str

        metadata.never_none = False
        stripped = re.sub(r"or None$", "", dtype_str)
        output_log(LOG_LEVEL_DEBUG,
                   f"'or None' is stripped: {dtype_str} -> {stripped}")

        return metadata, stripped

    # pylint: disable=R0913
    def _get_refined_data_type_fast(
            self, dtype_str: str, uniq_full_names: Set[str],
            uniq_module_names: Set[str], module_name: str,
            variable_kind: str,
            additional_info: Dict[str, typing.Any] = None) -> 'DataType':
        # pylint: disable=R0912,R0911,R0915
        if re.match(r"^\s*$", dtype_str):
            return ModifierDataType("typing.Any")

        if dtype_str == "Same type with self class":
            s = self._parse_custom_data_type(
                additional_info["self_class"], uniq_full_names,
                uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        if re.match(r"^(type|object|function)$", dtype_str):
            return ModifierDataType("typing.Any")

        if re.match(r"^Depends on function prototype", dtype_str):
            return ModifierDataType("typing.Any")

        if re.match(r"^(any|Any type.)$", dtype_str):
            return ModifierDataType("typing.Any")

        if re.match(r"^[23][dD] [Vv]ector$", dtype_str):
            s = self._parse_custom_data_type(
                "Vector", uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)
        if re.match(r"^4x4 mathutils.Matrix$", dtype_str):
            s = self._parse_custom_data_type(
                "Matrix", uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        m = re.match(r"^enum in \[(.*)\], default (.+)$", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("str"),
                BuiltinDataType("int")
            ]
            return MixinDataType(dtypes)
        # Ex: enum in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        m = re.match(r"^enum in \[(.*)\](, \(.+\))*$", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("str"),
                BuiltinDataType("int")
            ]
            return MixinDataType(dtypes)

        # Ex: enum set in {'KEYMAP_FALLBACK'}, (optional)
        m = re.match(r"^enum set in \{(.*)\}(, \(.+\))*$", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("str", ModifierDataType("set")),
                BuiltinDataType("int", ModifierDataType("set"))
            ]
            return MixinDataType(dtypes)

        # Ex: enum in :ref:`rna_enum_object_modifier_type_items`, (optional)
        m = re.match(r"^enum in :ref:`rna.*`", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("str"),
                BuiltinDataType("int")
            ]
            return MixinDataType(dtypes)

        # Ex: Enumerated constant
        m = re.match(r"^Enumerated constant$", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("str", ModifierDataType("set")),
                BuiltinDataType("int", ModifierDataType("set"))
            ]
            return MixinDataType(dtypes)

        # Ex: boolean, default False
        m = re.match(r"^boolean, default (False|True)$", dtype_str)
        if m:
            return BuiltinDataType("bool")
        # Ex: boolean array of 3 items, (optional)
        m = re.match(r"^(boolean) array of ([0-9]+) items(, .+)*$", dtype_str)
        if m:
            return BuiltinDataType("bool", ModifierDataType("list"))

        m = re.match(r"^boolean$", dtype_str)
        if m:
            return BuiltinDataType("bool")
        m = re.match(r"^bool$", dtype_str)
        if m:
            return BuiltinDataType("bool")

        m = re.match(r"^bytes$", dtype_str)
        if m:
            return BuiltinDataType("bytes")
        m = re.match(r"^byte sequence", dtype_str)
        if m:
            return BuiltinDataType(
                "bytes", ModifierDataType("typing.Sequence"))

        m = re.match(r"^[cC]allable.*", dtype_str)
        if m:
            return ModifierDataType("typing.Callable")

        m = re.match(
            r"^`((mathutils.)*(Color|Euler|Matrix|Quaternion|Vector))`$",
            dtype_str)
        if m:
            if variable_kind in ('FUNC_ARG', 'CONST', 'CLS_ATTR'):
                s = self._parse_custom_data_type(
                        m.group(1), uniq_full_names, uniq_module_names,
                        module_name)
                if s:
                    dtypes = [
                        BuiltinDataType("float", ModifierDataType(
                            "typing.Sequence")),
                        CustomDataType(s)
                    ]
                    return MixinDataType(dtypes)

        # Ex: int array of 2 items in [-32768, 32767], default (0, 0)
        m = re.match(
            r"^(int|float) array of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$",   # noqa # pylint: disable=C0301
            dtype_str)
        if m:
            if m.group(1) in ("int", "float"):
                return BuiltinDataType(m.group(1), CustomModifierDataType(
                    "bpy.types.bpy_prop_array"))
        # Ex: :`mathutils.Euler` rotation of 3 items in [-inf, inf],
        #     default (0.0, 0.0, 0.0)
        m = re.match(
            r"^`(mathutils.[a-zA-Z]+)` (rotation )*of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$",     # noqa # pylint: disable=C0301
            dtype_str
        )
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                tuple_elms = [BuiltinDataType("float")] * int(m.group(3))
                dtypes = [
                    BuiltinDataType("float", ModifierDataType("list")),
                    BuiltinDataType(
                        "float", ModifierDataType("tuple"),
                        modifier_add_info={
                            "tuple_elms": tuple_elms
                        }),
                    CustomDataType(s)
                ]
                return MixinDataType(dtypes)
        # Ex: float triplet
        m = re.match(r"^float triplet$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                "mathutils.Vector", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                dtypes = [
                    BuiltinDataType("float", ModifierDataType(
                        "typing.Sequence")),
                    CustomDataType(s)
                ]
                return MixinDataType(dtypes)
        # Ex: int in [-inf, inf], default 0, (readonly)
        m = re.match(
            r"^(int|float) in \[([-einf+0-9,. ]+)\](, .+)*$", dtype_str)
        if m:
            return BuiltinDataType(m.group(1))
        m = re.match(r"(int|float)$", dtype_str)
        if m:
            return BuiltinDataType(m.group(1))
        m = re.match(r"^unsigned int$", dtype_str)
        if m:
            return BuiltinDataType("int")
        m = re.match(r"^int \(boolean\)$", dtype_str)
        if m:
            return BuiltinDataType("int")
        m = re.match(r"^int sequence$", dtype_str)
        if m:
            return BuiltinDataType("int", ModifierDataType("typing.Sequence"))

        # Ex: float multi-dimensional array of 3 * 3 items in [-inf, inf]
        m = re.match(
            r"^float multi-dimensional array of ([0-9]) \* ([0-9]) items in "
            r"\[([-einf+0-9,. ]+)\](, .+)*$",
            dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("float", ModifierDataType("listlist")),
                BuiltinDataType(
                    "float", ModifierDataType("tupletuple"),
                    modifier_add_info={
                        "tuple_elms": [["float"] * int(m.group(1))] * int(m.group(2))   # noqa # pylint: disable=C0301
                    }
                )
            ]
            return MixinDataType(dtypes)
        m = re.match(
            r"^`mathutils.Matrix` of ([0-9]) \* ([0-9]) items in "
            r"\[([-einf+0-9,. ]+)\](, .+)*$",
            dtype_str)
        if m:
            s = self._parse_custom_data_type(
                "mathutils.Matrix", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                dtypes = [
                    BuiltinDataType("float", ModifierDataType("listlist")),
                    BuiltinDataType(
                        "float", ModifierDataType("tupletuple"),
                        modifier_add_info={
                            "tuple_elms": [["float"] * int(m.group(1))] * int(m.group(2))   # noqa # pylint: disable=C0301
                        }
                    ),
                    CustomDataType(s)
                ]
                return MixinDataType(dtypes)
        m = re.match(r"^double$", dtype_str)
        if m:
            return BuiltinDataType("float")
        m = re.match(r"^double \(float\)", dtype_str)
        if m:
            return BuiltinDataType("float")

        if re.match(r"^(str|string|strings|string)\.*$", dtype_str):
            return BuiltinDataType("str")
        if re.match(r"^tuple$", dtype_str):
            return ModifierDataType("tuple")
        if re.match(r"^sequence$", dtype_str):
            return ModifierDataType("typing.Sequence")

        if re.match(r"^`bgl.Buffer` ", dtype_str):
            s1 = self._parse_custom_data_type(
                "bgl.Buffer", uniq_full_names, uniq_module_names, module_name)
            if s1:
                return CustomDataType(s1)

        m = re.match(
            r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `([a-zA-Z0-9]+)`, $",
            dtype_str)
        if m:
            s1 = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            s2 = self._parse_custom_data_type(
                m.group(2), uniq_full_names, uniq_module_names, module_name)
            if s1 and s2:
                return CustomDataType(s1)

        m = re.match(r"^set of strings", dtype_str)
        if m:
            return BuiltinDataType("str", ModifierDataType("set"))

        # Ex: sequence of string tuples or a function
        m = re.match(r"^sequence of string tuples or a function$", dtype_str)
        if m:
            dtypes = [
                BuiltinDataType("int", ModifierDataType("listtuple"),
                                modifier_add_info={
                                    "tuple_elms": ["str", "str", "str"]
                                }),
                ModifierDataType("typing.Callable")
            ]
            return MixinDataType(dtypes)
        # Ex: sequence of bpy.types.Action
        m = re.match(r"^sequence of `([a-zA-Z0-9_.]+)`$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s, ModifierDataType("typing.Sequence"))
        # Ex: `bpy_prop_collection` of `ThemeStripColor`,
        #     (readonly, never None)
        m = re.match(
            r"^`bpy_prop_collection` of `([a-zA-Z0-9]+)`, $",
            dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(
                    s, CustomModifierDataType("bpy.types.bpy_prop_collection"))
        # Ex: List of FEdge objects
        m = re.match(r"^List of `([A-Za-z0-9]+)` objects$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s, ModifierDataType("list"))
        # Ex: list of FEdge
        m = re.match(r"^[Ll]ist of `([A-Za-z0-9_.]+)`$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s, ModifierDataType("list"))
        # Ex: list of ints
        m = re.match(r"^(list|sequence) of (float|int|str)", dtype_str)
        if m:
            return BuiltinDataType(m.group(2), ModifierDataType("list"))
        # Ex: list of (bmesh.types.BMVert)
        m = re.match(r"^list of \(([a-zA-Z.,` ]+)\)", dtype_str)
        if m:
            items = m.group(1).split(",")
            dtypes = []
            for item in items:
                im = re.match(r"^`([a-zA-Z.]+)`$", item.strip())
                if im:
                    s = self._parse_custom_data_type(
                        im.group(1), uniq_full_names, uniq_module_names,
                        module_name)
                    if s:
                        dtypes.append(
                            CustomDataType(s, ModifierDataType("list")))
            if len(dtypes) == 1:
                return dtypes[0]
            if len(dtypes) > 1:
                return MixinDataType(dtypes)
        # Ex: BMElemSeq of BMEdge
        m = re.match(r"`BMElemSeq` of `([a-zA-Z0-9]+)`$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                dtypes = [
                    CustomDataType(s, ModifierDataType("list")),
                    CustomDataType("bmesh.types.BMElemSeq")
                ]
                return MixinDataType(dtypes)
        # Ex: tuple of mathutils.Vector's
        m = re.match(r"^tuple of `([a-zA-Z0-9.]+)`('s)*$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                dd = CustomDataType(
                    s, ModifierDataType("tuple"),
                    modifier_add_info={"tuple_elms": [CustomDataType(s)]},
                    skip_refine=True)
                return dd

        m = re.match(
            r"^(BMVertSeq|BMEdgeSeq|BMFaceSeq|BMLoopSeq|BMEditSelSeq)$",
            dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                dtypes = [
                    CustomDataType(s.rstrip("Seq"), ModifierDataType("list")),
                    CustomDataType(s)
                ]
                return MixinDataType(dtypes)

        m = re.match(r"^dict with string keys$", dtype_str)
        if m:
            return ModifierDataType("dict")
        m = re.match(r"^iterable object$", dtype_str)
        if m:
            return ModifierDataType("list")
        m = re.match(r"^`*(list|dict|set|tuple)`*\.*$", dtype_str)
        if m:
            return ModifierDataType(m.group(1))

        # Ex: bpy.types.Struct subclass
        m = re.match(r"^`bpy.types.Struct` subclass$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                "bpy.types.Struct", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return CustomDataType(s)

        m = re.match(r"^`bpy_struct`$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                "bpy_struct", uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        # Ex: CLIP_OT_add_marker
        m = re.match(r"^`([A-Z]+)_OT_([A-Za-z_]+)`, $", dtype_str)
        if m:
            idname = f"bpy.ops.{m.group(1).lower()}.{m.group(2)}"
            s = self._parse_custom_data_type(
                idname, uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        m = re.match(r"^`([a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+)`$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        m = re.match(r"^`([a-zA-Z0-9_.]+)`(, )*$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        m = re.match(r"^[a-zA-Z0-9_.]+$", dtype_str)
        if m:
            s = self._parse_custom_data_type(
                m.group(0), uniq_full_names, uniq_module_names, module_name)
            if s:
                return CustomDataType(s)

        return None

    def _get_refined_data_type_slow(
            self, data_type: 'DataType', module_name: str) -> 'DataType':
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
            r"`",
        ]
        for sp in strip_pattens:
            dtype_str = re.sub(sp, "", dtype_str)

        def only_nonsense_chars(string_to_parse: str) -> bool:
            NONSENSE_CHARS = [",", " ", "(", ")"]
            for c in string_to_parse:
                if c not in NONSENSE_CHARS:
                    return False
            return True

        def parse_builtin_dtype(string_to_parse: str) -> Tuple[List[str], str]:
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

        def parse_custom_dtype(string_to_parse: str) -> Tuple[List[str], str]:
            dtype = []
            stripped_string = string_to_parse
            for entry in self._entry_points:
                if len(stripped_string) == 0:
                    break
                if entry.type not in ["constant", "class"]:
                    continue
                if has_data_type(stripped_string, entry.fullname()):
                    dtype.append(entry.fullname())
                    stripped_string = stripped_string.replace(
                        entry.fullname(), "")
                    if only_nonsense_chars(stripped_string):
                        stripped_string = ""
                    continue
                full_data_type = f"{module_name}.{stripped_string}"
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

        def parse_dict_with_strkey_case(
                string_to_parse: str) -> Tuple[List[Dict[str, str]], str]:
            dict_case = []
            stripped_string = string_to_parse
            for class_ in DICT_WITH_STRKEY_FORMAT:
                regex = r"{} of ([a-zA-z0-9_]+)".format(class_)     # noqa # pylint: disable=C0209
                m = re.search(regex, stripped_string)
                if m:
                    case = {}
                    case["modifier"] = "dict"
                    case["builtin_dtype"], _ = parse_builtin_dtype(
                        m.groups()[0])
                    case["custom_dtype"] = []
                    case["dict_key"] = "str"
                    if not case["builtin_dtype"]:
                        case["custom_dtype"], _ = parse_custom_dtype(
                            m.groups()[0])
                        if not case["custom_dtype"]:
                            continue
                    dict_case.append(case)
            return dict_case, stripped_string

        # Check "XXX of YYY" format
        def parse_listof_case(
                string_to_parse: str) -> Tuple[List[Dict[str, str]], str]:
            listof_case = []
            stripped_string = string_to_parse
            for class_, need_to_add in LISTOF_FORMAT.items():
                regex = r"{} of ([a-zA-z0-9_]+)".format(class_)     # noqa # pylint: disable=C0209
                m = re.search(regex, stripped_string)
                if m:
                    case = {}
                    case["modifier"] = "list"
                    case["builtin_dtype"], _ = parse_builtin_dtype(
                        m.groups()[0])
                    case["custom_dtype"] = []
                    case["self_dtype"] = None
                    if not case["builtin_dtype"]:
                        case["custom_dtype"], _ = parse_custom_dtype(
                            m.groups()[0])
                        if not case["custom_dtype"]:
                            continue
                    if need_to_add:
                        case["self_dtype"] = class_
                    stripped_string = stripped_string.replace(m.group(), "")
                    listof_case.append(case)
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return listof_case, stripped_string

        def parse_modifier(string_to_parse: str) -> Tuple[List[str], str]:
            modifier = None
            stripped_string = string_to_parse
            for type_ in MODIFIER_DATA_TYPE:
                if has_data_type(stripped_string, type_):
                    modifier = type_
                    # remove modifier from stripped_string
                    # pylint: disable=W0511
                    # TODO: need to clip only modifier string
                    #       (issue ex. hogelist -> hoge)
                    stripped_string = stripped_string.replace(type_, "")
                    break
            if not modifier:
                for (key, value) in MODIFIER_DATA_TYPE_ALIASES.items():
                    if has_data_type(stripped_string, key):
                        modifier = value
                        # remove modifier from stripped_string
                        # pylint: disable=W0511
                        # TODO: need to clip only modifier string
                        #       (issue ex. hogelist -> hoge)
                        stripped_string = stripped_string.replace(key, "")
                        break
            if only_nonsense_chars(stripped_string):
                stripped_string = ""
            return modifier, stripped_string

        dict_case, dtype_str = parse_dict_with_strkey_case(dtype_str)

        listof_case, dtype_str = parse_listof_case(dtype_str)
        modifier, dtype_str = parse_modifier(dtype_str)

        # at first we check built-in data type
        builtin_dtypes, dtype_str = parse_builtin_dtype(dtype_str)
        builtin_dtypes = list(set(builtin_dtypes))

        # and then, search from package entry points
        custom_dtypes, dtype_str = parse_custom_dtype(dtype_str)
        if not builtin_dtypes and not custom_dtypes and not modifier and \
                not listof_case:
            output_log(LOG_LEVEL_WARN,
                       f"Could not find any data type "
                       f"({remove_unencodable(data_type.to_string())})")
        custom_dtypes = list(set(custom_dtypes))

        if dtype_str:
            output_log(
                LOG_LEVEL_DEBUG,
                f"dtype_str is still exists ({remove_unencodable(dtype_str)})")

        dtype_list = []
        for case in dict_case:
            if case["builtin_dtype"]:
                dtype_list.append(
                    BuiltinDataType(
                        case["builtin_dtype"][0],
                        ModifierDataType(case["modifier"]),
                        {"dict_key": case["dict_key"]}))
            elif case["custom_dtype"]:
                dtype_list.append(
                    CustomDataType(
                        case["custom_dtype"][0],
                        ModifierDataType(case["modifier"]),
                        {"dict_key": case["dict_key"]}))

        for case in listof_case:
            if case["builtin_dtype"]:
                dtype_list.append(BuiltinDataType(
                    case["builtin_dtype"][0],
                    ModifierDataType(case["modifier"])))
            elif case["custom_dtype"]:
                dtype_list.append(CustomDataType(
                    case["custom_dtype"][0],
                    ModifierDataType(case["modifier"])))
            if case["self_dtype"]:
                dtype_list.append(CustomDataType(case["self_dtype"]))

        if modifier is None:
            for d in builtin_dtypes:
                dtype_list.append(BuiltinDataType(d))
            for d in custom_dtypes:
                dtype_list.append(CustomDataType(d))
        else:
            for d in builtin_dtypes:
                if modifier not in ("list", "set"):
                    output_log(LOG_LEVEL_WARN,
                               f"Modifier '{modifier}' does not support "
                               f"element type inference ({d})")
                    dtype_list.append(ModifierDataType(modifier))
                else:
                    dtype_list.append(BuiltinDataType(
                        d, ModifierDataType(modifier)))
            for d in custom_dtypes:
                if modifier not in ("list", "set"):
                    output_log(LOG_LEVEL_WARN,
                               f"Modifier '{modifier}' does not support "
                               f"element type inference ({d})")
                    dtype_list.append(ModifierDataType(modifier))
                else:
                    dtype_list.append(CustomDataType(
                        d, ModifierDataType(modifier)))
            if not builtin_dtypes and not custom_dtypes:
                dtype_list.append(ModifierDataType(modifier))

        if len(dtype_list) == 1:
            return dtype_list[0]
        if len(dtype_list) >= 2:
            return MixinDataType(dtype_list)
        return ModifierDataType("typing.Any")

    def _tweak_metadata(self, data_type: 'DataType', variable_kind: str):
        metadata = data_type.get_metadata()

        # Set default value if a parameter is variable.
        if variable_kind == 'FUNC_ARG':
            if metadata.optional and (metadata.default_value is None):
                if data_type.type() in ('BUILTIN', 'CUSTOM') and \
                   data_type.has_modifier():
                    if data_type.modifier().type() == 'MODIFIER':
                        DEFAULT_VALUE_MAP = {
                            "list": "[]",
                            "dict": "{}",
                            "set": "()",
                            "tuple": "()",
                            "listlist": "[]",
                            "Generic": "None",
                            "typing.Iterator": "[]",
                            "typing.Callable": "None",
                            "typing.Any": "None",
                            "typing.Sequence": "[]",
                        }
                        metadata.default_value = DEFAULT_VALUE_MAP[
                            data_type.modifier().modifier_data_type()]
                    elif data_type.modifier().type() == 'CUSTOM_MODIFIER':
                        metadata.default_value = "[]"
                else:
                    if data_type.type() == 'BUILTIN':
                        DEFAULT_VALUE_MAP = {
                            "bool": "False",
                            "str": "\"\"",
                            "bytes": "0",
                            "float": "0.0",
                            "int": "0"
                        }
                        metadata.default_value = DEFAULT_VALUE_MAP[
                            data_type.data_type()]
                    elif data_type.type() == 'CUSTOM':
                        metadata.default_value = "None"
                    elif data_type.type() == 'MIXIN':
                        metadata.default_value = "None"

    def get_refined_data_type(
            self, data_type: 'DataType', module_name: str,
            variable_kind: str, parameter_str: str = None,
            additional_info: Dict[str, typing.Any] = None) -> 'DataType':

        assert variable_kind in (
            'FUNC_ARG', 'FUNC_RET', 'CONST', 'CLS_ATTR', 'CLS_BASE')

        result = self._get_refined_data_type_internal(
            data_type, module_name, variable_kind, parameter_str,
            additional_info)

        self._tweak_metadata(result, variable_kind)

        output_log(
            LOG_LEVEL_DEBUG,
            f"Result of refining (kind={variable_kind}): "
            f"{data_type.to_string()} -> {result.to_string()} "
            f"({result.type()})")

        return result

    def _get_refined_data_type_internal(
            self, data_type: 'DataType', module_name: str,
            variable_kind: str, parameter_str: str,
            additional_info: Dict[str, typing.Any] = None) -> 'DataType':

        dtype_str = data_type.to_string()
        metadata, dtype_str = self._build_metadata(
            dtype_str, module_name, parameter_str, variable_kind)

        if data_type.type() == 'UNKNOWN':
            return UnknownDataType()

        if (data_type.type() in ['CUSTOM']) and data_type.skip_refine():
            dt = copy.copy(data_type)
            dt.set_metadata(metadata)
            return data_type

        if data_type.type() != 'INTERMIDIATE':
            output_log(
                LOG_LEVEL_WARN,
                f"data_type should be 'INTERMIDIATE' but {data_type.type()}")

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        is_optional = data_type.is_optional()

        # Ex. (Quaternion, float) pair
        m = re.match(r"^\((.*)\) pair$", dtype_str)
        if m:
            sp = m.group(1).split(",")
            dtypes = []
            for s in sp:
                d = self._get_refined_data_type_fast(
                    s.strip(), uniq_full_names, uniq_module_names,
                    module_name, variable_kind, additional_info)
                if d:
                    dtypes.append(d.data_type())
            if len(dtypes) >= 1:
                elms = [CustomDataType(d) for d in dtypes]
                dd = CustomDataType(
                    dtypes[0], ModifierDataType("tuple"),
                    modifier_add_info={"tuple_elms": elms},
                    skip_refine=True)
                dd.set_metadata(metadata)
                return dd

        result = self._get_refined_data_type_fast(
            dtype_str, uniq_full_names, uniq_module_names, module_name,
            variable_kind, additional_info)
        if result is not None:
            result.set_is_optional(is_optional)
            result.set_metadata(metadata)
            return result

        if ("," in dtype_str) or (" or " in dtype_str):
            sp = dtype_str.split(",")
            splist = []
            for s in sp:
                splist.extend(s.split(" or "))

            output_log(LOG_LEVEL_DEBUG, f"Split data type refining: {splist}")

            dtypes = []
            for s in splist:
                s = s.strip()
                result = self._get_refined_data_type_fast(
                    s, uniq_full_names, uniq_module_names, module_name,
                    variable_kind, additional_info)
                if result is not None:
                    if result.type() in ['BUILTIN', 'CUSTOM', 'MODIFIER']:
                        dtypes.append(result)
                    elif result.type() == 'MIXIN':
                        dtypes.extend(result.data_types())
            if len(dtypes) == 1:
                dtypes[0].set_is_optional(is_optional)
                dtypes[0].set_metadata(metadata)
                return dtypes[0]
            if len(dtypes) >= 2:
                result = MixinDataType(dtypes)
                result.set_is_optional(is_optional)
                result.set_metadata(metadata)
                return result

        output_log(
            LOG_LEVEL_DEBUG,
            f"Slow data type refining: {data_type.to_string()}")

        result = self._get_refined_data_type_slow(data_type, module_name)
        result.set_is_optional(is_optional)
        result.set_metadata(metadata)
        return result

    def get_base_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        sp = data_type.split(".")
        return sp[-1]

    def get_module_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        module_names = data_type.split(".")[:-1]

        def search(
                mod_names, structure: 'ModuleStructure', dtype: str,
                is_first_level: bool = False):
            if len(mod_names) == 0:
                return dtype
            for s in structure.children():
                if s.name != mod_names[0]:
                    continue
                if is_first_level:
                    return search(mod_names[1:], s, s.name)
                return search(mod_names[1:], s, dtype + "." + s.name)
            return ""

        relative_type = search(module_names, self._package_structure, "", True)

        return relative_type if relative_type != "" else None

    def _ensure_correct_data_type(self, data_type: str) -> str:
        mod_name = self.get_module_name(data_type)
        base_name = self.get_base_name(data_type)

        ensured = f"{mod_name}.{base_name}"
        if ensured != data_type:
            raise RuntimeError(
                f"Invalid data type: ({data_type} vs {ensured})")

        return ensured

    def get_generation_data_type(self, data_type: str,
                                 target_module: str) -> str:
        mod_names_full_1 = self.get_module_name(data_type)
        mod_names_full_2 = target_module

        if mod_names_full_1 is None or mod_names_full_2 is None:
            # pylint: disable=W0511
            # TODO: should return better data_type
            return data_type

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
                raise RuntimeError(
                    f"Should not reach this condition. ({rest_level_1} vs "
                    f"{rest_level_2})")

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
        return f"{self._module}.{self._name}"
