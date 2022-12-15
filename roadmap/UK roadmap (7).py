import networkx as nx
from graph import City, load_graph

def is_twentieth_century (year):
    return year and 1901 <= year <= 2000

def order (neighbors):
    def by_latitude (city):
        return city.latitude
    return iter (sorted (neighbors, key = by_latitude, reverse = True))

nodes, graph = load_graph ("roadmap/roadmap.dot", City.from_dict)
for node in nx.bfs_tree (graph, nodes ["edinburgh"]):
    print ("📍", node.name)
    if is_twentieth_century (node.year):
        print ("Found: ", node.name, node.year)
        break
else:
    print ("Not found")    