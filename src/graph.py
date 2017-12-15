"""Implement a class for a graph data structure."""


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
            for i in self._graph[key]:
                edges.append((key, i, self._graph[key][i]))
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
            raise ValueError('These edges do not exist.')

    def has_node(self, val):
        """Return true or false if node has value."""
        if val in self._graph:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return list of nodes connected node(val)."""
        try:
            self._graph[val]
            neighbors = {}
            for key in self._graph[val]:
                neighbors.setdefault(key, self._graph[val][key])
            else:
                return neighbors
        except KeyError:
            raise ValueError('This node dosent exit')

    def adjacent(self, val1, val2):
        """Return true if edge between vals, else false, & error if no val."""
        if val1 in self._graph and val2 in self._graph:
            if val2 in self._graph[val1]:
                return True
            else:
                return False
        else:
            raise ValueError('These edges do not exist.')

    def depth_first_traversal(self, start_val):
        """Traverse the graph from first edge of each node until ultimate."""
        if start_val in self._graph:
            depth_traversal = []
            path = [start_val]
            while path:
                val = path.pop()
                if val not in depth_traversal:
                    depth_traversal.append(val)
                    path = path + list(self._graph[val].keys())
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

    def dijkstra(self, start, end):
        """Dijkysta algorithm to calculate the shortest path."""
        distance = {start: 0}
        parents = {}
        not_visited = list(self._graph.keys())
        if start not in self._graph:
            raise ValueError('Your start node does not exist.')
        if self._graph[start] == {}:
            return 'Your start has no edges.'
        while not_visited:
            min_node = None
            for val in not_visited:
                if val in distance:
                    if min_node is None:
                        min_node = val
                    elif distance[val] < distance[min_node]:
                        min_node = val
            not_visited.remove(min_node)
            for edge in self._graph[min_node]:
                length = distance[min_node] + self._graph[min_node][edge]
                if edge not in distance or length < distance[edge]:
                    distance[edge] = length
                    parents[edge] = min_node
        if end in distance:
            total_distance = distance[end]
            path = [end]
            while end != start:
                if end in parents:
                    path.insert(0, parents[end])
                    end = parents[end]
                else:
                    return 'There is no path between these nodes.'
            return total_distance, path
        else:
            return 'There is no path between these nodes.'


if __name__ == '__main__':  # pragma: no cover
    graph_data = {
        'A': {'B': 0, 'D': 0},
        'B': {'A': 0, 'E': 0, 'D': 0},
        'C': {'A': 0, 'B': 0},
        'D': {},
        'E': {'D': 0, 'C': 0, 'B': 0, 'A': 0}
    }
    g = Graph()
    g._graph = graph_data
    print('Using the following graph:\n\n{}\n\nthe lists below show a '
          'depth_first_traversal followed by a '
          'breadth_first_traversal:'.format(graph_data))
    print('\nDepth First Traversal:')
    print(g.depth_first_traversal('A'))
    print('\nBreadth First Traversal:')
    print(g.breadth_first_traversal('A'))

    graph_data = {
        'George': {'Steve': 0, 'Jane': 0, 'Phil': 0},
        'Anne': {'Abe': 0, 'Uma': 0, 'George': 0},
        'George': {'Abe': 0, 'Steve': 0},
        'Steve': {'Anne': 0},
        'Abe': {'George': 0, 'Uma': 0, 'Steve': 0, 'Phil': 0},
        'Uma': {'Steve': 0},
        'Phil': {'Uma': 0, 'George': 0, 'Phil': 0},
        'Jane': {'Anne': 0},
    }
    g2 = Graph()
    g2._graph = graph_data
    print('\n\nHere is another example on the following graph:\n\n{}\n\nthe '
          'lists below, again, show a depth_first_traversal followed by a '
          'breadth_first_traversal:'.format(graph_data))
    print('\nDepth First Traversal:')
    print(g2.depth_first_traversal('Abe'))
    print('\nBreadth First Traversal:')
    print(g2.breadth_first_traversal('Abe'))
