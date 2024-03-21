from docutils import nodes


class SubNodeVisitor:
    # TODO: consider to use SparseNodeVisitor

    def __init__(self, node: nodes.Node):
        self.node = node

    def dispatch_visit(self, node: nodes.Node):
        node_name = node.__class__.__name__
        method = getattr(self, f"visit_{node_name}", self.unknown_visit)
        return method(node)

    def dispatch_depart(self, node: nodes.Node):
        node_name = node.__class__.__name__
        method = getattr(self, f"depart_{node_name}", self.unknown_depart)
        return method(node)

    def unknown_visit(self, node: nodes.Node):
        raise ValueError(
            f"{self.__class__} visiting unknown node type: "
            f"{node.__class__.__name__}\n\n{node.pformat()}")

    def unknown_depart(self, node: nodes.Node):
        raise ValueError(
            f"{self.__class__} departing unknown node type: "
            f"{node.__class__.__name__}\n\n{node.pformat()}")


def walk_sub_node(node: nodes.Node, visitor: SubNodeVisitor,
                  ignore_self: bool = True, call_depart: bool = False):
    should_stop = False

    try:
        if not ignore_self:
            visitor.dispatch_visit(node)
    except nodes.SkipChildren:
        return should_stop

    for child in node.children[:]:
        walk_sub_node(child, visitor, ignore_self=False, call_depart=call_depart)

    if call_depart and not ignore_self:
        visitor.dispatch_depart(node)

    return should_stop
