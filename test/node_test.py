# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import os, shutil
import unittest

from graph_utils import GraphUtils
from instance import Instance
from solution import Solution


class NodeTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-graph-type-1.txt'
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-simple-1.txt'
    GRAPH_SIMPLE_2_TEST_PTH = 'test_files/test-graph-simple-2.txt'
    CSV_OUTPUT_DIR = "test_files/output"
    CSV_OUTPUT_FILE = "table_test.csv"

    def test_read_file_ok(self):
        graph = Instance()
        graph.read_file(NodeTest.GRAPH_1_TEST_PTH)
        self.assertEqual(100, graph.get_total_nodes())
        self.assertEqual(2266, graph.get_total_edges())
        self.assertEqual(100, len(graph.get_nodes()), 100)
        self.assertTrue(GraphUtils.are_adjacent(graph.get_node(0), graph.get_node(1)))

    def test_obtain_clique_ok(self):
        graph = Instance()
        graph.read_file(NodeTest.GRAPH_SIMPLE_1_TEST_PTH)
        solution = Solution(graph)
        self.assertTrue(GraphUtils.is_clique(solution.get_graph()))

    def test_obtain_clique_ko(self):
        graph = Instance()
        graph.read_file(NodeTest.GRAPH_SIMPLE_2_TEST_PTH)
        solution = Solution(graph)
        self.assertFalse(GraphUtils.is_clique(solution.get_graph()))

    def test_create_table(self):
        if not os.path.isdir(NodeTest.CSV_OUTPUT_DIR):
            os.mkdir(NodeTest.CSV_OUTPUT_DIR)

        data = dict()
        data.update({'random-1': [100, 45.78]})
        data.update({'random-2': [150, 64.46]})
        csv_columns = ['|V|', 'D(%)']
        try:
            if os.altsep is None:
                file_sep = os.sep
            path = NodeTest.CSV_OUTPUT_DIR + file_sep + NodeTest.CSV_OUTPUT_FILE
            GraphUtils.create_csv_table(path, data, csv_columns)
            self.assertTrue(os.path.isfile(path))
        except IOError:
            self.fail("Test failed.")

        finally:
            if os.path.isdir(NodeTest.CSV_OUTPUT_DIR):
                shutil.rmtree(NodeTest.CSV_OUTPUT_DIR)


if __name__ == '__main__':
    unittest.main()
