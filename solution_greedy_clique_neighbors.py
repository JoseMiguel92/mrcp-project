# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random

from instance import Instance


class SolutionGreedyNeighbors:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = round(100 * self.graph.calculate_density(), 2)
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_clique_by_neighbors_wnode(self, vertex):
        vertices = list(self.graph.nodes.keys())
        clique = [vertices[vertex]]
        self.find_clique_by_neighbors_aux(vertex, vertex, clique)
        self.clique = clique
        self.cardinality = len(self.clique)
        return sorted(clique)

    def find_clique_by_neighbors(self):
        vertices = list(self.graph.nodes.keys())
        vertex = random.randrange(0, len(vertices), 1)
        clique = [vertices[vertex]]
        self.find_clique_by_neighbors_aux(vertex, vertex, clique)
        self.clique = clique
        self.cardinality = len(self.clique)
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
