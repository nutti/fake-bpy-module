import re
from typing import Any, Self

from docutils import nodes

from fake_bpy_module.analyzer.nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    ClassNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
    DescriptionNode,
    EnumNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    ModuleNode,
    NameNode,
    make_data_type_node,
)
from fake_bpy_module.analyzer.roles import ClassRef, EnumRef
from fake_bpy_module.utils import (
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_WARN,
    append_child,
    find_children,
    get_first_child,
    output_log,
    split_string_by_bar,
    split_string_by_comma,
)

from .transformer_base import TransformerBase

REGEX_MATCH_DATA_TYPE_PAIR = re.compile(r"^\((.*)\) pair$")
REGEX_MATCH_DATA_TYPE_WITH_DEFAULT = re.compile(r"(.*), default ([0-9a-zA-Z\"]+),$")  # noqa: E501

# pylint: disable=C0301
REGEX_MATCH_DATA_TYPE_SPACE = re.compile(r"^\s*$")
REGEX_MATCH_DATA_TYPE_ENUM_IN_DEFAULT = re.compile(r"^enum in \[(.*)\], default (.+)$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_ENUM_IN = re.compile(r"^enum in \[(.*)\](, \(.+\))*$")
REGEX_MATCH_DATA_TYPE_SET_IN = re.compile(r"^enum set in \{(.*)\}(, \(.+\))*$")
REGEX_MATCH_DATA_TYPE_SET_IN_RNA = re.compile(r"^enum set in `(.*)`(, \(.+\))*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT = re.compile(r"^boolean, default (False|True)$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF = re.compile(r"^boolean array of ([0-9]+) items(, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_MATHUTILS_VALUES = re.compile(r"^`((mathutils.)*(Color|Euler|Matrix|Quaternion|Vector))`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF = re.compile(r"^(int|float) array of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF = re.compile(r"^`(mathutils.[a-zA-Z]+)` (rotation )*of ([0-9]+) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_NUMBER_IN = re.compile(r"^(int|float) in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF = re.compile(r"^float multi-dimensional array of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_MATHUTILS_MATRIX_OF = re.compile(r"^`mathutils.Matrix` of ([0-9]) \* ([0-9]) items in \[([-einf+0-9,. ]+)\](, .+)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_STRING = re.compile(r"^(str|strings|string)\.*$")
REGEX_MATCH_DATA_TYPE_INTEGER = re.compile(r"^(int|integer|)\.*$")
REGEX_MATCH_DATA_TYPE_VALUE_BPY_PROP_COLLECTION_OF = re.compile(r"^`([a-zA-Z0-9]+)` `bpy_prop_collection` of `([a-zA-Z0-9]+)`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_SEQUENCE_OF = re.compile(r"^sequence of\s+`([a-zA-Z0-9_.]+)`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_BPY_PROP_COLLECTION_OF = re.compile(r"^`bpy_prop_collection` of `([a-zA-Z0-9]+)`")  # noqa: E501
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE_OBJECTS = re.compile(r"^List of `([A-Za-z0-9]+)` objects$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE = re.compile(r"^[Ll]ist of `([A-Za-z0-9_.]+)`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING = re.compile(r"^(list|sequence) of (float|int|str)")  # noqa: E501
REGEX_MATCH_DATA_TYPE_LIST_OF_PARENTHESES_VALUE = re.compile(r"^list of \(([a-zA-Z.,` ]+)\)")  # noqa: E501
REGEX_MATCH_DATA_TYPE_PAIR_OF_VALUE = re.compile(r"^pair of `([A-Za-z0-9_.]+)`")
REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE = re.compile(r"`BMElemSeq` of `([a-zA-Z0-9]+)`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_BMLAYERCOLLECTION_OF_VALUE = re.compile(r"`BMLayerCollection` of ([a-zA-Z0-9_]+)$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_BMLAYERCOLLECTION_OF_CLASS = re.compile(r"`BMLayerCollection` of `([a-zA-Z0-9._]+)`$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE = re.compile(r"^tuple of `([a-zA-Z0-9.]+)`('s)*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_LIST_OR_DICT_OR_SET_OR_TUPLE = re.compile(r"^`*(list|dict|set|tuple)`*\.*$")  # noqa: E501
REGEX_MATCH_DATA_TYPE_OT = re.compile(r"^`([A-Z]+)_OT_([A-Za-z_]+)`$")
REGEX_MATCH_DATA_TYPE_DOT = re.compile(r"^`([a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+)`$")
REGEX_MATCH_DATA_TYPE_DOT_COMMA = re.compile(r"^`([a-zA-Z0-9_.]+)`(,)*$")
REGEX_MATCH_DATA_TYPE_START_AND_END_WITH_PARENTHESES = re.compile(r"^\(([a-zA-Z0-9_.,` ]+)\)$")     # noqa: E501
REGEX_MATCH_DATA_TYPE_NAME = re.compile(r"^[a-zA-Z0-9_.]+$")
# pylint: enable=line-too-long

REGEX_MATCH_DESCRIPTION_TYPE_IN = re.compile(r"type in `(.*)`")
REGEX_MATCH_DESCRIPTION_ENUMERATOR_IN = re.compile(r"^Enumerator in `(.*)`")

# pylint: disable=C0301
_REGEX_DATA_TYPE_OPTION_STR = re.compile(r"\(([a-zA-Z, ]+?)\)$")
_REGEX_DATA_TYPE_OPTION_END_WITH_NONE = re.compile(r"or None$")
_REGEX_DATA_TYPE_OPTION_OPTIONAL = re.compile(r"(^|^An |\()[oO]ptional(\s|\))")
_REGEX_DATA_TYPE_STARTS_WITH_COLLECTION = re.compile(r"^(list|tuple|dict)")
_REGEX_DATA_TYPE_MODIFIER_TYPES = re.compile(r"^(Sequence|Callable|list|dict|tuple)?\[(.+)\]$")  # noqa: E501

REGEX_SPLIT_OR = re.compile(r" \| | or |,")


def snake_to_camel(name: str) -> str:
    return "".join(w.title() for w in name.split("_"))


def get_rna_enum_name(dtype_str: str) -> str:
    rna_enum_name = dtype_str.split("`")[1][len("rna_enum_"):]
    return snake_to_camel(rna_enum_name)


class EntryPoint:
    def __init__(self, module: str, name: str, type_: str) -> None:
        self.module: str = module
        self.name: str = name
        self.type: str = type_

    def fullname(self) -> str:
        return f"{self.module}.{self.name}"


class DataTypeRefiner(TransformerBase):

    def __init__(self, documents: list[nodes.document], **kwargs: dict) -> None:
        super().__init__(documents, **kwargs)
        self._entry_points = None
        if "entry_points" in kwargs:
            self._entry_points = kwargs["entry_points"]

        self._entry_points_cache: dict[str, set] = {}

    def _build_entry_points(
            self, documents: list[nodes.document]) -> list[EntryPoint]:
        entry_points: list[EntryPoint] = []

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

            enum_nodes = find_children(document, EnumNode)
            for enum_node in enum_nodes:
                enum_name = enum_node.element(NameNode).astext()
                entry = EntryPoint(module_name, enum_name, "enum")
                entry_points.append(entry)

        return entry_points

    def _parse_custom_data_type(
            self, string_to_parse: str, uniq_full_names: set[str],
            uniq_module_names: set[str], module_name: str) -> str:
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

    # pylint: disable=R0911,R0912,R0913,R0915
    def _get_refined_data_type_fast(  # noqa: C901, PLR0911, PLR0912
        self, dtype_str: str, uniq_full_names: set[str],
        uniq_module_names: set[str], module_name: str,
        variable_kind: str,
        additional_info: dict[str, Any] | None = None
    ) -> list[DataTypeNode]:

        dtype_str = dtype_str.strip().strip(",")

        if REGEX_MATCH_DATA_TYPE_SPACE.match(dtype_str):
            return [make_data_type_node("typing.Any")]

        if m := re.match(r"list of callable\[`([0-9a-zA-Z.]+)`\]", dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [
                    make_data_type_node("list[collections.abc.Callable"
                                        "[[`bpy.types.Scene`], None]]")
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

        if dtype_str.startswith("`AnyType`"):
            return [make_data_type_node("typing.Any")]

        if dtype_str == "None":
            return [make_data_type_node("None")]

        if dtype_str in ("any", "Any", "Any type."):
            return [make_data_type_node("typing.Any")]

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
            if "[]" in dtype_str or "['DEFAULT']" in dtype_str:
                return [make_data_type_node("str")]
            enum_values = ",".join(
                v.strip()
                for v in dtype_str.split("[")[1].split("]")[0].split(",")
            )
            return [make_data_type_node(f"typing.Literal[{enum_values}]")]
        # [Ex] enum in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
        if REGEX_MATCH_DATA_TYPE_ENUM_IN.match(dtype_str):
            if "[]" in dtype_str or "['DEFAULT']" in dtype_str:
                return [make_data_type_node("str")]
            enum_values = ",".join(
                v.strip()
                for v in dtype_str.split("[")[1].split("]")[0].split(",")
            )
            return [make_data_type_node(f"typing.Literal[{enum_values}]")]

        # [Ex] enum set in {'KEYMAP_FALLBACK'}, (optional)
        if REGEX_MATCH_DATA_TYPE_SET_IN.match(dtype_str):
            if "{}" in dtype_str:
                return [make_data_type_node("set[str]")]
            enum_values = ",".join(
                v.strip()
                for v in dtype_str.split("{")[1].split("}")[0].split(",")
            )
            return [make_data_type_node(f"set[typing.Literal[{enum_values}]]")]

        # [Ex] enum set in `rna_enum_operator_return_items`
        if REGEX_MATCH_DATA_TYPE_SET_IN_RNA.match(dtype_str):
            enum_literal_type = get_rna_enum_name(dtype_str)
            dtype_node = DataTypeNode()
            append_child(dtype_node, nodes.Text("set["))
            append_child(dtype_node,
                         EnumRef(text=f"bpy.typing.{enum_literal_type}"))
            append_child(dtype_node, nodes.Text("]"))
            return [dtype_node]

        # [Ex] enum in :ref:`rna_enum_object_modifier_type_items`, (optional)
        if dtype_str.startswith("enum in `rna"):
            enum_literal_type = get_rna_enum_name(dtype_str)
            dtype_node = DataTypeNode()
            append_child(dtype_node,
                         EnumRef(text=f"bpy.typing.{enum_literal_type}"))
            return [dtype_node]

        # [Ex] Enumerated constant
        if dtype_str == "Enumerated constant":
            return [make_data_type_node("set[str]")]

        # [Ex] boolean, default False
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_DEFAULT.match(dtype_str):
            return [make_data_type_node("bool")]
        # [Ex] boolean array of 3 items, (optional)
        if REGEX_MATCH_DATA_TYPE_BOOLEAN_ARRAY_OF.match(dtype_str):
            if variable_kind == 'FUNC_ARG':
                return [make_data_type_node("collections.abc.Iterable[bool]")]
            return [make_data_type_node("`bpy.types.bpy_prop_array`[bool]")]

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
                        else make_data_type_node(
                            "collections.abc.Sequence[float]"),
                        make_data_type_node(f"`{s}`")
                    ]

        # [Ex] int array of 2 items in [-32768, 32767], default (0, 0)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_ARRAY_OF.match(dtype_str):
            if m.group(1) in ("int", "float"):
                if variable_kind == 'FUNC_ARG':
                    return [make_data_type_node(
                        f"collections.abc.Iterable[{m.group(1)}]")]
                return [make_data_type_node(
                    f"`bpy.types.bpy_prop_array`[{m.group(1)}]")]
        # [Ex] `mathutils.Euler` rotation of 3 items
        #      in [-inf, inf], default (0.0, 0.0, 0.0)
        if m := REGEX_MATCH_DATA_TYPE_MATHUTILS_ARRAY_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names,
                module_name)
            if s:
                if variable_kind in ('CONST', 'CLS_ATTR', 'FUNC_RET'):
                    return [make_data_type_node(f"`{s}`")]
                return [make_data_type_node("collections.abc.Sequence[float]"),
                        make_data_type_node(f"`{s}`")]

        # [Ex] float triplet
        if dtype_str == "float triplet":
            s = self._parse_custom_data_type(
                "mathutils.Vector", uniq_full_names, uniq_module_names,
                module_name)
            if s:
                return [
                    make_data_type_node("collections.abc.Sequence[float]"),
                    make_data_type_node(f"`{s}`")
                ]
        # [Ex] int in [-inf, inf], default 0, (readonly)
        if m := REGEX_MATCH_DATA_TYPE_NUMBER_IN.match(dtype_str):
            return [make_data_type_node(m.group(1))]
        if dtype_str in ("int", "float"):
            return [make_data_type_node(dtype_str)]
        if dtype_str in ("unsigned int", "int (boolean)"):
            return [make_data_type_node("int")]
        if dtype_str == "int sequence":
            return [make_data_type_node("collections.abc.Sequence[int]")]

        # [Ex] float multi-dimensional array of 3 * 3 items in [-inf, inf]
        if m := REGEX_MATCH_DATA_TYPE_FLOAT_MULTI_DIMENSIONAL_ARRAY_OF.match(
                dtype_str):
            tuple_elems = [
                f"tuple[{', '.join(['float'] * int(m.group(2)))}]"
            ] * int(m.group(1))
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

        if m := REGEX_MATCH_DATA_TYPE_VALUE_BPY_PROP_COLLECTION_OF.match(
                dtype_str):
            s1 = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            s2 = self._parse_custom_data_type(
                m.group(2), uniq_full_names, uniq_module_names, module_name)
            if s1 and s2:
                return [make_data_type_node(f"`{s1}`")]

        if dtype_str.startswith("set of strings"):
            return [make_data_type_node("set[str]")]

        if dtype_str == "sequence of string tuples or a function":
            return [
                make_data_type_node("collections.abc.Iterable[collections.abc.Iterable[str]]"),
                make_data_type_node("collections.abc.Callable")
            ]
        # [Ex] sequence of bpy.types.Action
        if m := REGEX_MATCH_DATA_TYPE_SEQUENCE_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"list[`{s}`]")]
        # [Ex] `bpy_prop_collection` of `ThemeStripColor`,
        #     (readonly, never None)
        if m := REGEX_MATCH_DATA_TYPE_BPY_PROP_COLLECTION_OF.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(
                    f"`bpy.types.bpy_prop_collection`[`{s}`]")]
        # [Ex] List of FEdge objects
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE_OBJECTS.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"list[`{s}`]")]
        # [Ex] list of FEdge
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"list[`{s}`]")]
        # [Ex] list of ints
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_NUMBER_OR_STRING.match(dtype_str):
            return [make_data_type_node(f"list[{m.group(2)}]")]
        # [Ex] list of (bmesh.types.BMVert)
        if m := REGEX_MATCH_DATA_TYPE_LIST_OF_PARENTHESES_VALUE.match(
                dtype_str):
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
        # [Ex] pair of bmesh.types.BMVert
        if m := REGEX_MATCH_DATA_TYPE_PAIR_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"tuple[`{s}`, `{s}`]")]
        # [Ex] BMElemSeq of BMEdge
        if m := REGEX_MATCH_DATA_TYPE_BMELEMSEQ_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"`bmesh.types.BMElemSeq`[`{s}`]")]
        # [Ex] BMLayerCollection of float
        if m := REGEX_MATCH_DATA_TYPE_BMLAYERCOLLECTION_OF_VALUE.match(
                dtype_str):
            return [make_data_type_node(
                f"`bmesh.types.BMLayerCollection`[{m.group(1)}]"
            )]
        # [Ex] BMLayerCollection of `mathutils.Vector`
        if m := REGEX_MATCH_DATA_TYPE_BMLAYERCOLLECTION_OF_CLASS.match(
                dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(
                    f"`bmesh.types.BMLayerCollection`[`{s}`]"
                )]
        # [Ex] tuple of mathutils.Vector's
        if m := REGEX_MATCH_DATA_TYPE_TUPLE_OF_VALUE.match(dtype_str):
            s = self._parse_custom_data_type(
                m.group(1), uniq_full_names, uniq_module_names, module_name)
            if s:
                return [make_data_type_node(f"tuple[`{s}`, ...]")]

        # [Ex] (Vector, Quaternion, Vector)  # noqa: ERA001
        if m1 := REGEX_MATCH_DATA_TYPE_START_AND_END_WITH_PARENTHESES.match(
                dtype_str):
            splited = m1.group(1).split(",")
            dtypes = []
            for raw_sp in splited:
                sp = raw_sp.strip()
                if m2 := REGEX_MATCH_DATA_TYPE_DOT_COMMA.match(sp):
                    s = self._parse_custom_data_type(
                        m2.group(1), uniq_full_names, uniq_module_names,
                        module_name)
                    if s:
                        dtypes.append(f"`{s}`")
            if len(dtypes) != 0:
                elem_str = ", ".join(dtypes)
                return [make_data_type_node(f"tuple[{elem_str}]")]

        if dtype_str == "dict with string keys":
            return [make_data_type_node("dict[str, typing.Any]")]
        if dtype_str == "iterable object":
            return [make_data_type_node("list")]
        if m := REGEX_MATCH_DATA_TYPE_LIST_OR_DICT_OR_SET_OR_TUPLE.match(
                dtype_str):
            return [make_data_type_node(f"{m.group(1)}")]

        # [Ex] bpy.types.Struct subclass
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

        # [Ex] CLIP_OT_add_marker
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
        description_str: str | None = None,
        additional_info: dict[str, Any] | None = None
    ) -> tuple[list[str], str]:

        def may_have_rna_based_options(module_name: str) -> bool:
            if module_name.startswith("bpy."):
                if module_name == "bpy.utils":
                    return False
                if module_name == "bpy.path":
                    return False
                return True

            return False

        if may_have_rna_based_options(module_name):
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
                                   f"Unknown option '{opt}' is found from "
                                   f"{dtype_str}")

                # If there is unknown parameter options, we don't strip them
                # from original string.
                if not has_unknown_option:
                    option_results.extend(options)

                    # Strip the unused string to speed up the later parsing
                    # process.
                    stripped = _REGEX_DATA_TYPE_OPTION_STR.sub("", dtype_str)
                    output_log(LOG_LEVEL_DEBUG,
                               f"Data type is stripped: "
                               f"{dtype_str} -> {stripped}")
                    dtype_str = stripped

            # If readonly is specified, we should add never none as well.
            if "readonly" in option_results:
                option_results.append("never none")

            option_results = sorted(set(option_results))

            # Active object can accept None.
            if variable_kind in ('CONST', 'CLS_ATTR'):
                if additional_info["data_name"].startswith("active"):
                    if "never none" in option_results:
                        option_results.remove("never none")
                    option_results.append("accept none")

            return option_results, dtype_str

        is_never_none = True
        is_optional = False

        if m := _REGEX_DATA_TYPE_OPTION_END_WITH_NONE.search(dtype_str):
            stripped = _REGEX_DATA_TYPE_OPTION_END_WITH_NONE.sub("", dtype_str)
            output_log(LOG_LEVEL_DEBUG,
                       f"Data type is stripped: {dtype_str} -> {stripped}")
            dtype_str = stripped
            is_never_none = False

        if description_str is not None:
            if m := _REGEX_DATA_TYPE_OPTION_OPTIONAL.search(description_str):
                # If default value is not None, data type does not need
                # optional.
                is_never_none = (
                    additional_info["default_value"] not in ("", "None")
                )
                is_optional = True

        # If default value is None, data type must accept None.
        if is_never_none:
            if additional_info is not None:
                if "default_value" in additional_info:
                    if additional_info["default_value"] == "None":
                        is_never_none = False

        options = []
        if is_never_none:
            options.append("never none")
        if is_optional:
            options.append("optional")

        return sorted(options), dtype_str

    # pylint: disable=W0102
    def _get_refined_data_type(
        self, dtype_str: str, module_name: str,
        variable_kind: str,
        is_pointer_prop: bool = False,
        description_str: str | None = None,
        additional_info: dict[str, Any] | None = None,
        original_options: list[str] = []  # noqa: B006
    ) -> list[DataTypeNode]:

        assert variable_kind in (
            'FUNC_ARG', 'FUNC_RET', 'CONST', 'CLS_ATTR', 'CLS_BASE')

        options, dtype_str_changed = self._get_data_type_options(
            dtype_str, module_name, variable_kind,
            is_pointer_prop=is_pointer_prop,
            description_str=description_str, additional_info=additional_info)

        result = self._get_refined_data_type_internal(
            dtype_str_changed, module_name, variable_kind,
            additional_info=additional_info)

        def is_cls_attr_in_never_none_blacklist(
                class_full_name: str, attr_name: str) -> bool:
            blacklist = (
                "bpy.types.ID.library"
            )
            return f"{class_full_name}.{attr_name}" in blacklist

        # Add options.
        for r in result:
            option_results = original_options.copy()
            option_results.extend(options.copy())
            if "option" in r.attributes:
                option_results.extend(r.attributes["option"].split(","))

            # list object will not be None.
            if (variable_kind in ('CLS_ATTR', 'CONST') and
                    "never none" not in option_results):
                if _REGEX_DATA_TYPE_STARTS_WITH_COLLECTION.match(r.to_string()):
                    option_results.append("never none")

            # If data type is bpy.types.Context, it will be never None.
            if r.to_string() == "bpy.types.Context":
                option_results.append("never none")

            if variable_kind == 'CLS_ATTR':
                if is_cls_attr_in_never_none_blacklist(
                        additional_info["self_class"],
                        additional_info["data_name"]):
                    option_results.append("never none")

            option_results = sorted(set(option_results))
            r.attributes["option"] = ",".join(option_results)

        output_log(
            LOG_LEVEL_DEBUG,
            f"Result of refining (kind={variable_kind}): "
            f"{dtype_str} -> {', '.join(r.to_string() for r in result)}")

        return result

    def _get_refined_data_type_splited(
        self, dtype_str: str, module_name: str,
        variable_kind: str, additional_info: dict[str, Any] | None = None
    ) -> list[DataTypeNode]:

        dtype_str = dtype_str.strip()

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        # Handle Python typing syntax.
        if m := _REGEX_DATA_TYPE_MODIFIER_TYPES.match(dtype_str):
            modifier = m.group(1)
            if modifier is None:
                modifier = ""
            elements = split_string_by_comma(m.group(2), False)
            elm_dtype_nodes: list[list[DataTypeNode]] = []
            for elm in elements:
                dtype_nodes = self._get_refined_data_type_internal(
                    elm, module_name, variable_kind, additional_info)
                if len(dtype_nodes) >= 1:
                    elm_dtype_nodes.append(dtype_nodes)

            pydoc_to_typing_annotation = {
                "Sequence": "collections.abc.Sequence",
                "Callable": "collections.abc.Callable",
            }

            modifier = pydoc_to_typing_annotation.get(modifier, modifier)

            new_dtype_node = DataTypeNode()
            if len(elm_dtype_nodes) >= 1:
                append_child(new_dtype_node, nodes.Text(f"{modifier}["))
                for i, dtype_nodes in enumerate(elm_dtype_nodes):
                    for j, dtype_node in enumerate(dtype_nodes):
                        for child in dtype_node.children:
                            append_child(new_dtype_node, child)
                        if j != len(dtype_nodes) - 1:
                            append_child(new_dtype_node, nodes.Text(" | "))
                    if i != len(elm_dtype_nodes) - 1:
                        append_child(new_dtype_node, nodes.Text(", "))
                append_child(new_dtype_node, nodes.Text("]"))
            else:
                append_child(new_dtype_node, nodes.Text(modifier))
            return [new_dtype_node]

        # Ex. string, default "", -> string
        if m := REGEX_MATCH_DATA_TYPE_WITH_DEFAULT.match(dtype_str):
            dtype_str = m.group(1)

        # Ex. (Quaternion, float) pair
        if m := REGEX_MATCH_DATA_TYPE_PAIR.match(dtype_str):
            sp = m.group(1).split(",")
            dtypes: list[DataTypeNode] = []
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
            dtype_str, uniq_full_names, uniq_module_names,
            module_name, variable_kind, additional_info)
        if result is not None:
            return result

        if any(keyword in dtype_str for keyword in [" | ", " or ", ","]):
            splist = REGEX_SPLIT_OR.split(dtype_str)

            output_log(LOG_LEVEL_DEBUG, f"Split data type refining: {splist}")

            dtypes = []
            for sp in splist:
                s = sp.strip()
                result = self._get_refined_data_type_fast(
                    s, uniq_full_names, uniq_module_names,
                    module_name, variable_kind, additional_info)
                if result is not None:
                    dtypes.extend(result)
            return dtypes
        return []

    def _get_refined_data_type_internal(
        self, dtype_str: str, module_name: str,
        variable_kind: str, additional_info: dict[str, Any] | None = None
    ) -> list[DataTypeNode]:

        dtype_str = dtype_str.strip()

        dtype_strs_splited = split_string_by_bar(dtype_str)
        if len(dtype_strs_splited) == 0:
            return [make_data_type_node("typing.Any")]

        dtype_nodes = []
        for ds in dtype_strs_splited:
            dtypes = self._get_refined_data_type_splited(
                ds, module_name, variable_kind, additional_info)
            dtype_nodes.extend(dtypes)

        return dtype_nodes

    def _parse_from_description(
        self, module_name: str, dtype_nodes: list[DataTypeNode],
        description_str: str | None = None,
        additional_info: dict[str, Any] | None = None
    ) -> tuple[list[DataTypeNode], bool]:

        if description_str is None:
            return [], False

        uniq_full_names = self._entry_points_cache["uniq_full_names"]
        uniq_module_names = self._entry_points_cache["uniq_module_names"]

        if description_str == "An instance of this object.":
            s = self._parse_custom_data_type(
                additional_info["self_class"], uniq_full_names,
                uniq_module_names, module_name)
            return [make_data_type_node(f"`{s}`")], False

        if REGEX_MATCH_DESCRIPTION_ENUMERATOR_IN.match(description_str) or \
                REGEX_MATCH_DESCRIPTION_TYPE_IN.search(description_str):
            is_set = False
            for dtype_node in dtype_nodes:
                if dtype_node.to_string() == "set":
                    is_set = True
                    break

            if is_set:
                enum_literal_type = get_rna_enum_name(description_str)
                dtype_node = DataTypeNode()
                append_child(dtype_node, nodes.Text("set["))
                append_child(dtype_node,
                             EnumRef(text=f"bpy.typing.{enum_literal_type}"))
                append_child(dtype_node, nodes.Text("]"))
                return [dtype_node], True

            enum_literal_type = get_rna_enum_name(description_str)
            dtype_node = DataTypeNode()
            append_child(dtype_node,
                         EnumRef(text=f"bpy.typing.{enum_literal_type}"))
            return [dtype_node], True

        return [], False

    def _refine(self, document: nodes.document) -> None:
        def refine(dtype_list_node: DataTypeListNode, module_name: str,
                   variable_kind: str, description_str: str | None = None,
                   additional_info: dict[str, Any] | None = None) -> None:
            dtype_nodes = find_children(dtype_list_node, DataTypeNode)
            new_dtype_nodes = []

            parsed_dtype_nodes, skip_parse_dtype_node = \
                self._parse_from_description(
                    module_name, dtype_nodes, description_str=description_str,
                    additional_info=additional_info)
            new_dtype_nodes.extend(parsed_dtype_nodes)

            if skip_parse_dtype_node:
                for dtype_node in dtype_nodes:
                    dtype_list_node.remove(dtype_node)
                for node in new_dtype_nodes:
                    dtype_list_node.append_child(node)
                return

            for dtype_node in dtype_nodes:
                mod_options = []
                skip_refine = False
                if "mod-option" in dtype_node.attributes:
                    mod_options: list[str] = [
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
                        if class_ref.to_string() in ("bpy_prop_collection",
                                                     "bpy_prop_array"):
                            is_pointer_prop = False
                            break
                        # Accept like :class:`Object`
                        if (module_name == "bpy.types" and
                                class_ref.to_string().count(".") == 0):
                            continue
                        if not class_ref.to_string().startswith("bpy.types"):
                            is_pointer_prop = False
                            break

                options = []
                if "option" in dtype_node.attributes:
                    options = dtype_node.attributes["option"].split(",")
                new_dtype_nodes.extend(self._get_refined_data_type(
                    dtype_node.astext(), module_name, variable_kind,
                    is_pointer_prop=is_pointer_prop,
                    description_str=description_str,
                    additional_info=additional_info,
                    original_options=options))
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
                    default_value_node = arg_node.element(DefaultValueNode)
                    dtype_list_node = arg_node.element(DataTypeListNode)
                    refine(dtype_list_node, module_name, 'FUNC_ARG',
                           description_str=description,
                           additional_info={
                               "self_class": f"{module_name}.{class_name}",
                               "default_value": default_value_node.astext(),
                           })

                return_node = func_node.element(FunctionReturnNode)
                description = return_node.element(DescriptionNode).astext()
                dtype_list_node = return_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'FUNC_RET',
                       description_str=description,
                       additional_info={
                           "self_class": f"{module_name}.{class_name}"
                       })

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
            base_class_nodes = find_children(
                base_class_list_node, BaseClassNode)
            for base_class_node in base_class_nodes:
                dtype_list_node = base_class_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'CLS_BASE')

        func_nodes = find_children(document, FunctionNode)
        for func_node in func_nodes:
            arg_list_node = func_node.element(ArgumentListNode)
            arg_nodes = find_children(arg_list_node, ArgumentNode)
            for arg_node in arg_nodes:
                description = arg_node.element(DescriptionNode).astext()
                default_value_node = arg_node.element(DefaultValueNode)
                dtype_list_node = arg_node.element(DataTypeListNode)
                refine(dtype_list_node, module_name, 'FUNC_ARG',
                       description_str=description,
                       additional_info={
                           "default_value": default_value_node.astext(),
                       })

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
    def name(cls: type[Self]) -> str:
        return "data_type_refiner"

    def apply(self, **kwargs: dict) -> None:  # noqa: ARG002
        if self._entry_points is None:
            self._entry_points = self._build_entry_points(self.documents)

        self._entry_points_cache["uniq_full_names"] = {
            e.fullname() for e in self._entry_points}
        self._entry_points_cache["uniq_module_names"] = {
            e.module for e in self._entry_points}

        for document in self.documents:
            self._refine(document)
