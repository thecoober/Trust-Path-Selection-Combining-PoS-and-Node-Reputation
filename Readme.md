# Trust Path Selection Combining PoS and Node Reputation

This project simulates node reputation and PoS (Proof of Stake) mechanisms within a blockchain, combining these 
mechanisms to select the optimal transmission path from node A to node B. The security of the transmission path is 
ensured through signature algorithms. In this project, we assume there are 19 nodes, with their properties and edges 
recorded in the `property.py` file. Nodes are initially screened using PoS, and then the path with the highest overall 
reputation value is selected as the optimal transmission path. During data transmission, data is signed to ensure its 
security. If an error is detected during signature verification, it indicates that the data has been tampered with, 
and other paths are chosen for transmission based on their overall reputation values in descending order.

## Requirements

This project runs in a Python 3.11.9 environment and requires the following libraries:
```
matplotlib==3.9.0
networkx==3.3
cryptography==42.0.8
```
Install the required libraries using the following command:
```
pip install -r requirements.txt
```
## Usage
Run the `main.py` file to start simulating the information transmission process. The `createGraph` function creates the 
initial graph by reading data from the `property.py` file and performs PoS verification via the `PoS_verify` function, 
removing nodes with coin × coin holding time less than the `threshold`.

The `find_best_path` function sets the sender and receiver nodes, calculates the overall reputation values of all feasible 
paths, and sorts these paths from highest to lowest reputation.

Finally, the `simulate` function simulates the information transmission process. The message to be transmitted is set in 
the `message` parameter, and malicious nodes can be set through the `attacked_nodes` parameter (default is no malicious 
nodes). During transmission, each node signs the data using the `RSA` algorithm. If signature verification fails, 
indicates that the data has been tampered with, and an alternative path is chosen for transmission.

Malicious nodes are programmed to tamper with data, changing it to `error message`.


## Results

By directly running the `main.py` file, you can get the following results:
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
received message：  b'Important message'
optimal path:  ['A', 'C', 'D', 'F', 'G', 'I', 'K']
==========================================================================
```
Use the `find_sorted_paths` function to modify the sender and receiver nodes and the `simulate` function to modify the 
attacked nodes. In the current file, node `A` is chosen as the sender and node `K` as the receiver, with nodes `S` and `Q` 
being attacked and acting as malicious nodes. The initially generated graph is shown below.

<div align=center>
<img  src="figure/Initial graph.png" width="50%">
</div>

After PoS verification, nodes `O`, `Q`, and `J` are removed, with the remaining nodes shown below.

<div align=center>
<img  src="figure/PoS verified.png" width="50%">
</div>

The final selected optimal path is `['A', 'C', 'D', 'F', 'G', 'I', 'K']`, as shown below.

<div align=center>
<img  src="figure/optimal path.png" width="50%">
</div>

## Conclusion

In practice, this project represents a preliminary attempt to integrate multiple mechanisms, with each module having 
some issues. In actual use, more in-depth methods can replace the modules in this project. For example, a Byzantine 
fault-tolerant PoS mechanism can replace the simple asset proof method used in this project. More factors can be 
considered in the reputation calculation phase to comprehensively evaluate node reputation. Additionally, to ensure 
that transmitted information is only visible to the sender and receiver nodes and not to the relay nodes, symmetric 
encryption algorithms like "AES" can be used before sending the information. The encryption and decryption keys can be 
agreed upon by the sender and receiver nodes, further ensuring the confidentiality and security of information 
transmission.

