# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import csv
import os

from node import Node
from graph_utils import GraphUtils


class Instance:
    """ Represent a graph """

    def __init__(self):
        self.total_nodes = 0  #: Total of nodes of this graph.
        self.total_edges = 0  #: Total of edges of this graph.
        self.nodes = dict()  #: Dictionary with the set of nodes of this graph with their specific data.

    def get_total_nodes(self):
        return self.total_nodes

    def get_total_edges(self):
        return self.total_edges

    def get_nodes(self):
        return self.nodes

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def add_node(self, node_id, node):
        self.nodes.update({node_id: node})

    def set_total_nodes(self, total_nodes):
        self.total_nodes = total_nodes

    def set_total_edges(self, total_edges):
        self.total_edges = total_edges

    def _fill_neighbors_dict(self):
        for node in self.get_nodes().values():
            for neighbor in node.get_neighbor_indices():
                node_neighbor = self.get_nodes().get(neighbor)
                node.get_neighbors_dict().update({node_neighbor.get_node_id(): node_neighbor})

    def read_file(self, file_path):
        """Read a file of the path passed as a parameter (treated as a csv) and fill in the object data.
        Args:
            file_path (str): Path to the file that will be read and become an object.
        """
        if GraphUtils.TYPE_DIMACS2 in file_path:
            if GraphUtils.SET_SET_E in file_path:
                self.read_dimacs2_file(file_path, GraphUtils.SET_SET_E)
            else:
                self.read_dimacs2_file(file_path, GraphUtils.SET_SET_F)
        elif GraphUtils.TYPE_DIMACS10 in file_path:
            if GraphUtils.SET_SET_E in file_path:
                self.read_dimacs10_file(file_path, GraphUtils.SET_SET_E)
            else:
                self.read_dimacs10_file(file_path, GraphUtils.SET_SET_F)
        else:
            self.read_sets_file(file_path)

    def read_sets_file(self, file_path):
        count_line = 0
        node_id = 0
        with open(file_path) as file:
            for line in csv.reader(file, dialect='excel-tab'):
                if count_line == 0 and line[0] != '' and line[1] != '':
                    self.total_nodes = int(line[0])
                    self.total_edges = int(line[1])
                    count_line += 1
                    continue
                elif line[0] != '' and line[1] != '' and line[2] != '':
                    node = Node(node_id, float(line[0]), float(line[1]), int(line[2]))
                    if line[3] != '':
                        node.fill_neighbors_indices(line[3:])
                    self.add_node(node_id, node)
                    node_id += 1
        self._fill_neighbors_dict()

    def read_dimacs2_file(self, file_path, type_set):
        count_line = 0
        with open(file_path) as file:
            for line in csv.reader(file, dialect='excel-tab'):
                if count_line == 0 and line[0] != '' and line[1] != '':
                    self.total_nodes = int(line[0])
                    self.total_edges = int(line[1])
                    count_line += 1
                    continue
                elif line[0] != '' and line[1] != '':
                    if int(line[0]) not in self.nodes.keys():
                        node = Node()
                        node.node_id = int(line[0])
                        node.neighbors_indices.add(int(line[1]))
                        node.apply_type_set(type_set, self.total_nodes)
                        self.add_node(node.node_id, node)
                    else:
                        self.nodes.get(int(line[0])).neighbors_indices.add(int(line[1]))
                    if int(line[1]) not in self.nodes.keys():
                        node = Node()
                        node.node_id = int(line[1])
                        node.neighbors_indices.add(int(line[0]))
                        node.apply_type_set(type_set, self.total_nodes)
                        self.add_node(node.node_id, node)
                    else:
                        self.nodes.get(int(line[1])).neighbors_indices.add(int(line[0]))

        if type_set == GraphUtils.SET_SET_E:
            self._add_extra_vertex()

        self._fill_neighbors_dict()

    def read_dimacs10_file(self, file_path, type_set):
        count_line = 0
        node_id = 1
        with open(file_path) as file:
            for line in csv.reader(file, dialect='excel-tab'):
                if count_line == 0 and line[0] != '' and line[1] != '':
                    self.total_nodes = int(line[0])
                    self.total_edges = int(line[1])
                    count_line += 1
                    continue
                elif line[0] != '' and line[1] != '':
                    node = Node(node_id, 0.0, 0.0, int(line[0]))
                    node.apply_type_set(type_set, self.total_nodes)
                    if line[1] != '':
                        node.fill_neighbors_indices(line[1:])
                    self.add_node(node_id, node)
                    node_id += 1

        if type_set == GraphUtils.SET_SET_E:
            self._add_extra_vertex()

        self._fill_neighbors_dict()

    def _add_extra_vertex(self):
        total_keys = sorted(list(self.nodes.keys()))
        node_id = total_keys[-1] + 1
        node = Node(node_id, 1, 1, len(self.nodes))
        node.neighbors_indices = set(total_keys)
        self.add_node(node_id, node)

    def calculate_density(self):
        return round(100 * (2 * self.get_total_edges()) / (self.get_total_nodes() * (self.get_total_nodes() - 1)), 2)
