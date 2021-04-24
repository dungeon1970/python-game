import inventory, msvcrt

def other_options(answer):
    if answer == "i":
        inventory.get_items()

    elif answer == "q":
        print("Exit")
        quit()

