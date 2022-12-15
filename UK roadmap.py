from graph import City, load_graph

nodes, graph = load_graph ("roadmap.dot", City.from_dict)

print(nodes ["london"])
print (graph)

for neighbor, weights in sort_by (graph [nodes["london"]], by_distance):
    print (f"{weights ['distance']:>3} miles, {neighbor.name}")