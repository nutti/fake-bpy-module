import os
import re
from typing import TypeVar

from docutils import nodes

_ARG_LIST_WITH_BRACE_REGEX = re.compile(r"^\[([a-zA-Z0-9_,]+)\]$")

T = TypeVar("T", bound=nodes.Node)

LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_NOTICE = 2
LOG_LEVEL_WARN = 3
LOG_LEVEL_ERR = 4

LOG_LEVEL = LOG_LEVEL_WARN


def check_os() -> str:
    if os.name == "nt":
        return "Windows"
    if os.name == "posix":
        return "Linux"
    return ""


def output_log(level: int, message: str) -> None:
    LOG_LEVEL_LABEL: list[str] = ["DEBUG", "INFO", "NOTICE", "WARN", "ERR"]  # noqa: N806
    if level >= LOG_LEVEL:
        print(f"[{LOG_LEVEL_LABEL[level]}] {message}")


def remove_unencodable(str_: str) -> str:
    return str_.replace("\xb2", "").replace("\u2013", "").replace("\u2019", "")


def find_children(node: nodes.Node, node_type: type[T]) -> list[T]:
    result: list[T] = [child
                       for child in node.children
                       if isinstance(child, node_type)]

    return result


def get_first_child(node: nodes.Node, node_type: type[T]) -> T:
    for child in node.children:
        if isinstance(child, node_type):
            return child
    return None


def append_child(node: nodes.Node, item: nodes.Node) -> nodes.Node:
    node.insert(len(node.children), item)
    return item


# pylint: disable=R0912,R0915
def split_string_by(line: str, separator: str) -> list:
    level = 0
    splited = []
    current = ""
    line_to_parse = line

    # Handle case "arg1[, arg2]" -> "arg1, arg2"
    sp = line_to_parse.split(f"[{separator}")
    sub_strings = []
    for i, s in enumerate(sp):
        if i == 0:
            sub_strings.append(s)
        else:
            assert s[-1] == "]"
            sub_strings.append(s[:-1])
    line_to_parse = separator.join(sub_strings)

    # Handle case "[arg1]"
    m = _ARG_LIST_WITH_BRACE_REGEX.match(line_to_parse)
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
        if level == 0 and c == separator:
            splited.append(current)
            current = ""
        else:
            current += c

    if level != 0:
        raise ValueError(
            f"Level must be == 0 but {level} (Line: {line})")

    if current != "":
        splited.append(current)

    return [s.strip() for s in splited]


def split_string_by_comma(line: str) -> list:
    return split_string_by(line, ",")


def split_string_by_bar(line: str) -> list:
    return split_string_by(line, "|")
