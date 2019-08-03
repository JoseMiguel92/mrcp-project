from instance import Instance

GRAPH_1_PATH = 'sets/set-a/random-1.txt'

if __name__ == '__main__':
    graph = Instance()
    graph.read_file(GRAPH_1_PATH)
    node_compare = graph.get_nodes().get(0)
    for node in graph.get_nodes().values():
        if node.is_adjacent(node_compare):
            print('{} and {} are adjacents.'.format(node.get_node_id(), node_compare.get_node_id()))
        else:
            print('{} and {} aren\'t adjacents.'.format(node.get_node_id(), node_compare.get_node_id()))
