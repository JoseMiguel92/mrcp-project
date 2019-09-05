import unittest

from instance import Instance


class InstanceTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-graph-type-1.txt'

    def test_read_file_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_1_TEST_PTH)
        self.assertEqual(100, graph.get_total_nodes())
        self.assertEqual(2266, graph.get_total_edges())
        self.assertEqual(100, len(graph.get_nodes()), 100)
        self.assertTrue(graph.are_adjacents(graph.get_node(0), graph.get_node(1)))


if __name__ == '__main__':
    unittest.main()
