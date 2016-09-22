G_MODEL = "Guitar Model"
G_PRICE = "Price"
G_YEAR = "Year made"

from guitars import Guitar


def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    add_guitar(guitars)

    print("These are my guitars: ")

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.price,
                                                                  vintage_string))
def add_guitar(guitars):
    name = get_guitar_name()
    year = get_guitar_year()
    price = get_guitar_price()
    guitars.append(Guitar(name, year, price))
    print("{} ({}) : ${} added".format(name, year, price))

def get_guitar_name():
    print(G_MODEL)
    new_name = str(input(">>> "))
    return new_name

def get_guitar_year():
    print(G_YEAR)
    new_year = int(input(">>> "))
    return new_year

def get_guitar_price():
    print(G_PRICE)
    new_price = float(input(">>> "))
    return new_price
main()
