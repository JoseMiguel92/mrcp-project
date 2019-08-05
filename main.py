from instance import Instance
import time
from time import gmtime, strftime

# Graphs paths
GRAPH_1_PATH = 'sets/set-a/random-1.txt'
# Messages
# TODO ADD LOGGER
MAIN_INFO_ADJACENTS = 'Node {} and Node {} are adjacents.'
MAIN_INFO_NOT_ADJACENTS = 'Node {} and Node {} aren\'t adjacents.'
MAIN_INFO_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

if __name__ == '__main__':
    graph = Instance()
    graph.read_file(GRAPH_1_PATH)
    node_compare = graph.get_nodes().get(0)
    print(strftime(MAIN_INFO_TIME_FORMAT, gmtime()))
    for node in graph.get_nodes().values():
        if node.is_adjacent(node_compare):
            print(MAIN_INFO_ADJACENTS.format(node.get_node_id(), node_compare.get_node_id()))
        else:
            print(MAIN_INFO_NOT_ADJACENTS.format(node.get_node_id(), node_compare.get_node_id()))
    print(strftime(MAIN_INFO_TIME_FORMAT, gmtime()))
