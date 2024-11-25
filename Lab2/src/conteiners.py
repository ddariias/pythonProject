from abc import ABC, abstractmethod
from typing import Self


class Container(ABC):
    """
        Abstract base class for all types of containers.

        Attributes:
            id (int): Unique identifier for the container.
            weight (float): Weight of the container in kilograms.

        Methods:
            consumption() -> float:
                Abstract method to calculate the consumption of the container.
            __eq__(other: Self) -> bool:
                Checks if two containers are equal based on their class and weight.
        """
    def __init__(self, id: int,weight: float )-> None:
        self.id = id
        self.weight = weight

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__ (self, other: Self)-> bool:
        """
              Check if this container is equal to another container.

              Two containers are considered equal if they are of the same type and have the same weight.

              Args:
                  other (Container): The other container to compare with.

              Returns:
                  bool: True if the containers are equal, False otherwise.
              """
        return (self.__class__.__name__ == other.__class__.__name__ and
           self.weight == other.weight)


class BasicContainer(Container):
    """
       Represents a basic container.

       Attributes:
           UNIT_CONSUMPTION (float): Unit consumption rate for basic containers.

       Inherits all attributes and methods from Container.
       """

    UNIT_CONSUMPTION = 2.5

    def __init__(self, id:int,weight: float )-> None:
        super().__init__(id=id, weight= weight)

    def consumption(self) -> float:
        """
                Calculate the consumption of the basic container.

                Returns:
                    float: The consumption value.
                """
        return BasicContainer.UNIT_CONSUMPTION * self.weight


class HeavyContainer(Container):
    """
      Represents a heavy container.

      Attributes:
          UNIT_CONSUMPTION (float): Unit consumption rate for heavy containers.

      Inherits all attributes and methods from Container.
      """
    UNIT_CONSUMPTION = 3.0

    def __init__(self, id: int, weight: float) -> None:
        super().__init__(id=id, weight=weight)

    def consumption(self) -> float:
        """
               Calculate the consumption of the heavy container.

               Returns:
                   float: The consumption value.
               """
        return HeavyContainer.UNIT_CONSUMPTION * self.weight

class RefrigeratedContainer(HeavyContainer):
    """
        Represents a refrigerated container.

        Attributes:
            UNIT_CONSUMPTION (float): Unit consumption rate for refrigerated containers.

        Inherits all attributes and methods from HeavyContainer.
        """
    UNIT_CONSUMPTION = 5.0

    def __init__(self, id: int, weight: float) -> None:
        super().__init__(id=id, weight=weight)

    def consumption(self) -> float:
        """
               Calculate the consumption of the refrigerated container.

               Returns:
                   float: The consumption value.
               """
        return RefrigeratedContainer.UNIT_CONSUMPTION * self.weight


class LiquidContainer(HeavyContainer):
    """
        Represents a liquid container.

        Attributes:
            UNIT_CONSUMPTION (float): Unit consumption rate for liquid containers.

        Inherits all attributes and methods from HeavyContainer.
        """
    UNIT_CONSUMPTION = 4.0

    def __init__(self, id: int, weight: float) -> None:
        super().__init__(id=id, weight=weight)

    def consumption(self) -> float:
        """
                Calculate the consumption of the liquid container.

                Returns:
                    float: The consumption value.
                """
        return LiquidContainer.UNIT_CONSUMPTION * self.weight



def container_factory(id: int, weight: float )-> Container:
    """
       Factory function to create different types of containers based on weight and special requirements.

       Args:
           id (int): Unique identifier for the container.
           weight (float): Weight of the container in kilograms.
           special (str, optional): Special requirement code. 'R' for refrigerated, 'L' for liquid.

       Returns:
           Container: An instance of the appropriate Container subclass.

       Raises:
           ValueError: If an invalid special requirement code is provided.
       """
    if weight <= 3000:
        return BasicContainer(id, weight)
    elif special == "R":
        return RefrigeratedContainer(id, weight)
    elif special == "L":
        return LiquidContainer(id, weight)
    else:
        return HeavyContainer(id, weight)