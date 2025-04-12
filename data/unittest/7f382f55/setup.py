import time
import requests
import os
class Customer:
    def __init__(self, full_name, email_address, home_address, bank_card):
        self.full_name = full_name
        self.email_address = email_address
        self.home_address = home_address
        self.bank_card = bank_card

class Order:
    def __init__(self, order_id, client, item_list, total_amount, payment_method):
        self.order_id = order_id
        self.client = client
        self.item_list = item_list
        self.total_amount = total_amount
        self.payment_method = payment_method

invoices = {
    "INV001": Order("INV001", 
                    Customer("Alice Smith", "alice@domain.com", "789 Pine St, Anytown, USA", "9876-5432-1098-7654"),
                    ["Gadget A", "Gadget B"],
                    199.99,
                    "Credit Card")
}