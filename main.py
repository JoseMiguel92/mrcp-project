# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

from instance import Instance
from time import gmtime, strftime
import logging

from logger.logger import Logger

# Logs
Logger.init_log()
LOGGER = logging.getLogger(__name__)

# Graphs paths
GRAPH_PATH = 'sets/set-d/wind-2004.txt'

# Messages
MAIN_INFO_ADJACENTS = 'Node {} and Node {} are adjacents.'
MAIN_INFO_NOT_ADJACENTS = 'Node {} and Node {} aren\'t adjacents.'
MAIN_INFO_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


if __name__ == '__main__':
    graph = Instance()
    graph.read_file(GRAPH_PATH)
    node_compare = graph.get_nodes().get(0)
    LOGGER.debug(strftime(MAIN_INFO_TIME_FORMAT, gmtime()))
    for node in graph.get_nodes().values():
        if node.is_adjacent(node_compare):
            LOGGER.debug(MAIN_INFO_ADJACENTS.format(node.get_node_id(), node_compare.get_node_id()))
        else:
            LOGGER.debug(MAIN_INFO_NOT_ADJACENTS.format(node.get_node_id(), node_compare.get_node_id()))
    LOGGER.debug(strftime(MAIN_INFO_TIME_FORMAT, gmtime()))
