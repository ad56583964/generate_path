import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def getHctgFromDF(pandas_nodes: pd.DataFrame, target_node):
    return pandas_nodes['hctg'][target_node - 1]


edges_data = pd.read_csv("edges.csv", comment='#', header=None)
nodes_data = pd.read_csv("nodes.csv", comment='#', header=None)

edges = pd.DataFrame(edges_data)
nodes = pd.DataFrame(nodes_data)

edges.columns = ['n1', 'n2', 'ctg']
nodes.columns = ['node', 'x', 'y', 'hctg']

G = nx.from_pandas_edgelist(edges, source='n1', target='n2', edge_attr='ctg')

start_node = 1
end_node = 12

current_node = 1


# init past_cost dictionary
past_cost = dict()
for node in G:
    if node == 1:
        past_cost[node] = 0
    else:
        past_cost[node] = -1
# finish past_cost init

open_nodes = {start_node: getHctgFromDF(nodes, start_node)}

# traverse child/adj
for adj in G.nodes[current_node].adj:
    print(adj)

# print(past_cost)

# 1.change the node ?

# 2.sum of parent node ?

# nx.draw(G, with_labels=True)
# plt.show()
# G.add_node(1)

# print("Nodes" + str(G.nodes()))
