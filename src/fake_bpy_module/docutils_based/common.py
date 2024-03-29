import re
from typing import List, TypeVar, Type
from docutils import nodes


_ARG_LIST_1_REGEX = re.compile(r"^([a-zA-Z0-9_]+[^=]+?)\[,(.*)\]$")
_ARG_LIST_2_REGEX = re.compile(r"^\[([a-zA-Z0-9_]+)\]$")

T = TypeVar("T", bound=nodes.Node)


def find_children(node: nodes.Node, node_type: Type[T]) -> List[T]:
    result: List[T] = []
    for child in node.children:
        if isinstance(child, node_type):
            result.append(child)
    return result


def get_first_child(node: nodes.Node, node_type: Type[T]) -> T:
    for child in node.children:
        if isinstance(child, node_type):
            return child
    return None


def append_child(node: nodes.Node, item: nodes.Node) -> nodes.Node:
    node.insert(len(node.children), item)
    return item


# pylint: disable=R0912,R0915
def split_string_by_comma(line: str) -> list:
    level = 0
    params = []
    current = ""
    line_to_parse = line

    # Handle case "arg1[, arg2]" -> "arg1, arg2"
    m = _ARG_LIST_1_REGEX.match(line_to_parse)
    if m:
        line_to_parse = f"{m.group(1)},{m.group(2)}"
    # Handle case "[arg1]"
    m = _ARG_LIST_2_REGEX.match(line_to_parse)
    if m:
        line_to_parse = f"{m.group(1)}"

    for c in line_to_parse:
        if c in ("(", "{", "["):
            level += 1
        elif c in (")", "}", "]"):
            level -= 1
            if level < 0:
                raise ValueError(
                    f"Level must be >= 0 but {level} (Line: {line})")
        if level == 0 and c == ",":
            params.append(current)
            current = ""
        else:
            current += c

    if level != 0:
        raise ValueError(
            f"Level must be == 0 but {level} (Line: {line})")

    if current != "":
        params.append(current)

    return params
