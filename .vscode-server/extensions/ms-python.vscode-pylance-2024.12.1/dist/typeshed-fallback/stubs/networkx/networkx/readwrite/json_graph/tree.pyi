from networkx.utils.backends import _dispatchable

def tree_data(G, root, ident: str = "id", children: str = "children"): ...
@_dispatchable
def tree_graph(data, ident: str = "id", children: str = "children"): ...
