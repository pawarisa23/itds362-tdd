class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, converter, unit):
        return Quantity(self.amount, self.unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, converter, unit):
        amount = self.left.amount + self.right.amount
        return Quantity(amount, unit)


class Converter:
    def reduce(self, source, unit):
        return source.reduce(self, unit)
