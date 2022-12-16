from graph import City, load_graph

nodes, graph = load_graph ("roadmap.dot", City.from_dict)

print(nodes ["london"])
print (graph)

def sort_by (neighbors, strategy):
    return sorted (neighbors.items (), key = lambda item: strategy (item[1]))

def by_distance (weights):
    return float (weights ["distance"])

for neighbor, weights in sort_by (graph [nodes["london"]], by_distance):
    print (f"{weights ['distance']:>3} miles, {neighbor.name}")
