from createGraph import *
from util import *
from simulate import *


def main():
    print("==========================================================================")
    print("Create graph")
    # 创建graph
    initial_graph = createGraph()
    show_graph(initial_graph, title="Initial graph")

    print("==========================================================================")
    print("PoS verify to remove nodes with low reputation")
    # PoS验证
    graph = PoS_verify(initial_graph, 500)
    show_graph(graph, title="PoS verified")

    print("==========================================================================")
    print("Find paths and sort by reputation")
    # 找出最优路径并按声誉高低排序
    paths = find_sorted_paths(graph, 'A', 'K')

    print("==========================================================================")
    print("Simulate message transfer process")
    # 模拟传递过程
    # 如果需要添加攻击节点，在attack_nodes中添加节点名称即可
    flag, path = simulate(graph, paths, b"Important message", ['H'])

    # 打印结果
    if flag == 0:
        print("No valid path found")
        show_graph(graph, title="No valid path found")
    else:
        print("optimal path: ", path)
        show_graph(graph, path, title="optimal path")
    print("==========================================================================")


if __name__ == "__main__":
    main()
