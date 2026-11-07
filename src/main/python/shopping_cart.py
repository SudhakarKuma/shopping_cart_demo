class ShoppingCart:

    def __init__(self):
        self.subtotal = 0

    def add_item(self, price):
        self.subtotal += price

    def total(self):
        if self.subtotal > 1000:
            return self.subtotal*0.9
        return self.subtotal 