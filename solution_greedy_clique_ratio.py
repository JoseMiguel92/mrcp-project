# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random

from instance import Instance


class SolutionGreedyRatio:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = round(100 * self.graph.calculate_density(), 2)
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_clique_by_ratio(self):
        vertices = list(self.graph.nodes.keys())
        vertex = random.randrange(0, len(vertices), 1)
        clique = [vertices[vertex]]
        self.find_clique_by_ratio_aux(vertex, vertex, clique)
        self.clique = clique
        self.cardinality = len(self.clique)
        self.sol_value = self.calculate_total_ratio(self.clique)
        return sorted(clique)

    def find_clique_by_ratio_aux(self, root, father, clique):
        father_neighbors = self.graph.get_node(father).neighbors_indices
        current_ratio = -1
        node_chosen = None
        if father_neighbors:
            for node in father_neighbors:
                if node_chosen is None:
                    node_chosen = node
                    continue
                elif self.belong_to_clique(node, clique) and self.has_max_ratio(node, current_ratio, clique):
                    node_chosen = node
                    clique.append(node_chosen)

        else:
            return sorted(clique)

    def belong_to_clique(self, node, clique):
        belong = False
        if node not in clique:
            for vertex in clique:
                if node in self.graph.get_node(vertex).neighbors_indices:
                    belong = True
                    break
        return belong

    def has_max_ratio(self, node, current_ratio, clique):
        new_clique = clique.copy()
        new_clique.append(node)
        if current_ratio >= self.calculate_total_ratio(new_clique):
            return False
        else:
            return True

    def calculate_total_ratio(self, clique):
        total_p_weight = 0
        total_q_weight = 0
        for node in clique:
            total_p_weight += self.graph.get_node(node).p_weight
            total_q_weight += self.graph.get_node(node).q_weight

        return total_p_weight/total_q_weight
