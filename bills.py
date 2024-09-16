class Bill:
    """Represents a customer's bill, tracking spending and applying limits."""

    def __init__(self, limiting_amount: float, operator_id: int) -> None:
        """Initializes a Bill instance."""
        self.operator_id: int = operator_id
        self.limiting_amount: float = limiting_amount
        self.current_debt: float = 0.0

    def check(self, amount: float) -> bool:
        """Checks if adding a given amount would exceed the spending limit."""
        return self.current_debt + amount >= self.limiting_amount

    def add_debt(self, debt: float) -> None:
        """Adds a specified amount to the current debt, provided it does not exceed the limit."""
        tentative_debt = debt + self.current_debt
        if tentative_debt <= self.limiting_amount:
            self.current_debt += debt
            print(f"Added {debt} to the bill. Total debt: {self.current_debt}")
        else:
            print(f"Spending limit reached! Unable to add {debt} to the bill.")

    def pay(self, amount: float) -> None:
        """Allows the customer to pay off a part or all of their debt."""
        temp_payroll = self.current_debt - amount
        if temp_payroll < 0:
            self.limiting_amount += temp_payroll
        else:
            self.current_debt -= amount

    def change_limit(self, amount: float) -> None:
        """Adjusts the spending limit by a given amount."""
        self.limiting_amount += amount
        print(f"New spending limit: {self.limiting_amount}")
