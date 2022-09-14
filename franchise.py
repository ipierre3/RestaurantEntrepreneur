from logger import logger
from order_factory import OrderFactory

class Franchise:
    def __init__(self, location):
        self.location_number = int(location)

    def place_order(self):

        print(f"\nWelcome to Iggy's Italian Cuisine, location #{self.location_number}!")
        print("What're you in the mood for?")

        user_order = int(input("Type '1' for pizza, '2' for pasta, '3' for salad: "))

        while True:
            if user_order > 3:
                print("We don't have that option. Please choose an item from the menu")
                return self.place_order()
            elif user_order <= 0:
                print("We don't have that option. Please choose an item from the menu")
                return self.place_order()
            elif user_order == 1:
                return logger.log_transaction(OrderFactory.create_order("Pizza"), self.location_number)
            elif user_order == 2:
                return logger.log_transaction(OrderFactory.create_order("Pasta"), self.location_number)
            elif user_order == 3:
                return logger.log_transaction(OrderFactory.create_order("Salad"), self.location_number)
        
