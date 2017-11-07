import networkx as nx
import time

G = nx.read_graphml("/home/sharan/Desktop/punjab1.graphml")
start_time = time.time()
nx.degree_centrality(G)
print("--- %s seconds ---" % (time.time() - start_time))
