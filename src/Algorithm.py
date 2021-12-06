from Graph import Graph, Vertex


def get_neighbors(g: Graph, v: Vertex):
    return g.edges[v]


class BaseAlgorithm:

    def find_path(self, g: Graph, src: Vertex, dest: Vertex):
        pass
