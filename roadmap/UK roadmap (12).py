import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph ("roadmap.dot", City.from_dict)

city1 = nodes ["london"]
city2 = nodes ["edinburgh"]

def distance (weights):
    return float (weights ["distance"])

for city in dijkstra_shortest_path (graph, city1, city2, distance):
    print (city.name)