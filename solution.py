# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import time

from instance import Instance


class Solution:

    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = round(100 * self.graph.calculate_density(), 2)
        self.cliques = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_max_cliques_chosen_node(self, r, p, x, graph, cliques):
        if len(p) == 0 and len(x) == 0:
            cliques.append(r)
        else:
            chosen_node = next(iter(p.union(x)))
            for vertex in p.difference(graph.get_node(chosen_node).get_neighbor_indices()):
                neighbors = graph.get_node(vertex).get_neighbor_indices()
                self.find_max_cliques_chosen_node(r.union({vertex}), p.intersection(neighbors),
                                                  x.intersection(neighbors), graph, cliques)
                p.remove(vertex)
                x.add(vertex)

    def set_solution_max_cliques(self):
        start_time = time.time()
        p = set(self.graph.get_nodes().keys())
        r = set()
        x = set()
        graph = self.graph
        cliques = []
        for vertex in graph.get_nodes().keys():
            neighbors = graph.get_node(vertex).get_neighbor_indices()
            self.find_max_cliques_chosen_node(r.union({vertex}), p.intersection(neighbors), x.intersection(neighbors),
                                              graph, cliques)
            p.remove(vertex)
            x.add(vertex)

        self.compute_time = time.time() - start_time
        self.cliques = cliques

    def get_solution_max_cliques(self):
        if not self.cliques:
            self.set_solution_max_cliques()
            return self.cliques
        else:
            return self.cliques

    def collect_sol_data(self):
        data = dict()
        data.update({self.name: [self.graph.get_total_nodes(), self.density, self.sol_value,
                                 self.cardinality, self.compute_time]})
        return data
