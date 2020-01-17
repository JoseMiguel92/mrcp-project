# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import time
from abc import ABCMeta, abstractmethod

from graph_utils import GraphUtils


class SolutionGreedy(metaclass=ABCMeta):
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph, name):
        self.name = name
        self.graph = graph
        self.density = self.graph.calculate_density()
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_clique(self, vertex):
        clique = [vertex]
        start_time = time.time()
        self.find_clique_aux(vertex, clique)
        finish_time = time.time()
        self.clique = clique
        self.cardinality = len(self.clique)
        self.sol_value = GraphUtils.calculate_clique_ratio(self.graph, self.clique)
        self.compute_time = finish_time - start_time
        return clique

    def find_clique_aux(self, father, clique):
        adjacent = self.graph.get_node(father).neighbors_indices.copy()
        while len(adjacent) != 0:
            candidate = self.find_better(adjacent)
            if GraphUtils.become_clique(self.graph, clique, candidate):
                adjacent = GraphUtils.discard_adjacent(self.graph, adjacent, candidate)
                clique.append(candidate)
            else:
                adjacent.remove(candidate)

    @abstractmethod
    def find_better(self, adjacent):
        pass
