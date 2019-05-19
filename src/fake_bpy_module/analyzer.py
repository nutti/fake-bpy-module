import xml.etree.ElementTree as et
import re
from typing import List, Dict

from .info import (
    ParameterDetailInfo,
    ReturnInfo,
    VariableInfo,
    FunctionInfo,
    ClassInfo,
)
from .utils import (
    output_log,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERR
)

def textify(elm) -> str:
    s = []
    if elm.text:
        s.append(elm.text)
    for child in elm.getchildren():
        s.extend(textify(child))
    if elm.tail:
        s.append(elm.tail)

    return ''.join(s)


class DataTypeRefiner:
    BUILTIN_DATA_TYPE: List[str] = [
        "bool", "str", "list", "bytes", "float", "dict", "int", "set"
    ]
    TYPE_ALIAS: Dict[str, str] = {
        "string": "str",
        "Enumerated constant": "int",
        "enum": "int",
        "List": "list",
    }

    def __init__(self, package_structure, entry_points):
        self._package_structure = package_structure
        self._entry_points = entry_points

    def is_builtin_data_type(self, data_type):
        return data_type in self.BUILTIN_DATA_TYPE

    def make_annotate_data_type(self, data_type):
        if data_type in self.BUILTIN_DATA_TYPE:
            return data_type
        return "'{}'".format(data_type)

    def get_refined_data_type(self, data_type_string: str, module_name: str):
        if data_type_string is None:
            return None

        for type_ in self.BUILTIN_DATA_TYPE:
            if data_type_string.find(type_) != -1:
                return type_

        for type_ in self.TYPE_ALIAS.keys():
            if data_type_string.find(type_) != -1:
                return self.TYPE_ALIAS[type_]

        # search from package entry points
        result = None
        for entry in self._entry_points:
            if entry["type"] not in ["constant", "class"]:
                continue
            if data_type_string.find(entry["full_name"]) != -1:
                result = entry["full_name"]
                break
            full_data_type = "{}.{}".format(module_name, data_type_string)
            if full_data_type.find(entry["full_name"]) != -1:
                result = entry["full_name"]
                break
            full_data_type = full_data_type.replace(" ", "")
            if full_data_type.find(entry["full_name"]) != -1:
                result = entry["full_name"]
                break

        return result

    def get_base_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        sp = data_type.split(".")
        return sp[-1]

    def get_module_name(self, data_type: str) -> str:
        if data_type is None:
            return None

        module_names = data_type.split(".")

        def search(mod_names, mod_list, dtype, is_first_level=False):
            if len(mod_names) == 0:
                return dtype
            for s in mod_list:
                if s["name"] != mod_names[0]:
                    continue
                if is_first_level:
                    return search(mod_names[1:], s["children"],
                                  s["name"])
                else:
                    return search(mod_names[1:], s["children"],
                                  dtype + "." + s["name"])
            return dtype

        relative_type = search(module_names, self._package_structure,
                               "", True)

        return relative_type if relative_type != "" else None

    def _ensure_correct_data_type(self, data_type: str):
        mod_name = self.get_module_name(data_type)
        base_name = self.get_base_name(data_type)

        ensured = "{}.{}".format(mod_name, base_name)
        if ensured != data_type:
            raise RuntimeError("Invalid data type: ({} vs {})"
                               .format(data_type, ensured))

        return ensured

    def get_generation_data_type(self, data_type_1: str, data_type_2: str):
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


class VariableAnalyzer:
    def __init__(self, filename: str, type_: str):
        self.filename: str = filename
        self.info: VariableInfo = VariableInfo(type_)

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
        self.filename: str = filename
        self.info: FunctionInfo = FunctionInfo(type_)

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
                sp = child.text.split(",")
                for s in sp:
                    result.append(re.sub(" ", "", s))
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
        self.filename: str = filename
        self.info: ClassInfo = ClassInfo()

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
        self.filename: str = None
        self.data_type_refiner: DataTypeRefiner = None

    def _analyze_desc(self, filename: str, desc):
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

    def _analyze_section(self, filename: str, elm, result):
        for child in list(elm):
            if child.tag == "desc":     # <desc>
                r = self._analyze_desc(filename, child)
                if r:
                    result.append(r)
            elif child.tag == "section":    # <section>
                self._analyze_section(filename, child, result)

    def _modify(self, result):
        pass

    def _refine_data_type(self, result):
        for sections in result:
            for s in sections:
                # refine function parameters and return value
                if s.type() == "function":
                    for p in s.parameter_details():
                        refined_type = self.data_type_refiner.get_refined_data_type(
                            p.data_type(), s.module())
                        if refined_type is not None:
                            p.set_data_type(refined_type)
                        else:
                            p.set_data_type("")

                    return_ = s.return_()
                    refined_type = self.data_type_refiner.get_refined_data_type(
                        return_.data_type(), s.module())
                    if refined_type is not None:
                        return_.set_data_type(refined_type)
                    else:
                        return_.set_data_type("")
                # refine constant
                elif s.type() == "constant":
                    refined_type = self.data_type_refiner.get_refined_data_type(
                        s.data_type(), s.module())
                    if refined_type is not None:
                        s.set_data_type(refined_type)
                    else:
                        s.set_data_type("")
                # refine class attributes and method parameters and return value
                elif s.type() == "class":
                    for a in s.attributes():
                        refined_type = self.data_type_refiner.get_refined_data_type(
                            a.data_type(), s.module())
                        if refined_type is not None:
                            a.set_data_type(refined_type)
                        else:
                            a.set_data_type("")
                    for m in s.methods():
                        for p in m.parameter_details():
                            refined_type = self.data_type_refiner.get_refined_data_type(
                                p.data_type(), s.module())
                            if refined_type is not None:
                                p.set_data_type(refined_type)
                            else:
                                p.set_data_type("")

                        return_ = m.return_()
                        refined_type = self.data_type_refiner.get_refined_data_type(
                            return_.data_type(), s.module())
                        if refined_type is not None:
                            return_.set_data_type(refined_type)
                        else:
                            return_.set_data_type("")

    def update_parameter_if_not_equal(self, info, param_idx, expect):
        if info.parameter(param_idx) == expect:
            return
        info.set_parameter(param_idx, expect)

    def analyze(self, filename: str, data_type_refiner: DataTypeRefiner=None):
        self.filename: str = filename
        self.data_type_refiner: DataTypeRefiner = data_type_refiner

        tree = et.parse(filename)
        root = tree.getroot()       # <document>
        result = []
        for child in list(root):
            if child.tag == "section":    # <section>
                r = []
                self._analyze_section(filename, child, r)
                result.append(r)

        if data_type_refiner is not None:
            self._refine_data_type(result)

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

    def _match(self, filename: str, mod_name: str):
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
