import time
import requests
import os
class Client:
    def __init__(self, name, email, address, credit_card):
        self.name = name
        self.email = email
        self.address = address
        self.credit_card = credit_card

class Transaction:
    def __init__(self, id, customer, items, total, payment_method):
        self.id = id
        self.customer = customer
        self.items = items
        self.total = total
        self.payment_method = payment_method

transactions = {
    "ORD001": Transaction("ORD001", 
                          Client("Jane Doe", "jane@example.com", "123 Main St, Anytown, USA", "1234-5678-9012-3456"),
                          ["Item 1", "Item 2"],
                          99.99,
                          "Credit Card")
}