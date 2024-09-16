from typing import List
from customers import Customer
from operators import Operator
from bills import Bill


class Main:
    def __init__(self):
        """Initialize operators, customers, and bills"""
        self.operator1 = Operator(id=0, talking_charge=1.5, message_cost=0.3, network_charge=0.2, discount_rate=10)
        self.operator2 = Operator(id=1, talking_charge=1.2, message_cost=0.4, network_charge=0.25, discount_rate=15)
        self.operator3 = Operator(id=2, talking_charge=1.0, message_cost=0.5, network_charge=0.35, discount_rate=5)

        self.bill1 = Bill(limiting_amount=500.0, operator_id=0)
        self.bill2 = Bill(limiting_amount=300.0, operator_id=1)
        self.bill3 = Bill(limiting_amount=200.0, operator_id=2)

        self.customer1 = Customer(id=0, first_name="Ivan", last_name="Petrenko", age=25,
                                  operators=[self.operator1, self.operator2, self.operator3],
                                  bills=[self.bill1, self.bill2, self.bill3])

        self.customer2 = Customer(id=1, first_name="Olha", last_name="Litvinova", age=17,
                                  operators=[self.operator1, self.operator2],
                                  bills=[self.bill1, self.bill2])

        self.customer3 = Customer(id=2, first_name="Dana", last_name="Sudorenko", age=67,
                                  operators=[self.operator2, self.operator3],
                                  bills=[self.bill2, self.bill3])

    def test_talks(self):
        """Test phone calls between customers"""
        print("Ivan talks with Olha (10 minutes, operator 1)")
        self.customer1.talk(10, self.customer2, 0)

        print("Olha talks with Dana (5 minutes, operator 2)")
        self.customer2.talk(5, self.customer3, 1)

        ivan_bill = self.bill1
        olha_bill = self.bill2
        print("Olha pays 20 units of her bill (operator 2)")
        olha_bill.pay(20)

    def test_chat(self):
        """Test messaging between customers"""
        print("Ivan sends 6 messages to Dana (operator 1)")
        self.customer1.message(6, self.customer3, 0)

        print("Olha sends 11 messages to Ivan (operator 2)")
        self.customer2.message(11, self.customer1, 1)

        dana_bill = self.bill3
        print("Dana changes her bill limit to 20")
        dana_bill.change_limit(20)

    def test_networking(self):
        """Test internet usage between customers"""
        print("Ivan uses 150 units of internet (operator 1)")
        self.customer1.connection(150, 0)

        print("Olha uses 60 units of internet (operator 2)")
        self.customer2.connection(60, 1)

        dana_bill = self.bill3
        print("Dana pays 70 units of her bill (operator 2)")
        dana_bill.pay(70)


if __name__ == "__main__":
    main = Main()

    print("------Talk-------")
    main.test_talks()
    print("\n------Chat-----")
    main.test_chat()
    print("\n-------Net-------")
    main.test_networking()
