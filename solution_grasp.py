# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import random

from graph_utils import GraphUtils
from solution_greedy_adjacent import SolutionGreedyNeighbors
from solution_greedy_ratio import SolutionGreedyRatio


class SolutionGrasp:
    ADJACENT = "adjacent"
    RATIO = "ratio"
    LOGGER = logging.getLogger(__name__)

    def find_grasp_solution(self, graph, name, solution_type, fixed_seed, alpha):
        """ Find solution on graph with a GRASP algorithm. """
        random.seed(fixed_seed)
        total_keys = sorted(list(graph.nodes.keys()))
        vertex = random.randint(total_keys[0], total_keys[-1])
        solution = {vertex}
        cl = graph.nodes[vertex].neighbors_indices.copy()
        while len(cl) != 0:
            g_min, g_max, gc = self.get_g(cl, solution_type, graph, name)
            mu = g_max - alpha * (g_max - g_min)
            rcl = self.get_rcl(mu, gc)
            random.seed(fixed_seed)
            random_position = random.randint(0, len(rcl) - 1)
            u = rcl[random_position][0]
            solution = solution.union({u})
            cl -= {u}
            cl.intersection_update(graph.get_node(u).neighbors_indices)
        return solution

    def get_g(self, candidates_list, solution_type, graph, name):
        """ Find g_min and g_max with current candidate list and solution type chosen. """
        g_c = dict()
        for candidate in candidates_list:
            chosen_solution = None
            if solution_type == self.ADJACENT:
                chosen_solution = SolutionGreedyNeighbors(graph, name)
            if solution_type == self.RATIO:
                chosen_solution = SolutionGreedyRatio(graph, name)
            chosen_solution.find_clique(candidate)
            g_c.update({candidate: chosen_solution.sol_value})
        sorted_gc = sorted(g_c.items(), key=lambda kv: kv[1], reverse=True)
        g_min = sorted_gc[-1]
        g_max = sorted_gc[0]
        return g_min[1], g_max[1], sorted_gc

    @staticmethod
    def get_rcl(mu, gc):
        """ Get a remaining candidate list with mu limit. """
        position = 0
        for current_candidate in gc:
            if current_candidate[1] <= mu:
                break
            else:
                position += 1
        if position == 0:
            remaining_candidates = gc.copy()
        else:
            remaining_candidates = gc[:position].copy()
        return remaining_candidates

    # TODO complete and refactor
    def apply_ls(self, graph, solution, name):
        sol_copy = solution.copy()
        ratio_neighbors = set()
        for node in solution:
            ratio_neighbors.update(graph.nodes[node].neighbors_indices)
        o_ratio_neighbors = sorted(ratio_neighbors, key=lambda x: graph.nodes[x].p_weight / graph.nodes[x].q_weight,
                                   reverse=True)
        better_node = o_ratio_neighbors.pop(0)
        to_delete = set()
        for node in sol_copy:
            if better_node not in graph.nodes[node].neighbors_indices and better_node != node:
                to_delete.add(node)
        sol_copy = sol_copy - to_delete
        sol_copy.update({better_node})
        #
        cliques = dict()
        greedy_constructive = SolutionGreedyRatio(graph, name)
        for node in sol_copy:
            current_clique = greedy_constructive.find_clique(node)
            if GraphUtils.is_clique_solution(graph, current_clique):
                self.LOGGER.debug("is clique")
                cliques.update({node: current_clique})
        final_clique = self.complete_clique(solution, sol_copy, cliques)
        # FIXME logger
        if GraphUtils.is_clique_solution(graph, final_clique):
            self.LOGGER.debug("good solution")
        else:
            self.LOGGER.fatal("isn't a solution")

    def complete_clique(self, solution, clique_ls, cliques_neighbors):
        final_clique = set()
        for node, clique in cliques_neighbors.items():
            final_clique = final_clique.union(clique)
        return final_clique
