from dataclasses import dataclass
import config


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using GPS"""
    latitude, longitude = (-34.58126316837909, -58.433659373668306)
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 4), [latitude, longitude])
    return Coordinates(latitude, longitude)


if __name__ == "__main__":
    print(get_gps_coordinates())
