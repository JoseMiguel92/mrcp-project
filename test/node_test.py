import unittest

from instance import Instance


class InstanceTest(unittest.TestCase):
    GRAPH_1_TEST_PTH = 'test_files/test-random-1.txt'
    GRAPH_2_TEST_PTH = 'test_files/test-random-2.txt'
    GRAPH_3_TEST_PTH = 'test_files/test-random-3.txt'
    GRAPH_4_TEST_PTH = 'test_files/test-random-4.txt'
    GRAPH_5_TEST_PTH = 'test_files/test-random-5.txt'
    GRAPH_6_TEST_PTH = 'test_files/test-random-6.txt'
    GRAPH_7_TEST_PTH = 'test_files/test-random-7.txt'
    GRAPH_8_TEST_PTH = 'test_files/test-random-8.txt'
    GRAPH_9_TEST_PTH = 'test_files/test-random-9.txt'
    GRAPH_10_TEST_PTH = 'test_files/test-random-10.txt'
    GRAPH_MARKET1_TEST_PTH = 'test_files/test-market-1.txt'
    GRAPH_WIND2004_TEST_PTH = 'test_files/test-wind-2004.txt'

    def test_read_file_FileRandom1_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_1_TEST_PTH)
        self.assertEqual(100, graph.get_total_nodes())
        self.assertEqual(2266, graph.get_total_edges())
        self.assertEqual(100, len(graph.get_nodes()), 100)

    def test_read_file_FileMarket1_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_MARKET1_TEST_PTH)
        self.assertEqual(500, graph.get_total_nodes())
        self.assertEqual(23116, graph.get_total_edges())
        self.assertEqual(500, len(graph.get_nodes()))

    def test_read_file_FileWind2004_OK(self):
        graph = Instance()
        graph.read_file(InstanceTest.GRAPH_WIND2004_TEST_PTH)
        self.assertEqual(500, graph.get_total_nodes())
        self.assertEqual(10277, graph.get_total_edges())
        self.assertEqual(500, len(graph.get_nodes()))


if __name__ == '__main__':
    unittest.main()
