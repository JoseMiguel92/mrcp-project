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
            if GraphUtils.become_clique(graph, solution, u):
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

    def apply_ls(self, graph, solution):
        sol_copy = solution.copy()
        ratio_neighbors = set()
        for node in solution:
            ratio_neighbors.update(graph.nodes[node].neighbors_indices)
        o_ratio_neighbors = sorted(ratio_neighbors, key=lambda x: graph.nodes[x].p_weight / graph.nodes[x].q_weight,
                                   reverse=True)
        new_sol_temp = sol_copy.copy()
        ls_solutions = list()
        for node_ratio in o_ratio_neighbors:
            new_sol_temp.update({node_ratio})
            if not GraphUtils.is_clique_solution(graph, new_sol_temp):
                new_sol_temp = self.clean_conflicted_nodes(graph, node_ratio, new_sol_temp)
            if GraphUtils.is_clique_solution(graph, new_sol_temp):
                for node_clique in new_sol_temp:
                    result, result_ratio = self.find_clique_aux(graph, node_clique, new_sol_temp)
                    ls_solutions.append((len(result), result_ratio, result))
            else:
                new_sol_temp.discard(node_ratio)
        return self.give_solution(ls_solutions)

    def clean_conflicted_nodes(self, graph, better_node, new_sol_temp):
        to_delete = set()
        for node in new_sol_temp:
            if better_node not in graph.nodes[node].neighbors_indices and better_node != node:
                to_delete.add(node)
        local_sol = new_sol_temp.difference(to_delete)
        local_sol.update({better_node})
        return local_sol

    def find_clique_aux(self, graph, father, old_clique):
        clique = old_clique.copy()
        adjacent = graph.get_node(father).neighbors_indices.copy()
        while len(adjacent) != 0:
            candidate = self.find_better(graph, adjacent)
            if GraphUtils.become_clique(graph, clique, candidate):
                adjacent = GraphUtils.discard_adjacent(graph, adjacent, candidate)
                clique.update({candidate})
            else:
                adjacent.discard(candidate)
        return clique, GraphUtils.calculate_clique_ratio(graph, clique)

    def find_better(self, graph, adjacent):
        current_ratio = -1
        node_chosen = None
        for node in adjacent:
            node_ratio = graph.get_node(node).p_weight / graph.get_node(node).q_weight
            if node_ratio > current_ratio:
                current_ratio = node_ratio
                node_chosen = node

        return node_chosen

    def give_solution(self, ls_solutions):
        sort_by_cardinality = sorted(ls_solutions, key=lambda x: x[0], reverse=True)
        max_ratio = sort_by_cardinality[0][0]
        ls_tuple_max_cardinality = [(x, y, z) for (x, y, z) in sort_by_cardinality if x == max_ratio]
        sort_by_ratio = sorted(ls_tuple_max_cardinality, key=lambda x: x[1], reverse=True)
        return sort_by_ratio[0][2]
