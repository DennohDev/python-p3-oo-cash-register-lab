#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total = 0, items = None, last_transaction = 0):
    self.discount = discount
    self.total = total
    self.last_transaction = last_transaction
    self.items = items if items is not None else []
  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total+=(price*quantity)
    if quantity > 1:
      for i in range(quantity):
        self.items.append(title)
    else:
      self.items.append(title)
  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total - (self.total*self.discount/100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    self.total-=self.last_transaction