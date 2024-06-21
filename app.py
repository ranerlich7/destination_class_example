from dest.actions import add_destination, print_destinations
from storage.loadsave import load, save
from icecream import ic

my_destinations = []

def menu():
    load()
    ic(my_destinations)
    while True:
        ic("1-add")
        ic("2-list")
        ic("3-exit")
        selection = input("Your comman? ")
        if selection == "1":
            add_destination(my_destinations)
        if selection == "2":
            print_destinations(my_destinations)
            pass
        if selection == "3":
            save()
            exit()


if __name__ == "__main__":
    print("&&&&&&&", __name__)
    menu()
