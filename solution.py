# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from instance import Instance


class Solution:

    def __init__(self, graph: Instance):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def get_max_degree_node(self, nodes):
        nodes.sort(key=lambda node: node.get_degree(), reverse=True)
        return nodes.index(0)

    def ben_alg(self, r, p, x, graph):
        if len(p) == 0 and len(x) == 0:
            yield r
        for vertex in p.copy():
            r1 = r | {vertex}
            p1 = set([vertex_1 for vertex_1 in p if vertex_1 in graph.get_node(vertex).get_neighbor_indices()])
            x1 = set([vertex_1 for vertex_1 in x if vertex_1 in graph.get_node(vertex).get_neighbor_indices()])

            for node_r in self.ben_alg(r1, p1, x1, graph):
                yield node_r
            p.remove(vertex)
            x.add(vertex)

    def get_solution(self):
        r = set()
        p = set(self.get_graph().get_nodes().keys())
        x = set()
        graph = self.get_graph()
        return list(self.ben_alg(r, p, x, graph))
