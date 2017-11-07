import networkx as nx
from pyspark.sql import Row
import time

G = nx.read_graphml("/home/sharan/Desktop/punjab1.graphml")
nods = []
edgs = []
for i in G.edges():
    edgs.append(i)
for i in G.nodes():
    nods.append(i)


rdd1 = sc.parallelize(nods)
row_rdd = rdd1.map(lambda x: Row(x))


v = spark.createDataFrame(row_rdd,["id"])
e = spark.createDataFrame(edgs,["src","dst"])
from graphframes import *
g = GraphFrame(v, e)
start_time = time.time()
results = g.pageRank(resetProbability=0.15,maxIter=20)
results.vertices.select("id", "pagerank").show()
print("--- %s seconds ---" % (time.time() - start_time))
