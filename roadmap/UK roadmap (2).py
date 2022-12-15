import networkx as nx

graph = nx.nx_agraph.read_dot("roadmap/roadmap.dot")
print (graph.nodes ["london"])