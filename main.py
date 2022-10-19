from fractal_network import NetworkGenerator
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# generate fractal network
NetworkGenerator.graph(lvls=2, n=10)

# Network data path
network_filepath = "10-2.dat"

with open(file=network_filepath) as network_dat_file:
    network_data = network_dat_file.read()

network_data = network_data.splitlines()

node_df = pd.DataFrame(columns=[
    "node_idx",
    "node_label",
    "neighbor"
])

network_df = pd.DataFrame(columns=[
    "node_01",
    "node_02",
    "edge_weight"
])


for idx, each_node in enumerate(network_data):
    node_in_list = each_node.split(sep=" ")

    node_idx = node_in_list[0]
    node_label = node_in_list[1]
    node_neighbor = node_in_list[2]

    node_df.loc[len(node_df.index)] = [node_idx, node_label, node_neighbor]

    node_edges = node_in_list[3:]

    for edge_idx, node_info in enumerate(node_edges):

        if edge_idx % 2 == 0:
            neighbor_idx = node_edges[edge_idx]
            edge_weight = node_edges[edge_idx + 1]

            network_df.loc[len(network_df.index)] = [node_idx, neighbor_idx, edge_weight]


print(f"node_df length = {len(node_df)}")
print(f"network_df length = {len(network_df)}")

# Create graph network
graph_network = nx.from_pandas_edgelist(
                            df=network_df,
                            source="node_01",
                            target="node_02",
                            edge_attr="edge_weight")

# Visualize network
nx.draw_networkx(G=graph_network,
                 pos=nx.spring_layout(graph_network),
                 with_labels=False,
                 node_size=3)

plt.axis("off")
plt.show()