from typing import List, Self
from bills import Bill

class Customer:
    """Represents a customer with an ID, name, age, associated operators, and bills."""

    def __init__(self, id: int, first_name: str, last_name: str,
                 age: int, operators: List, bills: List) -> None:

        self.id: int = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.operators: List = operators
        self.bills: List = bills
        self.limiting_amount: float = 1000.0

    def talk(self, minutes: float, customer: Self, operator_id: int) -> None:
        """Simulates a phone call between this customer and another. """
        operator = self.operators[operator_id]
        cost = operator.calc_talking_cost(minutes, customer)
        bill = self.bills[operator_id]

        if bill.check(cost):
            bill.add_debt(cost)
            print(f"{self.first_name} talked to {customer.first_name} for {minutes} minutes. Cost: {cost}")
        else:
            print(f"Spending limit exceeded. The call cannot be completed.")

    def message(self, quantity: int, customer: Self, operator_id: int) -> None:
        """Simulates sending messages from this customer to another."""
        operator = self.operators[operator_id]
        cost = operator.calculate_message_cost(quantity, customer)
        bill = self.bills[operator_id]

        if bill.check(cost):
            bill.add_debt(cost)
            print(f"{self.first_name} sent {quantity} messages to {customer.first_name}. Cost: {cost}")
        else:
            print(f"Spending limit exceeded. Messages cannot be sent.")

    def connection(self, amount: float, operator_id: int) -> None:
        """Simulates an internet connection for this customer."""
        operator = self.operators[operator_id]
        cost = operator.calculate_network_cost(amount)
        bill = self.bills[operator_id]

        if bill.check(cost):
            bill.add_charge(cost)
            print(f"{self.first_name} used {amount} MB. Cost: {cost}")
        else:
            print(f"Spending limit exceeded. Internet connection failed.")








