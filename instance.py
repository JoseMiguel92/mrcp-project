import csv

from node import Node


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

    def are_adjacents(self, node_1, node_2):
        return node_1.is_adjacent(node_2)

    def add_node(self, node_id, node):
        self.nodes.update({node_id: node})

    def _fill_neighbors_indices(self, node, neighbors):
        for neighbor in neighbors:
            if neighbor != '':
                node.get_neighbor_indices().add(int(neighbor))

    def read_file(self, file_path):
        """Read a file of the path passed as a parameter (treated as a csv) and fill in the object data.
        Args:
            file_path (str): Path to the file that will be read and become an object.
        """
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
                        self._fill_neighbors_indices(node, line[3:])
                    self.add_node(node_id, node)
                    node_id += 1
