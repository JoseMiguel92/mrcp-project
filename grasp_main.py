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
CSV_OUTPUT_FILE = "solution_table"
ALL_FILES_TXT_EXT = "**/*.txt"
CSV_EXT = "csv"
CSV_OUTPUT_DIR = "output"

# Messages
MAIN_TOTAL_TIME = "Total time: {} seconds."
MAIN_LOG_PROCESS = "Processing: {0} - Solution type: {1} - Iteration: {2} - Alpha: {3} - Time: {4:1.5f}"
MAIN_SEP_NAMES = "_"

if __name__ == '__main__':
    fixed_seed = 1
    random_alpha = random.random()
    alpha_list = [0.25, 0.5, 0.75, random_alpha]
    graph = Instance()
    solution_types = [SolutionGrasp.RATIO, SolutionGrasp.ADJACENT]
    for solution_type in solution_types:
        for file in glob.glob(GRAPH_PATH_SETS + ALL_FILES_TXT_EXT, recursive=True):
            data = dict()
            filename = os.path.splitext(os.path.basename(file))[0]
            for alpha in alpha_list:
                for iteration in range(1, 101):
                    graph.read_file(file)
                    instance_solution = SolutionGrasp()
                    start_time = time.time()
                    solution = instance_solution.find_grasp_solution(graph, file, solution_type, fixed_seed, alpha)
                    find_grasp_sol_time = time.time() - start_time
                    ratio, density, cardinality = GraphUtils.calculate_solution(graph, solution)
                    table_key_name = filename + MAIN_SEP_NAMES + solution_type + MAIN_SEP_NAMES + str(
                        iteration) + MAIN_SEP_NAMES + str(alpha)
                    data.update({table_key_name: [graph.get_total_nodes(), density, ratio, cardinality,
                                                  find_grasp_sol_time, alpha]})
                    LOGGER.debug(MAIN_LOG_PROCESS.format(file, solution_type, iteration, alpha, find_grasp_sol_time))
            export_filename = CSV_OUTPUT_FILE + MAIN_SEP_NAMES + solution_type + filename + os.extsep + CSV_EXT
            GraphUtils.export_solution(CSV_OUTPUT_DIR, data, export_filename)

    sys.exit()
