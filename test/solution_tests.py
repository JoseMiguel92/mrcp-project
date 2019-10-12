# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import os
import unittest

from instance import Instance
from solution import Solution


class SolutionTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-graph-type-1.txt'
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-simple-1.txt'
    GRAPH_SIMPLE_2_TEST_PTH = 'test_files/test-graph-simple-2.txt'
    GRAPH_SIMPLE_s2_TEST_PTH = 'test_files/test-graph-simple-s2.txt'
    GRAPH_SIMPLE_3_TEST_PTH = 'test_files/test-graph-simple-3.txt'
    CSV_OUTPUT_FILE = "test_files/output/solution_table.csv"

    def test_solution_OK(self):
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_SIMPLE_1_TEST_PTH)
        solution = Solution(graph, 'test-graph-simple-1')
        cliques = solution.get_solution_max_cliques()
        print(cliques)
        expected_sol = [{0, 1, 2}]
        self.assertEqual(expected_sol, cliques)

    def test_calculate_density(self):
        exp_den = 45.78
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_1_TEST_PTH)
        percentage_cal_den = graph.calculate_density() * 100
        self.assertEqual(exp_den, round(percentage_cal_den, 2))

    def test_complete_1_sol(self):
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_1_TEST_PTH)
        solution = Solution(graph, 'random-1')
        cliques = solution.get_solution_max_cliques()
        self.assertTrue(os.path.isfile(self.CSV_OUTPUT_FILE))


if __name__ == '__main__':
    unittest.main()
