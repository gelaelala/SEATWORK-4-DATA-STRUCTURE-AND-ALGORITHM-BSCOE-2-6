import networkx as nx
from graph import City, load_graph

nodes, graph = load_graph ("roadmap.dot", City.from_dict)

city1 = nodes ["aberdeen"]
city2 = nodes ["perth"]