import ast
import re
from typing import ClassVar

from docutils import nodes
from docutils.parsers import rst

from fake_bpy_module import config
from fake_bpy_module.utils import (
    append_child,
    find_children,
    split_string_by_comma,
)

from .nodes import (
    ArgumentListNode,
    ArgumentNode,
    AttributeListNode,
    AttributeNode,
    BaseClassListNode,
    BaseClassNode,
    ClassNode,
    CodeNode,
    DataNode,
    DataTypeListNode,
    DataTypeNode,
    DefaultValueNode,
    DescriptionNode,
    EnumItemListNode,
    EnumItemNode,
    EnumNode,
    FunctionListNode,
    FunctionNode,
    FunctionReturnNode,
    ModTypeNode,
    ModuleNode,
    NameNode,
    make_data_type_node,
)

_ARG_REPLACE_1_REGEX = re.compile(r"<class '([a-zA-Z]+?)'>")
_ARG_REPLACE_2_REGEX = re.compile(r"<built-in function ([a-zA-Z]+?)>")
_ARG_REPLACE_3_REGEX = re.compile(r"\\")
_ARG_LIST_FROM_FUNC_DEF_REGEX = re.compile(r"([a-zA-Z0-9_]+)\s*\((.*)\)")


def parse_function_def(content: str) -> str:
    content = _ARG_REPLACE_1_REGEX.sub("\\1", content)
    content = _ARG_REPLACE_2_REGEX.sub("\\1", content)
    content = _ARG_REPLACE_3_REGEX.sub("", content)
    content.strip()

    m = _ARG_LIST_FROM_FUNC_DEF_REGEX.search(content)
    name = m.group(1)
    params = split_string_by_comma(m.group(2))

    # (test=DirectivesTest.test_invalid_function_arg_order)
    # Handle case:
    #   function_1(arg_1, arg_2, arg_3='NONE', arg_4=True, arg_5): pass
    fixed_params = []
    required_named_argument = False
    for param in params:
        p = param.strip()
        sp = p.split("=")
        assert len(sp) in (1, 2), f"{p} has length {len(sp)}"
        if len(sp) == 1:
            if required_named_argument:
                if p == "*":
                    required_named_argument = False
                if p.startswith("*"):
                    fixed_params.append(p)
                else:
                    fixed_params.append(f"{p}=None")
            else:
                fixed_params.append(p)
        elif len(sp) == 2:
            required_named_argument = True
            fixed_params.append(p)

    # Handle case:
    #   function_1(async=False): pass
    invalid_param_names = ["async"]
    fixed_params_tmp = fixed_params
    fixed_params = []
    for p in fixed_params_tmp:
        sp = p.split("=")
        if len(sp) == 1:
            if p in invalid_param_names:
                fixed_params.append(f"{p}_")
            else:
                fixed_params.append(p)
        elif len(sp) == 2:
            if sp[0] in invalid_param_names:
                fixed_params.append(f"{sp[0]}_={sp[1]}")
            else:
                fixed_params.append(p)

    return f"def {name}({', '.join(fixed_params)}): pass"


# pylint: disable=R0911
def parse_func_arg_default_value(expr: ast.expr) -> str | None:
    if expr is None:
        return None

    if isinstance(expr, ast.Constant):
        if isinstance(expr.value, str):
            return f'"{expr.value}"'
        if expr.value is None:
            return "None"
        return expr.value
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.List):
        return (
            f"""[{', '.join(str(parse_func_arg_default_value(e))
            for e in expr.elts)}]"""
            if len(expr.elts) > 0
            else "[]"
        )
    if isinstance(expr, ast.Tuple):
        return (
            f"""({', '.join(str(parse_func_arg_default_value(e))
            for e in expr.elts)})"""
            if len(expr.elts) > 0
            else "()"
        )
    if isinstance(expr, ast.Set):
        return (
            f"""{{{', '.join(str(parse_func_arg_default_value(e))
            for e in expr.elts)}}}"""
            if len(expr.elts) > 0
            else "set()"
        )
    if isinstance(expr, ast.Dict):
        return (
            f"""{{{', '.join(
            f'{parse_func_arg_default_value(k)}'
            f':{parse_func_arg_default_value(v)}'
            for k, v in zip(expr.keys, expr.values, strict=False))}}}"""
            if len(expr.keys) > 0
            else "{}"
        )
    if isinstance(expr, ast.UnaryOp):
        if isinstance(expr.op, ast.USub):
            operand = parse_func_arg_default_value(expr.operand)
            if isinstance(operand, float | int):
                return -operand     # pylint: disable=E1130
            if isinstance(operand, str):
                return "None"
            raise NotImplementedError(
                f"{type(operand)} is not supported as an operand of USub")
        raise NotImplementedError(
            f"{type(expr.op)} is not supported as an UnaryOp")
    if isinstance(expr, ast.BinOp):
        return "None"   # TODO: Should return result
    if isinstance(expr, ast.Subscript):
        value = parse_func_arg_default_value(expr.value)
        slice_ = parse_func_arg_default_value(expr.slice)
        return f"{value}[{slice_}]"
    if isinstance(expr, ast.Call):
        func = parse_func_arg_default_value(expr.func)
        args = ', '.join([str(parse_func_arg_default_value(arg))
                          for arg in expr.args])
        return f"{func}({args})"
    if isinstance(expr, ast.Attribute):
        # Support multi-level modules like sys.float_info.max.
        ids = []

        # Get all module ids.
        e = expr
        while hasattr(e, "value"):
            if hasattr(e.value, "attr"):
                ids.append(e.value.attr)
                e = e.value
            elif hasattr(e.value, "id"):
                ids.append(e.value.id)
                e = e.value
            else:
                raise NotImplementedError(f"{type(expr)} is not supported.")
        # ids will be ["float_info", "sys"] here.
        # So, reversing the order is needed.
        ids.reverse()
        ids.append(expr.attr)
        return ".".join(ids)
    raise NotImplementedError(
        f"{type(expr)} is not supported as a default value")


def build_function_node_from_def(fdef: str) -> FunctionNode:
    func_node = FunctionNode.create_template()

    m: ast.Module = ast.parse(fdef)
    func_def: ast.FunctionDef = m.body[0]

    # Get function name.
    func_node.element(NameNode).add_text(func_def.name)

    # Get function signature.
    arg_list_node = func_node.element(ArgumentListNode)
    for i, arg in enumerate(func_def.args.args):
        # Remove self argument which will be added later.
        if i == 0 and arg.arg == "self":
            continue
        arg_node = ArgumentNode.create_template(argument_type="arg")
        arg_node.element(NameNode).add_text(arg.arg)
        default_start = \
            len(func_def.args.args) - len(func_def.args.defaults)
        if i >= default_start:
            default = func_def.args.defaults[i - default_start]
            default_value = parse_func_arg_default_value(default)
            if default_value is not None:
                arg_node.element(DefaultValueNode).add_text(default_value)
        arg_list_node.append_child(arg_node)

    if func_def.args.vararg:
        arg_node = ArgumentNode.create_template(argument_type="vararg")
        arg_node.element(NameNode).add_text(func_def.args.vararg.arg)
        arg_list_node.append_child(arg_node)

    for i, arg in enumerate(func_def.args.kwonlyargs):
        arg_node = ArgumentNode.create_template(argument_type="kwonlyarg")
        arg_node.element(NameNode).add_text(arg.arg)
        default = func_def.args.kw_defaults[i]
        default_value = parse_func_arg_default_value(default)
        if default_value is not None:
            arg_node.element(DefaultValueNode).add_text(default_value)
        arg_list_node.append_child(arg_node)

    if func_def.args.kwarg:
        arg_node = ArgumentNode.create_template(argument_type="kwarg")
        arg_node.element(NameNode).add_text(func_def.args.kwarg.arg)
        arg_list_node.append_child(arg_node)

    return func_node


def parse_data_type(fbody_node: nodes.field_body) -> DataTypeNode:
    if len(fbody_node.children) == 0:
        return DataTypeNode(text=fbody_node.astext())

    para_node = fbody_node.children[0]
    if not isinstance(para_node, nodes.paragraph):
        return DataTypeNode(text=fbody_node.astext())

    dtype = DataTypeNode()
    for c in para_node.children:
        append_child(dtype, c)
    return dtype


class ModuleDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list[ModuleNode]:
        paragraph_node = nodes.paragraph()
        self.state.nested_parse(
            self.content, self.content_offset, paragraph_node)

        module_node = ModuleNode.create_template()

        # Get module name.
        module_name = self.arguments[0]
        if config.get_target() == "blender":
            if config.get_target_version() == "2.90":
                if module_name.startswith("bpy.types."):
                    module_name = module_name[:module_name.rfind(".")]
            elif config.get_target_version() in [
                    "2.91", "2.92", "2.93",
                    "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6",
                    "4.0", "4.1", "4.2",
                    "latest"]:
                if module_name == "bpy.data":
                    module_name = "bpy"
        elif config.get_target() == "upbge":
            if config.get_target_version() in ["latest"]:
                if module_name == "bpy.data":
                    module_name = "bpy"
        module_node.element(NameNode).add_text(module_name)

        # Get all descriptions.
        desc_str = ""
        for child in paragraph_node.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        module_node.element(DescriptionNode).add_text(desc_str)

        return [module_node]


class ClassDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    _CLASS_NAME_WITH_ARGS_REGEX = re.compile(
        r"([a-zA-Z0-9_]+)(\([a-zA-Z0-9_,=. ]+\))")
    _CLASS_NAME_REGEX = re.compile(r"([a-zA-Z0-9_]+)")

    def run(self) -> list[ClassNode]:
        paragraph_node = nodes.paragraph()
        self.state.nested_parse(
            self.content, self.content_offset, paragraph_node)

        class_node = ClassNode.create_template()
        class_name = self.arguments[0]

        # Ex: GPUBatch(type, buf, elem=None): -> GPUBatch
        # TODO: Need to parse class name with arguments to create
        #       __init__ method like __init__(type, buf, elem=None).
        #       We should consider Color(rgb) which will be added by mod file.
        if m := self._CLASS_NAME_WITH_ARGS_REGEX.match(class_name):
            class_name = m.group(1)

        # Get class name.
        # if m := self._CLASS_NAME_WITH_ARGS_REGEX_2.match(class_name):
        if m := self._CLASS_NAME_REGEX.match(class_name):
            content = m.group(1)
            class_node.element(NameNode).add_text(content)

        # Get all descriptions.
        desc_str = ""
        for child in paragraph_node.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        class_node.element(DescriptionNode).add_text(desc_str)

        # Get all attributes and methods.
        base_class_list_node = class_node.element(BaseClassListNode)
        attr_list_node = class_node.element(AttributeListNode)
        method_list_node = class_node.element(FunctionListNode)
        for child in paragraph_node.children:
            if isinstance(child, BaseClassListNode):
                for c in child.children:
                    base_class_list_node.append_child(c.deepcopy())
            elif isinstance(child, AttributeNode):
                attr_list_node.append_child(child)
            elif isinstance(child, DataNode):
                attr_node = AttributeNode()
                for node in child.children:
                    attr_node.append_child(node)
                attr_list_node.append_child(attr_node)
            elif isinstance(child, FunctionNode):
                method_list_node.append_child(child)

        # Get all field values.
        field_lists: nodes.field_list = paragraph_node.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                if fname_node.astext() == "generic-types":
                    class_node.attributes[fname_node.astext()] = \
                        fbody_node.astext()

        return [class_node]


class DataDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    node_class = DataNode

    _DATA_NAME_REGEX = re.compile(r"([0-9a-zA-Z_]+)")
    _OPTION_MODOPTION_FIELD_REFEX = re.compile(r"(mod-option|option)\s*(\S*)")

    def run(self) -> list[DataNode]:
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        node = self.node_class.create_template()

        # Parse "(Deprecated*" from the data name.
        data_name = self.arguments[0]
        index = data_name.rfind("(Deprecated")
        if index != -1:
            node.attributes["deprecated"] = data_name[index:]
            data_name = data_name[0:index]

        # Get attribute name.
        if m := self._DATA_NAME_REGEX.match(data_name):
            node.element(NameNode).add_text(m.group(1))

        # Get all descriptions.
        desc_str = ""
        for child in paragraph.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        node.element(DescriptionNode).add_text(desc_str)

        # Get all field values.
        dtype_list_node = node.element(DataTypeListNode)
        field_lists: nodes.field_list = paragraph.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                if fname_node.astext() == "type":
                    dtype = parse_data_type(fbody_node)
                    dtype_list_node.append_child(dtype)
                elif m := self._OPTION_MODOPTION_FIELD_REFEX.match(
                        fname_node.astext()):
                    for dtype_node in dtype_list_node.findall(DataTypeNode):
                        dtype_node.attributes[m.group(1)] = fbody_node.astext()

        return [node]


class AttributeDirective(DataDirective):
    node_class = AttributeNode


class FunctionDirective(rst.Directive):
    required_arguments = 1
    has_content = True
    final_argument_whitespace = True

    _FUNC_DEF_REGEX = re.compile(r"([a-zA-Z0-9_]+)\s*\((.*)\)")
    _ARG_FIELD_REGEX = re.compile(r"(arg|param|type)\s+([0-9a-zA-Z_]+)")
    _RETURN_FIELD_REGEX = re.compile(r"(return|rtype)")
    _OPTION_MODOPTION_FIELD_REGEX = re.compile(
        r"(mod-option|option)\s+(arg|rtype|function)\s*(\S*)")

    def _parse_arg_detail(self, arg_list_node: ArgumentListNode,
                          arg_name: str, detail_type: str,
                          detail_body: nodes.field_body) -> None:
        arg_node: ArgumentNode = None
        arg_nodes = find_children(arg_list_node, ArgumentNode)
        for node in arg_nodes:
            if node.element(NameNode).astext() == arg_name:
                arg_node = node
                break
        if arg_node:
            if detail_type in ("arg", "param"):
                arg_node.element(DescriptionNode).add_text(
                    detail_body.astext())
            elif detail_type == "type":
                dtype = parse_data_type(detail_body)
                arg_node.element(DataTypeListNode).append_child(dtype)

    def _parse_return_detail(self, return_node: FunctionReturnNode,
                             detail_type: str,
                             detail_body: nodes.field_body) -> None:
        if detail_type == "return":
            return_node.element(DescriptionNode).add_text(
                detail_body.astext())
        elif detail_type == "rtype":
            dtype = parse_data_type(detail_body)
            return_node.element(DataTypeListNode).append_child(dtype)

    def _parse_arg_option(self, arg_list_node: ArgumentListNode,
                          arg_name: str, option_type: str,
                          option_body: nodes.field_body) -> None:
        arg_node: ArgumentNode = None
        for child in arg_list_node.children:
            n = next(child.findall(NameNode))
            if n.astext() == arg_name:
                arg_node = n.parent
                break
        if arg_node:
            if option_body.astext() == "update-argument-type":
                arg_node.attributes[option_type] = option_body.astext()
            else:
                for dtype_node in arg_node.findall(DataTypeNode):
                    dtype_node.attributes[option_type] = option_body.astext()

    def _parse_return_option(self, return_node: FunctionReturnNode,
                             option_type: str,
                             option_body: nodes.field_body) -> None:
        for dtype_node in return_node.findall(DataTypeNode):
            dtype_node.attributes[option_type] = option_body.astext()

    def _parse_signature_detail(self, func_node: FunctionNode,
                                paragraph: nodes.paragraph) -> None:
        field_lists: nodes.field_list = paragraph.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                if m := self._ARG_FIELD_REGEX.match(fname_node.astext()):
                    arg_list_node = func_node.element(ArgumentListNode)
                    self._parse_arg_detail(arg_list_node, m.group(2),
                                           m.group(1), fbody_node)
                elif m := self._RETURN_FIELD_REGEX.match(fname_node.astext()):
                    func_ret_node = func_node.element(FunctionReturnNode)
                    self._parse_return_detail(func_ret_node, m.group(1),
                                              fbody_node)
                elif m := self._OPTION_MODOPTION_FIELD_REGEX.match(
                        fname_node.astext()):
                    if m.group(2) == "arg":
                        arg_list_node = func_node.element(ArgumentListNode)
                        self._parse_arg_option(arg_list_node, m.group(3),
                                               m.group(1), fbody_node)
                    elif m.group(2) == "rtype":
                        func_ret_node = func_node.element(FunctionReturnNode)
                        self._parse_return_option(func_ret_node, m.group(1),
                                                  fbody_node)
                    elif m.group(2) == "function":
                        func_node.attributes[m.group(1)] = fbody_node.astext()
                elif fname_node.astext() == "generic-types":
                    func_node.attributes[fname_node.astext()] = \
                        fbody_node.astext()

    def run(self) -> list[FunctionNode]:
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        # Parse "(Deprecated*" from the data name.
        func_name = self.arguments[0]
        index = func_name.rfind("(Deprecated")
        deprecated_str = None
        if index != -1:
            deprecated_str = func_name[index:]
            func_name = func_name[0:index]

        func_defs = []
        fdef_str: str = ""
        for fdef in func_name.split("\n"):
            if fdef[-1] == "\\":
                fdef_str += fdef[:-1]
            else:
                fdef_str += fdef
                ma = self._FUNC_DEF_REGEX.search(fdef_str)
                if ma:
                    func_defs.append(parse_function_def(fdef_str))
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
            func_node = build_function_node_from_def(fdef)

            # Add attributes.
            func_node.attributes["function_type"] = self.name
            if deprecated_str is not None:
                func_node.attributes["deprecated"] = deprecated_str

            # Get all descriptions.
            desc_str = ""
            for child in paragraph.children:
                if isinstance(child, nodes.paragraph):
                    desc_str += child.astext()
            func_node.element(DescriptionNode).add_text(desc_str)

            func_nodes.append(func_node)

            self._parse_signature_detail(func_node, paragraph)

        return func_nodes


# This directive is only used for test.
class EnumDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list[DataNode]:
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        node = EnumNode.create_template()

        # Parse enum name.
        enum_name = self.arguments[0]
        node.element(NameNode).add_text(enum_name)

        # Get all descriptions.
        desc_str = ""
        for child in paragraph.children:
            if isinstance(child, nodes.paragraph):
                desc_str += child.astext()
        node.element(DescriptionNode).add_text(desc_str)

        # Get all field values.
        enum_item_list_node = node.element(EnumItemListNode)
        field_lists: nodes.field_list = paragraph.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                enum_item_node = EnumItemNode.create_template()
                enum_item_node.element(NameNode).add_text(fname_node.astext())
                enum_item_node.element(DescriptionNode).add_text(fbody_node.astext())
                append_child(enum_item_list_node, enum_item_node)

        return [node]


class DocumentDirective(rst.Directive):
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list[nodes.paragraph]:
        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        content = " ".join(self.arguments)
        append_child(paragraph, nodes.Text(content))

        return [paragraph]


class LiteralIncludeDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec: ClassVar = {
        "lines": rst.directives.unchanged
    }

    def run(self) -> list[CodeNode]:
        path: str = self.arguments[0]
        code_node: CodeNode = CodeNode(text=path)

        return [code_node]


class NopDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self) -> list:
        return []


class ModTypeDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = False
    has_content = False

    def run(self) -> list[ModTypeNode]:
        mod_type: str = self.arguments[0]
        mod_type_node: ModTypeNode = ModTypeNode(text=mod_type)

        return [mod_type_node]


class BaseClassDirective(rst.Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    _MODOPTION_FIELD_REFEX = re.compile(r"mod-option\s+base-class")

    def run(self) -> list[BaseClassListNode]:
        base_classes: str = self.arguments[0]
        base_class_list_node: BaseClassListNode = BaseClassListNode()

        paragraph: nodes.paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        for sp in base_classes.split(", "):
            base_class_node = BaseClassNode.create_template()
            base_class_node.element(DataTypeListNode).append_child(make_data_type_node(sp))
            base_class_list_node.append_child(base_class_node)

        field_lists: nodes.field_list = paragraph.findall(nodes.field_list)
        for field_list in field_lists:
            for field in field_list:
                fname_node, fbody_node = field.children
                if self._MODOPTION_FIELD_REFEX.match(fname_node.astext()):
                    for base_class_node in base_class_list_node.children:
                        for dtype_node in base_class_node.findall(DataTypeNode):
                            dtype_node.attributes["mod-option"] = \
                                fbody_node.astext()

        return [base_class_list_node]


def register_directives() -> None:
    rst.directives.register_directive("module", ModuleDirective)
    rst.directives.register_directive("currentmodule", ModuleDirective)
    rst.directives.register_directive("class", ClassDirective)
    rst.directives.register_directive("base-class", BaseClassDirective)
    rst.directives.register_directive("function", FunctionDirective)
    rst.directives.register_directive("method", FunctionDirective)
    rst.directives.register_directive("classmethod", FunctionDirective)
    rst.directives.register_directive("staticmethod", FunctionDirective)
    rst.directives.register_directive("attribute", AttributeDirective)
    rst.directives.register_directive("property", AttributeDirective)
    rst.directives.register_directive("data", DataDirective)
    rst.directives.register_directive("DATA", DataDirective)
    rst.directives.register_directive("enum", EnumDirective)

    rst.directives.register_directive(
        "literalinclude", LiteralIncludeDirective)
    rst.directives.register_directive("seealso", DocumentDirective)
    rst.directives.register_directive("hlist", DocumentDirective)
    rst.directives.register_directive("toctree", DocumentDirective)
    rst.directives.register_directive("rubric", DocumentDirective)
    rst.directives.register_directive("deprecated", DocumentDirective)

    rst.directives.register_directive("include", NopDirective)

    rst.directives.register_directive("mod-type", ModTypeDirective)
