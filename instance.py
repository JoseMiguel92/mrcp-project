import csv

from node import Node


class Instance:
    def __init__(self):
        self.total_nodes = 0
        self.total_edges = 0
        self.nodes = dict()

    def get_total_nodes(self):
        return self.total_nodes

    def get_total_edges(self):
        return self.total_edges

    def get_nodes(self):
        return self.nodes

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def are_adjacents(self, node_id_1, node_id_2):
        return self.nodes.get(node_id_1).is_adjacent(node_id_2)

    def add_node(self, node_id, node):
        self.nodes.update({node_id: node})

    def _fill_neighbors_indices(self, node, neighbors):
        for neighbor in neighbors:
            if neighbor != '':
                node.get_neighbor_indices().append(neighbor)

    def read_file(self, file_path):
        count_line = 0
        node_id = 0
        with open(file_path) as file:
            for line in csv.reader(file, dialect='excel-tab'):
                if count_line == 0 and line[0] != '' and line[1] != '':
                    self.total_nodes = line[0]
                    self.total_edges = line[1]
                    count_line += 1
                    continue
                elif line[0] != '' and line[1] != '' and line[2] != '':
                    node = Node(node_id, line[0], line[1], line[2])
                    if line[3] != '':
                        self._fill_neighbors_indices(node, line[3:])
                    self.add_node(node_id, node)
                    node_id += 1
