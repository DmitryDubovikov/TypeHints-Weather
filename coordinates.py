from dataclasses import dataclass
from subprocess import run, CompletedProcess

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using ipinfo"""
    coordinates = _get_ipinfo_coordinates()
    return _round_coordinates(coordinates)


def _get_ipinfo_coordinates() -> Coordinates:
    result: CompletedProcess[str] = run(
        ["curl", "ipinfo.io/loc"], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise CantGetCoordinates
    return _parse_coordinates(result.stdout.strip())


def _parse_coordinates(ipinfo_result: str) -> Coordinates:
    coords = ipinfo_result.split(",")
    return Coordinates(latitude=float(coords[0]), longitude=float(coords[1]))


def _round_coordinates(coords: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coords
    return Coordinates(round(coords.latitude, 4), round(coords.longitude, 4))


if __name__ == "__main__":
    print(get_gps_coordinates())
