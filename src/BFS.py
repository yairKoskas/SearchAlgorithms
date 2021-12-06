from Graph import Graph, Vertex
from Singleton import Singleton
from Algorithm import BaseAlgorithm, get_neighbors


class BFS(BaseAlgorithm, metaclass=Singleton):

    def find_path(self, g: Graph, src: Vertex, dest: Vertex):
        q = [src]
        discovered = [src]
        while len(q) != 0:
            vert = q.pop(0)
            if vert == dest:
                return discovered
            for neighbor in get_neighbors(g, vert):
                if neighbor not in discovered:
                    discovered.append(neighbor)
                    q.append(neighbor)



