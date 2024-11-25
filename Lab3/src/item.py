from abc import ABC, abstractmethod

class Item(ABC):
    """
    Abstract base class for all types of items.

    Attributes:
        ID (int): Unique identifier for the item.
        weight (float): Weight of a single item.
        count (int): Number of items.
        containerID (int): Identifier for the container holding the item.
    """

    def __init__(self, item_id: int, weight: float, count: int, container_id: int):
        """
        Initialize an Item object.

        Args:
            item_id (int): Unique identifier for the item.
            weight (float): Weight of a single item.
            count (int): Number of items.
            container_id (int): Identifier for the container holding the item.
        """
        self.ID = item_id
        self.weight = weight
        self.count = count
        self.containerID = container_id

    @abstractmethod
    def get_total_weight(self) -> float:
        """
        Calculate and return the total weight of all items.

        Returns:
            float: Total weight of all items.
        """
        pass

class SmallItem(Item):
    """Class representing a small item."""

    def get_total_weight(self) -> float:
        """
        Calculate and return the total weight of all small items.

        Returns:
            float: Total weight of all small items.
        """
        return self.weight * self.count

class HeavyItem(Item):
    """Class representing a heavy item."""

    def get_total_weight(self) -> float:
        """
        Calculate and return the total weight of all heavy items.

        Returns:
            float: Total weight of all heavy items.
        """
        return self.weight * self.count

class RefrigeratedItem(Item):
    """Class representing a refrigerated item."""

    def get_total_weight(self) -> float:
        """
        Calculate and return the total weight of all refrigerated items.

        Returns:
            float: Total weight of all refrigerated items.
        """
        return self.weight * self.count

class LiquidItem(Item):
    """Class representing a liquid item."""

    def get_total_weight(self) -> float:
        """
        Calculate and return the total weight of all liquid items.

        Returns:
            float: Total weight of all liquid items.
        """
        return self.weight * self.count

class ItemFactory:
    """Factory class for creating different types of items."""

    @staticmethod
    def create_item(item_type: str, item_id: int, weight: float, count: int, container_id: int) -> Item:
        """
        Create and return an item of the specified type.

        Args:
            item_type (str): Type of the item to create ("small", "heavy", "refrigerated", or "liquid").
            item_id (int): Unique identifier for the item.
            weight (float): Weight of a single item.
            count (int): Number of items.
            container_id (int): Identifier for the container holding the item.

        Returns:
            Item: An instance of the specified item type.

        Raises:
            ValueError: If an unknown item type is provided.
        """
        if item_type == "small":
            return SmallItem(item_id, weight, count, container_id)
        elif item_type == "heavy":
            return HeavyItem(item_id, weight, count, container_id)
        elif item_type == "refrigerated":
            return RefrigeratedItem(item_id, weight, count, container_id)
        elif item_type == "liquid":
            return LiquidItem(item_id, weight, count, container_id)
        else:
            raise ValueError(f"Unknown item type: {item_type}")