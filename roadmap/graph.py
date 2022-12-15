from typing import NamedTuple
import networkx as nx
from queues import Queue


class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict (cls,attrs):
        return cls (
            name = attrs ["xlabel"],
            country = attrs ["country"],
            year = int (attrs ["year"]) or None,
            latitude = float (attrs ["latitude"]),
            longitude = float (attrs ["longitude"]),
        )

def load_graph (filename, node_factory):
    graph = nx.nx_agraph.read_dot (filename)
    nodes = {
        name: node_factory (attributes)
        for name, attributes in graph.nodes (data = True)
    }
    return nodes, nx.Graph (
        (nodes [name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges (data = True)
    )

def breadth_first_traverse (graph, source):
    queue = Queue (source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        for neighbor in graph.neighbors (node):
            if neighbor not in visited:
                visited.add (neighbor)
                queue.enqueue (neighbor)

def breadth_first_search (graph, source, predicate):
    for node in breadth_first_traverse (graph, source):
        if predicate (node):
            return node