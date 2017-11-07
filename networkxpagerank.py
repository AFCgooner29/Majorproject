import networkx as nx

G = nx.read_graphml("/home/sharan/Desktop/pagerank1.graphml")
g= nx.Graph(G)
nx.pagerank(G,0.15,20)
