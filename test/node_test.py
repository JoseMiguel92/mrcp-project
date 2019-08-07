import unittest

from instance import Instance


class InstanceTest(unittest.TestCase):
    GRAPH_TEST_PTH = 'test/test_files/test-random-1.txt'

    def test_read_file_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_TEST_PTH)
        self.assertEqual(graph.get_total_nodes(), '100')
        self.assertEqual(graph.get_total_edges(), '2266')
        self.assertEqual(len(graph.get_nodes()), 100)


if __name__ == '__main__':
    unittest.main()
