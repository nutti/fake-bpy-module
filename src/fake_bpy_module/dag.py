from typing import List, Dict


class Node:
    def __init__(self, data=None):
        self.data = data
        self.in_edges : List['Edge'] = []
        self.out_edges : List['Edge'] = []


class Edge:
    def __init__(self, src : 'Node', dst : 'Node'):
        self.src = src
        self.dst = dst


class DAG:
    def __init__(self):
        self.root_node : 'Node' = Node()
        self.nodes : List['Node'] = [self.root_node]
        self.edges : List['Edge'] = []

    def make_node(self, data=None) -> List['Node']:
        new_node = Node(data)
        self.nodes.append(new_node)
        self.make_edge(self.root_node, new_node)

        return new_node

    def make_edge(self, src : 'Node', dst : 'Node') -> 'Edge':
        new_edge = Edge(src, dst)
        src.out_edges.append(new_edge)
        dst.in_edges.append(new_edge)
        self.edges.append(new_edge)

        return new_edge


def topological_sort(graph : 'DAG') -> List['Node']:
    ref_counts : Dict['Node', int] = {}
    for node in graph.nodes:
        ref_counts[node] = len(node.in_edges)

    sorted_nodes : List['Node'] = []
    ready : List['Node'] = [graph.root_node]
    while ready:
        node = ready.pop(0)

        if node != graph.root_node:
            sorted_nodes.append(node)

        for e in node.out_edges:
            ref_counts[e.dst] -= 1
            if ref_counts[e.dst] == 0:
                ready.append(e.dst)

    if len(graph.nodes) != len(sorted_nodes) + 1:
        diff = set(graph.nodes) - set(sorted_nodes) - set([graph.root_node])
        node_data_list = {n.data for n in diff}
        raise ValueError("Cycle is detected. ({})".format(", ".join(node_data_list)))

    return sorted_nodes
