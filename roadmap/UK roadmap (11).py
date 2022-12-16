from graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs,
)

def is_twentieth_century (city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph ("roadmap.dot", City.from_dict)
city = dfs (graph, nodes ["edinburgh"], is_twentieth_century)
print (city.name)