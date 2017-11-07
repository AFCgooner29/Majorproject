import networkx as nx
import time

G = nx.read_graphml("/home/sharan/Desktop/punjab1.graphml")
g = nx.Graph(G)
start_time = time.time()
result = nx.pagerank(g)
print("--- %s seconds ---" % (time.time() - start_time))
for i in result:
    print i 
