# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from graph_utils import GraphUtils


class Node:

    def __init__(self, node_id=0, p_weight=0.0, q_weight=0.0, degree=0):
        self.node_id = node_id
        self.p_weight = p_weight
        self.q_weight = q_weight
        self.degree = degree
        self.neighbors_indices = set()
        self.neighbors_dict = dict()

    def set_node_id(self, node_id):
        self.node_id = node_id

    def set_p_weight(self, p_weight):
        self.p_weight = p_weight

    def set_q_weight(self, q_weight):
        self.q_weight = q_weight

    def set_degree(self, degree):
        self.degree = degree

    def set_neighbor_indices(self, neighbor_indices):
        self.neighbors_indices = neighbor_indices

    def fill_neighbors_indices(self, neighbors):
        for neighbor in neighbors:
            if neighbor != '':
                self.get_neighbor_indices().add(int(neighbor))

    def get_node_id(self):
        return self.node_id

    def get_p_weight(self):
        return self.p_weight

    def get_q_weight(self):
        return self.q_weight

    def get_degree(self):
        return self.degree

    def get_neighbor_indices(self):
        return self.neighbors_indices

    def get_neighbors_dict(self):
        return self.neighbors_dict

    def is_adjacent(self, node):
        return node.get_node_id() in self.get_neighbor_indices()

    def apply_type_set(self, type_set, total_nodes):
        if type_set == GraphUtils.SET_SET_E:
            self.p_weight = 1
            self.q_weight = 2
        elif type_set == GraphUtils.SET_SET_F:
            self.p_weight = self.node_id
            self.q_weight = total_nodes - self.node_id + 1
        else:
            raise Exception("Set type does not exists.")
