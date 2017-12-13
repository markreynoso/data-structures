"""Implement a class for graph data structure with weighted edges."""


class Graph(object):
    """Graph class."""

    def __init__(self):
        """Initialize a graph."""
        self._graph = {}

    def nodes(self):
        """Return a list of all nodes in graph."""
        return list(self._graph.keys())

    def edges(self):
        """Return a list of edges in graph."""
        edges = []
        for key in self._graph:
            for child in self._graph[key]:
                edges.append((key, child, self._graph[key][child]))
        return edges

    def add_node(self, val):
        """Add a node with value of val to graph."""
        self._graph.setdefault(val, {})

    def add_edge(self, val1, val2, weight=0):
        """Add a new edge to graph between val1 & val2 as well as add vals."""
        self.add_node(val1)
        self.add_node(val2)
        self._graph[val1][val2] = weight

    def del_node(self, val):
        """Delete node w/val from graph, raises exception if not exist."""
        if val in self._graph:
            del self._graph[val]
            for key in self._graph:
                if val in self._graph[key]:
                    del self._graph[key][val]
        else:
            raise ValueError('There is no node of that value in the graph.')

    def del_edge(self, val1, val2):
        """Delete edge between val1 & val2 from graph."""
        try:
            if val2 in self._graph[val1]:
                del self._graph[val1][val2]
            else:
                raise ValueError('These edges do not exist.')
        except KeyError:
            raise ValueError('This edge does not exist.')

    def has_node(self, val):
        """Return true or false if node has value."""
        return val in self._graph

    def neighbors(self, val):
        """Return list of nodes connected node(val)."""
        try:
            return list(self._graph[val].keys())
        except KeyError:
            raise ValueError('This node does not exist')

    def adjacent(self, val1, val2):
        """Return true if edge between vals, else false, & error if no val."""
        try:
            self._graph[val1]
            self._graph[val2]
            if val2 in self._graph[val1]:
                return True
            else:
                return False
        except KeyError:
            raise ValueError('Node is not a node in this graph')

    def depth_first_traversal(self, start_val):
        """Traverse the graph from first edge of each node until ultimate."""
        if start_val in self._graph:
            depth_traversal = []
            path = [start_val]
            while path:
                val = path.pop()
                if val not in depth_traversal:
                    depth_traversal.append(val)
                    path += list(self._graph[val].keys())
            return depth_traversal
        else:
            raise ValueError('Value is not in graph.')

    def breadth_first_traversal(self, start_val):
        """Traverse the graph by node's edges before moving to next node."""
        if start_val in self._graph:
            depth_traversal = []
            path = [start_val]
            while path:
                val = path.pop(0)
                if val not in depth_traversal:
                    depth_traversal.append(val)
                    path = path + list(self._graph[val].keys())
            return depth_traversal
        else:
            raise ValueError('Value is not in graph.')
