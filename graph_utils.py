# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from instance import Instance
import logging
import pandas as pd
import random

from logger.logger import Logger

# Logs
Logger.init_log()
LOGGER = logging.getLogger(__name__)


class GraphUtils:

    @staticmethod
    def are_adjacent(node_1, node_2):
        return node_1.is_adjacent(node_2)

    @staticmethod
    def create_graph(list_nodes):
        graph = Instance()
        graph.set_graph(list_nodes)
        return graph

    @staticmethod
    def is_clique(graph: Instance):
        """Check if a graph is a clique (all nodes of graph are connected to other
        nodes of graph).
            Args:
                 graph that check if is a clique.
            Returns:
                 bool: True if is a clique, False otherwise."""
        clique = True
        for node in graph.get_nodes().values():
            for node_to_compare in graph.get_nodes().values():
                if node.get_node_id() != node_to_compare.get_node_id():
                    if not GraphUtils.are_adjacent(node_to_compare, node):
                        return False
        return clique

    @staticmethod
    def create_csv_table(path, data, csv_columns):
        df = pd.DataFrame.from_dict(data, orient='index', columns=csv_columns)
        df.to_csv(path, sep=';', index=True)

    @staticmethod
    def get_random_node(graph):
        nodes = graph.get_nodes()
        random_node_id = random.randint(0, len(nodes))
        return graph.get_node(random_node_id)
