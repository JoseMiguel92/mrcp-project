# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import glob
import logging
import os
import random
import sys
import time

from graph_utils import GraphUtils
from instance import Instance
from logger.logger import Logger
from solution_grasp import SolutionGrasp

# Logs
Logger.init_log()
LOGGER = logging.getLogger(__name__)

# Sources
GRAPH_PATH_SETS = 'sets/'
CSV_OUTPUT_FILE = "solution_table_{0}_{1}.csv"
CSV_OUTPUT_FILE_LS = "solution_table_{0}_{1}_LS.csv"
ALL_FILES_TXT_EXT = "**/*.txt"
CSV_EXT = "csv"
CSV_OUTPUT_DIR = "output"

# Messages
MAIN_TOTAL_TIME = "Total time: {0} seconds."
MAIN_LOG_PROCESS = "Processing: {0} - Solution type: {1} - Iteration: {2} - Alpha: {3} - Time: {4:1.5f} - Clique: {5}"
MAIN_LOG_PROCESS_OLD = "Old Solution: {0} - Ratio: {1:.5f} - Cardinality: {2} - Time: {3:.5f}"
MAIN_LOG_PROCESS_LS = "New solution: {0} - Ratio: {1:.5f} - Cardinality: {2} - Time: {3:.5f}"
MAIN_SEP_NAMES = "_"

# Config
TOTAL_ITERATIONS = 100


def split_name(total_path):
    name_splitted = os.path.splitext(total_path)[0].split(os.sep)
    return "{0}_{1}".format(name_splitted[1], name_splitted[-1])


if __name__ == '__main__':
    fixed_seed = None
    random_alpha = random.random()
    alpha_list = [0.25, 0.5, 0.75, random_alpha]
    graph = Instance()
    solution_types = [SolutionGrasp.RATIO, SolutionGrasp.ADJACENT]
    for solution_type in solution_types:
        for file in glob.glob(GRAPH_PATH_SETS + ALL_FILES_TXT_EXT, recursive=True):
            data = dict()
            data_ls = dict()
            filename = os.path.splitext(os.path.basename(file))[0]
            graph.read_file(file)
            instance_solution = SolutionGrasp()
            for alpha in alpha_list:
                for iteration in range(1, TOTAL_ITERATIONS + 1):
                    start_time = time.time()
                    solution = instance_solution.find_grasp_solution(graph, file, solution_type, fixed_seed, alpha)
                    find_grasp_sol_time = time.time() - start_time
                    ratio, density, cardinality = GraphUtils.calculate_solution(graph, solution)

                    local_search_sol = instance_solution.apply_ls(graph, solution)
                    find_ls_sol_time = time.time() - start_time
                    ls_ratio, ls_density, ls_cardinality = GraphUtils.calculate_solution(graph, local_search_sol)

                    table_key_name = filename + MAIN_SEP_NAMES + solution_type + MAIN_SEP_NAMES + str(
                        iteration) + MAIN_SEP_NAMES + str(alpha)
                    data.update({table_key_name: [graph.get_total_nodes(), density, ratio, cardinality,
                                                  find_grasp_sol_time, alpha]})

                    data_ls.update({table_key_name: [graph.get_total_nodes(), ls_density, ls_ratio, ls_cardinality,
                                                     find_ls_sol_time, alpha]})

                    if GraphUtils.is_clique_solution(graph, solution):
                        LOGGER.debug(MAIN_LOG_PROCESS.format(file, solution_type, iteration, alpha, find_grasp_sol_time,
                                                             solution))
                    else:
                        LOGGER.fatal(MAIN_LOG_PROCESS.format(file, solution_type, iteration, alpha, find_grasp_sol_time,
                                                             solution))
                        sys.exit()

                    if GraphUtils.is_clique_solution(graph, local_search_sol):
                        LOGGER.debug(MAIN_LOG_PROCESS_OLD.format(solution, ratio, cardinality, find_grasp_sol_time))
                        LOGGER.debug(MAIN_LOG_PROCESS_LS.format(local_search_sol, ls_ratio, ls_cardinality,
                                                                find_ls_sol_time))
                    else:
                        LOGGER.fatal(
                            MAIN_LOG_PROCESS.format(file, solution_type, iteration, alpha, find_grasp_sol_time,
                                                    local_search_sol))
                        sys.exit()

            output_name = split_name(file)

            export_filename = CSV_OUTPUT_FILE.format(solution_type, output_name)
            GraphUtils.export_solution(CSV_OUTPUT_DIR, data, export_filename)

            export_filename_ls = CSV_OUTPUT_FILE_LS.format(solution_type, output_name)
            GraphUtils.export_solution(CSV_OUTPUT_DIR, data_ls, export_filename_ls)

    sys.exit()
