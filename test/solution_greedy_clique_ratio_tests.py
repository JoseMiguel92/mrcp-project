# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest

from instance import Instance
from solution_greedy_clique_ratio import SolutionGreedy


class SolutionGreedyCliqueRatioTest(unittest.TestCase):
    GRAPH_1_TEST = 'test_files/test-graph-greedy-simple-1.txt'
    GRAPH_2_TEST = "test_files/test-graph-type-1.txt"
    GRAPH_3_TEST = "test_files/test_graph_type_1_worst.txt"

    CSV_OUTPUT_FILE = "test_files/output/solution_table.csv"

    def test_find_ratio_clique_1_OK(self):
        pass


if __name__ == '__main__':
    unittest.main()
