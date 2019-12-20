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
MAIN_TOTAL_TIME = "Total time: {:1.2f} seconds"
MAIN_PROCESS_FILE = "Processing: {}"
MAIN_SOL_TYPE = "Solution type: {}"
MAIN_ITERATION = "Iteration: {}"
MAIN_SEP_NAMES = "_"

if __name__ == '__main__':
    fixed_seed = 1
    alpha = 0.5
    graph = Instance()
    solution_types = [SolutionGrasp.ADJACENT]
    data = dict()
    for solution_type in solution_types:
        LOGGER.debug(MAIN_SOL_TYPE.format(solution_type))
        for file in glob.glob(GRAPH_PATH_SETS + ALL_FILES_TXT_EXT, recursive=True):
            for iteration in range(1, 5):
                LOGGER.debug(MAIN_ITERATION.format(iteration))
                LOGGER.debug(MAIN_PROCESS_FILE.format(file))
                graph.read_file(file)
                instance_solution = SolutionGrasp()
                random.seed()
                alpha = random.random()
                print(alpha)
                start_time = time.time()
                solution = instance_solution.find_grasp_solution(graph, file, solution_type, fixed_seed, alpha)
                find_grasp_sol_time = time.time() - start_time
                ratio, density, cardinality = GraphUtils.calculate_solution(graph, solution)
                filename = os.path.splitext(os.path.basename(file))[0]
                table_key_name = filename + MAIN_SEP_NAMES + solution_type + MAIN_SEP_NAMES + str(iteration)
                data.update({table_key_name: [graph.get_total_nodes(), density, ratio, cardinality, find_grasp_sol_time,
                                              alpha]})
                LOGGER.debug(MAIN_TOTAL_TIME.format(find_grasp_sol_time))
        export_filename = CSV_OUTPUT_FILE + MAIN_SEP_NAMES + solution_type + os.extsep + CSV_EXT
        GraphUtils.export_solution(CSV_OUTPUT_DIR, data, export_filename)

    sys.exit()
