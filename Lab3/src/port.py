import json
import math
from typing import List, Dict, Any
from containers import Container

class Ship:
    """
    Represents a ship that can dock at ports.

    This class may be extended to include more functionality as needed.
    """

    def __init__(self, ship_id: str):
        """
        Initialize a Ship object.

        Args:
            ship_id (str): Unique identifier for the ship.
        """
        self.ship_id = ship_id

    def to_dict(self) -> Dict:
        """
        Convert the ship instance to a dictionary representation.

        Returns:
            Dict: A dictionary with ship attributes.
        """
        return {"ship_id": self.ship_id}

    @staticmethod
    def from_dict(data: Dict) -> 'Ship':
        """
        Create a Ship instance from a dictionary.

        Args:
            data (Dict): A dictionary containing ship attributes.

        Returns:
            Ship: A new Ship instance populated with the given data.
        """
        return Ship(data['ship_id'])


class Port:
    """
    Represents a port with geographical coordinates, container, and ship management capabilities.
    """

    def __init__(self, port_id: str, latitude: float, longitude: float):
        """
        Initialize a Port object.

        Args:
            port_id (str): Unique identifier for the port.
            latitude (float): Latitude coordinate of the port.
            longitude (float): Longitude coordinate of the port.
        """
        self.port_id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers: List[Container] = []
        self.ships: List[Ship] = []
        self.history: List[Ship] = []

    def load_container(self, container: Container) -> bool:
        """
        Load a container into the port.

        Args:
            container (Container): The container to be loaded.

        Returns:
            bool: True if the container was successfully loaded, False otherwise.
        """
        if container is None:
            print("Cannot load a None container.")
            return False

        if container not in self.containers:
            self.containers.append(container)
            return True

        print(f"Container {container.id} is already in the port.")
        return False

    def unload_container(self, container_id: str) -> bool:
        """
        Unload a container from the port.

        Args:
            container_id (str): The ID of the container to be unloaded.

        Returns:
            bool: True if the container was successfully unloaded, False otherwise.
        """
        for container in self.containers:
            if container.id == container_id:
                self.containers.remove(container)
                return True

        print(f"Container with ID {container_id} not found in the port.")
        return False

    def incoming_ship(self, ship: Ship) -> None:
        """
        Register an incoming ship at the port.

        Args:
            ship (Ship): The ship that is arriving at the port.
        """
        self.ships.append(ship)
        print(f"Ship {ship.ship_id} has arrived at Port {self.port_id}.")

    def outgoing_ship(self, ship: Ship) -> None:
        """
        Register an outgoing ship from the port.

        Args:
            ship (Ship): The ship that is leaving the port.
        """
        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.ship_id} has left Port {self.port_id}.")
        else:
            print(f"Ship {ship.ship_id} is not in Port {self.port_id}.")

    def calculate_distance(self, other_port: 'Port') -> float:
        """
        Calculate the distance between this port and another port.

        Args:
            other_port (Port): The other port to calculate the distance to.

        Returns:
            float: The calculated distance between the two ports.
        """
        return math.sqrt((self.latitude - other_port.latitude) ** 2 + (self.longitude - other_port.longitude) ** 2)

    def sail_to(self, destination_port: 'Port') -> None:
        """
        Simulate sailing from this port to a destination port.

        Args:
            destination_port (Port): The destination port.
        """
        print(f"Sailing from {self.port_id} to {destination_port.port_id}.")

    def to_dict(self) -> Dict:
        """
        Convert the Port instance to a dictionary representation.

        Returns:
            Dict: A dictionary containing the port's attributes.
        """
        return {
            "port_id": self.port_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "containers": [container.to_dict() for container in self.containers],
            "ships": [ship.to_dict() for ship in self.ships],
            "history": [ship.to_dict() for ship in self.history],
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Port':
        """
        Create a Port instance from a dictionary.

        Args:
            data (Dict): A dictionary containing port attributes.

        Returns:
            Port: A new Port instance populated with data from the dictionary.
        """
        port = Port(data['port_id'], data['latitude'], data['longitude'])
        return port

    def save_to_json(self, filename: str) -> None:
        """
        Save the port's data to a JSON file.

        Args:
            filename (str): The name of the file where the port's data will be saved.
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Port':
        """
        Load a Port instance from a JSON file.

        Args:
            filename (str): The name of the file from which to load the port's data.

        Returns:
            Port: A new Port instance populated with data from the JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return Port.from_dict(data)

    def __str__(self) -> str:
        """
        Return a string representation of the Port.

        Returns:
            str: A string describing the port's ID and coordinates.
        """
        return f"Port {self.port_id} at coordinates ({self.latitude}, {self.longitude})"
