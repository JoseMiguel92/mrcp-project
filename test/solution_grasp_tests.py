# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import unittest
import random
import bisect

from instance import Instance
from solution_grasp import SolutionGrasp


class SolutionGraspTests(unittest.TestCase):
    GRAPH_TEST = 'test_files/set-e/DIMACS2/johnson8-2-4.txt'
    GRAPH_SIMPLE_1_TEST_PTH = 'test_files/test-graph-type-1.txt'

    def test_grasp_OK(self):
        graph = Instance()
        file = SolutionGraspTests.GRAPH_SIMPLE_1_TEST_PTH
        graph.read_file(file)
        solution_type = SolutionGrasp.ADJACENT
        fixed_seed = 1
        alpha = 0.5
        instance_solution = SolutionGrasp()
        result = instance_solution.find_grasp_solution(graph, file, solution_type, fixed_seed, alpha)

    def test_random_seed(self):
        for i in range(13):
            random.seed(1)
            num = random.sample(range(10), 10)
            print("{0} : {1}".format(i, num))
        self.assertTrue(True)

    def test_bisect(self):
        g_c = list()
        bisect.insort(g_c, 100)
        bisect.insort(g_c, 90)
        bisect.insort(g_c, 30)
        bisect.insort(g_c, 45)
        bisect.insort(g_c, 60)
        bisect.insort(g_c, 59)
        print(g_c)
        num = 59
        pos = bisect.bisect_left(g_c, num)
        print(pos)
        g_c_result = g_c[pos:]
        g_c_result.reverse()
        print(g_c_result)

    def test_random(self):
        a = dict()
        for i in range(10):
            num_r = random.randint(0, 100)
            gen = {i:num_r}
            a.update(gen)
            print("{1} : {0}".format(num_r, i+1))
        for k, v in a:
            print("clave= {0}: valor= {1}".format(k, v))

    def test_apply_ls(self):
        solution = {16, 18, 19, 20, 21, 23}
        graph = Instance()
        file = SolutionGraspTests.GRAPH_TEST
        graph.read_file(file)
        instace_sol = SolutionGrasp()
        instace_sol.apply_ls(graph, solution)


if __name__ == '__main__':
    unittest.main()
