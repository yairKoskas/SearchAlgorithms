from Graph import Graph, Vertex


def get_neighbors(g: Graph, v: Vertex):
    neighbors = g.edges[v]
    neighbors.remove(v)
    return neighbors


def dfs(g: Graph, v: Vertex):
    s = [v]
    discovered = []
    while len(s) != 0:
        vert = s.pop()
        if vert not in discovered:
            discovered.append(vert)
            for neighbor in get_neighbors(g, vert):
                s.append(neighbor)
    return discovered
