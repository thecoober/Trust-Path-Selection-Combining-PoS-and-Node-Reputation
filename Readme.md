# 结合PoS和节点声誉的可信任传输路径选择

这个项目模拟了区块链中的节点声誉和 PoS 机制，结合这两个机制来选择从节点 A 到节点 B 最优的传输路径，
并通过签名算法保证传输路径的安全性。在这个项目中，我们假设有 19 个节点，节点的各项属性和边记录在 `property.py` 文件中。
通过 PoS 对节点进行初次筛选，然后选择总体声誉值最高的路径作为最优传输路径。在传输数据的过程中对数据进行签名，以保证数据的安全性。
若在验证签名过程中出现错误，则说明数据被篡改，因此依据总体声誉值依次从高到低选择其余路径进行传输。

## 需求
本项目在 Python 3.11.9 环境下运行，需要以下库的支持：
```
matplotlib==3.9.0
networkx==3.3
cryptography==42.0.8
```
通过运行以下命令安装所需库：
```
pip install -r requirements.txt
```
## 使用
运行 `main.py` 文件，即可开始模拟信息传递过程。其中，`createGraph`函数通过读取`property.py` 文件的数据创建初始图，
并通过`PoS_verify`函数对初始图进行权益证明，将代币数×持有时间小于`threshold`的节点删除。

`find_best_path`函数设定信息发出节点和信息接收节点，通过计算所有可行途径的总体声誉值，按总体声誉值高低对所有可行路径从高到低排序。

最后 `simulate` 函数模拟信息传递过程，要传递的信息在参数`message`中进行设定，恶意节点通过`attacked_nodes`参数进行设置，默认不存在恶意节点。
`simulate` 函数传递过程中每个节点都对数据进行签名，签名算法为`RSA`，若签名验证失败，则说明数据被篡改，选择其他路径进行传输。

恶意节点的行为被设定为篡改数据，所有途径恶意节点的信息都被篡改为 `error message`。

## 结果
直接运行 `main.py` 文件，可以得到如下结果：
```
==========================================================================
Create graph
==========================================================================
PoS verify to remove nodes with low reputation
remove node:  O
remove node:  Q
remove node:  J
==========================================================================
Find paths and sort by reputation
The top eight paths are:
['A', 'B', 'S', 'H', 'K']                total reputation:    0.88      
['A', 'C', 'D', 'B', 'S', 'H', 'K']      total reputation:    0.84      
['A', 'B', 'S', 'H', 'N', 'K']           total reputation:    0.79      
['A', 'C', 'D', 'B', 'S', 'H', 'N', 'K'] total reputation:    0.76      
['A', 'C', 'D', 'F', 'G', 'I', 'K']      total reputation:    0.73      
['A', 'C', 'D', 'F', 'H', 'K']           total reputation:    0.73      
['A', 'B', 'D', 'F', 'G', 'I', 'K']      total reputation:    0.72      
['A', 'B', 'D', 'F', 'H', 'K']           total reputation:    0.72      
==========================================================================
Simulate message transfer process
message decrypt:  b'Important message'
optimal path:  ['A', 'C', 'D', 'F', 'G', 'I', 'K']
==========================================================================
```
通过`find_sorted_paths`函数修改信息发送方和接收方，通过`simulate`函数修改被攻击节点，在现有文件中，选择节点`A`作为信息发送方，
节点`K`作为信息接收方，其中`S`和`Q`节点被攻击，为恶意节点。直接生成的 graph 如下图所示。
<div align=center>
<img  src="figure/Initial graph.png" width="50%">
</div>

经过 PoS 机制筛选后，删除了节点 `O`, `Q`, `J`，剩余节点如下图所示。
<div align=center>
<img  src="figure/PoS verified.png" width="50%">
</div>

最终筛选出的最优路径为 `['A', 'C', 'D', 'F', 'G', 'I', 'K']`，如下图所示。
<div align=center>
<img  src="figure/optimal path.png" width="50%">
</div>