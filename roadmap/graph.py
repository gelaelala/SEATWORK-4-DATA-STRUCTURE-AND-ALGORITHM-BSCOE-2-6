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

def shortest_path (graph, source, destination, order_by = None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    while queue:
        node = queue.dequeue()
        neighbors = list (graph.neighbors (node))
        if order_by:
            neighbors.sort (key = order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous [neighbor] = node
                if neighbor == destination:
                    return retrace (previous, source, destination)