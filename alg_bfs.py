from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np

def bfs(graph_adj_d, start_vertex):
    """Breadth First Search (BFS) algorithm with single source 
    by queue.

    Time complexity for graph G(V, E): O(|V|+|E|).
    """
    distance_d = {v: np.inf for v in graph_adj_d.keys()}
    distance_d[start_vertex] = 0
    visit_queue = []
    visit_queue.insert(0, start_vertex)
    while visit_queue:
        v_visit = visit_queue.pop()
        for v_neighbor in graph_adj_d[v_visit]:
            # If v_neighbor is not visited.
            if np.isinf(distance_d[v_neighbor]):
                visit_queue.insert(0, v_neighbor)
                distance_d[v_neighbor] += 1
    return distance_d


def main():
    # Undirected graph by adjacency list.
    graph_adj_d = {
        'A': ['B', 'D', 'G'],
        'B': ['A', 'E', 'F'],
        'C': ['F', 'H'],
        'D': ['A', 'F'],
        'E': ['B', 'G'],
        'F': ['B', 'C', 'D'],
        'G': ['A', 'E'],
        'H': ['C']
    }
    print('Graph:\n{}'.format(graph_adj_d))

    start_vertex = 'A'
    print('Start vertex: {}'.format(start_vertex))
    distance_d = bfs(graph_adj_d, start_vertex)
    print('Using BFS with queue, the distance dict is\n{}'
          .format(distance_d))


if __name__ == '__main__':
    main()