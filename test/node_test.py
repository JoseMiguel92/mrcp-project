import unittest

from instance import Instance


class InstanceTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-random-1.txt'
    GRAPH_2_TEST_PTH = 'test_files/test-random-2.txt'
    GRAPH_3_TEST_PTH = 'test_files/test-random-3.txt'
    GRAPH_4_TEST_PTH = 'test_files/test-random-4.txt'
    GRAPH_5_TEST_PTH = 'test_files/test-random-5.txt'

    def test_read_file_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_1_TEST_PTH)
        self.assertEqual(graph.get_total_nodes(), 100)
        self.assertEqual(graph.get_total_edges(), 2266)
        self.assertEqual(len(graph.get_nodes()), 100)

    def test_read_file_File2_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_2_TEST_PTH)
        self.assertEqual(graph.get_total_nodes(), 150)
        self.assertEqual(graph.get_total_edges(), 5212)
        self.assertEqual(len(graph.get_nodes()), 150)


if __name__ == '__main__':
    unittest.main()
