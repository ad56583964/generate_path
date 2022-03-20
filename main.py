import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time


def getHctgFromDF(pandas_nodes: pd.DataFrame, target_node):
    return pandas_nodes['hctg'][target_node - 1]


def getMinOpenNode(input_open_nodes: dict):
    open_min = min(zip(input_open_nodes.values(), input_open_nodes.keys()))
    print('@@ GotMin: '+str(open_min[1]))
    return open_min[1]


edges_data = pd.read_csv("edges.csv", comment='#', header=None)
nodes_data = pd.read_csv("nodes.csv", comment='#', header=None)

edges = pd.DataFrame(edges_data)
nodes = pd.DataFrame(nodes_data)

edges.columns = ['n1', 'n2', 'ctg']
nodes.columns = ['node', 'x', 'y', 'hctg']

G = nx.from_pandas_edgelist(edges, source='n1', target='n2', edge_attr='ctg')

start_node = 1
end_node = 12

current_node = start_node


# init past_cost dictionary
past_cost = dict()
for node in G:
    if node == 1:
        past_cost[node] = 0
    else:
        past_cost[node] = -1
# finish past_cost init

# default cost??
open_nodes = {start_node: getHctgFromDF(nodes, start_node)}
close_nodes = dict()
# print(G.adj[1])
# traverse child/adj
est_tot_cost = dict()

for adj_node, data in G.adj[current_node].items():
    print('Now: '+str(adj_node))
    # print('&parent:'+str(current_node))
    past_cost[adj_node] = past_cost[current_node] + data['ctg']
    # print('# past_cost: '+str(past_cost[adj_node]))
    # print('# hctg[parent_node]:' + str(getHctgFromDF(nodes, adj_node)))
    est_tot_cost[adj_node] = past_cost[adj_node] + getHctgFromDF(nodes, adj_node)
    print('## est_tot_cost: '+str(est_tot_cost[adj_node]))
    print('+++OPEN ['+str(adj_node)+']+++')
    open_nodes[adj_node] = est_tot_cost[adj_node]
    time.sleep(0.5)
# finish once traverse
# close the 'parent'
close_nodes[current_node] = open_nodes[current_node]
print('--- CLOSE ['+str(current_node)+']---')
open_nodes.pop(current_node)

print(open_nodes)
print(close_nodes)

# find the lowest open_node
current_node = getMinOpenNode(open_nodes)

for adj_node, data in G.adj[current_node].items():
    if close_nodes.get(adj_node):
        continue
    print('Now: '+str(adj_node))
    # print('&parent:'+str(current_node))
    past_cost[adj_node] = past_cost[current_node] + data['ctg']
    # print('# past_cost: '+str(past_cost[adj_node]))
    # print('# hctg[parent_node]:' + str(getHctgFromDF(nodes, adj_node)))
    est_tot_cost[adj_node] = past_cost[adj_node] + getHctgFromDF(nodes, adj_node)
    print('## est_tot_cost: '+str(est_tot_cost[adj_node]))
    print('+++OPEN ['+str(adj_node)+']+++')
    open_nodes[adj_node] = est_tot_cost[adj_node]
    time.sleep(0.5)
# print(past_cost)
close_nodes[current_node] = open_nodes[current_node]
print('--- CLOSE ['+str(current_node)+']---')
open_nodes.pop(current_node)
# 1.change the node ?

# 2.sum of parent node ?

nx.draw(G, with_labels=True)
plt.show()
# G.add_node(1)

# print("Nodes" + str(G.nodes()))
