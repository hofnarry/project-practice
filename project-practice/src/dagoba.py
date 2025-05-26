class Vertex:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data or {}

class Edge:
    def __init__(self, from_vertex, to_vertex, label=None):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.label = label

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, id, data=None):
        if id not in self.vertices:
            self.vertices[id] = Vertex(id, data)

    def add_edge(self, from_id, to_id, label=None, reverse=False):
        if from_id in self.vertices and to_id in self.vertices:
            self.edges.append(Edge(from_id, to_id, label))
            if reverse:
                self.edges.append(Edge(to_id, from_id, label))

    def v(self, vertex_id):
        return Traversal(self, vertex_id)

class Traversal:
    def __init__(self, graph, start_vertex_id):
        self.graph = graph
        self.start_vertex_id = start_vertex_id
        self.current = [start_vertex_id]

    def out(self, label=None):
        result = []
        for edge in self.graph.edges:
            if edge.from_vertex in self.current and (label is None or edge.label == label):
                result.append(edge.to_vertex)
        self.current = result
        return self

    def run(self):
        return [self.graph.vertices[vid].data for vid in self.current]
