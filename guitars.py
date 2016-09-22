class Guitar:
    def __init__(self, name="", year=0, price=0):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        return "{} ({}) : ${:2f}".format(self.name, self.year, self.price)

    def get_age(self):
        return 2016 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
