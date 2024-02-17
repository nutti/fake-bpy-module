import ast
import re
from docutils.parsers import rst
from docutils import nodes

from .nodes import (
    ModuleNode,
    ClassNode,
    DataNode,
    AttributeNode,
    AttributeListNode,
    FunctionNode,
    FunctionListNode,
    ArgumentNode,
    ArgumentListNode,
    DefaultValueNode,
    FunctionReturnNode,
    NameNode,
    DescriptionNode,
    DataTypeNode,
    DataTypeListNode,

    CodeNode,
)

from .. import configuration


def append_child(node: nodes.Node, item: nodes.Node):
    node.insert(len(node.children), item)


class ModuleDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        paragraph_node = nodes.paragraph()
        self.state.nested_parse(
            self.content, self.content_offset, paragraph_node)

        module_node = ModuleNode()

        # Get module name.
        module_name = self.arguments[0]
        if configuration.get_target() == "blender":
            if configuration.get_target_version() == "2.90":
                if module_name.startswith("bpy.types."):
                    module_name = module_name[:module_name.rfind(".")]
            elif configuration.get_target_version() in [
                    "2.91", "2.92", "2.93",
                    "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6",
                    "4.0",
                    "latest"]:
                if module_name == "bpy.data":
                    module_name = "bpy"
        append_child(module_node, NameNode(text=module_name))

        # Get all descriptions.
        desc_str = ""
        for child in paragraph_node.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        desc_node = DescriptionNode(text=desc_str)
        append_child(module_node, desc_node)

        return [module_node]


class ClassDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    _CLASS_NAME_REGEX = re.compile(r"([a-zA-Z0-9_]+)(\([a-zA-Z0-9_,]+\))*")

    def run(self):
        paragraph_node = nodes.paragraph()
        self.state.nested_parse(
            self.content, self.content_offset, paragraph_node)

        class_node = ClassNode()

        # Get class name.
        # TODO: Parse argument to create __init__ method
        #       ex. class GPUBatch(type, buf, elem=None):
        if m := self._CLASS_NAME_REGEX.match(self.arguments[0]):
            content = m.group(1)
            append_child(class_node, NameNode(text=content))

        # Get all descriptions.
        desc_str = ""
        for child in paragraph_node.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        desc_node = DescriptionNode(text=desc_str)
        append_child(class_node, desc_node)

        # Get all attributes and methods.
        attr_list_node = AttributeListNode()
        method_list_node = FunctionListNode()
        for child in paragraph_node.children:
            if isinstance(child, AttributeNode):
                append_child(attr_list_node, child)
            elif isinstance(child, DataNode):
                attr_node = AttributeNode()
                for node in child.children:
                    append_child(attr_node, node)
                append_child(attr_list_node, attr_node)
            elif isinstance(child, FunctionNode):
                append_child(method_list_node, child)
        append_child(class_node, attr_list_node)
        append_child(class_node, method_list_node)

        return [class_node]


class DataDirective(rst.Directive):
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        "noindex": rst.directives.unchanged
    }

    node_class = DataNode

    _DATA_NAME_REGEX = re.compile(r"([0-9a-zA-Z_]+)")

    def run(self):
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        node = self.node_class()

        # TODO: parse "(Deprecated)" from the optional argument.

        # Get attribute name.
        if m := self._DATA_NAME_REGEX.match(self.arguments[0]):
            name = NameNode(text=m.group(1))
            append_child(node, name)

        # Get all descriptions.
        desc_str = ""
        for child in paragraph.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        desc_node = DescriptionNode(text=desc_str)
        append_child(node, desc_node)

        # Get all field values.
        field_lists: nodes.field_list = paragraph.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                if fname_node.astext() == "type":
                    dtype_list = DataTypeListNode()
                    dtype = DataTypeNode(text=fbody_node.astext())
                    append_child(dtype_list, dtype)
                    append_child(node, dtype_list)

        return [node]


class AttributeDirective(DataDirective):
    node_class = AttributeNode


class FunctionDirective(rst.Directive):
    required_arguments = 1
    has_content = True
    final_argument_whitespace = True

    _ARG_LIST_1_REGEX = re.compile(r"^([a-zA-Z0-9_]+[^=]+?)\[,(.*)\]$")
    _ARG_LIST_2_REGEX = re.compile(r"^\[([a-zA-Z0-9_]+)\]$")
    _ARG_REPLACE_1_REGEX = re.compile(r"<class '([a-zA-Z]+?)'>")
    _ARG_REPLACE_2_REGEX = re.compile(r"<built-in function ([a-zA-Z]+?)>")
    _ARG_REPLACE_3_REGEX = re.compile(r"\\")
    _ARG_LIST_FROM_FUNC_DEF_REGEX = re.compile(r"([a-zA-Z0-9_]+)\s*\((.*)\)")
    _FUNC_DEF_REGEX = re.compile(r"([a-zA-Z0-9_]+)\s*\((.*)\)")
    _DEPRECATED_REGEX = re.compile(r"\s*\(Deprecated\)$")
    _ARG_FIELD_REGEX = re.compile(r"(arg|param|type)\s+([0-9a-zA-Z_]+)")
    _RETURN_FIELD_REGEX = re.compile(r"(return|rtype)")

    def _parse_parameters(self, line: str) -> list:
        level = 0
        params = []
        current = ""
        line_to_parse = line

        # Handle Case:
        #   "arg1[, arg2]" -> "arg1, arg2"
        m = self._ARG_LIST_1_REGEX.match(line_to_parse)
        if m:
            line_to_parse = f"{m.group(1)},{m.group(2)}"
        # Handle Case:
        #   "[arg1]"
        m = self._ARG_LIST_2_REGEX.match(line_to_parse)
        if m:
            line_to_parse = f"{m.group(1)}"

        for c in line_to_parse:
            if c in ("(", "{", "["):
                level += 1
            elif c in (")", "}", "]"):
                level -= 1
                if level < 0:
                    raise ValueError(f"Level must be >= 0 but {level} "
                                     f"(Line: {line})")
            if level == 0 and c == ",":
                params.append(current.strip())
                current = ""
            else:
                current += c

        if level != 0:
            raise ValueError(f"Level must be == 0 but {level} (Line: {line})")

        if current != "":
            params.append(current.strip())

        return params

    def _parse_function_def(self, content) -> list:
        content = self._ARG_REPLACE_1_REGEX.sub("\\1", content)
        content = self._ARG_REPLACE_2_REGEX.sub("\\1", content)
        content = self._ARG_REPLACE_3_REGEX.sub("", content)
        content.strip()

        m = self._ARG_LIST_FROM_FUNC_DEF_REGEX.search(content)
        name = m.group(1)
        params = self._parse_parameters(m.group(2))

        # (test=DirectivesTest.test_invalid_function_arg_order)
        # Handle case:
        #   function_1(arg_1, arg_2, arg_3='NONE', arg_4=True, arg_5): pass
        fixed_params = []
        required_named_argument = False
        for p in params:
            sp = p.split("=")
            assert len(sp) in (1, 2)
            if len(sp) == 1:
                if required_named_argument:
                    fixed_params.append(f"{p}=None")
                else:
                    fixed_params.append(p)
            elif len(sp) == 2:
                required_named_argument = True
                fixed_params.append(p)

        content = f"def {name}({', '.join(fixed_params)}): pass"

        return content

    # pylint: disable=R0911
    def _parse_default_value(self, expr: ast.expr):
        if expr is None:
            return None

        if isinstance(expr, ast.Constant):
            if isinstance(expr.value, str):
                return f"\"{expr.value}\""
            if expr.value is None:
                return "None"
            return expr.value
        if isinstance(expr, ast.Name):
            return "None"   # TODO: Should be "expr.id"
        if isinstance(expr, ast.List):
            return [self._parse_default_value(e) for e in expr.elts]
        if isinstance(expr, ast.Tuple):
            return tuple((self._parse_default_value(e) for e in expr.elts))
        if isinstance(expr, ast.Set):
            return {self._parse_default_value(e) for e in expr.elts}
        if isinstance(expr, ast.Dict):
            return {
                self._parse_default_value(k): self._parse_default_value(v)
                for k, v in zip(expr.keys, expr.values)}
        if isinstance(expr, ast.UnaryOp):
            if isinstance(expr.op, ast.USub):
                operand = self._parse_default_value(expr.operand)
                if isinstance(operand, (float, int)):
                    return -operand     # pylint: disable=E1130
                if isinstance(operand, str):
                    return "None"
                raise NotImplementedError(
                    f"{type(operand)} is not supported as an operand of USub")
            raise NotImplementedError(
                f"{type(expr.op)} is not supported as an UnaryOp")
        if isinstance(expr, ast.BinOp):
            return "None"   # TODO
        if isinstance(expr, ast.Subscript):
            value = self._parse_default_value(expr.value)
            slice_ = self._parse_default_value(expr.slice)
            return f"{value}[{slice_}]"
        if isinstance(expr, ast.Call):
            func = self._parse_default_value(expr.func)
            args = ', '.join([str(self._parse_default_value(arg))
                              for arg in expr.args])
            return f"{func}({args})"
        if isinstance(expr, ast.Attribute):
            return "None"   # TODO: Should be "expr.attr"
        raise NotImplementedError(
            f"{type(expr)} is not supported as a default value")

    def run(self):
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        func_defs = []
        fdef_str: str = ""
        for fdef in self.arguments[0].split("\n"):
            if fdef[-1] == "\\":
                fdef_str += fdef[:-1]
            else:
                fdef_str += fdef
                ma = self._FUNC_DEF_REGEX.search(fdef_str)
                if ma:
                    # TODO: Mark a deprecated flag.
                    fdef_str = self._DEPRECATED_REGEX.sub("", fdef_str)
                    func_defs.append(self._parse_function_def(fdef_str))
                else:
                    # (test=DirectivesTest.test_invalid_function)
                    # Handle case:
                    #   .. function:: function_1()
                    #      function_1 description
                    append_child(paragraph, nodes.paragraph(text=fdef_str))
                fdef_str = ""

        func_nodes: list = []
        # pylint: disable=R1702
        for fdef in func_defs:
            func_node = FunctionNode(function_type=self.name)

            m: ast.Module = ast.parse(fdef)
            func_def: ast.FunctionDef = m.body[0]

            # Get function name.
            append_child(func_node, NameNode(text=func_def.name))

            # Get all descriptions.
            desc_str = ""
            for child in paragraph.children:
                if isinstance(child, nodes.paragraph):
                    desc_str += child.astext()
            desc_node = DescriptionNode(text=desc_str)
            append_child(func_node, desc_node)

            func_nodes.append(func_node)

            # Get function signature.
            arg_list_node = ArgumentListNode()
            for i, arg in enumerate(func_def.args.args):
                arg_node = ArgumentNode(argument_type="arg")
                append_child(arg_node, NameNode(text=arg.arg))
                default_start = \
                    len(func_def.args.args) - len(func_def.args.defaults)
                if i >= default_start:
                    default = func_def.args.defaults[i - default_start]
                    default_value = self._parse_default_value(default)
                    if default_value is not None:
                        append_child(
                            arg_node, DefaultValueNode(text=default_value))
                append_child(arg_list_node, arg_node)

            if func_def.args.vararg:
                arg_node = ArgumentNode(argument_type="vararg")
                append_child(
                    arg_node, NameNode(text=func_def.args.vararg.arg))
                append_child(arg_list_node, arg_node)

            for i, arg in enumerate(func_def.args.kwonlyargs):
                arg_node = ArgumentNode(argument_type="kwonlyarg")
                append_child(arg_node, NameNode(text=arg.arg))
                default = func_def.args.kw_defaults[i]
                default_value = self._parse_default_value(default)
                if default_value is not None:
                    append_child(
                        arg_node, DefaultValueNode(text=default_value))
                append_child(arg_list_node, arg_node)

            if func_def.args.kwarg:
                arg_node = ArgumentNode(argument_type="kwarg")
                append_child(arg_node, NameNode(text=func_def.args.kwarg.arg))
                append_child(arg_list_node, arg_node)

            append_child(func_node, arg_list_node)

            # Get signature details
            field_lists: nodes.field_list = paragraph.findall(
                nodes.field_list)
            for field_list in field_lists:
                for field in field_list:
                    fname_node, fbody_node = field.children
                    m = self._ARG_FIELD_REGEX.match(fname_node.astext())
                    if m:
                        arg_name = m.group(2)
                        arg_node: ArgumentNode = None
                        for child in arg_list_node.children:
                            n = next(child.findall(NameNode))
                            if n.astext() == arg_name:
                                arg_node = n.parent
                                break
                        if arg_node:
                            if m.group(1) in ("arg", "param"):
                                desc_node = DescriptionNode(
                                    text=fbody_node.astext())
                                append_child(arg_node, desc_node)
                            elif m.group(1) == "type":
                                data_type_list_node = DataTypeListNode(
                                    "",
                                    DataTypeNode(text=fbody_node.astext()))
                                append_child(arg_node, data_type_list_node)
                    m = self._RETURN_FIELD_REGEX.match(fname_node.astext())
                    if m:
                        r = list(func_node.findall(FunctionReturnNode))
                        if len(r) == 0:
                            func_ret_node = FunctionReturnNode()
                            append_child(func_node, func_ret_node)
                        else:
                            func_ret_node = r[0]
                        if m.group(1) == "return":
                            desc_node = DescriptionNode(
                                text=fbody_node.astext())
                            append_child(func_ret_node, desc_node)
                        elif m.group(1) == "rtype":
                            data_type_list_node = DataTypeListNode(
                                "", DataTypeNode(text=fbody_node.astext()))
                            append_child(func_ret_node, data_type_list_node)

        return func_nodes


class DocumentDirective(rst.Directive):
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        content = " ".join(self.arguments)
        append_child(paragraph, nodes.Text(content))

        return [paragraph]


class LiteralIncludeDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "lines": rst.directives.unchanged
    }

    def run(self):
        path: str = self.arguments[0]
        code_node: CodeNode = CodeNode(text=path)

        return [code_node]


class NopDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        return []


def register_directives():
    rst.directives.register_directive("module", ModuleDirective)
    rst.directives.register_directive("currentmodule", ModuleDirective)
    rst.directives.register_directive("class", ClassDirective)
    rst.directives.register_directive("function", FunctionDirective)
    rst.directives.register_directive("method", FunctionDirective)
    rst.directives.register_directive("classmethod", FunctionDirective)
    rst.directives.register_directive("staticmethod", FunctionDirective)
    rst.directives.register_directive("attribute", AttributeDirective)
    rst.directives.register_directive("property", AttributeDirective)
    rst.directives.register_directive("data", DataDirective)
    rst.directives.register_directive("DATA", DataDirective)

    rst.directives.register_directive(
        "literalinclude", LiteralIncludeDirective)
    rst.directives.register_directive("seealso", DocumentDirective)
    rst.directives.register_directive("hlist", DocumentDirective)
    rst.directives.register_directive("toctree", DocumentDirective)
    rst.directives.register_directive("rubric", DocumentDirective)
    rst.directives.register_directive("deprecated", DocumentDirective)

    rst.directives.register_directive("include", NopDirective)
