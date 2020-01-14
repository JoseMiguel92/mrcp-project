# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random
import time

from instance import Instance
from graph_utils import GraphUtils


class SolutionGreedyRatio:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = self.graph.calculate_density()
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_clique_by_ratio_wnode(self, vertex):
        clique = [vertex]
        start_time = time.time()
        self.find_clique_by_ratio_aux(vertex, vertex, clique)
        if GraphUtils.verify_clique(self.graph, clique):
            print("es clique")
            print(clique)
        else:
            print("no es clique")
            print(clique)
        finish_time = time.time()
        self.clique = clique
        self.cardinality = len(self.clique)
        self.sol_value = self.calculate_total_ratio(self.clique)
        self.compute_time = finish_time - start_time
        return sorted(clique)

    def find_clique_by_ratio(self):
        vertices = list(self.graph.nodes.keys())
        vertex = random.randrange(0, len(vertices), 1)
        return self.find_clique_by_ratio_wnode(vertex)

    def find_clique_by_ratio_aux(self, root, father, clique):
        father_neighbors = self.graph.get_node(father).neighbors_indices
        current_ratio = -1
        node_chosen = None
        if father_neighbors:
            for node in father_neighbors:
                if node_chosen is None:
                    node_chosen = node
                    continue
                elif self.belong_to_clique(node, clique):
                    better_ratio, current_ratio = self.has_max_ratio(node, current_ratio, clique)
                    if better_ratio:
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
        new_ratio = self.calculate_total_ratio(new_clique)
        if current_ratio >= new_ratio:
            return False, current_ratio
        else:
            return True, new_ratio

    def calculate_total_ratio(self, clique):
        total_p_weight = 0
        total_q_weight = 0
        for node in clique:
            total_p_weight += self.graph.get_node(node).p_weight
            total_q_weight += self.graph.get_node(node).q_weight

        return total_p_weight/total_q_weight
