from typing import List

from dataclasses import dataclass

from Lab2.src.conteiners import Container


class IShip:
    def sail_to(self, port: 'port') -> bool:
        ...

    def re_fuel(self, amount: float) -> None:
        ...

    def load(self, container: Container) -> bool:
        ...

    def un_load(self, container: Container) -> bool:
        ...

    def get_current_containers(self) -> List[Container]:
        ...


@dataclass
class ContainerLimits:
    max_all_containers: int
    max_heavy_containers: int
    max_refrigerated_containers: int
    max_liquid_containers: int


class Ship(IShip):
    """
       Represents a ship that can transport containers between ports.

       This class implements the IShip interface and provides functionality for
       managing a ship's fuel, containers, and movement between ports.

       Attributes:
           id (int): Unique identifier for the ship.
           fuel (float): Current amount of fuel in the ship.
           current_port (Port): The port where the ship is currently located.
           total_weight_capacity (int): Maximum weight the ship can carry.
           fuel_consumption_per_km (float): Amount of fuel consumed per kilometer traveled.
           container_limits (ContainerLimits): Limits for different types of containers.
           containers (List[Container]): List of containers currently loaded on the ship.

       Methods:
           get_current_containers() -> List[Container]:
               Returns a sorted list of containers currently on the ship.

           sail_to(port: Port) -> bool:
               Attempts to sail the ship to the given port, consuming fuel in the process.

           re_fuel(amount: float) -> None:
               Adds the specified amount of fuel to the ship.

           load(container: Container) -> bool:
               Attempts to load a container onto the ship.

           un_load(container: Container) -> bool:
               Attempts to unload a container from the ship.
       """

    def __init__(self,
                 id: int,
                 fuel: float,
                 current_port: 'Port',
                 total_weight_capacity: int,
                 fuel_consumption_per_km: float,
                 container_limits: ContainerLimits) -> None:
        self.id = id
        self.fuel = fuel
        self.current_port = current_port
        self.total_weight_capacity = total_weight_capacity
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.container_limits = container_limits
        self.containers: List[Container] = []

    def get_current_containers(self) -> List[Container]:
        return sorted(self.containers, key=lambda x: x.id)

    def sail_to(self, port: 'port') -> bool:
        distance = self.current_port.get_distance(port)
        required_fuel = distance * self.fuel_consumption_per_km

        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            self.current_port = port
            return True
        return False

    def re_fuel(self, amount: float) -> None:
        self.fuel += amount

    def load(self, container: Container) -> bool:
        if len(self.containers) < self.container_limits.max_all_containers:
            self.containers.append(container)
            return True
        return False

    def un_load(self, container: Container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False