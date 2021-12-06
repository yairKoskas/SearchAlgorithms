from abc import ABC, abstractmethod
from typing import List


class Vertex:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return other.name == self.name

    def __le__(self, other):
        return other.name > self.name

    def __ge__(self, other):
        return other.name < self.name

    def __cmp__(self, other):
        return str.__cmp__(self.name, other.name)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return '('+self.name+')'


class Graph(ABC):

    def __init__(self, vertices: List[Vertex]):
        if not isinstance(vertices, set):
            try:
                self.vertices = set(vertices)
            except TypeError:
                raise ValueError('Given vertices aren\'t valid')
        self.vertices = list(set(vertices))  # lazy solution to remove duplicates
        self.edges = {}
        for i in self.vertices:
            self.edges[i] = []

    @abstractmethod
    def add_edge(self, v1: Vertex, v2: Vertex):
        pass

    def add_vertex(self, v1: Vertex):
        for i in self.vertices:
            if i.name == v1.name:
                return
        self.vertices.append(v1)


class DirectedGraph(Graph):

    def add_edge(self, v1, v2):
        if isinstance(v1, str):
            v1 = Vertex(v1)
        if isinstance(v2, str):
            v2 = Vertex(v2)
        self.edges[v1].append(v2)


class UndirectedGraph(Graph):

    def add_edge(self, v1, v2):
        if isinstance(v1, str):
            v1 = Vertex(v1)
        if isinstance(v2, str):
            v2 = Vertex(v2)
        self.edges[v1].append(v2)
        self.edges[v2].append(v1)

