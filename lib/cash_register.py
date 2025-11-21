#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.last_transaction = amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total = self.total * (100 - self.discount) / 100
        if self.total.is_integer():
            self.total = int(self.total)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0