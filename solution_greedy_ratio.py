# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from solution_greedy import SolutionGreedy


class SolutionGreedyRatio(SolutionGreedy):

    def __init__(self, graph, name):
        super().__init__(graph, name)

    def find_better(self, adjacent):
        """ Find better candidate (with better ratio) from adjacent and verify if him form a clique. """
        current_ratio = -1
        node_chosen = None
        for node in adjacent:
            node_ratio = self.graph.get_node(node).p_weight / self.graph.get_node(node).q_weight
            if node_ratio > current_ratio:
                current_ratio = node_ratio
                node_chosen = node

        return node_chosen
