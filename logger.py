from order import Order
from franchise import Franchise

class Logger:

    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self):
        
        self.transaction_count += 1
        self.daily_sales += int(Order.price)

        self.log = open("log.txt", "a")
        self.log.write(f"TRX#{self.transaction_count}: {Order.dish_name} at location {Franchise.location_number} - ${Order.price}. Total: ${self.daily_sales}")
        self.log.close()

logger = Logger()