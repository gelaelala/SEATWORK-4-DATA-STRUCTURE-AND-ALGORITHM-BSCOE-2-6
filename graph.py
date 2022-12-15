from typing import NamedTuple
import networkx as nx

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