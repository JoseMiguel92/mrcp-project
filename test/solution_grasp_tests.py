# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest
import random

from instance import Instance
from solution_greedy_clique_neighbors import SolutionGreedyNeighbors
from solution_greedy_clique_ratio import SolutionGreedyRatio


class SolutionGraspTests(unittest.TestCase):
    ADJACENT = "adjacent"
    RATIO = "ratio"
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-type-1.txt'

    def test_grasp_OK(self):
        graph = Instance()
        file = SolutionGraspTests.GRAPH_SIMPLE_1_TEST_PTH
        graph.read_file(file)  # parametro
        solution_type = self.ADJACENT  # parametro
        fixed_seed = 1  # parametro
        number_vertices = len(graph.nodes)
        random.seed(fixed_seed)
        vertex = random.randint(0, number_vertices-1)
        g_v = None

        if solution_type == self.ADJACENT:
            sgn = SolutionGreedyNeighbors(graph, file)
            g_v = sgn.find_clique_by_neighbors_wnode(vertex)
        if solution_type == self.RATIO:
            sgr = SolutionGreedyRatio(graph, file)
            g_v = sgr.find_clique_by_ratio_wnode(vertex)
        solution = {vertex}
        cl = graph.nodes.keys()  # lista de nodos del grafo
        while len(cl) != 0:
            g_min, g_max = self.get_g(cl, g_v)
            alpha = 0.33  # rango entre 0.0 y 1.0  # parametro
            mu = g_max - alpha * (g_max - g_min)
            rcl = self.get_rcl(mu, g_v, cl)  # lista con los g(v) pertenecientes a cl mayores que mu
            random.seed(fixed_seed)
            random_position = random.randint(0, len(rcl) - 1)
            u = rcl[random_position]
            solution = solution.union({u})
            cl -= {u}
            cl -= cl.intersection(graph.get_node(u).neighbors_indices)  # todos los nodos no adyacentes a u de g(v)?

    def get_g(self, candidates_list, g_v):
        g_v_set = set(g_v)
        g_v_set.intersection_update(candidates_list)
        g_min = min(g_v_set)
        g_max = max(g_v_set)
        return g_min, g_max

    def get_rcl(self, mu, node_list, candidates_list):
        remaining_candidates = sorted(list(set(node_list) & set(candidates_list)))
        remaining_candidates.reverse()
        position = 0
        for candidate in remaining_candidates:
            if candidate < mu:
                break
            else:
                position += 1
        return remaining_candidates[:position]

    def test_random_seed(self):
        for i in range(13):
            random.seed(1)
            num = random.sample(range(10), 10)
            print("{0} : {1}".format(i, num))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
