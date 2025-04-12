import time
import requests
import os
class Buyer:
    def __init__(self, name, email, address, credit_card):
        self.name = name
        self.email = email
        self.address = address
        self.credit_card = credit_card

class PurchaseOrder:
    def __init__(self, id, customer, items, total, payment_method):
        self.id = id
        self.customer = customer
        self.items = items
        self.total = total
        self.payment_method = payment_method

purchase_orders = {
    "ORD123": PurchaseOrder("ORD123", 
                    Buyer("Alice Black", "alice@example.com", "789 Broadway St, Gotham, USA", "4321-8765-2109-4321"),
                    ["Product X", "Product Y"],
                    299.50,
                    "Debit Card")
}