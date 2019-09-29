# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest

from instance import Instance
from solution import Solution
from graph_utils import GraphUtils


class SolutionTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-graph-type-1.txt'
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-simple-1.txt'
    GRAPH_SIMPLE_2_TEST_PTH = 'test_files/test-graph-simple-2.txt'
    GRAPH_SIMPLE_s2_TEST_PTH = 'test_files/test-graph-simple-s2.txt'
    GRAPH_SIMPLE_3_TEST_PTH = 'test_files/test-graph-simple-3.txt'
    CSV_OUTPUT_FILE = "test_files/output/table_test.csv"

    def test_solution_1(self):
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_SIMPLE_1_TEST_PTH)
        solution = Solution(graph)
        cliques = solution.get_solution()
        print(cliques)
        expected_sol = [{0, 1, 2}]
        self.assertEqual(expected_sol, cliques)

    def test_solution_s2(self):
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_SIMPLE_s2_TEST_PTH)
        solution = Solution(graph)
        cliques = solution.get_solution()
        print(cliques)
        expected_sol = [{0, 1, 2}, {0, 2, 3}]
        self.assertEqual(expected_sol, cliques)

    def test_solution_3(self):
        graph = Instance()
        graph.read_file(SolutionTest.GRAPH_SIMPLE_3_TEST_PTH)
        solution = Solution(graph)
        cliques = solution.get_solution()
        print(cliques)
        expected_sol = [{0, 1, 4}, {1, 2}, {2, 3, 5}]
        self.assertEqual(expected_sol, cliques)


if __name__ == '__main__':
    unittest.main()
