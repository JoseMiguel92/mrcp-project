# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from solution_greedy import SolutionGreedy


class SolutionGreedyNeighbors(SolutionGreedy):

    def __init__(self, graph, name):
        super().__init__(graph, name)

    def find_better(self, adjacent):
        """ Find better candidate (with better ratio) from adjacent and verify if him form a clique. """
        current_neighbors = -1
        node_chosen = None
        for node in adjacent:
            node_neighbors = len(self.graph.get_node(node).neighbors_indices)
            if node_neighbors > current_neighbors:
                current_neighbors = node_neighbors
                node_chosen = node

        return node_chosen
