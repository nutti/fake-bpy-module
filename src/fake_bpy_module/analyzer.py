import re
from typing import List, IO, Any
import json

from .common import (
    IntermidiateDataType,
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
)


class AnalysisResult:
    def __init__(self):
        self.section_info: List['SectionInfo'] = []


class RstLevel:
    def __init__(self, level: int = 0, spaces: str = ""):
        self._level = level
        self._spaces = spaces

    def __str__(self) -> str:
        return "Level: {}, Spaces: {}".format(self.level(), self.num_spaces())

    def level(self) -> int:
        return self._level

    def spaces(self) -> str:
        return self._spaces

    def num_spaces(self) -> int:
        return len(self.spaces())

    def make_next_level(self, spaces_to_add: str) -> 'RstLevel':
        new_level = RstLevel(self._level + 1, self._spaces + spaces_to_add)
        return new_level


class BaseAnalyzer:
    def __init__(self):
        self.support_bge: bool = False
        self.current_file: str = None
        self.current_module: str = None
        self.current_base_classes: str = None
        self.blender_version: str = None

    def set_blender_version(self, version: str):
        self.blender_version = version

    def enable_bge_support(self):
        self.support_bge = True

    def _is_bge_supported(self) -> bool:
        return self.support_bge

    def _cleanup_string(self, line: str) -> str:
        result = line

        result = re.sub(r":class:", " ", result)
        result = re.sub(r"`", " ", result)
        result = re.sub(r"^\s+", "", result)
        result = re.sub(r"\s+$", "", result)
        result = re.sub(r"\s+", " ", result)

        return result

    def _invalid_line(self, line: str, level: 'RstLevel'):
        raise ValueError("Invalid line: {} (File name: {}, Level: {})"
                         .format(line.rstrip("\n"), self.current_file, level))

    def _skip_until_next_le_level(self, file: IO[Any], level: 'RstLevel'):
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
        m = re.match(r"^\.\. (currentmodule|module):: ([a-zA-Z0-9._]+)", line)
        if m is None:
            self._invalid_line(line, level)

        module_name = m.group(2)

        if self.blender_version is not None and self.blender_version != "":
            version = [int(sp) for sp in self.blender_version.split(".")]
            if not self.support_bge:
                if version == [2, 90]:
                    if module_name.startswith("bpy.types."):
                        module_name = module_name[:module_name.rfind(".")]
                if version == [2, 91]:
                    if module_name == "bpy.data":
                        module_name = "bpy"
                if version == [2, 92]:
                    if module_name == "bpy.data":
                        module_name = "bpy"
                if version == [2, 93]:
                    if module_name == "bpy.data":
                        module_name = "bpy"

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

    def _parse_description(self, file: IO[Any], level: 'RstLevel') -> str:
        line = file.readline()
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\S+"
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(arg|type|return|rtype)", line):
                file.seek(last_pos)
                return description
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s*)\S+", line):
                description += line
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return description

    def _has_le_level_start(self, line: str, level: 'RstLevel') -> bool:
        pattern = r"^\s{0," + str(level.num_spaces()) + r"}\.\."
        if re.match(pattern, line):
            return True
        return False

    def _has_le_level_string(self, line: str, level: 'RstLevel') -> bool:
        pattern = r"^\s{0," + str(level.num_spaces()) + r"}\S+"
        if re.match(pattern, line):
            return True
        return False

    def _parse_func_detail(self, file: IO[Any], level: 'RstLevel') -> dict:
        def _parse_type(file: IO[Any], level: 'RstLevel') -> List[dict]:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:type ([a-zA-Z0-9_, ]+):(.*)"
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(arg|type|return|rtype)", line):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):
                    # TODO: should use this when we handle multiple line.
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line).group(1)
                    data_type = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["data_type"] += data_type
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return infos
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return infos

        def _parse_arg(file: IO[Any], level: 'RstLevel') -> List[dict]:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:(arg|param) ([a-zA-Z0-9_, ]+)\s*.*:(.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            infos = []
            for s in self._parse_comma_separated_string(m.group(2)):
                infos.append({
                    "name": self._cleanup_string(s),
                    "type": "parameter",
                    "description": m.group(3),
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
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):
                    description = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["description"] += description
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return infos
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return infos

        def _parse_return(file: IO[Any], level: 'RstLevel') -> str:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:return.*:(.*)"   # TODO: handle :return vert: or :return (min, max): case
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return description
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):
                    description += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):
                    file.seek(last_pos)
                    return description
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return description

        def _parse_rtype(file: IO[Any], level: 'RstLevel') -> str:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:rtype.*:(.*)"   # TODO: handle :rtype vert: or :rtype (min, max): case
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):
                    file.seek(last_pos)
                    return data_type
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):
                    data_type += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type):", line):
                self._skip_until_next_le_level(file, level=level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|param|return|rtype)", line):
                m = re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|param|return|rtype)", line)
                file.seek(last_pos)
                if m.group(1) == "type":
                    parameters_types.extend(_parse_type(file, level))
                elif m.group(1) in ["arg", "param"]:
                    parameters_args.extend(_parse_arg(file, level))
                elif m.group(1) == "return":
                    if return_ is not None:
                        raise ValueError(":return must be appeared only once: {} (File name: {}, Level: {})"
                                         .format(self.current_file, line, level.level()))
                    return_ = _parse_return(file, level)
                elif m.group(1) == "rtype":
                    if return_type is not None:
                        raise ValueError(":rtype must be appeared only once: {} (File name: {}, Level: {})"
                                         .format(self.current_file, line, level.level()))
                    return_type = _parse_rtype(file, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(file):", line):
                self._skip_until_next_le_level(file, level=level)
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                break
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
                    param_info.append_description(" " + self._cleanup_string(pa["description"]))
                    param_info.set_description(self._cleanup_string(param_info.description()))
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
        line_to_parse = line
        for c in line_to_parse:
            if c in ("(", "{", "["):
                level += 1
            elif c in (")", "}", "]"):
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


        def is_builtin_value(value):
            # Numerical default value.
            m = re.search(r"^[-0-9.+e*]+$", value)
            if m is not None:
                return True

            # String default value.
            m = re.search(r"^('|\")(.*)('|\")$", value)
            if m is not None:
                return True

            # Built-in default value.
            m = re.search(r"^(None|True|False)$", value)
            if m is not None:
                return True

            # Bin, hex, oct default value.
            m = re.search(r"0[box][0-9A-Fa-f]+", value)
            if m is not None:
                return True

            return False

        # Convert data type to string about the custom data type.
        params_converted = []
        for p in params:
            m = re.search(r"(.*)=(.*)", p)
            if m is None:
                # No default value.
                params_converted.append(p)
                continue

            param_variable = m.group(1)
            default_value = m.group(2)
            if is_builtin_value(default_value):
                params_converted.append(p)
                continue

            m = re.search(r"^\s*\{(.*)\}\s*$", default_value)
            if m is not None:
                # Set default value.
                params_converted.append(p)
                continue

            m = re.search(r"^\s*\[(.*)\]\s*$", default_value)
            if m is not None:
                # List list value.
                params_converted.append(p)
                continue

            m = re.search(r"^\s*\((.*)\)\s*$", default_value)
            if m is not None:
                # Tuple default value.
                params_converted.append(p)
                continue

            # Custom data type
            params_converted.append("{}='{}'".format(param_variable, default_value))
            output_log(LOG_LEVEL_NOTICE, "'{}' is a parameter with custom data type".format(p))

        return params_converted

    def _parse_constant(self, file: IO[Any], level: 'RstLevel') -> 'VariableInfo':
        def _parse_type(file: IO[Any], level: 'RstLevel') -> str:
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:type: (.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            type_str = m.group(1)

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    file.seek(last_pos)
                    return type_str
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return type_str
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return type_str
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                    file.seek(last_pos)
                    type_str += " " + self._parse_description(file, level=level.make_next_level(next_level_spaces))
                    type_str = self._cleanup_string(type_str)
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (data|attribute|DATA):: ([a-zA-Z0-9_]+):*$"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = VariableInfo("constant")
        info.set_name(self._cleanup_string(m.group(2)))
        if self.current_module is not None:
            info.set_module(self.current_module)

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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line).group(1)
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(self._cleanup_string(_parse_type(file, level=level.make_next_level(next_level_spaces)))))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block)::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block)::", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (to do)", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (to do)", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. _[a-zA-Z0-9-_]+:", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. _[a-zA-Z0-9-_]+:", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_attribute(self, file: IO[Any], level: 'RstLevel') -> 'VariableInfo':
        def _parse_type(file: IO[Any], level: 'RstLevel') -> str:
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:type: (.*)"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            type_str = m.group(1)

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    file.seek(last_pos)
                    return type_str
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return type_str
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return type_str
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                    file.seek(last_pos)
                    type_str += " " + self._parse_description(file, level=level.make_next_level(next_level_spaces))
                    type_str = self._cleanup_string(type_str)
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (data|attribute):: ([a-zA-Z0-9_]+)$"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = VariableInfo("attribute")
        info.set_name(self._cleanup_string(m.group(2)))
        if self.current_module is not None:
            info.set_module(self.current_module)

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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line).group(1)
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(self._cleanup_string(_parse_type(file, level=level.make_next_level(next_level_spaces)))))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|warning|note|code-block|deprecated)::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|warning|note|code-block|deprecated)::", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note):", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note):", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _get_multiline_string(self, file: IO[Any], level: 'RstLevel') -> str:
        line = file.readline()
        line = line.rstrip("\n")
        long_line = line
        while len(line) >= 1 and line[-1] == "\\":
            line = file.readline()
            line = line.rstrip("\n")
            long_line += line
        long_line = re.sub(r"\\", "", long_line)

        return long_line

    def _parse_function(self, file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
        line = self._get_multiline_string(file, level)
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (function|method):: ([a-zA-Z0-9_]+)\s*\((.*)\)"
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = FunctionInfo("function")
        info.set_name(self._cleanup_string(m.group(2)))
        if self.current_module is not None:
            info.set_module(self.current_module)
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
            elif self._has_le_level_string(line, level):
                file.seek(last_pos)
                return info
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)
                file.seek(last_pos)
                detail = self._parse_func_detail(file, level=level.make_next_level(next_level_spaces))
                info.add_parameter_details(detail["parameters"])
                if detail["return"] is not None:
                    info.set_return(detail["return"])
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|note|warning|code-block)::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|note|warning|code-block)::", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (warning):", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (warning):", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_class(self, file: IO[Any], level: 'RstLevel') -> 'ClassInfo':
        def _parse_method(file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = self._get_multiline_string(file, level)
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. method:: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("method")
            info.set_name(self._cleanup_string(m.group(1)))
            if self.current_module is not None:
                info.set_module(self.current_module)
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
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso|deprecated)::", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso|deprecated)::", line).group(1)
                    self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                    info.set_description(self._cleanup_string(info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_class_method(file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. classmethod:: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("classmethod")
            info.set_name(self._cleanup_string(m.group(1)))
            if self.current_module is not None:
                info.set_module(self.current_module)
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|warning)::", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|warning)::", line).group(1)
                    self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line).group(1)
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                    info.set_description(self._cleanup_string(info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_static_method(file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (staticmethod|function):: ([a-zA-Z0-9_]+)\((.*)\):*$"
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("staticmethod")
            info.set_name(self._cleanup_string(m.group(2)))
            if self.current_module is not None:
                info.set_module(self.current_module)
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
                elif self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)
                    file.seek(last_pos)
                    detail = self._parse_func_detail(file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|tip)::", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|tip)::", line).group(1)
                    self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                    info.set_description(self._cleanup_string(info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        line = file.readline()
        m = re.match(r"^\s{" + str(level.num_spaces()) + r"}\.\. class:: ([a-zA-Z0-9_]+)(\([a-zA-Z0-9_,]+\))*", line)
        if m is None:
            self._invalid_line(line, level)

        class_name = self._cleanup_string(m.group(1))

        info = ClassInfo()
        info.set_name(class_name)
        if self.current_module is not None:
            info.set_module(self.current_module)
        if self.current_base_classes is not None:
            info.add_base_classes(self.current_base_classes)

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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. data::", line):
                # TODO: Should use assignment expression introduced in Python 3.8
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. data::", line).group(1)
                file.seek(last_pos)
                attr = self._parse_attribute(file, level=level.make_next_level(next_level_spaces))
                attr.set_class(class_name)
                info.add_attribute(attr)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. attribute::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. attribute::", line).group(1)
                is_deprecated = re.search(r"\(Deprecated", line) is not None
                if self._is_bge_supported() and is_deprecated:
                    self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
                else:
                    file.seek(last_pos)
                    attr = self._parse_attribute(file, level=level.make_next_level(next_level_spaces))
                    attr.set_class(class_name)
                    info.add_attribute(attr)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. method::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. method::", line).group(1)
                file.seek(last_pos)
                method = _parse_method(file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. classmethod::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. classmethod::", line).group(1)
                file.seek(last_pos)
                method = _parse_class_method(file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. staticmethod::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. staticmethod::", line).group(1)
                file.seek(last_pos)
                method = _parse_static_method(file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. function::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. function::", line).group(1)
                file.seek(last_pos)
                method = _parse_static_method(file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso)::", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso)::", line).group(1)
                self._skip_until_next_le_level(file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(self._parse_description(file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
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
            self.current_base_classes = None
            if self._is_bge_supported() and re.search(r"/bge\.types\.(?!rst)", filename) is not None:
                self.current_module = "bge.types"
            else:
                self.current_module = None
            while line:
                if re.match(r"^base (class|classes) ---", line):
                    if self.current_base_classes is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    self.current_base_classes = self._parse_base_class(file, level=RstLevel())
                elif re.match(r"^\.\. (currentmodule|module)::", line):
                    if self.current_module is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    self.current_module = self._cleanup_string(self._parse_module(file, level=RstLevel()))
                elif re.match(r"^\.\. class::", line):
                    file.seek(last_pos)
                    class_info = self._parse_class(file, level=RstLevel())
                    section.add_info(class_info)
                elif re.match(r"^\.\. function::", line):
                    is_deprecated = re.search(r"\(Deprecated", line) is not None
                    if self._is_bge_supported() and is_deprecated:
                        self._skip_until_next_le_level(file, level=RstLevel())
                    else:
                        file.seek(last_pos)
                        function_info = self._parse_function(file, level=RstLevel())
                        section.add_info(function_info)
                elif re.match(r"^\.\. method::", line):
                    file.seek(last_pos)
                    function_info = self._parse_function(file, level=RstLevel())
                    section.add_info(function_info)
                elif re.match(r"^\.\. (data|DATA)::", line):
                    is_deprecated = re.search(r"\(Deprecated", line) is not None
                    if self._is_bge_supported() and is_deprecated:
                        self._skip_until_next_le_level(file, level=RstLevel())
                    else:
                        file.seek(last_pos)
                        data_info = self._parse_constant(file, level=RstLevel())
                        section.add_info(data_info)
                elif re.match(r"^\.\. attribute::", line):
                    file.seek(last_pos)
                    data_info = self._parse_constant(file, level=RstLevel())
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
                      re.match(r"^\.\. note:", line) or
                      re.match(r"^\.\. note,", line) or
                      re.match(r"^\.\.$", line) or
                      re.match(r"^\.\. _[a-zA-Z0-9-_]+:", line) or
                      re.match(r"^   :Attributes:", line)):
                    self._skip_until_next_le_level(file, level=RstLevel())
                elif re.match(r"^\.\.", line):
                    self._invalid_line(line, 0)
                elif re.match(r"^\s+\.\.", line):
                    self._invalid_line(line, 0)
                elif re.match(r"^\s+:", line):
                    self._invalid_line(line, 0)
                last_pos = file.tell()
                line = file.readline()

        section_none_removed = SectionInfo()
        for info in section.info_list:
            if info.module() is not None:
                section_none_removed.add_info(info)

        return section_none_removed

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
                            if (("module" in item) and (info.module() == item["module"])) or\
                               (("module" not in item) and (info.module() is None)):
                                remove_list.append(info)
                        for rm in remove_list:
                            section.info_list.remove(rm)
                            output_log(LOG_LEVEL_NOTICE,
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
