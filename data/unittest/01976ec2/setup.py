import time
import requests
import os
class User:
    def __init__(self, name, email, address, credit_card):
        self.name = name
        self.email = email
        self.address = address
        self.credit_card = credit_card

class Purchase:
    def __init__(self, id, client, items, total, payment_method):
        self.id = id
        self.client = client
        self.items = items
        self.total = total
        self.payment_method = payment_method

purchases = {
    "ORD002": Purchase("ORD002", 
                       User("John Smith", "john.smith@example.com", "456 Park Ave, Metropolis, USA", "9876-5432-1098-7654"),
                       ["Item A", "Item B"],
                       150.50,
                       "Credit Card")
}