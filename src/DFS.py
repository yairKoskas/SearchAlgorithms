from Graph import Graph, Vertex
from Singleton import Singleton
from Algorithm import BaseAlgorithm, get_neighbors


class DFS(BaseAlgorithm, metaclass=Singleton):

    def find_path(self, g: Graph, src: Vertex, dest: Vertex):
        s = [src]
        discovered = []
        while len(s) != 0:
            vert = s.pop()
            if vert not in discovered:
                discovered.append(vert)
                if vert == dest:
                    return discovered
                for neighbor in get_neighbors(g, vert):
                    s.append(neighbor)

        # if we didn't find a path
        return None
