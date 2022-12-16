import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph ("raodmap.dot", City.from_dict)

city1 = nodes ["london"]
city2 = nodes ["edinburgh"]