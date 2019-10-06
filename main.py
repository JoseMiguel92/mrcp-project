# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import logging
import os

from instance import Instance
from logger.logger import Logger
from solution import Solution
from graph_utils import GraphUtils
import time

# Logs
Logger.init_log()
LOGGER = logging.getLogger(__name__)

# Graphs paths
GRAPH_PATH = 'sets/set-a/'

# Messages
MAIN_TIME = "Total time: {:1.10f} seconds"

if __name__ == '__main__':

    start_time = time.time()

    data = dict()

    for file in os.listdir(GRAPH_PATH):
        graph = Instance()
        graph.read_file(GRAPH_PATH + file)
        solution = Solution(graph, os.path.splitext(file)[0])
        solution.set_solution_max_cliques()
        data.update(solution.collect_sol_data())

    GraphUtils.export_solution(data)
    LOGGER.debug(MAIN_TIME.format(time.time() - start_time))

