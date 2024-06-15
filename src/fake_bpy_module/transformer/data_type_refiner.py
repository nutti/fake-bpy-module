import re
import typing
from typing import List, Dict, Set, Tuple
from docutils import nodes

from .transformer_base import TransformerBase
from ..analyzer.nodes import (
    ModuleNode,
    NameNode,
    DescriptionNode,
    ClassNode,
    FunctionListNode,
    FunctionNode,
    ArgumentListNode,
    ArgumentNode,
    FunctionReturnNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    make_data_type_node,
)
from ..analyzer.roles import (
    ClassRef,
)
from ..utils import get_first_child, find_children, output_log, LOG_LEVEL_WARN, LOG_LEVEL_DEBUG


REGEX_MATCH_DATA_TYPE_PAIR = re.compile(r"^\((.*)\) pair$")
REGEX_MATCH_DATA_TYPE_WITH_DEFAULT = re.compile(r"(.*), default ([0-9a-zA-Z\"]+),$")

# pylint: disable=line-too-long
REGEX_MATCH_DATA_TYPE_SPACE = re.compile(r"^\s*$")
REGEX_MATCH_DATA_TYPE_ENUM_IN_DEFAULT = re.compile(r"^enum in \[(.*)\], default (.+)$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_ENUM_IN = re.compile(r"^enum in \[(.*)\](, \(.+\))*,?$")
REGEX_MATCH_DATA_TYPE_SET_IN = re.compile(r"^enum set in \{(.*)\}(, \(.+\))*,?$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT = re.compile(r"^boolean, default (False|True)$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF = re.compile(r"^boolean array of ([0-9]+) items(, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_VALUES = re.compile(r"^`((mathutils.)*(Color|Euler|Matrix|Quaternion|Vector))`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF = re.compile(r"^(int|float) array of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF = re.compile(r"^`(mathutils.[a-zA-Z]+)` (rotation )*of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_NUMBER_IN = re.compile(r"^(int|float) in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF = re.compile(r"^float multi-dimensional array of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_MATHUTILS_MATRIX_OF = re.compile(r"^`mathutils.Matrix` of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_STRING = re.compile(r"^(str|strings|string)\.*$")
REGEX_MATCH_DATA_TYPE_INTEGER = re.compile(r"^(int|integer|)\.*$")
REGEX_MATCH_DATA_TYPE_VALUE_BPY_PROP_COLLECTION_OF = re.compile(r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `([a-zA-Z0-9]+)`,$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_SEQUENCE_OF = re.compile(r"^sequence of\s+`([a-zA-Z0-9_.]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BPY_PROP_COLLECTION_OF = re.compile(r"^`bpy_prop_collection` of `([a-zA-Z0-9]+)`")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE_OBJECTS = re.compile(r"^List of `([A-Za-z0-9]+)` objects$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE = re.compile(r"^[Ll]ist of `([A-Za-z0-9_.]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING = re.compile(r"^(list|sequence) of (float|int|str)")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OF_PARENTHESES_VALUE = re.compile(r"^list of \(([a-zA-Z.,` ]+)\)")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_PAIR_OF_VALUE = re.compile(r"^pair of `([A-Za-z0-9_.]+)`")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE = re.compile(r"`BMElemSeq` of `([a-zA-Z0-9]+)`$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE = re.compile(r"^tuple of `([a-zA-Z0-9.]+)`('s)*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_LIST_OR_DICT_OR_SET_OR_TUPLE = re.compile(r"^`*(list|dict|set|tuple)`*\.*$")  # noqa # pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_OT = re.compile(r"^`([A-Z]+)_OT_([A-Za-z_]+)`,$")
REGEX_MATCH_DATA_TYPE_DOT = re.compile(r"^`([a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+)`$")
REGEX_MATCH_DATA_TYPE_DOT_COMMA = re.compile(r"^`([a-zA-Z0-9_.]+)`(,)*$")
REGEX_MATCH_DATA_TYPE_START_AND_END_WITH_PARENTHESES = re.compile(r"^\(([a-zA-Z0-9_.,` ]+)\)$")
REGEX_MATCH_DATA_TYPE_NAME = re.compile(r"^[a-zA-Z0-9_.]+$")
# pylint: enable=line-too-long

_REGEX_DATA_TYPE_OPTION_STR = re.compile(r"\(([a-zA-Z, ]+?)\)$")
_REGEX_DATA_TYPE_OPTION_END_WITH_NONE = re.compile(r"or None$")
_REGEX_DATA_TYPE_OPTION_OPTIONAL = re.compile(r"(^|\s|\()[oO]ptional(\s|\))")
_REGEX_DATA_TYPE_STARTS_WITH_COLLECTION = re.compile(r"^(list|tuple|dict)")


class EntryPoint:
    def __init__(self, module: str, name: str, type_: str):
        self.module: str = module
        self.name: str = name
        self.type: str = type_

    def fullname(self) -> str:
        return f"{self.module}.{self.name}"


class DataTypeRefiner(TransformerBase):

    def __init__(self, documents: List[nodes.document], **kwargs):
        super().__init__(documents, **kwargs)
        self._entry_points = None
        if "entry_points" in kwargs:
            self._entry_points = kwargs["entry_points"]

        self._entry_points_cache: Dict[str, Set] = {}

    def _build_entry_points(self, documents: List[nodes.document]) -> List['EntryPoint']:
        entry_points: List['EntryPoint'] = []

        for document in documents:
            module_node = get_first_child(document, ModuleNode)
            if module_node is None:
                continue

            module_name = module_node.element(NameNode).astext()

            class_nodes = find_children(document, ClassNode)
            for class_node in class_nodes:
                class_name = class_node.element(NameNode).astext()
                entry = EntryPoint(module_name, class_name, "class")
                entry_points.append(entry)

            func_nodes = find_children(document, FunctionNode)
            for func_node in func_nodes:
                func_name = func_node.element(NameNode).astext()
                entry = EntryPoint(module_name, func_name, "function")
                entry_points.append(entry)

            data_nodes = find_children(document, DataNode)
            for data_node in data_nodes:
                data_name = data_node.element(NameNode).astext()
                entry = EntryPoint(module_name, data_name, "constant")
                entry_points.append(entry)

        return entry_points

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
                    make_data_type_node("list[collections.abc.Callable[[`bpy.types.Scene`], None]]")
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
                return [make_data_type_node("collections.abc.Sequence[float]"),
                        make_data_type_node(f"`{s}`")]
        if dtype_str in ("4x4 `mathutils.Matrix`", "4x4 `Matrix`"):
            s = self._parse_custom_data_type(
                "Matrix", uniq_full_names, uniq_module_names, module_name)
            if s:
                if variable_kind == 'FUNC_RET':
                    return [make_data_type_node(f"`{s}`")]
                return [
                    make_data_type_node(
                        "collections.abc.Sequence[collections.abc.Sequence[float]]"),
                    make_data_type_node(f"`{s}`")]

        if REGEX_MATCH_DATA_TYPE_ENUM_IN_DEFAULT.match(dtype_str):
            return [make_data_type_node("str")]
        # Ex: enum in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        if REGEX_MATCH_DATA_TYPE_ENUM_IN.match(dtype_str):
            return [make_data_type_node("str")]

        # Ex: enum set in {'KEYMAP_FALLBACK'}, (optional)
        if REGEX_MATCH_DATA_TYPE_SET_IN.match(dtype_str):
            return [make_data_type_node("set[str]")]

        # Ex: enum in :ref:`rna_enum_object_modifier_type_items`, (optional)
        if dtype_str.startswith("enum in `rna"):
            return [make_data_type_node("str")]

        # Ex: Enumerated constant
        if dtype_str == "Enumerated constant":
            return [make_data_type_node("set[str]")]

        # Ex: boolean, default False
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT.match(dtype_str):
            return [make_data_type_node("bool")]
        # Ex: boolean array of 3 items, (optional)
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF.match(dtype_str):
            return [make_data_type_node("list[bool]")]

        if dtype_str == "boolean":
            return [make_data_type_node("bool")]
        if dtype_str == "bool":
            return [make_data_type_node("bool")]

        if dtype_str == "bytes":
            return [make_data_type_node("bytes")]
        if dtype_str.startswith("byte sequence"):
            return [make_data_type_node("collections.abc.Sequence[bytes]")]

        if dtype_str.lower().startswith("callable"):
            return [make_data_type_node("collections.abc.Callable")]

        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_VALUES.match(dtype_str):
            if variable_kind in ('FUNC_ARG', 'CONST', 'CLS_ATTR'):
                s = self._parse_custom_data_type(
                    m.group(1), uniq_full_names, uniq_module_names,
                    module_name)
                if s:
                    if variable_kind in ('CONST', 'CLS_ATTR'):
                        return [make_data_type_node(f"`{s}`")]
                    return [
                        make_data_type_node(
                            "collections.abc.Sequence[collections.abc.Sequence[float]]")
                        if m.group(3) == "Matrix"
                        else make_data_type_node("collections.abc.Sequence[float]"),
                        make_data_type_node(f"`{s}`")
                    ]

        # Ex: int array of 2 items in [-32768, 32767], default (0, 0)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF.match(dtype_str):
            if m.group(1) in ("int", "float"):
                if variable_kind == 'FUNC_ARG':
                    return [make_data_type_node(f"collections.abc.Iterable[{m.group(1)}]")]
                return [make_data_type_node(f"`bpy.types.bpy_prop_array`[{m.group(1)}]")]
        # Ex: :`mathutils.Euler` rotation of 3 items in [-inf, inf],
        #     default (0.0, 0.0, 0.0)
        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                if variable_kind in ('CONST', 'CLS_ATTR', 'FUNC_RET'):
                    return [make_data_type_node(f"`{s}`")]
                return [make_data_type_node("collections.abc.Sequence[float]"),
                        make_data_type_node(f"`{s}`")]

        # Ex: float triplet
        if dtype_str == "float triplet":
            s = self._parse_custom_data_type(
                "mathutils.Vector", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [
                    make_data_type_node("collections.abc.Sequence[float]"),
                    make_data_type_node(f"`{s}`")
                ]
        # Ex: int in [-inf, inf], default 0, (readonly)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_IN.match(dtype_str):
            return [make_data_type_node(m.group(1))]
        if dtype_str in ("int", "float"):
            return [make_data_type_node(dtype_str)]
        if dtype_str in ("unsigned int", "int (boolean)"):
            return [make_data_type_node("int")]
        if dtype_str == "int sequence":
            return [make_data_type_node("collections.abc.Sequence[int]")]

        # Ex: float multi-dimensional array of 3 * 3 items in [-inf, inf]
        if m := REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF.match(dtype_str):  # noqa # pylint: disable=C0301
            tuple_elems = [
                f"tuple[{', '.join(['float'] * int(m.group(1)))}]"
            ] * int(m.group(2))
            return [
                make_data_type_node("list[list[float]]"),
                make_data_type_node(f"tuple[{', '.join(tuple_elems)}]")
            ]

        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_MATRIX_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                "mathutils.Matrix", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                if variable_kind in ('CONST', 'CLS_ATTR', 'FUNC_RET'):
                    return [make_data_type_node(f"`{s}`")]
                return [
                    make_data_type_node(
                        "collections.abc.Sequence[collections.abc.Sequence[float]]"),
                    make_data_type_node(f"`{s}`")
                ]

        if dtype_str == "double":
            return [make_data_type_node("float")]
        if dtype_str.startswith("double (float)"):
            return [make_data_type_node("float")]

        if REGEX_MATCH_DATA_TYPE_STRING.match(dtype_str):
            return [make_data_type_node("str")]
        if REGEX_MATCH_DATA_TYPE_INTEGER.match(dtype_str):
            return [make_data_type_node("int")]
        if dtype_str == "tuple":
            return [make_data_type_node("tuple")]
        if dtype_str == "sequence":
            return [make_data_type_node("collections.abc.Sequence")]

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
            return [make_data_type_node("set[str]")]

        # [Pattern] sequence of string tuples or a function
        # [Test]
        #   File: refiner_test.py
        #   Function: test_get_refined_data_type_for_various_patterns
        #   Pattern: sequence of string tuples or a function
        if dtype_str == "sequence of string tuples or a function":
            return [
                make_data_type_node("collections.abc.Iterable[collections.abc.Iterable[str]]"),
                make_data_type_node("collections.abc.Callable")
            ]
        # Ex: sequence of bpy.types.Action
        if m := REGEX_MATCH_DATA_TYPE_SEQUENCE_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"list[`{s}`]")]
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
                return [make_data_type_node(f"list[`{s}`]")]
        # Ex: list of FEdge
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"list[`{s}`]")]
        # Ex: list of ints
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING.match(dtype_str):  # noqa # pylint: disable=C0301
            return [make_data_type_node(f"list[{m.group(2)}]")]
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
                        dtypes.append(make_data_type_node(f"list[`{s}`]"))
            return dtypes
        # Ex: pair of bmesh.types.BMVert
        if m := REGEX_MATCH_DATA_TYPE_PAIR_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"tuple[`{s}`, `{s}`]")]
        # Ex: BMElemSeq of BMEdge
        if m := REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [
                    make_data_type_node(f"list[`{s}`]"),
                    make_data_type_node("`bmesh.types.BMElemSeq`")
                ]
        # Ex: tuple of mathutils.Vector's
        if m := REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"tuple[`{s}`, ...]")]

        # Ex: (Vector, Quaternion, Vector)
        if m1 := REGEX_MATCH_DATA_TYPE_START_AND_END_WITH_PARENTHESES.match(dtype_str):
            splited = m1.group(1).split(",")
            dtypes = []
            for sp in splited:
                sp = sp.strip()
                if m2 := REGEX_MATCH_DATA_TYPE_DOT_COMMA.match(sp):
                    s = self._parse_custom_data_type(
                        m2.group(1), uniq_full_names, uniq_module_names, module_name)
                    if s:
                        dtypes.append(f"`{s}`")
            if len(dtypes) != 0:
                elem_str = ", ".join(dtypes)
                return [make_data_type_node(f"tuple[{elem_str}]")]

        if dtype_str == "dict with string keys":
            return [make_data_type_node("dict[str, typing.Any]")]
        if dtype_str == "iterable object":
            return [make_data_type_node("list")]
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

    def _get_data_type_options(
            self, dtype_str: str, module_name: str, variable_kind: str,
            is_pointer_prop: bool = False,
            description_str: str = None,
            additional_info: Dict[str, typing.Any] = None) -> Tuple[List[str], str]:
        if module_name.startswith("bpy."):
            option_results = []

            # If not pointer property, should not accept None.
            if variable_kind == 'CLS_ATTR':
                if not is_pointer_prop:
                    option_results.append("never none")
            elif variable_kind == 'CONST':
                option_results.append("never none")

            if m := _REGEX_DATA_TYPE_OPTION_STR.search(dtype_str):
                option_str = m.group(1)
                options = [sp.strip().lower() for sp in option_str.split(",")]
                has_unknown_option = False
                for opt in options:
                    if opt not in ("optional", "readonly", "never none"):
                        has_unknown_option = True
                        output_log(LOG_LEVEL_WARN,
                                   f"Unknown option '{opt}' is found from {dtype_str}")

                # If there is unknown parameter options, we don't strip them from
                # original string.
                if not has_unknown_option:
                    option_results.extend(options)

                    # Strip the unused string to speed up the later parsing process.
                    stripped = _REGEX_DATA_TYPE_OPTION_STR.sub("", dtype_str)
                    output_log(LOG_LEVEL_DEBUG, f"Data type is stripped: {dtype_str} -> {stripped}")
                    dtype_str = stripped

            # If readonly is specified, we should add never none as well.
            if "readonly" in option_results:
                option_results.append("never none")

            option_results = sorted(list(set(option_results)))

            # Active object can accept None.
            if variable_kind in ('CONST', 'CLS_ATTR'):
                if additional_info["data_name"].startswith("active"):
                    if "never none" in option_results:
                        option_results.remove("never none")
                    option_results.append("accept none")

            return option_results, dtype_str

        # From this, we assumed non-bpy module.

        if m := _REGEX_DATA_TYPE_OPTION_END_WITH_NONE.search(dtype_str):
            stripped = _REGEX_DATA_TYPE_OPTION_END_WITH_NONE.sub("", dtype_str)
            output_log(LOG_LEVEL_DEBUG, f"Data type is stripped: {dtype_str} -> {stripped}")

            return [""], stripped

        if description_str is not None:
            if m := _REGEX_DATA_TYPE_OPTION_OPTIONAL.search(description_str):
                return [""], dtype_str

        return ["never none"], dtype_str

    def _get_refined_data_type(
            self, dtype_str: str, module_name: str, variable_kind: str,
            is_pointer_prop: bool = False,
            description_str: str = None,
            additional_info: Dict[str, typing.Any] = None) -> List[DataTypeNode]:

        assert variable_kind in (
            'FUNC_ARG', 'FUNC_RET', 'CONST', 'CLS_ATTR', 'CLS_BASE')

        options, dtype_str_changed = self._get_data_type_options(
            dtype_str, module_name, variable_kind,
            is_pointer_prop=is_pointer_prop,
            description_str=description_str, additional_info=additional_info)

        result = self._get_refined_data_type_internal(
            dtype_str_changed, module_name, variable_kind, additional_info=additional_info)

        # Add options.
        for r in result:
            option_results = options.copy()
            if "option" in r.attributes:
                option_results.extend(r.attributes["option"].split(","))
            # list object will not be None.
            if variable_kind in ('CLS_ATTR', 'CONST') and "never none" not in option_results:
                if _REGEX_DATA_TYPE_STARTS_WITH_COLLECTION.match(r.to_string()):
                    option_results.append("never none")
            r.attributes["option"] = ",".join(option_results)

        output_log(
            LOG_LEVEL_DEBUG,
            f"Result of refining (kind={variable_kind}): "
            f"{dtype_str} -> {', '.join(r.to_string() for r in result)}")

        return result

    def _get_refined_data_type_internal(
            self, dtype_str: str, module_name: str, variable_kind: str,
            additional_info: Dict[str, typing.Any] = None) -> List[DataTypeNode]:

        dtype_str = dtype_str.strip()

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        # Ex. string, default "", -> string
        if m := REGEX_MATCH_DATA_TYPE_WITH_DEFAULT.match(dtype_str):
            dtype_str = m.group(1)

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
                    f"tuple[{', '.join([d.astext() for d in dtypes])}]")]

        result = self._get_refined_data_type_fast(
            dtype_str, uniq_full_names, uniq_module_names, module_name,
            variable_kind, additional_info)
        if result is not None:
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
            return dtypes
        return []

    def _parse_from_description(
            self, module_name: str, description_str: str = None,
            additional_info: Dict[str, typing.Any] = None) -> List[DataTypeNode]:

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        if description_str == "An instance of this object.":
            s = self._parse_custom_data_type(
                additional_info["self_class"], uniq_full_names,
                uniq_module_names, module_name)
            return [make_data_type_node(f"`{s}`")]

        return []

    def _refine(self, document: nodes.document):
        def refine(dtype_list_node: DataTypeListNode, module_name: str,
                   variable_kind: str, description_str: str = None,
                   additional_info: Dict[str, typing.Any] = None):
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            new_dtype_nodes = []

            new_dtype_nodes.extend(self._parse_from_description(
                module_name, description_str=description_str,
                additional_info=additional_info))

            for dtype_node in dtype_nodes:
                mod_options = []
                skip_refine = False
                if "mod-option" in dtype_node.attributes:
                    mod_options: List[str] = [
                        sp.strip()
                        for sp in dtype_node.attributes["mod-option"].split(",")
                    ]
                    skip_refine = "skip-refine" in mod_options
                if skip_refine:
                    continue

                is_pointer_prop = False
                class_refs = find_children(dtype_node, ClassRef)
                if len(class_refs) >= 1:
                    is_pointer_prop = True
                    # Omit collection property and non-bpy types.
                    for class_ref in class_refs:
                        if class_ref.to_string() in ("bpy_prop_collection", "bpy_prop_array"):
                            is_pointer_prop = False
                            break
                        # Accept like :class:`Object`
                        if module_name == "bpy.types" and class_ref.to_string().count(".") == 0:
                            continue
                        if not class_ref.to_string().startswith("bpy.types"):
                            is_pointer_prop = False
                            break

                new_dtype_nodes.extend(self._get_refined_data_type(
                    dtype_node.astext(), module_name, variable_kind,
                    is_pointer_prop=is_pointer_prop,
                    description_str=description_str,
                    additional_info=additional_info))
                dtype_list_node.remove(dtype_node)

            for node in new_dtype_nodes:
                dtype_list_node.append_child(node)

        module_node = get_first_child(document, ModuleNode)
        if module_node is None:
            return
        module_name = module_node.element(NameNode).astext()

        class_nodes = find_children(document, ClassNode)
        for class_node in class_nodes:
            class_name = class_node.element(NameNode).astext()

            func_list_node = class_node.element(FunctionListNode)
            func_nodes = find_children(func_list_node, FunctionNode)
            for func_node in func_nodes:
                arg_list_node = func_node.element(ArgumentListNode)
                arg_nodes = find_children(arg_list_node, ArgumentNode)
                for arg_node in arg_nodes:
                    description = arg_node.element(DescriptionNode).astext()
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'FUNC_ARG',
                           description_str=description,
                           additional_info={"self_class": f"{module_name}.{class_name}"})

                return_node = func_node.element(FunctionReturnNode)
                description = return_node.element(DescriptionNode).astext()
                dtype_list_node = return_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'FUNC_RET',
                       description_str=description,
                       additional_info={"self_class": f"{module_name}.{class_name}"})

            attr_list_node = class_node.element(AttributeListNode)
            attr_nodes = find_children(attr_list_node, AttributeNode)
            for attr_node in attr_nodes:
                attr_name = attr_node.element(NameNode).astext()
                dtype_list_node = attr_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'CLS_ATTR',
                       additional_info={
                           "self_class": f"{module_name}.{class_name}",
                           "data_name": f"{attr_name}"
                       })

            base_class_list_node = class_node.element(BaseClassListNode)
            base_class_nodes = find_children(base_class_list_node, BaseClassNode)
            for base_class_node in base_class_nodes:
                dtype_list_node = base_class_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'CLS_BASE')

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            arg_list_node = func_node.element(ArgumentListNode)
            arg_nodes = find_children(arg_list_node, ArgumentNode)
            for arg_node in arg_nodes:
                description = arg_node.element(DescriptionNode).astext()
                dtype_list_node = arg_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'FUNC_ARG',
                       description_str=description)

            return_node = func_node.element(FunctionReturnNode)
            dtype_list_node = return_node.element(DataTypeListNode)
            refine(dtype_list_node, module_name, 'FUNC_RET')

        data_nodes = find_children(document, DataNode)
        for data_node in data_nodes:
            data_name = data_node.element(NameNode).astext()
            dtype_list_node = data_node.element(DataTypeListNode)
            refine(dtype_list_node, module_name, 'CONST',
                   additional_info={"data_name": f"{data_name}"})

    @classmethod
    def name(cls) -> str:
        return "data_type_refiner"

    def apply(self, **kwargs):
        if self._entry_points is None:
            self._entry_points = self._build_entry_points(self.documents)

        self._entry_points_cache["uniq_full_names"] = {
            e.fullname() for e in self._entry_points}
        self._entry_points_cache["uniq_module_names"] = {
            e.module for e in self._entry_points}

        for document in self.documents:
            self._refine(document)
