# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging

from instance import Instance


class SolutionGreedy:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, graph: Instance, name):
        self.name = name
        self.graph = graph
        self.density = round(100 * self.graph.calculate_density(), 2)
        self.clique = []
        self.sol_value = 0.0
        self.cardinality = 0.0
        self.compute_time = 0.0

    def find_max_clique(self):
        vertices = list(self.graph.nodes.keys())
        cliques = dict()
        for vertex in vertices:
            clique = [vertices[vertex]]
            for v in vertices:
                if v in clique:
                    continue
                is_next = True
                for u in clique:
                    if u in self.graph.nodes[v].neighbors_indices:
                        continue
                    else:
                        is_next = False
                        break
                if is_next:
                    clique.append(v)

            cliques.update({len(clique): clique})

        max_clique = list(set(cliques.keys()))[-1]
        return sorted(cliques.get(max_clique))
