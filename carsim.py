WELCOME = "Let's drive!"
MENU = "Menu:\nd) drive\nr) refuel\nq) quit"
DISTANCETODRIVE = "How many km do you wish to drive?"
ADDFUEL = "How many units of fuel do you want to add to the car?"

from car import Car


def main():
    print(WELCOME)
    car_name = input("Enter your car name: ")
    vehical = Car(100, car_name)

    print(vehical)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            menu_drive(vehical)
        elif choice == 'R':
            menu_refuel(vehical)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Good bye {}'s driver.".format(car_name))


def menu_drive(vehical):
    while True:
        try:
            print(DISTANCETODRIVE)
            travel_distance = int(input(">>> "))
            if travel_distance >= 1:
                vehical.drive(travel_distance)
                print("The car drove {}km".format(travel_distance))
                if vehical.fuel <= 0:
                    dry_tank = vehical.fuel - travel_distance
                    print("The car drove {}km and ran out of fuel".format(dry_tank))
                    return dry_tank
                print(vehical)
                return travel_distance
            else:
                print("Distance must be >= 0")
        except ValueError:
            print("Invalid choice")


def menu_refuel(vehical):
    while True:
        try:
            print(ADDFUEL)
            add_count_fuel = int(input(">>> "))
            if add_count_fuel >= 1:
                vehical.add_fuel(add_count_fuel)
                print("Added {} units of fuel.".format(add_count_fuel))
                print(vehical)
                return add_count_fuel
            else:
                print("Fuel amount must be >= 0")
        except ValueError:
            print("Invalid choice")


main()
