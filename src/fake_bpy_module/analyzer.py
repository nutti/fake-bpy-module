import re
from typing import List, IO, Any
import json
import copy

from .common import (
    CustomDataType,
    DataType,
    IntermidiateDataType,
    ModifierDataType,
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


# pylint: disable=R0903
class AnalysisResult:
    def __init__(self):
        self.section_info: List['SectionInfo'] = []


class RstLevel:
    def __init__(self, level: int = 0, spaces: str = ""):
        self._level = level
        self._spaces = spaces

    def __str__(self) -> str:
        return f"Level: {self.level()}, Spaces: {self.num_spaces()}"

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
        stripped = line.rstrip("\n")
        raise ValueError(
            f"Invalid line: {stripped} "
            f"(File name: {self.current_file}, Level: {level})")

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

        if not self.support_bge:
            if self.blender_version == "2.90":
                if module_name.startswith("bpy.types."):
                    module_name = module_name[:module_name.rfind(".")]
            elif self.blender_version in [
                    "2.91", "2.92", "2.93", "3.0", "3.1", "3.2", "latest"]:
                if module_name == "bpy.data":
                    module_name = "bpy"

        return module_name

    def _parse_base_class(self, file: IO[Any], level: int) -> List[DataType]:
        line = file.readline()
        m = re.match(r"^base (class|classes) --- (.*)", line)
        if m is None:
            self._invalid_line(line, level)

        base_classes = []
        sps = self._split_string_by_comma(self._cleanup_string(m.group(2)))
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(arg|type|return|rtype)", line):  # noqa # pylint: disable=C0301
                file.seek(last_pos)
                return description
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s*)\S+", line):  # noqa # pylint: disable=C0301
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

    # pylint: disable=R0912,R0914,R0915
    def _parse_func_detail(self, file: IO[Any], level: 'RstLevel') -> dict:
        def _parse_type(file: IO[Any], level: 'RstLevel') -> List[dict]:
            last_pos = file.tell()
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:type ([a-zA-Z0-9_, ]+):(.*)"  # noqa # pylint: disable=C0301
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            infos = []
            for s in self._split_string_by_comma(m.group(1)):
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(arg|type|return|rtype)", line):  # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):    # noqa # pylint: disable=C0301
                    # TODO: support multiple line.
                    data_type = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["data_type"] += data_type
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):     # noqa # pylint: disable=C0301
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
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:(arg|param) ([a-zA-Z0-9_, ]+)\s*.*:(.*)"  # noqa # pylint: disable=C0301
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            infos = []
            for s in self._split_string_by_comma(m.group(2)):
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):  # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    return infos
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):    # noqa # pylint: disable=C0301
                    description = re.sub(r"\s+", " ", line)
                    for info in infos:
                        info["description"] += description
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):     # noqa # pylint: disable=C0301
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
            # TODO: handle :return vert: or :return (min, max): case
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:return.*:(.*)"
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):  # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    return description
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):    # noqa # pylint: disable=C0301
                    description += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):     # noqa # pylint: disable=C0301
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
            # TODO: handle :rtype vert: or :rtype (min, max): case
            pattern = r"^\s{" + str(level.num_spaces()) + r"}:rtype.*:(.*)"
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|return|rtype)", line):  # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    return data_type
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)(\S+)", line):    # noqa
                    data_type += re.sub(r"\s+", " ", line)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\S+)", line):     # noqa
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type):", line):  # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(file, level=level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|param|return|rtype)", line):    # noqa # pylint: disable=C0301
                m = re.match(r"^\s{" + str(level.num_spaces()) + r"}:(type|arg|param|return|rtype)", line)  # noqa # pylint: disable=C0301
                file.seek(last_pos)
                if m.group(1) == "type":
                    parameters_types.extend(_parse_type(file, level))
                elif m.group(1) in ["arg", "param"]:
                    parameters_args.extend(_parse_arg(file, level))
                elif m.group(1) == "return":
                    if return_ is not None:
                        raise ValueError(
                            f":return must be appeared only once: "
                            f"{self.current_file} (File name: {line}, "
                            f"Level: {level.level()})")
                    return_ = _parse_return(file, level)
                elif m.group(1) == "rtype":
                    if return_type is not None:
                        raise ValueError(
                            f":rtype must be appeared only once: "
                            f"{self.current_file} (File name: {line}, "
                            f"Level: {level.level()})")
                    return_type = _parse_rtype(file, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}:(file):", line):  # noqa # pylint: disable=C0301
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
            for pa in parameters_args:
                if pt["name"] == pa["name"]:
                    param_info.append_description(
                        " " + self._cleanup_string(pa["description"]))
                    param_info.set_description(
                        self._cleanup_string(param_info.description()))

            is_optional = False
            if (param_info.description() is not None) and \
                    ("optional" in param_info.description()):
                is_optional = True
            dt = IntermidiateDataType(self._cleanup_string(pt["data_type"]))
            dt.set_is_optional(is_optional)
            param_info.set_data_type(dt)

            info["parameters"].append(param_info)
        for pa in parameters_args:
            for pi in parameters_types:
                if pi["name"] == pa["name"]:
                    break
            else:
                param_info = ParameterDetailInfo()
                param_info.set_name(self._cleanup_string(pa["name"]))
                param_info.append_description(
                    " " + self._cleanup_string(pa["description"]))

                is_optional = False
                if (param_info.description() is not None) and \
                        ("optional" in param_info.description()):
                    is_optional = True
                dt = IntermidiateDataType(
                    self._cleanup_string(pa["data_type"]))
                dt.set_is_optional(is_optional)
                param_info.set_data_type(dt)

                info["parameters"].append(param_info)

        if return_ is not None and return_type is not None:
            return_info = ReturnInfo()
            if return_ is not None:
                return_info.set_description(self._cleanup_string(return_))
            if return_type is not None:
                return_info.set_data_type(IntermidiateDataType(
                    self._cleanup_string(return_type)))
            info["return"] = return_info

        return info

    # pylint: disable=R0912,R0915
    def _split_string_by_comma(self, line: str) -> List[str]:
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
                    raise ValueError(f"Level must be >= 0 but {level} "
                                     f"(File name: {self.current_file}, "
                                     f"Line: {line})")
            if level == 0 and c == ",":
                params.append(current)
                current = ""
            else:
                current += c

        if level != 0:
            raise ValueError(f"Level must be == 0 but {level} "
                             f"(File name: {self.current_file}, Line: {line})")

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
            params_converted.append(f"{param_variable}='{default_value}'")
            output_log(LOG_LEVEL_NOTICE,
                       f"'{p}' is a parameter with custom data type")

        return params_converted

    def _parse_constant(
            self, file: IO[Any], level: 'RstLevel') -> 'VariableInfo':
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
                if self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return type_str
                if self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return type_str

                if re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    type_str += " " + self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))
                    type_str = self._cleanup_string(type_str)
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (data|attribute|DATA):: ([a-zA-Z0-9_]+):*$"   # noqa # pylint: disable=C0301
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line):   # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line).group(1)    # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(
                    self._cleanup_string(_parse_type(
                        file,
                        level=level.make_next_level(next_level_spaces)))))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block)::", line):     # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block)::", line).group(1)  # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (to do)", line):     # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (to do)", line).group(1)  # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. _[a-zA-Z0-9-_]+:", line):    # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. _[a-zA-Z0-9-_]+:", line).group(1)     # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(
                    self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_attribute(
            self, file: IO[Any], level: 'RstLevel') -> 'VariableInfo':
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
                if self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return type_str
                if self._has_le_level_string(line, level):
                    file.seek(last_pos)
                    return type_str

                if re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    type_str += " " + self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))
                    type_str = self._cleanup_string(type_str)
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return type_str

        line = file.readline()
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (data|attribute):: ([a-zA-Z0-9_]+)$"  # noqa # pylint: disable=C0301
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
            elif re.match(
                    r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line):
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):type:", line).group(1)    # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.set_data_type(IntermidiateDataType(self._cleanup_string(
                    _parse_type(
                        file,
                        level=level.make_next_level(next_level_spaces)))))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|warning|note|code-block|deprecated)::", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|warning|note|code-block|deprecated)::", line).group(1)   # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note):", line):     # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note):", line).group(1)  # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(
                    r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(
                    self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _get_multiline_string(self, file: IO[Any], _: 'RstLevel') -> str:
        line = file.readline()
        line = line.rstrip("\n")
        long_line = line
        while len(line) >= 1 and line[-1] == "\\":
            line = file.readline()
            line = line.rstrip("\n")
            long_line += line
        long_line = re.sub(r"\\", "", long_line)

        return long_line

    def _parse_function(
            self, file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
        line = self._get_multiline_string(file, level)
        pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (function|method|staticmethod):: ([a-zA-Z0-9_]+)\s*\((.*)\)"  # noqa # pylint: disable=C0301
        m = re.match(pattern, line)
        if m is None:
            self._invalid_line(line, level)

        info = FunctionInfo("function")
        info.set_name(self._cleanup_string(m.group(2)))
        if self.current_module is not None:
            info.set_module(self.current_module)
        for p in self._split_string_by_comma(m.group(3)):
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):   # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)    # noqa # pylint: disable=C0301
                file.seek(last_pos)
                detail = self._parse_func_detail(
                    file, level=level.make_next_level(next_level_spaces))
                info.add_parameter_details(detail["parameters"])
                if detail["return"] is not None:
                    info.set_return(detail["return"])
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|note|warning|code-block)::", line):     # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (seealso|note|warning|code-block)::", line).group(1)  # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (warning):", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (warning):", line).group(1)   # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(
                    self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))))
                info.set_description(self._cleanup_string(info.description()))
            else:
                self._invalid_line(line, level)
            last_pos = file.tell()
            line = file.readline()

        return info

    def _parse_class(self, file: IO[Any], level: 'RstLevel') -> 'ClassInfo':
        def _parse_method(file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = self._get_multiline_string(file, level)
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. method:: ([a-zA-Z0-9_]+)\((.*)\):*$"  # noqa # pylint: disable=C0301
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("method")
            info.set_name(self._cleanup_string(m.group(1)))
            if self.current_module is not None:
                info.set_module(self.current_module)
            for p in self._split_string_by_comma(m.group(2)):
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):   # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)    # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    detail = self._parse_func_detail(
                        file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso|deprecated)::", line):   # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso|deprecated)::", line).group(1)    # noqa # pylint: disable=C0301
                    self._skip_until_next_le_level(
                        file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(
                        self._parse_description(
                            file,
                            level=level.make_next_level(next_level_spaces))))
                    info.set_description(self._cleanup_string(
                        info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_class_method(
                file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. classmethod:: ([a-zA-Z0-9_]+)\((.*)\):*$"     # noqa # pylint: disable=C0301
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("classmethod")
            info.set_name(self._cleanup_string(m.group(1)))
            if self.current_module is not None:
                info.set_module(self.current_module)
            for p in self._split_string_by_comma(m.group(2)):
                info.add_parameter(self._cleanup_string(p))

            last_pos = file.tell()
            line = file.readline()
            while line:
                if re.match(r"^\s*$", line):
                    pass
                elif self._has_le_level_start(line, level):
                    file.seek(last_pos)
                    return info
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):   # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)    # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    detail = self._parse_func_detail(
                        file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|warning|literalinclude)::", line):     # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|warning|literalinclude)::", line).group(1)  # noqa # pylint: disable=C0301
                    self._skip_until_next_le_level(
                        file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line).group(1)  # noqa # pylint: disable=C0301
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(
                        self._parse_description(
                            file,
                            level=level.make_next_level(next_level_spaces))))
                    info.set_description(
                        self._cleanup_string(info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        def _parse_static_method(
                file: IO[Any], level: 'RstLevel') -> 'FunctionInfo':
            line = file.readline()
            pattern = r"^\s{" + str(level.num_spaces()) + r"}\.\. (staticmethod|function):: ([a-zA-Z0-9_]+)\((.*)\):*$"     # noqa # pylint: disable=C0301
            m = re.match(pattern, line)
            if m is None:
                self._invalid_line(line, level)

            info = FunctionInfo("staticmethod")
            info.set_name(self._cleanup_string(m.group(2)))
            if self.current_module is not None:
                info.set_module(self.current_module)
            for p in self._split_string_by_comma(m.group(3)):
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
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line):   # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+):(type|arg|param|return|rtype)", line).group(1)    # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    detail = self._parse_func_detail(
                        file, level=level.make_next_level(next_level_spaces))
                    info.add_parameter_details(detail["parameters"])
                    if detail["return"] is not None:
                        info.set_return(detail["return"])
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|tip)::", line):    # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|tip)::", line).group(1)     # noqa # pylint: disable=C0301
                    self._skip_until_next_le_level(
                        file, level=level.make_next_level(next_level_spaces))
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                    self._invalid_line(line, level)
                elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                    next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                    file.seek(last_pos)
                    info.append_description(" " + self._cleanup_string(
                        self._parse_description(
                            file,
                            level=level.make_next_level(next_level_spaces))))
                    info.set_description(
                        self._cleanup_string(info.description()))
                else:
                    self._invalid_line(line, level)
                last_pos = file.tell()
                line = file.readline()

            return info

        line = file.readline()
        m = re.match(r"^\s{" + str(level.num_spaces()) + r"}\.\. class:: ([a-zA-Z0-9_]+)(\([a-zA-Z0-9_,]+\))*", line)   # noqa # pylint: disable=C0301
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
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. data::", line):  # noqa # pylint: disable=C0301
                # TODO: Should use assignment expression introduced
                #       in Python 3.8
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. data::", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                attr = self._parse_attribute(
                    file, level=level.make_next_level(next_level_spaces))
                attr.set_class(class_name)
                info.add_attribute(attr)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. attribute::", line):     # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. attribute::", line).group(1)  # noqa # pylint: disable=C0301
                is_deprecated = re.search(r"\(Deprecated", line) is not None
                if self._is_bge_supported() and is_deprecated:
                    self._skip_until_next_le_level(
                        file, level=level.make_next_level(next_level_spaces))
                else:
                    file.seek(last_pos)
                    attr = self._parse_attribute(
                        file, level=level.make_next_level(next_level_spaces))
                    attr.set_class(class_name)
                    info.add_attribute(attr)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. method::", line):    # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. method::", line).group(1)     # noqa # pylint: disable=C0301
                file.seek(last_pos)
                method = _parse_method(
                    file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. classmethod::", line):   # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. classmethod::", line).group(1)    # noqa # pylint: disable=C0301
                file.seek(last_pos)
                method = _parse_class_method(
                    file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. staticmethod::", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. staticmethod::", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                method = _parse_static_method(
                    file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. function::", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. function::", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                method = _parse_static_method(
                    file, level=level.make_next_level(next_level_spaces))
                method.set_class(class_name)
                info.add_method(method)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso)::", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\. (note|code-block|warning|literalinclude|seealso)::", line).group(1)   # noqa # pylint: disable=C0301
                self._skip_until_next_le_level(
                    file, level=level.make_next_level(next_level_spaces))
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\.\.", line):     # noqa # pylint: disable=C0301
                self._invalid_line(line, level)
            elif re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line):  # noqa # pylint: disable=C0301
                next_level_spaces = re.match(r"^\s{" + str(level.num_spaces()) + r"}(\s+)\S+", line).group(1)   # noqa # pylint: disable=C0301
                file.seek(last_pos)
                info.append_description(" " + self._cleanup_string(
                    self._parse_description(
                        file, level=level.make_next_level(next_level_spaces))))
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
            if self._is_bge_supported() and \
                    re.search(r"/bge\.types\.(?!rst)", filename) is not None:
                self.current_module = "bge.types"
            else:
                self.current_module = None
            while line:
                if re.match(r"^base (class|classes) ---", line):
                    if self.current_base_classes is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    self.current_base_classes = self._parse_base_class(
                        file, level=RstLevel())
                elif re.match(r"^\.\. (currentmodule|module)::", line):
                    if self.current_module is not None:
                        self._invalid_line(line, 0)
                    file.seek(last_pos)
                    self.current_module = self._cleanup_string(
                        self._parse_module(file, level=RstLevel()))
                elif re.match(r"^\.\. class::", line):
                    file.seek(last_pos)
                    class_info = self._parse_class(file, level=RstLevel())
                    section.add_info(class_info)
                elif re.match(r"^\.\. function::", line):
                    deprecated = re.search(r"\(Deprecated", line) is not None
                    if self._is_bge_supported() and deprecated:
                        self._skip_until_next_le_level(file, level=RstLevel())
                    else:
                        file.seek(last_pos)
                        function_info = self._parse_function(
                            file, level=RstLevel())
                        section.add_info(function_info)
                elif re.match(r"^\.\. (method|staticmethod)::", line):
                    file.seek(last_pos)
                    function_info = self._parse_function(
                        file, level=RstLevel())
                    section.add_info(function_info)
                elif re.match(r"^\.\. (data|DATA)::", line):
                    deprecated = re.search(r"\(Deprecated", line) is not None
                    if self._is_bge_supported() and deprecated:
                        self._skip_until_next_le_level(file, level=RstLevel())
                    else:
                        file.seek(last_pos)
                        data_info = self._parse_constant(
                            file, level=RstLevel())
                        section.add_info(data_info)
                elif re.match(r"^\.\. attribute::", line):
                    file.seek(last_pos)
                    data_info = self._parse_constant(file, level=RstLevel())
                    section.add_info(data_info)
                # pylint: disable=R0916
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
                      re.match(r"^   :Attributes:", line) or
                      re.match(r"^\s+\.\. deprecated::", line)):
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
        super().__init__()
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
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if (("module" in item) and
                                    (info.module() == item["module"])) or \
                               (("module" not in item) and
                                    (info.module() is None)):
                                remove_list.append(info)
                        for rm in remove_list:
                            section.info_list.remove(rm)
                            output_log(
                                LOG_LEVEL_NOTICE,
                                f"{rm.name()} (type={rm.type()}) is removed")

            # Process "new" field
            #   - Add item if the same item doesn't exist in AnalysisResult.
            if "new" in data.keys():
                new_section = SectionInfo()
                for item in data["new"]:

                    # check if entry is already registered
                    has_entry = False
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
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
                            raise RuntimeError(
                                f"Unsupported Type: {item['type']}")
                    else:
                        output_log(LOG_LEVEL_WARN,
                                   f"{item['name']} is already registered")

                result.section_info.append(new_section)

            # Process "append" field
            #   - Add item's field if the same exists in AnalysisResult.
            #   - Value of item's field must be None.
            if "append" in data.keys():
                for item in data["append"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
                                continue
                            info.from_dict(item, 'APPEND')

            # Process "update" field
            #   - Update item's field if the same exists in AnalysisResult.
            #   - Value of item's field can be None or some values.
            if "update" in data.keys():
                for item in data["update"]:
                    for section in result.section_info:
                        for info in section.info_list:
                            if ("type" not in item) or \
                                    info.type() != item["type"]:
                                continue
                            if ("name" not in item) or \
                                    info.name() != item["name"]:
                                continue
                            if ("module" not in item) or \
                                    info.module() != item["module"]:
                                continue
                            info.from_dict(item, 'UPDATE')

    def _modify_post_process(self, result: 'AnalysisResult'):
        pass

    def _modify(self, result: 'AnalysisResult'):
        self._modify_with_mod_files(result)
        self._modify_post_process(result)


class BpyModuleAnalyzer(AnalyzerWithModFile):

    def _add_bpy_ops_override_parameters(self, result: 'AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.ops", info.module()):
                    continue
                if info.type() != "function":
                    continue

                func_info: 'FunctionInfo' = info

                func_info.add_parameter("override_context=None", 0)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("override_context")
                param_detail.set_data_type(IntermidiateDataType(
                    "dict, bpy.types.Context"))
                func_info.add_parameter_detail(param_detail, 0)

                func_info.add_parameter("execution_context=None", 1)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("execution_context")
                param_detail.set_data_type(IntermidiateDataType("str, int"))
                func_info.add_parameter_detail(param_detail, 1)

                func_info.add_parameter("undo=None", 2)
                param_detail = ParameterDetailInfo()
                param_detail.set_name("undo")
                param_detail.set_data_type(IntermidiateDataType("bool"))
                func_info.add_parameter_detail(param_detail, 2)

                if len(func_info.parameters()) >= 4:
                    func_info.add_parameter("*", 3)

    def _make_bpy_context_variable(self, result: 'AnalysisResult'):
        bpy_context_module_infos: List['VariableInfo'] = []
        bpy_context_class_info: 'ClassInfo' = None
        for section in result.section_info:
            info_list_copied = copy.copy(section.info_list)
            for info in info_list_copied:
                if info.module() == "bpy.context":
                    bpy_context_module_infos.append(info)
                    section.info_list.remove(info)
                if info.module() == "bpy.types" and \
                        info.type() == "class" and info.name() == "Context":
                    bpy_context_class_info = info

        if bpy_context_class_info is None:
            output_log(LOG_LEVEL_WARN, "Failed to find bpy.types.Context")
            return

        attribute_names = [
            attr.name() for attr in bpy_context_class_info.attributes()]
        for info_to_add in bpy_context_module_infos:
            if info_to_add.type() != "constant":
                raise Exception(f"{info_to_add.name()} (module: "
                                f"{info_to_add.module()}) must be constant")
            if info_to_add.name() in attribute_names:
                output_log(LOG_LEVEL_WARN,
                           f"Attribute {info_to_add.name()} has already "
                           "registered in bpy.types.Context")
                continue
            var_info = VariableInfo("attribute")
            var_info.set_name(info_to_add.name())
            var_info.set_module(bpy_context_class_info.module())
            var_info.set_description(info_to_add.description())
            var_info.set_class(bpy_context_class_info.name())
            var_info.set_data_type(info_to_add.data_type())
            bpy_context_class_info.add_attribute(var_info)

        info = VariableInfo("constant")
        info.set_name("context")
        info.set_module("bpy")
        info.set_data_type(IntermidiateDataType("bpy.types.Context"))
        section = SectionInfo()
        section.add_info(info)
        result.section_info.append(section)

    def _add_getitem_and_setitem(self, class_info: 'ClassInfo', dtype: str):
        info = FunctionInfo("method")
        info.set_name("__getitem__")
        info.set_parameters(["key"])
        param_detail_info = ParameterDetailInfo()
        param_detail_info.set_name("key")
        param_detail_info.set_description("")
        param_detail_info.set_data_type(IntermidiateDataType("int, str"))
        info.set_parameter_details([param_detail_info])
        info.set_class(class_info.name())
        info.set_module(class_info.module())
        return_info = ReturnInfo()
        return_info.set_description("")
        return_info.set_data_type(CustomDataType(dtype, skip_refine=True))
        info.set_return(return_info)
        class_info.add_method(info)

        info = FunctionInfo("method")
        info.set_name("__setitem__")
        info.set_parameters(["key", "value"])
        param_detail_info_key = ParameterDetailInfo()
        param_detail_info_key.set_name("key")
        param_detail_info_key.set_description("")
        param_detail_info_key.set_data_type(IntermidiateDataType("int, str"))
        param_detail_info_value = ParameterDetailInfo()
        param_detail_info_value.set_name("value")
        param_detail_info_value.set_description("")
        param_detail_info_value.set_data_type(CustomDataType(
            dtype, skip_refine=True))
        info.set_parameter_details([
            param_detail_info_key, param_detail_info_value])
        info.set_class(class_info.name())
        info.set_module(class_info.module())
        class_info.add_method(info)

    def _add_iter_and_next(self, class_info: 'ClassInfo', dtype: str):
        info = FunctionInfo("method")
        info.set_name("__iter__")
        info.set_parameters([])
        info.set_parameter_details([])
        info.set_class(class_info.name())
        info.set_module(class_info.module())
        return_info = ReturnInfo()
        return_info.set_description("")
        return_info.set_data_type(CustomDataType(
            "GenericType", ModifierDataType("typing.Iterator"),
            skip_refine=True))
        info.set_return(return_info)
        class_info.add_method(info)

        info = FunctionInfo("method")
        info.set_name("__next__")
        info.set_parameters([])
        info.set_parameter_details([])
        info.set_class(class_info.name())
        info.set_module(class_info.module())
        return_info = ReturnInfo()
        return_info.set_description("")
        return_info.set_data_type(CustomDataType(dtype, skip_refine=True))
        info.set_return(return_info)
        class_info.add_method(info)

    def _tweak_bpy_types_classes(self, result: 'AnalysisResult'):
        for section in result.section_info:
            for info in section.info_list:
                if not re.match(r"^bpy.types", info.module()):
                    continue
                if info.type() != "class":
                    continue
                if info.name() == "bpy_prop_collection":
                    # class bpy_prop_collection(Generic[GenericType]):
                    #     def __getitem__(self, key: Union[str, int])
                    #         -> GenericType:
                    #     def __setitem__(self, key: Union[str, int],
                    #                     value: GenericType):
                    self._add_getitem_and_setitem(info, "GenericType")
                    self._add_iter_and_next(info, "GenericType")
                    info.add_base_class(
                        CustomDataType(
                            "GenericType", ModifierDataType("Generic"),
                            skip_refine=True))
                elif info.name() == "bpy_struct":
                    # class bpy_struct():
                    #     def __getitem__(self, key: Union[str, int]) -> Any:
                    #     def __setitem__(self, key: Union[str, int],
                    #                     value: Any):
                    self._add_getitem_and_setitem(info, "typing.Any")

    def _modify(self, result: 'AnalysisResult'):
        super()._modify(result)
        self._add_bpy_ops_override_parameters(result)
        self._make_bpy_context_variable(result)

        # After this, we could not infer data types as ItermidiateDataType
        self._tweak_bpy_types_classes(result)
