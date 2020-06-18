import xml.etree.ElementTree as et
import re
from typing import List, IO, Any
import json

from .common import (
    IntermidiateDataType,
    Info,
    ParameterDetailInfo,
    ReturnInfo,
    VariableInfo,
    FunctionInfo,
    ClassInfo,
    SectionInfo,
)
from .utils import (
    output_log,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERR
)


class AnalysisResult:
    def __init__(self):
        self.section_info: List['SectionInfo'] = []


class BaseAnalyzer:
    def __init__(self):
        self.current_file: str = None

    def _get_level_space_count(self, level: int) -> int:
        return level * 3

    def _cleanup_string(self, line: str) -> str:
        result = line

        result = re.sub(r":class:", " ", result)
        result = re.sub(r"`", " ", result)
        result = re.sub(r"^\s+", "", result)
        result = re.sub(r"\s+$", "", result)
        result = re.sub(r"\s+", " ", result)

        return result

    def _invalid_line(self, line: str, level: int):
        raise ValueError("Invalid line: {} (File name: {}, Level: {})"
                         .format(line.rstrip("\n"), self.current_file, level))

    def _skip_until_next_le_level(self, file: IO[Any], level: int):
        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return
            last_pos = file.tell()
            line = file.readline()

    def _parse_module(self, file: IO[Any], level: int) -> str:
        line = file.readline()
        m = re.match(r"^\.\. module:: ([a-zA-Z0-9._]+)", line)
        if m is None:
            self._invalid_line(line, level)

        module_name = m.group(1)

        return module_name

    def _parse_base_class(self, file: IO[Any], level: int) -> List['DataType']:
        line = file.readline()
        m = re.match(r"^base (class|classes) --- (.*)", line)
        if m is None:
            self._invalid_line(line, level)
        
        base_classes = []
        sps = self._parse_comma_separated_string(self._cleanup_string(m.group(2)))
        for sp in sps:
            base_classes.append(IntermidiateDataType(self._cleanup_string(sp)))

        return base_classes

    def _parse_description(self, file: IO[Any], level: int) -> str:
        line = file.readline()
        pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}.*"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        description = line

        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return description
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return description
            elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(arg|type|return|rtype)", line):
                file.seek(last_pos)
                return description
            elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}.*", line):
                description += line
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return description

    def _has_le_level_start(self, line: str, level: int) -> bool:
        for lv in range(level+1):
            pattern = r"^\s{" + str(lv*3) + r"}\.\."
            if re.match(pattern, line):
                return True
        return False

    def _has_le_level_string(self, line: str, level: int) -> bool:
        for lv in range(level+1):
            pattern = r"^\s{" + str(lv*3) + r"}\S+"
            if re.match(pattern, line):
                return True
        return False

    def _parse_func_detail(self, file: IO[Any], level: int) -> dict:
        def _parse_type(file: IO[Any], level: int) -> List[dict]:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:type ([a-zA-Z0-9_, ]+):(.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            infos = []
            for s in self._parse_comma_separated_string(m.group(1)):
                infos.append({
                    "name": self._cleanup_string(s),
                    "type": "parameter",
                    "description": "",
                    "data_type": m.group(2),
                })

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return infos
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(arg|type|return|rtype)", line):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\s*(\S+)", line):
                    data_type = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["data_type"] += data_type
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return infos
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return infos

        def _parse_arg(file: IO[Any], level: int) -> List[dict]:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:arg ([a-zA-Z0-9_, ]+):(.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            infos = []
            for s in self._parse_comma_separated_string(m.group(1)):
                infos.append({
                    "name": self._cleanup_string(s),
                    "type": "parameter",
                    "description": m.group(2),
                    "data_type": "",
                })

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^disabled: set global orientation in Collada assets", line):
                    pass
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(self._get_level_space_count(level) - 1) + r"," + str(self._get_level_space_count(level+1) + 8) + r"}(\S+)", line):
                    description = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["description"] += description
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return infos
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return infos

        def _parse_return(file: IO[Any], level: int) -> str:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:return.*:(.*)"   # TODO: handle :return vert: or :return (min, max): case
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            description = re.sub(r"\s+", " ", m.group(1))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return description
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return description
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}(\s*\S+)", line):
                    description += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return description
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return description

        def _parse_rtype(file: IO[Any], level: int) -> str:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:rtype.*:(.*)"   # TODO: handle :rtype vert: or :rtype (min, max): case
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            data_type = re.sub(r"\s+", " ", m.group(1))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return data_type
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return data_type
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return data_type
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}(\S+)", line):
                    data_type += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return data_type
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return data_type

        parameters_types = []
        parameters_args = []
        return_type = None
        return_ = None
        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                break
            elif re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(type|arg|return|rtype)", line):
                m = re.match(r"^\s{" + str(self._get_level_space_count(level)) + r"}:(type|arg|return|rtype)", line)
                file.seek(last_pos)
                if m.group(1) == "type":
                    parameters_types.extend(_parse_type(file, level))
                elif m.group(1) == "arg":
                    parameters_args.extend(_parse_arg(file, level))
                elif m.group(1) == "return":
                    if return_ is not None:
                        raise ValueError(":return must be appeared only once: {} (File name: {}, Level: {})"
                                         .format(self.current_file, line, level))
                    return_ = _parse_return(file, level)
                elif m.group(1) == "rtype":
                    if return_type is not None:
                        raise ValueError(":rtype must be appeared only once: {} (File name: {}, Level: {})"
                                         .format(self.current_file, line, level))
                    return_type = _parse_rtype(file, level)
            last_pos = file.tell()
            line = file.readline()

        # Merge.
        info = {
            "parameters": [],
            "return": None,
        }

        for pt in parameters_types:
            param_info = ParameterDetailInfo()
            param_info.set_name(self._cleanup_string(pt["name"]))
            param_info.set_data_type(IntermidiateDataType(self._cleanup_string(pt["data_type"])))
            for pa in parameters_args:
                if pt["name"] == pa["name"]:
                    param_info.append_description(self._cleanup_string(pa["description"]) + " ")
            info["parameters"].append(param_info)
        for pa in parameters_args:
            for pi in parameters_types:
                if pi["name"] == pa["name"]:
                    break
            else:
                param_info = ParameterDetailInfo()
                param_info.set_name(self._cleanup_string(pa["name"]))
                param_info.set_data_type(IntermidiateDataType(self._cleanup_string(pa["data_type"])))
                info["parameters"].append(param_info)

        if return_ is not None and return_type is not None:
            return_info = ReturnInfo()
            if return_ is not None:
                return_info.set_description(self._cleanup_string(return_))
            if return_type is not None:
                return_info.set_data_type(IntermidiateDataType(self._cleanup_string(return_type)))
            info["return"] = return_info

        return info

    def _parse_comma_separated_string(self, line: str) -> List[str]:
        level = 0
        params = []
        current = ""
        for c in line:
            if c == "(":
                level += 1
            elif c ==")":
                level -= 1
                if level < 0:
                    raise ValueError("Level must be >= 0 but {} (File name: {}, Line: {})"
                                     .format(level, self.current_file, line))
            if level == 0 and c == ",":
                params.append(current)
                current = ""
            else:
                current += c

        if level != 0:
            raise ValueError("Level must be == 0 but {} (File name: {}, Line: {})"
                             .format(level, self.current_file, line))

        if current != "":
            params.append(current)

        return params

    def _parse_constant(self, file: IO[Any], level: int) -> 'VariableInfo':
        def _parse_type(file: IO[Any], level: int) -> str:
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:type: (.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            type_str = m.group(1)

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. (data|attribute):: ([a-zA-Z0-9_]+):*$"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = VariableInfo("constant")
        info.set_name(self._cleanup_string(m.group(2)))

        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return info
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:type:", line):
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(self._cleanup_string(_parse_type(file, level=level+1))))
            elif (re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. code-block::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. _[a-zA-Z0-9-_]+:", line)):
                self._skip_until_next_le_level(file, level=level+1)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                file.seek(last_pos)
                info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_attribute(self, file: IO[Any], level: int) -> 'VariableInfo':
        def _parse_type(file: IO[Any], level: int) -> str:
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}:type: (.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            type_str = m.group(1)

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. (data|attribute):: ([a-zA-Z0-9_]+)$"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = VariableInfo("attribute")
        info.set_name(self._cleanup_string(m.group(2)))

        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return info
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:type:", line):
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(self._cleanup_string(_parse_type(file, level=level+1))))
            elif (re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. seealso::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. warning::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line)):
                self._skip_until_next_le_level(file, level=level+1)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                file.seek(last_pos)
                info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_function(self, file: IO[Any], level: int) -> 'FunctionInfo':
        line = file.readline()
        pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. (function|method):: ([a-zA-Z0-9_]+)\s*\((.*)\)"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = FunctionInfo("function")
        info.set_name(self._cleanup_string(m.group(2)))
        for p in self._parse_comma_separated_string(m.group(3)):
            info.add_parameter(self._cleanup_string(p))

        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^Computes the Constrained Delaunay Triangulation of a set of vertices, with edges", line):
                pass
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:", line):
                file.seek(last_pos)
                detail = self._parse_func_detail(file, level=level+1)
                info.add_parameter_details(detail["parameters"])
                if detail["return"] is not None:
                    info.set_return(detail["return"])
            elif (re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. seealso::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. warning::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. code-block::", line)):
                self._skip_until_next_le_level(file, level=level+1)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                file.seek(last_pos)
                info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_class(self, file: IO[Any], level: int) -> 'ClassInfo':
        def _parse_method(file: IO[Any], level: int) -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. method:: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                # Special case for freestyle.shaders.rst
                pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. method:: (__init__)\((num_iterations=100, factor_point=0.1),$"
                m = re.match(pattern, line)
                if m is None:
                    self._invalid_line(line, level)

                # Skip until ')' is found.
                line = file.readline()
                while line:
                    if re.match(r"\)$", line):
                        break
                    line = file.readline()

            info = FunctionInfo("method")
            info.set_name(self._cleanup_string(m.group(1)))
            for p in self._parse_comma_separated_string(m.group(2)):
                info.add_parameter(self._cleanup_string(p))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:", line):
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level+1)
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif (re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line) or
                      re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. code-block::", line) or
                      re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. warning::", line) or
                      re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. literalinclude::", line) or
                      re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. seealso::", line)):
                    self._skip_until_next_le_level(file, level=level+1)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                    file.seek(last_pos)
                    info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_class_method(file: IO[Any], level: int) -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. classmethod:: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("classmethod")
            info.set_name(self._cleanup_string(m.group(1)))
            for p in self._parse_comma_separated_string(m.group(2)):
                info.add_parameter(self._cleanup_string(p))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:", line):
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level+1)
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                    file.seek(last_pos)
                    info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_static_method(file: IO[Any], level: int) -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(self._get_level_space_count(level)) + r"}\.\. (staticmethod|function):: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("staticmethod")
            info.set_name(self._cleanup_string(m.group(2)))
            for p in self._parse_comma_separated_string(m.group(3)):
                info.add_parameter(self._cleanup_string(p))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}:", line):
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level+1)
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line):
                    self._skip_until_next_le_level(file, level=level+1)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                    file.seek(last_pos)
                    info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        line = file.readline()
        m = re.match(r"^\.\. class:: ([a-zA-Z0-9_]+)(\([a-zA-Z0-9_,]+\))*", line)
        if m is None:
            self._invalid_line(line, level)

        class_name = self._cleanup_string(m.group(1))

        info = ClassInfo()
        info.set_name(class_name)

        last_pos = file.tell()
        line = file.readline()
        while line:
            if re.match(r"^\s*$", line):
                pass
            elif self._has_le_level_start(line, level):
                file.seek(last_pos)
                return info
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. data::", line):
                file.seek(last_pos)
                attr = self._parse_attribute(file, level=level+1)
                attr.set_class(class_name)
                info.add_attribute(attr)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. attribute::", line):
                file.seek(last_pos)
                attr = self._parse_attribute(file, level=level+1)
                attr.set_class(class_name)
                info.add_attribute(attr)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. method::", line):
                file.seek(last_pos)
                method = _parse_method(file, level=level+1)
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. classmethod::", line):
                file.seek(last_pos)
                method = _parse_class_method(file, level=level+1)
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. staticmethod::", line):
                file.seek(last_pos)
                method = _parse_static_method(file, level=level+1)
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. function::", line):
                file.seek(last_pos)
                method = _parse_static_method(file, level=level+1)
                method.set_class(class_name)
                info.add_method(method)
            elif (re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. note::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. code-block::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. warning::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. literalinclude::", line) or
                  re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\. seealso::", line)):
                self._skip_until_next_le_level(file, level=level+1)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(self._get_level_space_count(level+1)) + r"}\S+", line):
                file.seek(last_pos)
                info.append_description(self._cleanup_string(self._parse_description(file, level=level+1)) + " ")
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _modify(self, result: 'AnalysisResult'):
        pass

    def _analyze_by_file(self, filename: str) -> 'SectionInfo':
        self.current_file = filename

        with open(filename, "r", encoding="utf-8") as file:
            last_pos = file.tell()
            line = file.readline()
            section = SectionInfo()
            module_name = None
            base_classes = None
            while line:
                if re.match(r"^base (class|classes) ---", line):
                    if base_classes is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    base_classes = self._parse_base_class(file, level=0)
                elif re.match(r"^\.\. module::", line):
                    if module_name is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    module_name = self._cleanup_string(self._parse_module(file, level=0))
                elif re.match(r"^\.\. class::", line):
                    file.seek(last_pos)
                    class_info = self._parse_class(file, level=0)
                    class_info.set_module(module_name)
                    if base_classes is not None:
                        class_info.add_base_classes(base_classes)
                    section.add_info(class_info)
                elif re.match(r"^\.\. function::", line):
                    file.seek(last_pos)
                    function_info = self._parse_function(file, level=0)
                    function_info.set_module(module_name)
                    section.add_info(function_info)
                elif re.match(r"^\.\. method::", line):
                    file.seek(last_pos)
                    function_info = self._parse_function(file, level=0)
                    function_info.set_module(module_name)
                    section.add_info(function_info)
                elif re.match(r"^\.\. data::", line):
                    file.seek(last_pos)
                    data_info = self._parse_constant(file, level=0)
                    data_info.set_module(module_name)
                    section.add_info(data_info)
                elif re.match(r"^\.\. attribute::", line):
                    file.seek(last_pos)
                    data_info = self._parse_constant(file, level=0)
                    data_info.set_module(module_name)
                    section.add_info(data_info)
                elif (re.match(r"^\.\. include::", line) or
                      re.match(r"^\.\. literalinclude::", line) or
                      re.match(r"^\.\. note::", line) or
                      re.match(r"^\.\. rubric::", line) or
                      re.match(r"^\.\. hlist::", line) or
                      re.match(r"^\.\. toctree::", line) or
                      re.match(r"^\.\. warning::", line) or
                      re.match(r"^\.\. code-block::", line) or
                      re.match(r"^\.\. seealso::", line) or
                      re.match(r"^\.\. note,", line) or
                      re.match(r"^\.\.$", line) or
                      re.match(r"^\.\. _[a-zA-Z0-9-_]+:", line)):
                    self._skip_until_next_le_level(file, level=0)
                elif re.match(r"^\.\.", line):
                    self._invalid_line(line, 0)
                last_pos = file.tell()
                line = file.readline()

        return section

    def analyze(self, filenames: List[str]) -> 'AnalysisResult':
        result = AnalysisResult()
        for f in filenames:
            info = self._analyze_by_file(f)
            result.section_info.append(info)

        self._modify(result)

        return result


class AnalyzerWithModFile(BaseAnalyzer):
    def __init__(self, mod_files: List[str]):
        super(AnalyzerWithModFile, self).__init__()
        self._mod_files: List[str] = mod_files

    def _modify_with_mod_files(self, result: 'AnalysisResult'):
        for mod_file in self._mod_files:
            self._modify_with_mod_file(mod_file, result)

    def _modify_with_mod_file(self, mod_file: str, result: 'AnalysisResult'):
        with open(mod_file, encoding="utf-8") as f:
            data = json.load(f)

            # Process "remove" field
            #   - Remove item if the same item exists in AnalysisResult.
            if "remove" in data.keys():
                for item in data["remove"]:
                    for section in result.section_info:
                        remove_list = []
                        for info in section.info_list:
                            if ("type" not in item) or (info.type() != item["type"]):
                                continue
                            if ("name" not in item) or (info.name() != item["name"]):
                                continue
                            if (("module" in item) and (info.module() != item["module"])) or\
                               (("module" not in item) and (info.module() is None)):
                                remove_list.append(info)
                        for rm in remove_list:
                            section.info_list.remove(rm)
                            output_log(LOG_LEVEL_WARN,
                                       "{} (type={}) is removed"
                                       .format(rm.name(), rm.type()))

            # Process "new" field
            #   - Add item if the same item doesn't exist in AnalysisResult.
            if "new" in data.keys():
                new_section = SectionInfo()
                for item in data["new"]:

                    # check if entry is already registered
                    has_entry = False
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or (info.type() != item["type"]):
                                continue
                            if ("name" not in item) or (info.name() != item["name"]):
                                continue
                            if ("module" not in item) or (info.module() != item["module"]):
                                continue
                            has_entry = True
                            break
                        if has_entry:
                            break

                    if not has_entry:
                        if item["type"] == "constant":
                            new_v = VariableInfo("constant")
                            new_v.from_dict(item, 'NEW')
                            new_section.info_list.append(new_v)
                        elif item["type"] == "function":
                            new_f = FunctionInfo("function")
                            new_f.from_dict(item, 'NEW')
                            new_section.info_list.append(new_f)
                        elif item["type"] == "class":
                            new_c = ClassInfo()
                            new_c.from_dict(item, 'NEW')
                            new_section.info_list.append(new_c)
                        else:
                            raise RuntimeError("Unsupported Type: {}"
                                               .format(item["type"]))
                    else:
                        output_log(LOG_LEVEL_WARN,
                                   "{} is already registered"
                                   .format(item["name"]))

                result.section_info.append(new_section)

            # Process "append" field
            #   - Add item's field if the same exists in AnalysisResult.
            #   - Value of item's field must be None.
            if "append" in data.keys():
                for item in data["append"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or (info.type() != item["type"]):
                                continue
                            if ("name" not in item) or (info.name() != item["name"]):
                                continue
                            if ("module" not in item) or (info.module() != item["module"]):
                                continue
                            info.from_dict(item, 'APPEND')

            # Process "update" field
            #   - Update item's field if the same exists in AnalysisResult.
            #   - Value of item's field can be None or some values.
            if "update" in data.keys():
                for item in data["update"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or (info.type() != item["type"]):
                                continue
                            if ("name" not in item) or (info.name() != item["name"]):
                                continue
                            if ("module" not in item) or (info.module() != item["module"]):
                                continue
                            info.from_dict(item, 'UPDATE')

    def _modify_post_process(self, result: 'AnalysisResult'):
        pass

    def _modify(self, result: 'AnalysisResult'):
        self._modify_with_mod_files(result)
        self._modify_post_process(result)
