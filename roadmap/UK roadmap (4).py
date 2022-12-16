from graph import City, load_graph


nodes, graph = load_graph ("roadmap.dot", City.from_dict)
for neighbor in graph.neighbors(nodes["london"]):
    print (neighbor.name)
