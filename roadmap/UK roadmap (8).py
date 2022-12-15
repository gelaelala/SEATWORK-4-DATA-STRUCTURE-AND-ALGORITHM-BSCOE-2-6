from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century (city):
    return city.year and 1901 <= year <= 2000

