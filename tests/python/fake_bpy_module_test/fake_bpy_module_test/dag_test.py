from . import common
from fake_bpy_module.dag import (
    Node,
    Edge,
    DAG,
    topological_sort,
)


class DAGTest(common.FakeBpyModuleTestBase):

    name = "DAGTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_node(self):
        node = Node("A")

        self.assertEqual(node.data(), "A")
        self.assertEqual(node.num_in_edges(), 0)
        self.assertEqual(node.num_out_edges(), 0)
        self.assertEqual(node.in_edges(), [])
        self.assertEqual(node.out_edges(), [])

    def test_edge(self):
        node_1 = Node("A")
        node_2 = Node("B")
        edge = Edge(node_1, node_2)

        self.assertEqual(node_1.num_in_edges(), 0)
        self.assertEqual(node_1.num_out_edges(), 1)
        self.assertEqual(node_1.out_edges()[0], edge)
        self.assertEqual(node_2.num_in_edges(), 1)
        self.assertEqual(node_2.in_edges()[0], edge)
        self.assertEqual(node_2.num_out_edges(), 0)

        self.assertEqual(edge.src(), node_1)
        self.assertEqual(edge.dst(), node_2)

    def test_dag(self):
        dag = DAG()
        node_1 = dag.make_node("A")
        node_2 = dag.make_node("B")
        node_3 = dag.make_node("C")
        edge_1 = dag.make_edge(node_1, node_2)
        edge_2 = dag.make_edge(node_1, node_3)

        self.assertEqual(dag.num_nodes(), 3)
        self.assertEqual(dag.num_edges(), 2)
        self.assertSetEqual(set(dag.nodes()), {node_1, node_2, node_3})
        self.assertSetEqual(set(dag.edges()), {edge_1, edge_2})

    def test_topological_sort_1(self):
        dag = DAG()
        node_1 = dag.make_node("A")
        node_2 = dag.make_node("B")
        node_3 = dag.make_node("C")
        edge_1 = dag.make_edge(node_2, node_1)
        edge_2 = dag.make_edge(node_1, node_3)

        sorted_nodes = topological_sort(dag)
        self.assertEquals(sorted_nodes, [node_2, node_1, node_3])

    def test_topological_sort_2(self):
        dag = DAG()
        node_1 = dag.make_node("A")
        node_2 = dag.make_node("B")
        node_3 = dag.make_node("C")
        edge_1 = dag.make_edge(node_1, node_2)
        edge_2 = dag.make_edge(node_1, node_3)

        sorted_nodes = topological_sort(dag)
        self.assertEquals(sorted_nodes, [node_1, node_2, node_3])

    def test_topological_sort_3(self):
        dag = DAG()
        node_1 = dag.make_node("A")
        node_2 = dag.make_node("B")
        node_3 = dag.make_node("C")
        node_4 = dag.make_node("C")
        edge_1 = dag.make_edge(node_1, node_2)
        edge_2 = dag.make_edge(node_2, node_3)
        edge_2 = dag.make_edge(node_1, node_4)

        sorted_nodes = topological_sort(dag)
        self.assertEquals(sorted_nodes, [node_1, node_2, node_4, node_3])

    def test_topological_sort_detect_cycle(self):
        dag = DAG()
        node_1 = dag.make_node("A")
        node_2 = dag.make_node("B")
        node_3 = dag.make_node("C")
        edge_1 = dag.make_edge(node_1, node_2)
        edge_2 = dag.make_edge(node_2, node_3)
        edge_3 = dag.make_edge(node_3, node_1)

        with self.assertRaises(ValueError):
            topological_sort(dag)
