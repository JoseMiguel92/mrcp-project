# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest
import os


from instance import Instance
from solution_greedy_clique_ratio import SolutionGreedyRatio


class SolutionGreedyCliqueRatioTest(unittest.TestCase):
    GRAPH_1_TEST = 'test_files/test-graph-greedy-simple-1.txt'
    GRAPH_2_TEST = "test_files/test-graph-type-1.txt"
    GRAPH_3_TEST = "test_files/test_graph_type_1_worst.txt"

    CSV_OUTPUT_FILE = "test_files/output/solution_table.csv"

    def test_find_ratio_clique_1_OK(self):
        file = SolutionGreedyCliqueRatioTest.GRAPH_2_TEST
        graph = Instance()
        graph.read_file(file)
        solution = SolutionGreedyRatio(graph, os.path.splitext(file)[0])
        clique = solution.find_clique_by_ratio()
        print(clique)
        print(solution.cardinality)
        print(solution.sol_value)

    def test_find_ratio_clique_2_OK(self):
        file = SolutionGreedyCliqueRatioTest.GRAPH_3_TEST
        graph = Instance()
        graph.read_file(file)
        solution = SolutionGreedyRatio(graph, os.path.splitext(file)[0])
        clique = solution.find_clique_by_ratio()
        print(clique)
        print(solution.cardinality)
        print(solution.sol_value)


if __name__ == '__main__':
    unittest.main()
