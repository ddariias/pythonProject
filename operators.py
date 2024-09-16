from typing import TYPE_CHECKING
from customers import Customer

if TYPE_CHECKING:
    from customers import Customer


class Operator:
    """Represents a mobile operator with charges for calls, messages, and internet."""

    def __init__(self, id: int, talking_charge: float,
                 message_cost: float, network_charge: float,
                 discount_rate: int) -> None:
        """Initializes an Operator instance."""
        self.id = id
        self.talking_charge: float = talking_charge
        self.message_cost: float = message_cost
        self.network_charge: float = network_charge
        self.discount_rate: int = discount_rate

    def calc_talking_cost(self, minutes: float, customer: Customer) -> float:
        """Calculate the cost of a call based on duration and customer age."""
        cost = self.talking_charge * minutes

        if customer.age < 18 or customer.age > 65:
            cost *= (1 - self.discount_rate / 100)

        print(f"Call to {customer.first_name}, {customer.last_name} costs {cost}")
        return cost

    def calculate_message_cost(self, quantity: int, customer: Customer) -> float:
        """Calculate the total cost of sending messages."""
        return quantity * self.message_cost

    def calculate_network_cost(self, amount: float) -> float:
        """Calculate the cost of internet usage."""
        return amount * self.network_charge









