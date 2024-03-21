import re
from typing import List, Dict, Set, Tuple
import typing
from docutils import nodes

from .docutils_based.analyzer.nodes import (
    DataTypeNode,
)
from .docutils_based.analyzer.roles import (
    ClassRef,
)
from .docutils_based.common import append_child

from .utils import (
    output_log,
    LOG_LEVEL_WARN,
    LOG_LEVEL_DEBUG,
)

BUILTIN_DATA_TYPE: List[str] = [
    "bool", "str", "bytes", "float", "int",
]

MODIFIER_DATA_TYPE: List[str] = [
    "list", "dict", "set", "tuple",
    "iteriter",
    "listlist", "tupletuple",
    "listtuple", "listcallable",
    "Generic",
    "typing.Iterator",
    "typing.Iterable",
    "typing.Callable",
    "typing.Any",
    "typing.Sequence",
]

CUSTOM_MODIFIER_MODIFIER_DATA_TYPE: List[str] = [
    "bpy.types.bpy_prop_collection",
    "bpy.types.bpy_prop_array",
]

MODIFIER_DATA_TYPE_TO_TYPING: Dict[str, str] = {
    "list": "typing.List",
    "dict": "typing.Dict",
    "set": "typing.Set",
    "tuple": "typing.Tuple",
    "Generic": "typing.Generic",
    "typing.Iterator": "typing.Iterator",
    "typing.Iterable": "typing.Iterable",
    "typing.Callable": "typing.Callable",
    "typing.Sequence": "typing.Sequence",
    "typing.Any": "typing.Any",
}

ALLOWED_CHAR_BEFORE = {" ", "("}
ALLOWED_CHAR_AFTER = {" ", ",", ")"}

REGEX_MATCH_DATA_TYPE_PAIR = re.compile(r"^\((.*)\) pair$")

# pylint: disable=line-too-long
REGEX_MATCH_DATA_TYPE_SPACE = re.compile(r"^\s*$")
REGEX_MATCH_DATA_TYPE_ENUM_IN_DEFAULT = re.compile(r"^enum in \[(.*)\], default (.+)$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_ENUM_IN = re.compile(r"^enum in \[(.*)\](, \(.+\))*$")
REGEX_MATCH_DATA_TYPE_SET_IN = re.compile(r"^enum set in \{(.*)\}(, \(.+\))*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT = re.compile(r"^boolean, default (False|True)$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF = re.compile(r"^boolean array of ([0-9]+) items(, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_VALUES = re.compile(r"^`((mathutils.)*(Color|Euler|Matrix|Quaternion|Vector))`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF = re.compile(r"^(int|float) array of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF = re.compile(r"^`(mathutils.[a-zA-Z]+)` (rotation )*of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_NUMBER_IN = re.compile(r"^(int|float) in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_ENDSWITH_NUMBER = re.compile(r"(int|float)$")
REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF = re.compile(r"^float multi-dimensional array of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_MATRIX_OF = re.compile(r"^`mathutils.Matrix` of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_STRING = re.compile(r"^(str|string|strings|string)\.*$")
REGEX_MATCH_DATA_TYPE_VALUE_BPY_PROP_COLLECTION_OF = re.compile(r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `([a-zA-Z0-9]+)`, $")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_SEQUENCE_OF = re.compile(r"^sequence of `([a-zA-Z0-9_.]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BPY_PROP_COLLECTION_OF = re.compile(r"^`bpy_prop_collection` of `([a-zA-Z0-9]+)`, $")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE_OBJECTS = re.compile(r"^List of `([A-Za-z0-9]+)` objects$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE = re.compile(r"^[Ll]ist of `([A-Za-z0-9_.]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING = re.compile(r"^(list|sequence) of (float|int|str)")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_PARENTHESES_VALUE = re.compile(r"^list of \(([a-zA-Z.,` ]+)\)")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE = re.compile(r"`BMElemSeq` of `([a-zA-Z0-9]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE = re.compile(r"^tuple of `([a-zA-Z0-9.]+)`('s)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OR_DICT_OR_SET_OR_TUPLE = re.compile(r"^`*(list|dict|set|tuple)`*\.*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_OT = re.compile(r"^`([A-Z]+)_OT_([A-Za-z_]+)`, $")
REGEX_MATCH_DATA_TYPE_DOT = re.compile(r"^`([a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+)`$")
REGEX_MATCH_DATA_TYPE_DOT_COMMA = re.compile(r"^`([a-zA-Z0-9_.]+)`(, )*$")
REGEX_MATCH_DATA_TYPE_NAME = re.compile(r"^[a-zA-Z0-9_.]+$")
# pylint: enable=line-too-long


def make_data_type_node(dtype_str) -> DataTypeNode:
    in_quote = False
    current_text = ""
    result = []
    for c in dtype_str:
        if c == "`":
            if in_quote:
                if current_text != "":
                    result.append(nodes.Text(current_text))
                    current_text = ""
                in_quote = True
            else:
                result.append(ClassRef(text=current_text))
                current_text = ""
                in_quote = False
        else:
            current_text += c
    if current_text != "":
        result.append(nodes.Text(current_text))

    dtype_node = DataTypeNode()
    for r in result:
        append_child(dtype_node, r)

    return dtype_node


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
            additional_info: Dict[str, typing.Any] = None) -> List['DataTypeNode']:
        # pylint: disable=R0912,R0911,R0915
        if REGEX_MATCH_DATA_TYPE_SPACE.match(dtype_str):
            return [make_data_type_node("typing.Any")]

        if m := re.match(r"list of callable\[`([0-9a-zA-Z.]+)`\]", dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [
                    make_data_type_node("typing.List[typing.Callable[[`bpy.types.Scene`, None]]]")
                ]

        if dtype_str == "Same type with self class":
            s = self._parse_custom_data_type(
                additional_info["self_class"], uniq_full_names,
                uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if dtype_str in ("type", "object", "function"):
            return [make_data_type_node("typing.Any")]

        if dtype_str.startswith("Depends on function prototype"):
            return [make_data_type_node("typing.Any")]

        # [Pattern] `AnyType`
        # [Test]
        #   File: refiner_test.py
        #   Function: test_get_refined_data_type_for_various_patterns
        #   Pattern: `AnyType`
        if dtype_str.startswith("`AnyType`"):
            return [make_data_type_node("typing.Any")]

        if dtype_str in ("any", "Any type."):
            return [make_data_type_node("typing.Any")]

        # "[23][dD] [Vv]ector"
        if dtype_str[1:].lower() == "d vector":
            s = self._parse_custom_data_type(
                "Vector", uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]
        if dtype_str == "4x4 mathutils.Matrix":
            s = self._parse_custom_data_type(
                "Matrix", uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if REGEX_MATCH_DATA_TYPE_ENUM_IN_DEFAULT.match(dtype_str):
            return [make_data_type_node("str"), make_data_type_node("int")]
        # Ex: enum in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        if REGEX_MATCH_DATA_TYPE_ENUM_IN.match(dtype_str):
            return [make_data_type_node("str"), make_data_type_node("int")]

        # Ex: enum set in {'KEYMAP_FALLBACK'}, (optional)
        if REGEX_MATCH_DATA_TYPE_SET_IN.match(dtype_str):
            return [make_data_type_node("typing.Set[str]"),
                    make_data_type_node("typing.Set[int]")]

        # Ex: enum in :ref:`rna_enum_object_modifier_type_items`, (optional)
        if dtype_str.startswith("enum in :ref:`rna"):
            return [make_data_type_node("str"), make_data_type_node("int")]

        # Ex: Enumerated constant
        if dtype_str == "Enumerated constant":
            return [make_data_type_node("typing.Set[str]"),
                    make_data_type_node("typing.Set[int]")]

        # Ex: boolean, default False
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT.match(dtype_str):
            return [make_data_type_node("bool")]
        # Ex: boolean array of 3 items, (optional)
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF.match(dtype_str):
            return [make_data_type_node("typing.List[bool]")]

        if dtype_str == "boolean":
            return [make_data_type_node("bool")]
        if dtype_str == "bool":
            return [make_data_type_node("bool")]

        if dtype_str == "bytes":
            return [make_data_type_node("bytes")]
        if dtype_str.startswith("byte sequence"):
            return [make_data_type_node("typing.Sequence[bytes]")]

        if dtype_str.lower().startswith("callable"):
            return [make_data_type_node("typing.Callable")]

        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_VALUES.match(dtype_str):
            if variable_kind in ('FUNC_ARG', 'CONST', 'CLS_ATTR'):
                s = self._parse_custom_data_type(
                    m.group(1), uniq_full_names, uniq_module_names,
                    module_name)
                if s:
                    return [make_data_type_node("typing.Sequence[float]"),
                            make_data_type_node(f"`{s}`")]

        # Ex: int array of 2 items in [-32768, 32767], default (0, 0)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF.match(dtype_str):
            if m.group(1) in ("int", "float"):
                if variable_kind == 'FUNC_ARG':
                    return [make_data_type_node(f"typing.Iterable[{m.group(1)}]")]
                return [make_data_type_node(f"`bpy.types.bpy_prop_array`[{m.group(1)}]")]
        # Ex: :`mathutils.Euler` rotation of 3 items in [-inf, inf],
        #     default (0.0, 0.0, 0.0)
        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                tuple_elms = ["float"] * int(m.group(3))
                return [
                    make_data_type_node("typing.List[float]"),
                    make_data_type_node(f"typing.Tuple[{', '.join(tuple_elms)}]"),
                    make_data_type_node(f"`{s}`")
                ]

        # Ex: float triplet
        if dtype_str == "float triplet":
            s = self._parse_custom_data_type(
                "mathutils.Vector", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [
                    make_data_type_node("typing.Sequence[float]"),
                    make_data_type_node(f"`{s}`")
                ]
        # Ex: int in [-inf, inf], default 0, (readonly)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_IN.match(dtype_str):
            return [make_data_type_node(m.group(1))]
        if m := REGEX_MATCH_DATA_TYPE_ENDSWITH_NUMBER.match(dtype_str):
            return [make_data_type_node(m.group(1))]
        if dtype_str in ("unsigned int", "int (boolean)"):
            return [make_data_type_node("int")]
        if dtype_str == "int sequence":
            return [make_data_type_node("typing.Sequence[int]")]

        # Ex: float multi-dimensional array of 3 * 3 items in [-inf, inf]
        if m := REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF.match(dtype_str):  # noqa # pylint: disable=C0301
            tuple_elems = [
                f"typing.Tuple[{', '.join(['float'] * int(m.group(1)))}]"
            ] * int(m.group(2))
            return [
                make_data_type_node("typing.List[typing.List[float]]"),
                make_data_type_node(f"typing.Tuple[{', '.join(tuple_elems)}]")
            ]

        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_MATRIX_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                "mathutils.Matrix", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                tuple_elems = [
                    f"typing.Tuple[{', '.join(['float'] * int(m.group(1)))}]"
                ] * int(m.group(2))
                return [
                    make_data_type_node("typing.List[typing.List[float]]"),
                    make_data_type_node(f"typing.Tuple[{', '.join(tuple_elems)}]"),
                    make_data_type_node(f"`{s}`")
                ]

        if dtype_str == "double":
            return [make_data_type_node("float")]
        if dtype_str.startswith("double (float)"):
            return [make_data_type_node("float")]

        if REGEX_MATCH_DATA_TYPE_STRING.match(dtype_str):
            return [make_data_type_node("str")]
        if dtype_str == "tuple":
            return [make_data_type_node("typing.Tuple")]
        if dtype_str == "sequence":
            return [make_data_type_node("typing.Sequence")]

        if dtype_str.startswith("`bgl.Buffer` "):
            s1 = self._parse_custom_data_type(
                "bgl.Buffer", uniq_full_names, uniq_module_names, module_name)
            if s1:
                return [make_data_type_node(f"`{s1}`")]

        if m := REGEX_MATCH_DATA_TYPE_VALUE_BPY_PROP_COLLECTION_OF.match(dtype_str):  # noqa # pylint: disable=C0301
            s1 = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            s2 = self._parse_custom_data_type(
                m.group(2), uniq_full_names, uniq_module_names, module_name)
            if s1 and s2:
                return [make_data_type_node(f"`{s1}`")]

        if dtype_str.startswith("set of strings"):
            return [make_data_type_node("typing.Set[str]")]

        # [Pattern] sequence of string tuples or a function
        # [Test]
        #   File: refiner_test.py
        #   Function: test_get_refined_data_type_for_various_patterns
        #   Pattern: sequence of string tuples or a function
        if dtype_str == "sequence of string tuples or a function":
            return [
                make_data_type_node("typing.Iterable[typing.Iterable[str]]"),
                make_data_type_node("typing.Callable")
            ]
        # Ex: sequence of bpy.types.Action
        if m := REGEX_MATCH_DATA_TYPE_SEQUENCE_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"typing.Iterable[`{s}`]")]
        # Ex: `bpy_prop_collection` of `ThemeStripColor`,
        #     (readonly, never None)
        if m := REGEX_MATCH_DATA_TYPE_BPY_PROP_COLLECTION_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`bpy.types.bpy_prop_collection`[`{s}`]")]
        # Ex: List of FEdge objects
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE_OBJECTS.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"typing.List[`{s}`]")]
        # Ex: list of FEdge
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"typing.List[`{s}`]")]
        # Ex: list of ints
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING.match(dtype_str):  # noqa # pylint: disable=C0301
            return [make_data_type_node(f"typing.List[`{m.group(2)}`]")]
        # Ex: list of (bmesh.types.BMVert)
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_PARENTHESES_VALUE.match(dtype_str):  # noqa # pylint: disable=C0301
            items = m.group(1).split(",")
            dtypes = []
            for item in items:
                im = re.match(r"^`([a-zA-Z.]+)`$", item.strip())
                if im:
                    s = self._parse_custom_data_type(
                        im.group(1), uniq_full_names, uniq_module_names,
                        module_name)
                    if s:
                        dtypes.append(make_data_type_node(f"typing.List[`{s}`]"))
            return dtypes
        # Ex: BMElemSeq of BMEdge
        if m := REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [
                    make_data_type_node(f"typing.List[`{s}`]"),
                    make_data_type_node("`bmesh.types.BMElemSeq`")
                ]
        # Ex: tuple of mathutils.Vector's
        if m := REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"typing.Tuple[`{s}`]")]

        if dtype_str in ("BMVertSeq", "BMEdgeSeq", "BMFaceSeq", "BMLoopSeq", "BMEditSelSeq"):  # noqa # pylint: disable=C0301
            s = self._parse_custom_data_type(
                dtype_str, uniq_full_names, uniq_module_names, module_name)
            if s:
                return [
                    make_data_type_node(f"typing.List[`{s.rstrip('Seq')}`]"),
                    make_data_type_node(f"`{s}`")
                ]

        if dtype_str == "dict with string keys":
            return [make_data_type_node("typing.Dict")]
        if dtype_str == "iterable object":
            return [make_data_type_node("typing.List")]
        if m := REGEX_MATCH_DATA_TYPE_LIST_OR_DICT_OR_SET_OR_TUPLE.match(dtype_str):  # noqa # pylint: disable=C0301
            return [make_data_type_node(f"{m.group(1)}")]

        # Ex: bpy.types.Struct subclass
        if dtype_str == "`bpy.types.Struct` subclass":
            s = self._parse_custom_data_type(
                "bpy.types.Struct", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if dtype_str == "`bpy_struct`":
            s = self._parse_custom_data_type(
                "bpy_struct", uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        # Ex: CLIP_OT_add_marker
        if m := REGEX_MATCH_DATA_TYPE_OT.match(dtype_str):
            idname = f"bpy.ops.{m.group(1).lower()}.{m.group(2)}"
            s = self._parse_custom_data_type(
                idname, uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if m := REGEX_MATCH_DATA_TYPE_DOT.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if m := REGEX_MATCH_DATA_TYPE_DOT_COMMA.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        if m := REGEX_MATCH_DATA_TYPE_NAME.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(0), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`{s}`")]

        return None

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
            self, dtype_str: str, module_name: str,
            variable_kind: str, parameter_str: str = None,
            additional_info: Dict[str, typing.Any] = None) -> List[DataTypeNode]:

        assert variable_kind in (
            'FUNC_ARG', 'FUNC_RET', 'CONST', 'CLS_ATTR', 'CLS_BASE')

        result = self._get_refined_data_type_internal(
            dtype_str, module_name, variable_kind, parameter_str,
            additional_info)

        # self._tweak_metadata(result, variable_kind)

        output_log(
            LOG_LEVEL_DEBUG,
            f"Result of refining (kind={variable_kind}): "
            f"{dtype_str} -> {', '.join(r.to_string() for r in result)}")

        return result

    def _get_refined_data_type_internal(
            self, dtype_str: str, module_name: str,
            variable_kind: str, parameter_str: str,
            additional_info: Dict[str, typing.Any] = None) -> List[DataTypeNode]:

        dtype_str.strip()
        _, dtype_str = self._build_metadata(
            dtype_str, module_name, parameter_str, variable_kind)

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        # TODO: is_optional = data_type.is_optional()

        # Ex. (Quaternion, float) pair
        if m := REGEX_MATCH_DATA_TYPE_PAIR.match(dtype_str):
            sp = m.group(1).split(",")
            dtypes: List[DataTypeNode] = []
            for s in sp:
                d = self._get_refined_data_type_fast(
                    s.strip(), uniq_full_names, uniq_module_names,
                    module_name, variable_kind, additional_info)
                if d is not None:
                    dtypes.extend(d)
            if len(dtypes) >= 1:
                return [make_data_type_node(
                    f"typing.Tuple[{', '.join([d.astext() for d in dtypes])}]")]
                # dd.set_metadata(metadata)
                # return dd

        result = self._get_refined_data_type_fast(
            dtype_str, uniq_full_names, uniq_module_names, module_name,
            variable_kind, additional_info)
        if result is not None:
            # result.set_is_optional(is_optional)
            # result.set_metadata(metadata)
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
                    dtypes.extend(result)
            # dtypes[0].set_is_optional(is_optional)
            # dtypes[0].set_metadata(metadata)
            return dtypes
        return []

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
    def __init__(self, module: str, name: str, type_: str):
        self.module: str = module
        self.name: str = name
        self.type: str = type_

    def fullname(self) -> str:
        return f"{self.module}.{self.name}"
