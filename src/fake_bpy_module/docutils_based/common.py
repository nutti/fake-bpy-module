import re


_ARG_LIST_1_REGEX = re.compile(r"^([a-zA-Z0-9_]+[^=]+?)\[,(.*)\]$")
_ARG_LIST_2_REGEX = re.compile(r"^\[([a-zA-Z0-9_]+)\]$")


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
