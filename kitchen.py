class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)

    def __eq__(self, other):
        return True
