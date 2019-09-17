# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import random
from instance import Instance


class Solution:
    def __init__(self, graph: Instance):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def get_random_node(self):
        nodes = self.graph.get_nodes()
        random_node_id = random.randint(0, len(nodes))
        return self.graph.get_node(random_node_id)

    def is_clique(self):
        """Check if a graph is a clique (all nodes of graph are connected to all others
        nodes of graph).
            Args:
                 graph that check if is a clique.
            Returns:
                 bool: True if is a clique, False otherwise."""
        clique = True
        nodes = self.graph.get_nodes()
        for node in nodes.values():
            if len(set(nodes.keys()) - node.get_neighbor_indices()) > 1:
                return False
        return clique
