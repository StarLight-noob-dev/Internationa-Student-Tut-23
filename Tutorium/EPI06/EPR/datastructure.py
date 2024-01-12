def generate_edges(graph):
    """ Returns a list tuples, each tuple represents an edge. """
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


def find_isolated_nodes(graph):
    """ Returns a list of isolated nodes (undirected graphs) - from lecture notes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated


def find_isolated_nodes_directed(graph):
    """ Returns a list of isolated nodes (directed graphs). """
    isolated = []
    isolated2 = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    # isolated now contains nodes without starting edge
    # need to be checked if there are ending edges for them
    for node in isolated:
        for key in graph.keys():
            if node in graph.get(key):
                isolated2.append(node)
    for node in isolated2:
        if node in isolated:
            isolated.remove(node)
    return isolated


def enter_node(graph, node):
    """ Enters a new node with an empty set of edges. """
    if node in graph.keys():
        return None  # node is already included
    graph.update({node: set()})


def enter_nodes(graph):
    """ To enter the nodes and egdes by the user. """
    while True:
        node = input("Please enter a value for the Vertex\
                \n(To stop givin Nodes write '0'):  ")
        if node == "0":
            break
        enter_node(graph, node)
    print("The Vertex that you enter are: ", graph.keys())
    print("Please enter the Edges of the graph, you can stop given the value '0' ")
    while True:
        node_start = input(
            "Please enter the starting Vertex for the Edge (Stop '0'): ")
        if node_start == "0":
            break
        if node_start in graph.keys():
            while True:
                node_end = input("Give the end Vertex for the Edge: ")
                if node_end in graph.keys():
                    values = graph.get(node_start)
                    values.add(node_end)
                    graph.update({node_start: values})
                    break
    print("The given Edges are: ", generate_edges(graph))


def find_root(graph):
    """ Find a list of nodes no other node points to
     if this list consists of one node only, it should be
     a root node (with the precondition that it is a directed
     graph and a tree (zusammenhängend und kreisfrei)). """
    p_roots = list(graph.keys())
    for key in graph.keys():
        for value in graph.get(key):
            if value in p_roots:
                p_roots.remove(value)
    if len(p_roots) == 1:
        print("The Tree has one ROOT! ", p_roots)
        return p_roots
    print("The Tree does NOT have a ROOT!")
    return None


def check_if_tree(graph):
    """ Checks if it is a tree and returns an according boolean. Also provides print statements
    with small reasons for it. """
    if len(find_isolated_nodes_directed(graph)) > 0 and len(graph.keys()) > 1:
        print("This is not a Tree, reason: Not all Vertices are connected!")
        return False
    x = len(generate_edges(graph))  # Number of edges
    z = len(graph.keys())  # Number of nodes
    if x + 1 == z:
        print("It is a Tree, beacause all Vertices have a connection and the ammount of Edges + 1 = Number of Vertices")
        return True
    print("Not a Tree, all vertices have connection but the number of Vertices", z, " is not the number of Edges ", z,
          " plus 1!")
    return False


if __name__ == '__main__':
    graph = {}
    enter_nodes(graph)
    tree = check_if_tree(graph)
    if tree:
        # list the leaves - basically we can reuse "find_isolated_nodes" for not directed graphs
        print("Blätter sind: ", find_isolated_nodes(graph))
        find_root(graph)