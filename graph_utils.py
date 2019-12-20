# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random
import os

import pandas as pd

from instance import Instance
from logger.logger import Logger

# Logs
Logger.init_log()
LOGGER = logging.getLogger(__name__)

LOG_ERROR_WRITE_DOC = 'Error when writing a file.'


class GraphUtils:

    @staticmethod
    def are_adjacent(node_1, node_2):
        return node_1.is_adjacent(node_2)

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
    def create_mrcp_csv_table(path, data):
        """ Create a csv file in disk with table result of the clique search in a graph.
            The columns are:
                |V|: Number of vertices of the graph.
                D(%): Density of the graph.
                ƒ: solution value.
                c: cardinality.
                t(sec): computation time in seconds.
            Args:
                path to save a file.
                data to fill the table.
        """
        csv_columns = ['|V|', 'D(%)', 'ƒ', 'c', 't(sec)', 'α']
        df = pd.DataFrame.from_dict(data, orient='index', columns=csv_columns)
        df.to_csv(path, sep=';', index=True)

    @staticmethod
    def get_random_node(nodes):
        return random.randint(0, len(nodes))

    @staticmethod
    def get_max_degree_node(self, nodes):
        nodes.sort(key=lambda node: node.get_degree(), reverse=True)
        return nodes.index(0)

    @staticmethod
    def export_solution(output, data, name):
        if not os.path.isdir(output):
            os.mkdir(output)
        try:
            if os.altsep is None:
                file_sep = os.sep
            path = output + file_sep + name
            GraphUtils.create_mrcp_csv_table(path, data)
        except IOError:
            LOGGER.error(LOG_ERROR_WRITE_DOC)

    @staticmethod
    def calculate_clique_ratio(graph, clique):
        total_p_weight = 0
        total_q_weight = 0
        for node in clique:
            total_p_weight += graph.get_node(node).p_weight
            total_q_weight += graph.get_node(node).q_weight

        return total_p_weight / total_q_weight

    @staticmethod
    def calculate_solution(graph, clique):
        ratio = GraphUtils.calculate_clique_ratio(graph, clique)
        density = graph.calculate_density()
        cardinality = len(clique)
        return ratio, density, cardinality
