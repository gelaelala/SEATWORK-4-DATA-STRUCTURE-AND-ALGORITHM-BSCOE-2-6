from graph import City, load_graph

nodes, graph = load_graph ("roadmap.dot", City.from_dict)

print(nodes ["london"])
print (graph)

for neighbor, weights in graph [nodes["london"]].items():
    print (weights ["distance"], neighbor.name)