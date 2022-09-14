class Logger:

    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, Order, location_number):
        
        self.transaction_count += 1
        self.daily_sales += int(Order)

        self.log = open("log.txt", "a")
        self.log.write(f"TRX#{self.transaction_count}: {Order} at location {location_number} - ${Order}. Total: ${self.daily_sales}")
        self.log.close()

logger = Logger()