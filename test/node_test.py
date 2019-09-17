# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest

from instance import Instance
from solution import Solution


class InstanceTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-graph-type-1.txt'
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-simple-1.txt'
    GRAPH_SIMPLE_2_TEST_PTH = 'test_files/test-graph-simple-2.txt'

    def test_read_file_ok(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_1_TEST_PTH)
        self.assertEqual(100, graph.get_total_nodes())
        self.assertEqual(2266, graph.get_total_edges())
        self.assertEqual(100, len(graph.get_nodes()), 100)
        self.assertTrue(graph.are_adjacents(graph.get_node(0), graph.get_node(1)))

    def test_obtain_clique_ok(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_SIMPLE_1_TEST_PTH)
        solution = Solution(graph)
        self.assertTrue(solution.is_clique())

    def test_obtain_clique_ko(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_SIMPLE_2_TEST_PTH)
        solution = Solution(graph)
        self.assertFalse(solution.is_clique())


if __name__ == '__main__':
    unittest.main()
