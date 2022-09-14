from pasta import Pasta
from pizza import Pizza
from salad import Salad

class OrderFactory:
    
    @staticmethod
    def create_order(name):
        if name == "pizza":
            return Pizza()
        elif name == "Pasta":
            return Pasta()
        elif name == "Salad":
            return Salad()