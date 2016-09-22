"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from car import Car


def main():
    bus = Car(180, "Bus")
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
    print('')#adds a blank space between bus and limo

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)


main()
