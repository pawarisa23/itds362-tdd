class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, converter, unit):
        rate = converter.rate(self.unit, unit)
        return Quantity(self.amount * rate, unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, converter, unit):
        amount = (self.left.reduce(converter, unit).amount
                  + self.right.reduce(converter, unit).amount)
        return Quantity(amount, unit)

    def __repr__(self):
        return f"Sum({self.left!r}, {self.right!r})"


class Converter:
    def __init__(self):
        self.rates = {}

    def add_rate(self, source, target, rate):
        self.rates[(source, target)] = rate

    def rate(self, source, target):
        if source == target:
            return 1
        return self.rates[(source, target)]

    def reduce(self, source, unit):
        return source.reduce(self, unit)
