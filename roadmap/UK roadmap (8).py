from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century (city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph ("roadmap/roadmap.dot", City.from_dict)
city = bfs (graph, nodes ["edinburgh"], is_twentieth_century)
print(city.name )

