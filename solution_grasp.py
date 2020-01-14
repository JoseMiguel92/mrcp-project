# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random
import bisect

from solution_greedy_clique_neighbors import SolutionGreedyNeighbors
from solution_greedy_clique_ratio import SolutionGreedyRatio


class SolutionGrasp:
    ADJACENT = "adjacent"
    RATIO = "ratio"
    LOGGER = logging.getLogger(__name__)

    def find_grasp_solution(self, graph, name, solution_type, fixed_seed, alpha):
        """ Finf solution on graph with a GRASP algorithm. """
        number_vertices = len(graph.nodes)
        random.seed(fixed_seed)
        total_keys = sorted(list(graph.nodes.keys()))
        vertex = random.randint(total_keys[0], total_keys[-1])
        solution = {vertex}
        cl = graph.nodes[vertex].neighbors_indices
        while len(cl) != 0:
            g_min, g_max = self.get_g(cl, solution_type, graph, name)
            mu = g_max - alpha * (g_max - g_min)
            rcl = self.get_rcl(mu, cl)
            random.seed(fixed_seed)
            random_position = random.randint(0, len(rcl) - 1)
            u = rcl[random_position]
            solution = solution.union({u})
            cl -= {u}
            cl -= cl.intersection(graph.get_node(u).neighbors_indices)
        return solution

    def get_g(self, candidates_list, solution_type, graph, name):
        """ Find g_min and g_max with current candidate list and solution type chosen. """
        g_c = dict()
        for candidate in candidates_list:
            chosen_solution = None
            if solution_type == self.ADJACENT:
                chosen_solution = SolutionGreedyNeighbors(graph, name)
                chosen_solution.find_clique_by_neighbors_wnode(candidate)
            if solution_type == self.RATIO:
                chosen_solution = SolutionGreedyRatio(graph, name)
                chosen_solution.find_clique_by_ratio_wnode(candidate)
            g_c.update({candidate: chosen_solution.sol_value})
        sorted_gc = sorted(g_c.items(), key=lambda kv: kv[1])
        g_min = sorted_gc[0]
        g_max = sorted_gc[-1]
        return g_min[0], g_max[0]

    def get_rcl(self, mu, cl):
        """ Get a remaining candidate list with mu limit. """
        remaining_candidates_temp = sorted(list(cl))
        position = bisect.bisect_left(remaining_candidates_temp, mu)
        remaining_candidates = remaining_candidates_temp[position:]
        remaining_candidates.reverse()
        return remaining_candidates
