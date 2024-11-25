from typing import Protocol, Any, Tuple, List, Self

from Lab2.src.conteiners import Container

from geopy import distance


class IPort(Protocol):
    def incoming_ship(self, ship: Any)-> None:
        ...

    def outgoing_ship(self, ship: Any)-> None:
        ...


class Port:
    """
        Represents a port that can handle ships and containers.

        This class implements the IPort interface and provides functionality for
        managing ships, containers, and calculating distances between ports.

        Attributes:
            id (int): Unique identifier for the port.
            coordinates (Tuple[float, float]): Geographic coordinates of the port (latitude, longitude).
            containers (List[Container]): List of containers currently at the port.
            ship_history (List[int]): List of IDs of ships that have visited the port.
            ships (List[Any]): List of ships currently docked at the port.

        Methods:
            get_distance(port: Self) -> float:
                Calculates the distance between this port and another port.

            incoming_ship(ship: Any) -> None:
                Registers a ship as having arrived at the port.

            outgoing_ship(ship: Any) -> None:
                Registers a ship as having departed from the port.
        """
    def __init__(self, id: int, coordinates: Tuple[float, float])-> None:
        self.id: int = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List[Container] = []
        self.ship_history: List[int] = []
        self.ships: List[Any] = []

    def get_distance(self, port: Self)-> float:
        """
               Calculate the distance between this port and another port.

               Args:
                   port (Port): The other port to calculate the distance to.

               Returns:
                   float: The distance in kilometers between the two ports.
               """
        return distance.geodesic(port.coordinates, self.coordinates).km

    def incoming_ship(self, ship: Any) -> None:
        """
               Register a ship as having arrived at the port.

               If the ship is not already in the port's list of ships, it is added.

               Args:
                   ship (Any): The ship that has arrived at the port.
               """
        if ship not in self.ships:
            self.ships.append(ship)

    def outgoing_ship(self, ship: Any) -> None:
        """
               Register a ship as having departed from the port.

               If the ship is in the port's list of ships, it is removed.

               Args:
                   ship (Any): The ship that has departed from the port.
               """
        if ship in self.ships:
            self.ships.remove(ship)