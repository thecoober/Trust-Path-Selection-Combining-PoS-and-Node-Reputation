from vertify import *


def simulate(graph, paths, message, attacked_nodes=None):
    """
    模拟传递过程
    :param graph: graph
    :param paths: 排序后通道
    :param message: 需要传递的信息
    :param attacked_nodes: 被攻击节点
    :return: flag: 0表示没有找到有效路径，1表示找到有效路径
                paths: 找到的有效路径
    """
    # 生成每个节点的密钥对
    if attacked_nodes is None:
        attacked_nodes = []
    keys = {node: rsa.generate_private_key(public_exponent=65537, key_size=2048) for node in graph.nodes}
    public_keys = {node: keys[node].public_key() for node in graph.nodes}

    # 开始传播
    valid_path = 0
    valid_flag = 0

    for i in range(len(paths)):
        # 签名并传递消息
        current_message = message
        is_valid = True
        for node in paths[i][:-1]:
            if node in attacked_nodes:
                current_message = b"error message"
                signature = sign_message(rsa.generate_private_key(public_exponent=65537, key_size=2048), current_message)
            else:
                signature = sign_message(keys[node], current_message)

            # 下一个节点验证签名
            if not verify_signature(public_keys[node], current_message, signature):
                is_valid = False
                break

        if is_valid:
            print("received message： ", current_message)
            valid_path = i
            valid_flag = 1
            break

    return valid_flag, paths[valid_path]
