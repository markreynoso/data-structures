"""Test for Shorest distance graph."""
from graph import Graph

import pytest

graph = {
    'A': {'C': 4,
          'B': 2,
          'D': 5
          },
    'C': {'G': 20,
          'D': 8
          },
    'B': {'E': 8
          },
    'D': {'C': 4,
          'B': 3,
          'F': 10,
          'G': 15
          },
    'E': {'F': 8,
          'D': 8
          },
    'F': {'G': 5
          },
    'G': {}
}

test_graph = {
    'A': {'B': 5,
          'C': 6
          },
    'B': {'D': 2
          },
    'C': {'E': 8,
          'F': 4
          },
    'D': {'E': 2,
          'G': 10
          },
    'E': {'G': 10,
          'F': 4
          },
}


def test_dijkstra():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = graph
    assert g.dijkstra('A', 'F') == (15, ['A', 'D', 'F'])


def test_dijkstra_returns_list():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = test_graph
    assert g.dijkstra('A', 'E') == (9, ['A', 'B', 'D', 'E'])


def test_dijkstra_returns_list_from_path_a_g():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = test_graph
    assert g.dijkstra('A', 'G') == (17, ['A', 'B', 'D', 'G'])


def test_dijkstra_that_start_no_children_return_emty_dict():
    """Test dijkstra returns each nodes best parents."""
    g = Graph()
    g._graph = graph
    assert g.dijkstra('G', 'A') == 'There is no path between these nodes.'

# def test_dijkstra_raises_valueerror_if_start_has_no_edges():
#     """Test shortest distance raises ValueError if start has no edges."""
#     g = Graph()
#     g._graph = test_graph
#     with pytest.raises(ValueError):
#         g.dijkstra('G', 'A')
