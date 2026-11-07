class ShoppingCart:

    def __init__(self):
        self.subtotal = 0

    def add_item(self, price):
        self.subtotal += price

    def total(self):
        total = self.subtotal
        if 0 < self.subtotal < 500:
            total += 100 
        if self.subtotal > 1000:
            total *= 0.9
        return total 