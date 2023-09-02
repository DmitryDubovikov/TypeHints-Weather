from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using GPS"""
    return Coordinates(-34.58126316837909, -58.433659373668306)
