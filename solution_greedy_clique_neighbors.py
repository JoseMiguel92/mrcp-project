# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random
import time

from instance import Instance


class SolutionGreedyNeighbors:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = self.graph.calculate_density()
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_clique_by_neighbors_wnode(self, vertex):
        vertices = list(self.graph.nodes.keys())
        clique = [vertices[vertex]]
        start_time = time.time()
        self.find_clique_by_neighbors_aux(vertex, vertex, clique)
        finish_time = time.time()
        self.clique = clique
        self.cardinality = len(self.clique)
        self.sol_value = self.calculate_total_ratio(self.clique)
        self.compute_time = finish_time - start_time
        return sorted(clique)

    def find_clique_by_neighbors(self):
        vertices = list(self.graph.nodes.keys())
        vertex = random.randrange(0, len(vertices), 1)
        clique = [vertices[vertex]]
        start_time = time.time()
        self.find_clique_by_neighbors_aux(vertex, vertex, clique)
        finish_time = time.time()
        self.clique = clique
        self.cardinality = len(self.clique)
        self.sol_value = self.calculate_total_ratio(self.clique)
        self.compute_time = finish_time - start_time
        return sorted(clique)

    def find_clique_by_neighbors_aux(self, root, father, clique):
        root_neighbors = self.graph.get_node(root).neighbors_indices
        father_good_neighbors = self.filter_neighbors(root, self.graph.get_node(father).neighbors_indices, clique)
        node_chosen = None
        if father_good_neighbors:
            for node in father_good_neighbors:
                if node_chosen is None:
                    node_chosen = node

                elif self.graph.get_node(node).neighbors_indices.intersection(root_neighbors) > self.graph.get_node(
                        node_chosen).neighbors_indices.intersection(root_neighbors):
                    node_chosen = node

            clique.append(node_chosen)
            self.find_clique_by_neighbors_aux(root, node_chosen, clique)
        else:
            return sorted(clique)

    def filter_neighbors(self, root, neighbors, clique):
        good_neighbors = set()
        for node in neighbors:
            if node in clique:
                continue
            if node not in self.graph.get_node(root).neighbors_indices:
                continue
            good_neighbors.add(node)

        return good_neighbors

    def calculate_total_ratio(self, clique):
        total_p_weight = 0
        total_q_weight = 0
        for node in clique:
            total_p_weight += self.graph.get_node(node).p_weight
            total_q_weight += self.graph.get_node(node).q_weight

        return total_p_weight/total_q_weight
