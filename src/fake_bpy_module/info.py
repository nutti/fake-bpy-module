from .utils import (
    check_os,
    remove_unencodable,
)
from typing import List

class Info:
    def __init__(self):
        self._type: str = None

    def name(self):
        raise NotImplementedError()

    def module(self):
        raise NotImplementedError()

    def type(self) -> str:
        if self._type is None:
            raise RuntimeError("'type' is empty")
        return self._type

    def to_dict(self):
        raise NotImplementedError()


class ParameterDetailInfo(Info):
    def __init__(self):
        super(ParameterDetailInfo, self).__init__()
        self._type: str = "parameter"
        self._name: str = None
        self._description: str = None
        self._data_type: str = None

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def set_description(self, desc: str):
        self._description = desc

    def set_data_type(self, dtype: str):
        self._data_type = dtype

    def data_type(self) -> str:
        return self._data_type

    def to_dict(self) -> dict:
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._description is None:
            self._description = ""

        if self._data_type is None:
            self._data_type = ""

        if check_os() == "Windows":
            data = {
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type),
            }
        else:
            data = {
                "name": self._name,
                "description": self._description,
                "data_type": self._data_type,
            }

        return data


class ReturnInfo(Info):
    def __init__(self):
        super(ReturnInfo, self).__init__()
        self._type: str = "return"
        self._description: str = None
        self._data_type: str = None

    def data_type(self) -> str:
        return self._data_type

    def set_description(self, desc: str):
        self._description = desc

    def set_data_type(self, dtype: str):
        self._data_type = dtype

    def to_dict(self) -> dict:
        if self._description is None:
            self._description = ""

        if self._data_type is None:
            self._data_type = ""

        if check_os() == "Windows":
            data = {
                "description": remove_unencodable(self._description),
                "data_type": remove_unencodable(self._data_type),
            }
        else:
            data = {
                "description": self._description,
                "data_type": self._data_type,
            }

        return data


class VariableInfo(Info):
    supported_type: List[str] = ["constant", "attribute"]

    def __init__(self, type_: str):
        super(VariableInfo, self).__init__()
        self._type: str = type_
        self._name: str = None
        self._description: str = None
        self._class: str = None
        self._module: str = None
        self._data_type: str = None

    def name(self) -> str:
        return self._name

    def data_type(self) -> str:
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

    def set_data_type(self, data_type: str):
        self._data_type = data_type

    def to_dict(self) -> dict:
        if self._type not in self.supported_type:
            raise RuntimeError("'type' must be ({})"
                               .format(self.supported_type))

        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._description is None:
            self._description = ""

        if self._class is None:
            self._class = ""

        if self._module is None:
            self._module = ""

        if self._data_type is None:
            self._data_type = ""

        if check_os() == "Windows":
            data = {
                "type": self._type,
                "name": remove_unencodable(self._name),
                "description": remove_unencodable(self._description),
                "class": remove_unencodable(self._class),
                "module": remove_unencodable(self._module),
                "data_type": remove_unencodable(self._data_type),
            }
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "class": self._class,
                "module": self._module,
                "data_type": self._data_type,
            }

        return data


class FunctionInfo(Info):
    supported_type: List[str] = ["function", "method"]

    def __init__(self, type_: str):
        super(FunctionInfo, self).__init__()
        self._type: str = type_
        self._name: str = None
        self._parameters: List[str] = []
        self._parameter_details: List[ParameterDetailInfo] = []
        self._return: ReturnInfo = None
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

    def parameter_details(self) -> List[ParameterDetailInfo]:
        return self._parameter_details

    def return_(self) -> ReturnInfo:
        return self._return

    def set_parameters(self, params: List[str]):
        self._parameters = []
        self.add_parameters(params)

    def set_parameter(self, idx: int, param: str):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        self._parameters[idx] = param

    def add_parameter(self, param: str):
        self._parameters.append(param)

    def add_parameters(self, params: List[str]):
        for p in params:
            self.add_parameter(p)

    def remove_parameter(self, idx: int):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        del self._parameters[idx]

    def add_parameter_detail(self, param: ParameterDetailInfo):
        if param.type() != "parameter":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("parameter", param.type()))
        self._parameter_details.append(param)

    def add_parameter_details(self, params: List[ParameterDetailInfo]):
        for p in params:
            if p.type() != "parameter":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("parameter", p.type()))
            self.add_parameter_detail(p)

    def set_class(self, class_: str):
        self._class = class_

    def module(self) -> str:
        return self._module

    def set_module(self, module_: str):
        self._module = module_

    def set_return(self, return_: ReturnInfo):
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


class ClassInfo(Info):
    def __init__(self):
        super(ClassInfo, self).__init__()
        self._type: str = "class"
        self._name: str = None
        self._description: str = None
        self._module: str = None
        self._methods: List[FunctionInfo] = []
        self._attributes: List[VariableInfo] = []

    def name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def module(self) -> str:
        return self._module

    def attributes(self) -> List[VariableInfo]:
        return self._attributes

    def set_module(self, module_: str):
        self._module = module_

    def set_description(self, desc: str):
        self._description = desc

    def methods(self) -> List[FunctionInfo]:
        return self._methods

    def add_method(self, method: FunctionInfo):
        if method.type() != "method":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("method", method.type()))
        self._methods.append(method)

    def add_methods(self, methods: List[FunctionInfo]):
        for m in methods:
            if m.type() != "method":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("method", m.type()))
            self.add_method(m)

    def add_attribute(self, attr: VariableInfo):
        if attr.type() != "attribute":
            raise RuntimeError("Expected Info.type() is {} but {}."
                               .format("attribute", attr.type()))
        self._attributes.append(attr)

    def add_attributes(self, attrs: List[VariableInfo]):
        for a in attrs:
            if a.type() != "attribute":
                raise RuntimeError("Expected Info.type() is {} but {}."
                                   .format("attribute", a.type()))
            self.add_attribute(a)

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
            }
        else:
            data = {
                "type": self._type,
                "name": self._name,
                "description": self._description,
                "module": self._module,
                "methods": [m.to_dict() for m in self._methods],
                "attributes": [a.to_dict() for a in self._attributes],
            }

        return data