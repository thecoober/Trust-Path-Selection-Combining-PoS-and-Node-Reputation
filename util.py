from networkx.algorithms.simple_paths import all_simple_paths
import matplotlib.pyplot as plt
import networkx as nx
import os


def PoS_verify(graph, threshold=500):
    """
    PoS验证，删除代币数乘以持有时间小于阈值的节点
    :param graph: 初始图
    :param threshold: 阈值
    :return: 删除后图
    """
    result = graph.copy()
    for node in graph.nodes(data=True):
        if node[1]['coin']*node[1]['coin_age'] < threshold:
            print("remove node: ", node[0])
            result.remove_node(node[0])
    return result


def calculate_path_probability(path, graph):
    joint_prob = 1.0
    for i in range(len(path) - 1):
        node = path[i + 1]
        prob = graph.nodes[node]['reputation']
        joint_prob *= prob
    return joint_prob


def find_sorted_paths(graph, s, t):
    """
    Find all simple paths from s to t and sort them by the product of the reputation of the nodes on the path
    :param graph: graph
    :param s: 信息发出节点
    :param t: 信息接收节点
    :return: 排序好的路径
    """
    paths = list(all_simple_paths(graph, source=s, target=t))
    path_probabilities = {tuple(path): calculate_path_probability(path, graph) for path in paths}
    paths.sort(key=lambda path: path_probabilities[tuple(path)], reverse=True)
    print("The top eight paths are:")
    for i in range(8):
        print("{:<40} {:<20} {:<10}".format(str(paths[i]), "total reputation:",
                                            round(path_probabilities[tuple(paths[i])], 2)))
    return paths


def show_graph(graph, path=None, title=None):
    if title is not None:
        plt.title(title)
    pos = nx.spring_layout(graph, seed=50)

    if path is None:
        nx.draw(graph, pos)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_family='sans-serif', font_color='white')
    else:
        E = graph.edges()
        path_edge = [(path[i+1], path[i]) for i in range(len(path) - 1)]
        path_edge.extend([(path[i], path[i + 1]) for i in range(len(path) - 1)])
        colors = ['black' if edge not in path_edge else 'red' for edge in E]
        edge_width = [1 if edge not in path_edge else 4 for edge in E]
        nx.draw(graph, pos, edge_color=colors, width=edge_width)
        nx.draw_networkx_labels(graph, pos, font_size=12, font_family='sans-serif', font_color='white')

    if not os.path.exists("./result"):
        os.mkdir("./result")
    plt.savefig(os.path.join("./result/", title))
    plt.show()
