from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using GPS"""
    return Coordinates(-34.58126316837909, -58.433659373668306)
