import os
from docutils import nodes
from docutils.core import publish_doctree

from fake_bpy_module.analyzer.nodes import (  # pylint: disable=E0401
    DataNode,
    NameNode,
    FunctionNode,
)
from fake_bpy_module.utils import (  # pylint: disable=E0401
    check_os,
    output_log,
    remove_unencodable,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_INFO,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERR,
    find_children,
    get_first_child,
    append_child,
    split_string_by_comma,
)
from . import common


class UtilsTest(common.FakeBpyModuleTestBase):
    name = "UtilsTest"
    module_name = __module__

    def test_check_os(self):
        to_osname = {
            "nt": "Windows",
            "posix": "Linux",
        }

        self.assertEqual(check_os(), to_osname[os.name])

    def test_output_log(self):
        output_log(LOG_LEVEL_DEBUG, "Debug")
        output_log(LOG_LEVEL_INFO, "Info")
        output_log(LOG_LEVEL_NOTICE, "Notice")
        output_log(LOG_LEVEL_WARN, "Warning")
        output_log(LOG_LEVEL_ERR, "Error")

    def test_remove_unencodable(self):
        original_string = "\xb2AAA\u2013BBB\u2019"
        expect = "AAABBB"

        actual = remove_unencodable(original_string)

        self.assertEqual(expect, actual)

    def test_find_children(self):
        document: nodes.document = publish_doctree(""".. module:: module.a

.. data:: DATA_1

.. function:: function_1()

.. data:: DATA_2

""")

        data_nodes = find_children(document, DataNode)
        self.assertEqual(len(data_nodes), 2)

        self.assertEqual(data_nodes[0].element(NameNode).astext(), "DATA_1")
        self.assertEqual(data_nodes[1].element(NameNode).astext(), "DATA_2")

    def test_get_find_children(self):
        document: nodes.document = publish_doctree(""".. module:: module.a

.. data:: DATA_1

.. function:: function_1()

.. data:: DATA_2

""")

        data_node = get_first_child(document, DataNode)
        self.assertIsNotNone(data_node)

        self.assertEqual(data_node.element(NameNode).astext(), "DATA_1")

    def test_append_child(self):
        document: nodes.document = publish_doctree(""".. module:: module.a

.. data:: DATA_1

""")

        func_node = FunctionNode.create_template()
        func_node.element(NameNode).add_text("function_1")
        append_child(document, func_node)

        self.assertEqual(
            document.pformat(),
            """<document source="<string>">
    <module>
        <name>
            module.a
        <description>
    <data>
        <name>
            DATA_1
        <description>
        <data-type-list>
    <function>
        <name>
            function_1
        <description>
        <argument-list>
        <return>
            <description>
            <data-type-list>
""",
        )

    def test_split_string_by_comma(self):
        sp = split_string_by_comma("a, b")
        self.assertListEqual(sp, ["a", "b"])

        sp = split_string_by_comma("a")
        self.assertListEqual(sp, ["a"])

        sp = split_string_by_comma("a ,b")
        self.assertListEqual(sp, ["a", "b"])

        sp = split_string_by_comma("a[, b]")
        self.assertListEqual(sp, ["a", "b"])

        sp = split_string_by_comma("[a]")
        self.assertListEqual(sp, ["a"])

        sp = split_string_by_comma("a=10, b=3.0")
        self.assertListEqual(sp, ["a=10", "b=3.0"])

        sp = split_string_by_comma("a=[1, 3], b=1.3, c=2")
        self.assertListEqual(sp, ["a=[1, 3]", "b=1.3", "c=2"])

        sp = split_string_by_comma("a, b=(1, 3), c=2")
        self.assertListEqual(sp, ["a", "b=(1, 3)", "c=2"])

        sp = split_string_by_comma("a, b=[1, 3], c=2")
        self.assertListEqual(sp, ["a", "b=[1, 3]", "c=2"])

        sp = split_string_by_comma("a, b={1, 3}, c=2")
        self.assertListEqual(sp, ["a", "b={1, 3}", "c=2"])

        sp = split_string_by_comma("a, b=(1, 3), c={2, 4}")
        self.assertListEqual(sp, ["a", "b=(1, 3)", "c={2, 4}"])

        sp = split_string_by_comma("a, b=((1, 3), (2, 4))")
        self.assertListEqual(sp, ["a", "b=((1, 3), (2, 4))"])

        sp = split_string_by_comma("a[, b=1.3][, c=2]")
        self.assertListEqual(sp, ["a", "b=1.3", "c=2"])

        sp = split_string_by_comma("a=[1, 4][, b=1.3][, c=2]")
        self.assertListEqual(sp, ["a=[1, 4]", "b=1.3", "c=2"])
