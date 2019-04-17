# coding: UTF-8

import xml.etree.ElementTree as et
import glob
import re
import pathlib
import argparse
import json
import os
from yapf.yapflib.yapf_api import FormatCode


INDENT = "    "
INPUT_DIR = "."
OUTPUT_DIR = "./out"
SUPPORTED_TARGET = ["pycharm"]
TARGET = "pycharm"
DUMP = False
SUPPORTED_STYLE_FORMAT = ["none", "pep8"]
STYLE_FORMAT = "pep8"

OS_NAME = "Linux"

LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_NOTICE = 2
LOG_LEVEL_WARN = 3
LOG_LEVEL_ERR = 4

LOG_LEVEL_LABEL = ["DEBUG", "INFO", "NOTICE", "WARN", "ERR"]

LOG_LEVEL = LOG_LEVEL_WARN


def remove_unencodable(str_):
    """
    :type str_: str
    :param str_: string to remove unencodable character
    :return: string removed unencodable character
    """
    s = str_.replace('\xb2', '')
    s = s.replace('\u2013', '')
    s = s.replace('\u2019', '')
    return s


def output_log(level, message):
    if level >= LOG_LEVEL:
        print("[{0}] {1}".format(LOG_LEVEL_LABEL[level], message))


def textify(elm):
    s = []
    if elm.text:
        s.append(elm.text)
    for child in elm.getchildren():
        s.extend(textify(child))
    if elm.tail:
        s.append(elm.tail)

    return ''.join(s)


class Info:
    def __init__(self):
        self._type = None

    def type(self):
        if self._type is None:
            raise RuntimeError("'type' is empty")
        return self._type


class ParameterDetailInfo(Info):
    def __init__(self):
        super(ParameterDetailInfo, self).__init__()
        self._type = "parameter"
        self._name = None
        self._description = None
        self._data_type = None

    def set_name(self, name):
        self._name = name

    def set_description(self, desc):
        self._description = desc

    def set_data_type(self, dtype):
        self._data_type = dtype

    def to_dict(self):
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._description is None:
            self._description = ""

        if self._data_type is None:
            self._data_type = ""

        if OS_NAME == "Windows":
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
        self._type = "return"
        self._description = None
        self._data_type = None

    def set_description(self, desc):
        self._description = desc

    def set_data_type(self, dtype):
        self._data_type = dtype

    def to_dict(self):
        if self._description is None:
            self._description = ""

        if self._data_type is None:
            self._data_type = ""

        if OS_NAME == "Windows":
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


class ClassInfo(Info):
    def __init__(self):
        super(ClassInfo, self).__init__()
        self._type = "class"
        self._name = None
        self._description = None
        self._module = None
        self._methods = []
        self._attributes = []

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def module(self):
        return self._module

    def set_module(self, module_):
        self._module = module_

    def set_description(self, desc):
        self._description = desc

    def methods(self):
        return self._methods

    def add_method(self, method):
        self._methods.append(method)

    def add_methods(self, methods):
        for m in methods:
            self.add_method(m)

    def add_attribute(self, attr):
        self._attributes.append(attr)

    def add_attributes(self, attrs):
        for a in attrs:
            self.add_attribute(a)

    def to_dict(self):
        if self._name is None:
            raise RuntimeError("'name' is empty")

        if self._module is None:
            self._module = ""

        if self._description is None:
            self._description = ""

        if OS_NAME == "Windows":
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


class VariableInfo(Info):
    supported_type = ["constant", "attribute"]

    def __init__(self, type_):
        super(VariableInfo, self).__init__()
        self._type = type_
        self._name = None
        self._description = None
        self._class = None
        self._module = None
        self._data_type = None

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_description(self, desc):
        self._description = desc

    def set_class(self, class_):
        self._class = class_

    def module(self):
        return self._module

    def set_module(self, module_):
        self._module = module_

    def set_data_type(self, data_type):
        self._data_type = data_type

    def to_dict(self):
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

        if OS_NAME == "Windows":
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
    supported_type = ["function", "method"]

    def __init__(self, type_):
        super(FunctionInfo, self).__init__()
        self._type = type_
        self._name = None
        self._parameters = []
        self._parameter_details = []
        self._return = None
        self._class = None
        self._module = None
        self._description = None

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def equal_to_fullname(self, fullname):
        return self._name == fullname

    def parameters(self):
        return self._parameters

    def parameter(self, idx):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        return self._parameters[idx]

    def set_parameters(self, params):
        self._parameters = []
        self.add_parameters(params)

    def set_parameter(self, idx, param):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        self._parameters[idx] = param

    def add_parameter(self, param):
        self._parameters.append(param)

    def add_parameters(self, params):
        for p in params:
            self.add_parameter(p)

    def remove_parameter(self, idx):
        if idx >= len(self._parameters):
            raise RuntimeError("Out of range")
        del self._parameters[idx]

    def add_parameter_detail(self, param):
        self._parameter_details.append(param)

    def add_parameter_details(self, params):
        for p in params:
            self.add_parameter_detail(p)

    def set_class(self, class_):
        self._class = class_

    def module(self):
        return self._module

    def set_module(self, module_):
        self._module = module_

    def set_return(self, return_):
        self._return = return_

    def set_description(self, desc):
        self._description = desc

    def to_dict(self):
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

        if OS_NAME == "Windows":
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


class VariableAnalyzer:
    def __init__(self, filename, type_):
        self.filename = filename
        self.info = VariableInfo(type_)

    def _parse_field(self, elm, result):
        field_type = ""
        for child in list(elm):
            if child.tag == "field_name":
                field_type = child.text
            elif child.tag == "field_body":
                if field_type == "Type":
                    result["data_dtype"] = re.sub(r'\s+', ' ', textify(child))

    def _parse_field_list(self, elm, result):
        for child in list(elm):
            if child.tag == "field":
                self._parse_field(child, result)

    def _parse_desc_content(self, elm, result):
        for child in list(elm):
            if child.tag == "paragraph":
                result["desc"] = re.sub(r'\s+', ' ', textify(child))
            elif child.tag == "field_list":
                self._parse_field_list(child, result)

    def analyze(self, elm):
        signature_analyzed = False
        for child in list(elm):
            if child.tag == "desc_signature":
                if signature_analyzed:
                    msg = "desc_content must be parsed after parsing " \
                          "desc_signature"
                    output_log(LOG_LEVEL_ERR, msg)
                    raise RuntimeError(msg)

                # get name data
                name = child.get("fullname")
                if name is None:
                    name = child.find("desc_name").text   # for constant data
                class_ = child.get("class")
                if (class_ is not None) and (class_ != ""):
                    idx = name.rfind(class_)    # for class attribute
                    if idx != -1:
                        name = name[idx + len(class_) + 1:]
                self.info.set_name(name)

                # get module/class data
                self.info.set_class(class_)
                self.info.set_module(child.get("module"))

                signature_analyzed = True

            elif child.tag == "desc_content":
                if not signature_analyzed:
                    msg = "desc_signature must be parsed before parsing " \
                          "desc_content"
                    output_log(LOG_LEVEL_ERR, msg)
                    raise RuntimeError(msg)

                result = {}
                self._parse_desc_content(child, result)

                # get description/dtype data
                if "desc" in result:
                    self.info.set_description(result["desc"])
                if "data_dtype" in result:
                    self.info.set_data_type(result["data_dtype"])

        if not signature_analyzed:
            msg = "The data data is not parsed"
            output_log(LOG_LEVEL_ERR, msg)
            raise RuntimeError(msg)

        return self.info


class FunctionAnalyzer:
    def __init__(self, filename, type_):
        self.filename = filename
        self.info = FunctionInfo(type_)

    def _get_return_type_paragraph(self, elm):
        all_str = textify(elm)
        s = re.sub(r'\s+', ' ', all_str)
        return s

    def _get_return_type(self, elm):
        for child in list(elm):
            if child.tag == "paragraph":
                return self._get_return_type_paragraph(child)

        output_log(
            LOG_LEVEL_WARN,
            "<paragraph> is not found (filename={0})".format(self.filename)
        )
        return ""

    def _get_param_paragraph(self, elm):
        """
        parse

          <paragraph>
            <literal_strong>
              [name]
            </literal_strong>
            <literal_emphasis>
              [type]
            </literal_emphasis>
            [desc]
          </paragraph>

        or

          <paragraph>
            <strong>
              [name]
            </strong>
            <literal_emphasis>
              [type]
            </literal_emphasis>
            [desc]
          </paragraph>
        """

        name = None
        for l in list(elm):
            if (l.tag == "literal_strong") or (l.tag == "strong"):
                name = l.text
        str_ = textify(elm)
        if name is None:
            output_log(
                LOG_LEVEL_WARN,
                "<literal_strong> or <strong> is not found. "
                "(filename={0})".format(self.filename)
            )
            return None

        str_ = re.sub(r'\s+', ' ',  str_)
        str_ = re.sub(r'\(\s+', '(', str_)
        r = re.compile("([a-zA-Z0-9_]+) \((.+)\) – (.+)")
        result = r.findall(str_)
        if result:
            info = ParameterDetailInfo()
            info.set_name(result[0][0])
            info.set_description(result[0][2])
            info.set_data_type(result[0][1])
            return info

        r = re.compile("([a-zA-Z0-9_]+) – (.+)")
        result = r.findall(str_)
        if result:
            info = ParameterDetailInfo()
            info.set_name(result[0][0])
            info.set_description(result[0][1])
            return info

        r = re.compile("([a-zA-Z0-9_]+) \((.+)\) – ")
        result = r.findall(str_)
        if result:
            info = ParameterDetailInfo()
            info.set_name(result[0][0])
            info.set_data_type(result[0][1])
            return info

        output_log(
            LOG_LEVEL_WARN,
            "Does not match any paramter pattern. "
            "(filename={}, str={})".format(self.filename, str_)
        )

        return None

    def _analyze_list_item(self, elm):
        paragraph = None
        for child in list(elm):
            if child.tag == "paragraph":
                paragraph = child
                break

        if not paragraph:
            output_log(
                LOG_LEVEL_WARN,
                "<paragraph> is not found (filename={0})".format(self.filename)
            )
            return None

        return self._get_param_paragraph(paragraph)

    def _parse_bullet_list(self, elm):
        items = []
        for child in list(elm):
            if child.tag == "list_item":
                item = self._analyze_list_item(child)
                if item is not None:
                    items.append(item)
        return items

    def _analyze_param_list(self, elm, result):
        params = []
        for child in list(elm):
            if child.tag == "bullet_list":
                params = self._parse_bullet_list(child)
            elif child.tag == "paragraph":
                p = self._get_param_paragraph(child)
                if p:
                    params = [p]

        result["params_detail"] = params

    def _parse_field(self, elm, result):
        field_type = ""
        for child in list(elm):
            if child.tag == "field_name":
                field_type = child.text
            elif child.tag == "field_body":
                if field_type == "Parameters":
                    self._analyze_param_list(child, result)
                elif field_type == "Return type":
                    result["return_dtype"] = self._get_return_type(child)
                elif field_type == "Returns":
                    result["return_desc"] = re.sub(r'\s+', ' ', textify(child))

    def _parse_field_list(self, elm, result):
        for child in list(elm):
            if child.tag == "field":
                self._parse_field(child, result)

    def _parse_desc_content(self, elm, result):
        for child in list(elm):
            if child.tag == "paragraph":
                result["desc"] = re.sub(r'\s+', ' ', textify(child))
            elif child.tag == "field_list":
                self._parse_field_list(child, result)

    def _get_parameters(self, elm):
        result = []
        for child in list(elm):
            if child.tag == "desc_parameter":
                result.append(child.text)
        return result

    def analyze(self, elm):
        signature_analyzed = False
        for child in list(elm):
            if child.tag == "desc_signature":
                if signature_analyzed:
                    continue

                fullname = child.get("fullname")
                text = child.find("desc_name").text
                lp = text.find("(")
                rp = text.find(")")
                if lp == -1:
                    output_log(
                        LOG_LEVEL_NOTICE,
                        "'(' and ')' are not found (text={0})".format(text)
                    )

                    # get name data
                    name = text

                    # get parameters
                    params = []
                    c = child.find("desc_parameterlist")
                    if c is not None:
                        params = self._get_parameters(c)

                else:
                    # get name data
                    name = text[0:lp]

                    # get parameters
                    params = [re.sub(" ", "", p)
                              for p in text[lp + 1:rp].split(",")]

                self.info.set_name(name)
                self.info.add_parameters(params)

                # validate name data
                if not self.info.equal_to_fullname(fullname):
                    if fullname is not None:
                        output_log(
                            LOG_LEVEL_NOTICE,
                            "fullname does not match text "
                            "(fullname={0}, text={1})".format(fullname, name)
                        )

                # get module/class data
                self.info.set_module(child.get("module"))
                self.info.set_class(child.get("class"))

                signature_analyzed = True

            elif child.tag == "desc_content":
                if not signature_analyzed:
                    msg = "desc_signature must be parsed before parsing " \
                          "desc_content"
                    output_log(LOG_LEVEL_ERR, msg)
                    raise RuntimeError(msg)

                result = {}
                self._parse_desc_content(child, result)

                # get description data
                if "desc" in result.keys():
                    self.info.set_description(result["desc"])

                # get return data
                return_builder = ReturnInfo()
                if "return_dtype" in result.keys():
                    return_builder.set_data_type(result["return_dtype"])
                if "return_desc" in result.keys():
                    return_builder.set_description(result["return_desc"])
                self.info.set_return(return_builder)

                # get params_detail data
                if "params_detail" in result.keys():
                    self.info.add_parameter_details(result["params_detail"])
                break

        if not signature_analyzed:
            msg = "The function data is not parsed"
            output_log(LOG_LEVEL_ERR, msg)
            raise RuntimeError(msg)

        return self.info


class ClassAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.info = ClassInfo()

    def _parse_desc(self, desc, result):
        attr = desc.get("desctype")
        if attr == "function" or attr == "method":
            if "method" not in result:
                result["method"] = []
            analyzer = FunctionAnalyzer(self.filename, "method")
            m = analyzer.analyze(desc)
            result["method"].append(m)
        elif attr == "attribute" or attr == "data":
            if "attribute" not in result:
                result["attribute"] = []
            analyzer = VariableAnalyzer(self.filename, "attribute")
            a = analyzer.analyze(desc)
            result["attribute"].append(a)

    def _parse_desc_content(self, elm, result):
        for child in list(elm):
            if child.tag == "paragraph":
                result["desc"] = re.sub(r'\s+', ' ', textify(child))
            elif child.tag == "desc":
                self._parse_desc(child, result)

    def analyze(self, elm):
        signature_analyzed = False
        for child in list(elm):
            if child.tag == "desc_signature":
                if signature_analyzed:
                    continue        # ignore

                # get name data
                self.info.set_name(child.get("fullname"))

                # get module data
                self.info.set_module(child.get("module"))

                signature_analyzed = True

            elif child.tag == "desc_content":
                if not signature_analyzed:
                    msg = "desc_signature must be parsed before parsing " \
                          "desc_content"
                    output_log(LOG_LEVEL_ERR, msg)
                    raise RuntimeError(msg)

                # get description data
                result = {}
                self._parse_desc_content(child, result)
                if "desc" in result.keys():
                    self.info.set_description(result["desc"])
                if "method" in result.keys():
                    self.info.add_methods(result["method"])
                if "attribute" in result.keys():
                    self.info.add_attributes(result["attribute"])

        if not signature_analyzed:
            msg = "The class data is not parsed"
            output_log(LOG_LEVEL_ERR, msg)
            raise RuntimeError(msg)

        return self.info


class BaseAnalyzer:
    def __init__(self):
        self.filename = None

    def _analyze_desc(self, filename, desc):
        result = None
        attr = desc.get("desctype")
        if attr == "function" or attr == "method":
            analyzer = FunctionAnalyzer(filename, "function")
            result = analyzer.analyze(desc)
        elif attr == "data":
            analyzer = VariableAnalyzer(filename, "constant")
            result = analyzer.analyze(desc)
        elif attr == "class":
            analyzer = ClassAnalyzer(filename)
            result = analyzer.analyze(desc)

        return result

    def _analyze_section(self, filename, elm, result):
        for child in list(elm):
            if child.tag == "desc":     # <desc>
                r = self._analyze_desc(filename, child)
                if r:
                    result.append(r)
            elif child.tag == "section":    # <section>
                self._analyze_section(filename, child, result)

    def _modify(self, result):
        pass

    def update_parameter_if_not_equal(self, info, param_idx, expect):
        if info.parameter(param_idx) == expect:
            return
        info.set_parameter(param_idx, expect)

    def analyze(self, filename):
        self.filename = filename
        tree = et.parse(filename)
        root = tree.getroot()       # <document>
        result = []
        for child in list(root):
            if child.tag == "section":    # <section>
                r = []
                self._analyze_section(filename, child, r)
                result.append(r)

        self._modify(result)

        return result


class MathutilsAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            info = VariableInfo("constant")
            info.set_name("STDPERLIN")
            info.set_module("mathutils.noise")
            sections.insert(0, info)
            for s in sections:
                if s.type() == "function":
                    for i, p in enumerate(s.parameters()):
                        s.set_parameter(i, re.sub("=noise.types.", "=", p))
                    if s.name() == "barycentric_transform":
                        s.set_parameter(4, "tri_b1")
                        s.set_parameter(5, "tri_b2")
                        s.set_parameter(6, "tri_b3")
                    elif s.name() == "intersect_point_line":
                        s.set_parameter(2, "line_p2")
                elif s.type() == "class":
                    # add __init__ method if __init__ is missing.
                    # all classes defined in mathutils module don't have
                    # __init__ method
                    found = False
                    for m in s.methods():
                        if m.name() == "__init__":
                            found = True
                            break
                    if not found:
                        if s.name() == "KDTree":
                            info = FunctionInfo("method")
                            info.set_name("__init__")
                            info.add_parameter("size")
                            info.set_module(s.module())
                            info.set_return(ReturnInfo())
                            s.add_method(info)
                        elif s.name() != "BVHTree":
                            info = FunctionInfo("method")
                            info.set_name("__init__")
                            info.add_parameter("val")
                            info.set_module(s.module())
                            info.set_return(ReturnInfo())
                            s.add_method(info)


class BpyAnalyzer(BaseAnalyzer):
    def __handle_ui_layout(self, info):
        for m in info.methods():
            if m.name() == "template_list":
                self.update_parameter_if_not_equal(m, 2, "dataptr=\"\"")
                self.update_parameter_if_not_equal(m, 3, "propname=\"\"")
                self.update_parameter_if_not_equal(m, 4, "active_dataptr=\"\"")
                self.update_parameter_if_not_equal(m, 5, "active_propname=0")

    def _match(self, filename, mod_name):
        p = re.compile(r".*{}\.xml$".format(mod_name.replace(r'.', r'\.')))
        return True if p.match(filename) else False

    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "class":
                    if s.name() == "BlendData":
                        for m in s.methods():
                            for i, p in enumerate(m.parameters()):
                                if p.find("key_types=") != -1:
                                    m.set_parameter(i, "key_types")
                                elif p.find("value_types=") != -1:
                                    m.set_parameter(i, "value_types")
                    if self._match(self.filename, "bpy.types.UILayout"):
                        if s.name() == "UILayout":
                            self.__handle_ui_layout(s)
                elif s.type() == "function":
                    if s.name() == "RemoveProperty":
                        for i, p in enumerate(s.parameters()):
                            if p.find("attr=") != -1:
                                s.set_parameter(i, "attr")


class BglAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "function":
                    if s.module() is None:
                        s.set_module("bgl")


class BpyExtraAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "function":
                    if s.name() == "path_reference_copy":
                        s.set_parameter(1, "report='print'")


class BmeshAnalyzer(BaseAnalyzer):
    def __rename_duplicate(self, info):
        for i, l in enumerate(info.parameters()):
            count = 0
            for j, s in enumerate(info.parameters()):
                if l == s:
                    count = count + 1
                    if count >= 2:
                        info.set_parameter(i, s + "_" + str(count))

    def __handle_extrude_face_region(self, info):
        self.update_parameter_if_not_equal(info, 0, "bmesh")
        self.update_parameter_if_not_equal(info, 1, "geom=[]")
        self.update_parameter_if_not_equal(info, 2, "edges_exclude=[]")
        self.update_parameter_if_not_equal(info, 3, "use_keep_orig=False")
        self.update_parameter_if_not_equal(info, 4, "use_select_history=False")

    def __handle_translate(self, info):
        self.update_parameter_if_not_equal(info, 0, "bmesh")
        self.update_parameter_if_not_equal(info, 1, "vec=Vector()")
        self.update_parameter_if_not_equal(info, 2, "space=Matrix()")
        self.update_parameter_if_not_equal(info, 3, "verts=[]")

    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "function":
                    if s.name() == "wireframe":
                        self.__rename_duplicate(s)
                    elif s.name() == 'extrude_face_region':
                        self.__handle_extrude_face_region(s)
                    elif s.name() == 'translate':
                        self.__handle_translate(s)


class GpuAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "constant":
                    if s.name() == "GPU_DYNAMIC_MIST_ENABLE:":
                        s.set_name(s.name()[:-1])
                        s.set_module("gpu")


class FreestyleAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s.type() == "class":
                    if s.name() == "SmoothingShader":
                        for m in s.methods():
                            if m.name()[0:9] == "__init__":
                                m.set_name("__init__")
                                m.set_parameters([
                                    "num_iterations=100",
                                    "factor_point=0.1",
                                    "factor_curvature=0.0",
                                    "factor_curvature_difference=0.2",
                                    "aniso_point=0.0",
                                    "aniso_normal=0.0",
                                    "aniso_curvature=0.0",
                                    "carricature_factor=1.0"
                                ])
                elif s.type() == "function":
                    if (s.name() == "angle_x_normal") or \
                       (s.name() == "normal_at_I0D"):
                        for i, p in enumerate(s.parameters()):
                            if p == "it: Interface0DIterator":
                                s.set_parameter(i, p[0:2])
                    elif s.name() == "pairwise":
                        s.remove_parameter(len(s.parameters()) - 1)
                        for i, p in enumerate(s.parameters()):
                            if p[0:6] == "types=":
                                s.set_parameter(i, "types={}")


class BaseGenerator:
    def __init__(self):
        self.mod_name = None

    def _gen_function_code(self, info):
        data = info.to_dict()
        str_ = ""

        str_ += "def " + data["name"] + "("
        if len(data["parameters"]):
            str_ += ", ".join(data["parameters"])
        str_ += "):\n"

        # documentation
        str_ += INDENT + "'''{}\n\n".format(data["description"])
        for p in data["parameter_details"]:
            str_ += INDENT + ":param {}: {}\n"\
                .format(p["name"], p["description"])
            str_ += INDENT + ":type {}: {}\n"\
                .format(p["name"], p["data_type"])
        if data["return"]["description"] != "":
            str_ += INDENT + ":return: {}\n"\
                .format(data["return"]["description"])
        str_ += INDENT + "'''\n\n"

        str_ += INDENT + "pass" + "\n"
        str_ += "\n\n"

        return str_

    def _gen_class_code(self, info):
        data = info.to_dict()
        if data["name"] is None:
            output_log(
                LOG_LEVEL_WARN, "Invalid data name. (data={})".format(data)
            )
            return
        str_ = ""

        str_ += "class " + data["name"] + ":\n"

        if data["description"] != "":
            str_ += INDENT + "'''{}'''\n\n".format(data["description"])

        for a in data["attributes"]:
            str_ += INDENT + a["name"] + " = None\n"
            str_ += INDENT + "'''"
            if a["description"] != "":
                str_ += "{}".format(a["description"])
            if a["data_type"] != "":
                str_ += "\n\n" + INDENT + ":type: {}\n"\
                    .format(a["data_type"]) + INDENT
            str_ += "'''\n\n"
        if len(data["attributes"]) > 0:
            str_ += "\n"

        for m in data["methods"]:
            str_ += INDENT + "def " + m["name"] + "(self"
            if len(m["parameters"]):
                str_ += ", " + ", ".join(m["parameters"])
            str_ += "):\n"

            # documentation
            str_ += INDENT * 2 + "'''{}\n\n".format(m["description"])
            for p in m["parameter_details"]:
                str_ += INDENT * 2 + ":param {}: {}\n"\
                    .format(p["name"], p["description"])
                str_ += INDENT * 2 + ":type {}: {}\n"\
                    .format(p["name"], p["data_type"])
            if m["return"]["data_type"] != "":
                str_ += INDENT * 2 + ":rtype: {}\n"\
                    .format(m["return"]["data_type"])
            if m["return"]["description"] != "":
                str_ += INDENT * 2 + ":return: {}\n"\
                    .format(m["return"]["description"])
            str_ += INDENT * 2 + "'''\n"

            str_ += INDENT * 2 + "pass\n"
            str_ += "\n"

        if len(data["attributes"]) == 0 and len(data["methods"]) == 0:
            str_ += INDENT + "pass\n\n\n"

        return str_

    def _gen_constant_code(self, info):
        data = info.to_dict()
        str_ = ""

        str_ += data["name"] + " = None"
        if data["data_type"] != "":
            str_ += "  # type: {}".format(data["data_type"])
        str_ += "\n"
        if data["description"] != "":
            str_ += "'''{}'''"\
                .format(remove_unencodable(data["description"]))
        str_ += "\n\n"

        return str_

    def print_header(self, file):
        pass

    def generate(self, filename, data, style_config='pep8'):
        self.mod_name = data["name"]

        # at first, sort data to avoid generating large diff
        sorted_data = sorted(
            data["data"],
            key=lambda x : (x.type(), x.name())
        )

        with open(filename, "w", encoding="utf-8") as file:
            self.print_header(file)

            code_data = ""

            for mod in data["child_modules"]:
                code_data += "from . import {}\n".format(mod)
            if len(data["child_modules"]) >= 1:
                code_data += "\n\n"

            for info in sorted_data:
                # if "type" not in s:
                #     continue
                if info.type() == "function":
                    code_data += self._gen_function_code(info)
                elif info.type() == "class":
                    code_data += self._gen_class_code(info)
                elif info.type() == "constant":
                    code_data += self._gen_constant_code(info)

            if style_config != "none":
                file.write(FormatCode(code_data, style_config=style_config)[0])
            else:
                file.write(code_data)

    def dump_json(self, filename, data):
        json_data = [info.to_dict() for info in data["data"]]
        with open(filename, "w") as f:
            json.dump(json_data, f, indent=4)


class BpyGenerator(BaseGenerator):
    def print_header(self, file):
        if self.mod_name == "bpy":
            file.write("from .context import Context as context\n")
            file.write("\n")


class BmeshGenerator(BaseGenerator):
    def print_header(self, file):
        if self.mod_name == "bmesh.ops":
            file.write("from ..mathutils import Vector, Matrix\n")
            file.write("\n")


# build module structure
def build_module_structure(modules):
    def build(mod_name, structure):
        sp = mod_name.split(".")
        for i in structure:
            if i["name"] == sp[0]:
                item = i
                break
        else:
            item = {"name": sp[0], "children": []}
            structure.append(item)
        if len(sp) >= 2:
            s = ".".join(sp[1:])
            build(s, item["children"])

    structure = []
    for m in modules:
        build(m, structure)

    return structure


def make_module_dirs(base_path, structure):
    def make_dir(path, structure):
        for item in structure:
            if len(item["children"]) >= 1:
                dir_path = path + "/" + item["name"]
                pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)
                if dir_path == base_path:
                    continue
                make_dir(dir_path, item["children"])

    make_dir(base_path, structure)


def find_mod(modules, xml_file):
    modname_raw = re.sub("\.", "/", xml_file.module())

    def find(name, mods, raw):
        for m in mods:
            mod_name = name + m["name"]
            if mod_name == raw:
                if len(m["children"]) == 0:
                    return mod_name + ".py"
                else:
                    return mod_name + "/__init__.py"
            if len(m["children"]) > 0:
                ret = find(mod_name + "/", m["children"], raw)
                if ret:
                    return ret

    return find("", modules, modname_raw)


def build_generation_info(analyze_results, module_structure):
    def find_target_file(name, structure, target):
        for m in structure:
            mod_name = name + m["name"]
            if mod_name == target:
                if len(m["children"]) == 0:
                    return mod_name + ".py"
                else:
                    return mod_name + "/__init__.py"

            if len(m["children"]) > 0:
                ret = find_target_file(mod_name + "/", m["children"], target)
                if ret:
                    return ret
        return None

    def build_child_modules(info, name, structure):
        for m in structure:
            mod_name = name + m["name"]
            if len(m["children"]) == 0:
                filename = re.sub("\.", "/", mod_name) + ".py"
                info[filename] = {
                    "data": [],
                    "child_modules": [],
                    "name": mod_name
                }
            else:
                filename = re.sub("\.", "/", mod_name) + "/__init__.py"
                info[filename] = {
                    "data": [],
                    "child_modules": [child["name"] for child in m["children"]],
                    "name": mod_name
                }
                build_child_modules(info, mod_name + ".", m["children"])

    # build child modules
    generator_info = {}
    build_child_modules(generator_info, "", module_structure)

    # build data
    for r in analyze_results:
        for sections in r:
            for s in sections:
                target = find_target_file("", module_structure,
                                          re.sub("\.", "/", s.module()))
                if target is None:
                    raise RuntimeError("Could not find target file to generate "
                                       "(target: {})".format(s.module()))
                if target not in generator_info:
                    raise RuntimeError("Could not find target in generator_info "
                                       "(target: {})".format(s.module()))
                generator_info[target]["data"].append(s)


    return generator_info


def gen_package(path, xml_files, analyzer, generator):
    global DUMP
    global STYLE_FORMAT

    # replace windows path separator
    new_xml_files = [f.replace("\\", "/") for f in xml_files]

    # analyze all .xml files
    analyze_results = []
    for f in new_xml_files:
        analyze_results.append(analyzer.analyze(f))

    # collect module list
    module_list = []
    for r in analyze_results:
        for sections in r:
            for s in sections:
                if s.module() not in module_list:
                    module_list.append(s.module())

    # build module structure
    module_structure = build_module_structure(module_list)

    # create module directories/files
    make_module_dirs(path, module_structure)

    # map between result of analyze and module structure
    generation_info = build_generation_info(analyze_results, module_structure)

    for key in generation_info.keys():
        # dump if necessary
        if DUMP:
            generator.dump_json(path + "/" + key + "-dump.json",
                                generation_info[key])
        # generate python code
        generator.generate(path + "/" + key, generation_info[key], STYLE_FORMAT)


def gen_bpy_context_skelton():
    filename = "{}/bpy/context.py".format(OUTPUT_DIR)
    with open(filename, "w", encoding="utf-8") as file:
        file.write("class Context:\n")
        file.write(INDENT + "# pylint: dynamic-attributes = .*\n")
        file.write(INDENT + "def __init__(self, **kwargs):\n")
        file.write(INDENT * 2 + "pass\n")


def gen_bpy_package():
    all_files = glob.glob(INPUT_DIR + "/bpy*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    gen_package(OUTPUT_DIR, files, BpyAnalyzer(), BpyGenerator())
    # generate bpy.context skelton file.
    # this is a skelton file to suppress the pylint error.
    gen_bpy_context_skelton()


def gen_bgl_module():
    files = glob.glob(INPUT_DIR + "/bgl*.xml")
    gen_package(OUTPUT_DIR, files, BglAnalyzer(), BaseGenerator())


def gen_blf_module():
    files = glob.glob(INPUT_DIR + "/blf*.xml")
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_mathutils_package():
    files = glob.glob(INPUT_DIR + "/mathutils*.xml")
    gen_package(OUTPUT_DIR, files, MathutilsAnalyzer(), BaseGenerator())


def gen_gpu_module():
    files = glob.glob(INPUT_DIR + "/gpu*.xml")
    gen_package(OUTPUT_DIR, files, GpuAnalyzer(), BaseGenerator())


def gen_freestyle_package():
    files = glob.glob(INPUT_DIR + "/freestyle*.xml")
    gen_package(OUTPUT_DIR, files, FreestyleAnalyzer(), BaseGenerator())


def gen_bpy_extra_package():
    files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    gen_package(OUTPUT_DIR, files, BpyExtraAnalyzer(), BaseGenerator())


def gen_aud_module():
    files = glob.glob(INPUT_DIR + "/aud*.xml")
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_bmesh_package():
    files = glob.glob(INPUT_DIR + "/bmesh*.xml")
    gen_package(OUTPUT_DIR, files, BmeshAnalyzer(), BmeshGenerator())


def parse_options():
    global INPUT_DIR, OUTPUT_DIR, SUPPORTED_TARGET, TARGET, DUMP, STYLE_FORMAT
    usage = "Usage: python {} [-i <input_dir>] [-o <output_dir>] [-t <target>]"\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_dir", type=str, help="Input Directory"
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output Directory"
    )
    parser.add_argument(
        "-t", dest="target", type=str, help="Target (pycharm)"
    )
    parser.add_argument(
        "-d", dest="dump", action="store_true",
        help="Dump intermediate structure to JSON files"
    )
    parser.add_argument(
        "-f", dest="style_format", type=str, help="Style format (None, pep8)"
    )
    args = parser.parse_args()
    if args.input_dir:
        INPUT_DIR = args.input_dir
    if args.output_dir:
        OUTPUT_DIR = args.output_dir

    if args.target in SUPPORTED_TARGET:
        TARGET = args.target
    else:
        raise RuntimeError("Not supported target {}. (Supported Target: {})"
                           .format(args.target, SUPPORTED_TARGET))

    if args.style_format in SUPPORTED_STYLE_FORMAT:
        STYLE_FORMAT = args.style_format
    else:
        raise RuntimeError("Not supported style format {}. "
                           "(Supported Style Format: {})"
                           .format(args.style_format, SUPPORTED_STYLE_FORMAT))

    if args.dump:
        DUMP = True


def check_os():
    global OS_NAME
    if os.name == "nt":
        OS_NAME = "Windows"
    elif os.name == "posix":
        OS_NAME = "Linux"


def main():
    check_os()
    parse_options()
    gen_bpy_package()
    gen_bgl_module()
    gen_blf_module()
    gen_mathutils_package()
    gen_gpu_module()
    gen_freestyle_package()
    gen_bpy_extra_package()
    gen_aud_module()
    gen_bmesh_package()


if __name__ == "__main__":
    main()
