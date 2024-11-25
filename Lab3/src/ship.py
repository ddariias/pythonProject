from abc import ABC, abstractmethod
from containers import Container
from typing import List, Dict
from src.item import Item


class IShip(ABC):
    """Interface for ships."""

    @abstractmethod
    def sail_to(self, port: 'Port') -> bool:
        """Moves the ship to a specified port."""
        pass

    @abstractmethod
    def re_fuel(self, amount: float) -> None:
        """Refuels the ship with a specified amount of fuel."""
        pass

    @abstractmethod
    def load(self, container: Container) -> bool:
        """Loads a container onto the ship."""
        pass

    @abstractmethod
    def unload(self, container: Container) -> bool:
        """Unloads a container from the ship."""
        pass

    @abstractmethod
    def get_current_containers(self) -> List[Container]:
        """Returns the list of containers currently on the ship."""
        pass


class Ship(IShip):
    """Abstract class for various types of ships."""

    def __init__(self, name: str, max_weight: float, fuel_capacity: float):
        """
        Initializes a Ship object.

        Args:
            name (str): The name of the ship.
            max_weight (float): The maximum weight the ship can carry.
            fuel_capacity (float): The fuel capacity of the ship.
        """
        self.name = name
        self.max_weight = max_weight
        self.fuel_capacity = fuel_capacity
        self.current_weight = 0
        self.containers: List[Container] = []

    def sail_to(self, port: 'Port') -> bool:
        """Sails the ship to a specified port."""
        # Logic for sailing the ship to a port goes here
        pass

    def re_fuel(self, amount: float) -> None:
        """Refuels the ship with the specified amount of fuel."""
        # Logic for refueling the ship goes here
        pass

    def load(self, container: Container) -> bool:
        """Loads a container onto the ship, checking weight limits."""
        if self.current_weight + container.weight <= self.max_weight:
            self.containers.append(container)
            self.current_weight += container.weight
            return True
        return False

    def unload(self, container: Container) -> bool:
        """Unloads a container from the ship."""
        if container in self.containers:
            self.containers.remove(container)
            self.current_weight -= container.weight
            return True
        return False

    def get_current_containers(self) -> List[Container]:
        """Returns the list of containers currently on the ship."""
        return self.containers


class LightWeightShip(Ship):
    """Represents a lightweight ship with smaller capacity."""

    def __init__(self):
        """Initializes a lightweight ship with predefined attributes."""
        super().__init__(name="Lightweight Ship", max_weight=1000, fuel_capacity=500)


class MediumShip(Ship):
    """Represents a medium-sized ship with moderate capacity."""

    def __init__(self):
        """Initializes a medium ship with predefined attributes."""
        super().__init__(name="Medium Ship", max_weight=2000, fuel_capacity=1000)


class HeavyShip(Ship):
    """Represents a heavy ship with large capacity."""

    def __init__(self):
        """Initializes a heavy ship with predefined attributes."""
        super().__init__(name="Heavy Ship", max_weight=3000, fuel_capacity=1500)


class ShipBuilder:
    """Builder class for creating ships."""

    def __init__(self):
        """Initializes the ShipBuilder with no ship."""
        self.ship = None

    def set_ship_type(self, ship_type: str) -> 'ShipBuilder':
        """
        Sets the type of ship to build.

        Args:
            ship_type (str): The type of ship to build ("lightweight", "medium", or "heavy").

        Returns:
            ShipBuilder: The builder instance for method chaining.
        """
        if ship_type == "lightweight":
            self.ship = LightWeightShip()
        elif ship_type == "medium":
            self.ship = MediumShip()
        elif ship_type == "heavy":
            self.ship = HeavyShip()
        return self

    def set_max_weight(self, max_weight: float) -> 'ShipBuilder':
        """
        Sets the maximum weight capacity for the ship.

        Args:
            max_weight (float): The maximum weight capacity.

        Returns:
            ShipBuilder: The builder instance for method chaining.
        """
        if self.ship:
            self.ship.max_weight = max_weight
        return self

    def set_fuel_capacity(self, fuel_capacity: float) -> 'ShipBuilder':
        """
        Sets the fuel capacity for the ship.

        Args:
            fuel_capacity (float): The fuel capacity.

        Returns:
            ShipBuilder: The builder instance for method chaining.
        """
        if self.ship:
            self.ship.fuel_capacity = fuel_capacity
        return self

    def build(self) -> Ship:
        """
        Builds and returns the constructed ship.

        Returns:
            Ship: The constructed ship instance.
        """
        return self.ship
