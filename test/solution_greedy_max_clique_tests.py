# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest

from instance import Instance
from solution_greedy_max_clique import SolutionGreedy


class SolutionGreedyMaxCliqueTest(unittest.TestCase):
    GRAPH_1_TEST = 'test_files/test-graph-greedy-simple-1.txt'
    GRAPH_2_TEST = "test_files/test-graph-type-1.txt"
    GRAPH_3_TEST = "test_files/test_graph_type_1_worst.txt"

    CSV_OUTPUT_FILE = "test_files/output/solution_table.csv"

    def test_find_max_clique_1_OK(self):
        graph = Instance()
        graph.read_file(SolutionGreedyMaxCliqueTest.GRAPH_1_TEST)
        solution = SolutionGreedy(graph, 'test_graph_greedy_simple_1')
        max_clique = solution.find_max_clique()
        print(max_clique)
        self.assertEqual([1, 2, 3, 5], max_clique)

    def test_find_max_clique_2_OK(self):
        graph = Instance()
        graph.read_file(SolutionGreedyMaxCliqueTest.GRAPH_2_TEST)
        solution = SolutionGreedy(graph, 'test_graph_type_1')
        max_clique = solution.find_max_clique()
        print(max_clique)
        self.assertEqual([3, 11, 17, 21, 25, 28, 32, 36, 38, 39, 66, 72], max_clique)

    def test_find_max_clique_3_OK(self):
        graph = Instance()
        graph.read_file(SolutionGreedyMaxCliqueTest.GRAPH_3_TEST)
        solution = SolutionGreedy(graph, 'test_graph_type_1_worst')
        max_clique = solution.find_max_clique()
        print(max_clique)
        self.assertEqual([0, 6, 7, 8, 9, 40, 92, 99, 109, 115, 142, 154, 284, 307, 366, 379, 402, 412, 429, 448],
                         max_clique)


if __name__ == '__main__':
    unittest.main()
