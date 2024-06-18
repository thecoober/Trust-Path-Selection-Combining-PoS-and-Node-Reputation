import networkx as nx
import property


def createGraph():
    """
    创建图
    :return: 所创建对象
    """
    graph = nx.Graph()
    graph.add_edges_from(property.edge)
    nx.set_node_attributes(graph, property.reputation, 'reputation')
    nx.set_node_attributes(graph, property.coin, 'coin')
    nx.set_node_attributes(graph, property.coin_age, 'coin_age')
    return graph
