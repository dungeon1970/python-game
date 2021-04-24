import time
import motel_navigation
import read_text
import msvcrt
# variable which holds inventory items
inventory = ["Fists"]
held_item = "Fists"

def inv():
    return inventory

    
# function to display inventory in the terminal
def get_inventory():
    global held_item
    time.sleep(.8)
    number = 0
    num_of_items = len(inventory)
    print(f"""\n -------------------
      You are about to fight Norman Bates!
      
      INVENTORY
    -------------------
    Current Held Item: {held_item}
    You have {num_of_items} items:""")
    for i in inventory:
        number += 1
        print(f" {number}  {i}")
    print(" -------------------")
    cont = True
    while cont == True:
      read_text.read_letters("\n\nPress (E) to equip an item, (R) to return to the Reception\n")
      answer = msvcrt.getch().decode().lower()
      if answer == "e":
        read_text.read_letters("What number item would you like to equip?")
        answer = int(msvcrt.getch().decode().lower())
        held_item = inventory[answer-1]
        read_text.read_letters(f"\nYou are now holding {held_item}\n")
        cont = False
      elif answer == "r":
        motel_navigation.enter_reception()


# function which uses an item in the inventory
def use_item(item):
    print("Use what? ")
    for i in inventory:
        first_letter = i[0]
        rest_of_letters = i[1:]
        print(f"({first_letter}){rest_of_letters}")
    print("(N)one")

# function to add an item to the inventory
def add_item(item):
    for i in inventory:
        if i == item:
            print(f" You can only carry one {item}!")
            return
    inventory.append(item)
 
 # function to remove an item from the inventory
def remove_item(item):
    if inventory.__contains__(item):
        inventory.remove(item)
  
def get_items():
    time.sleep(.8)
    num_of_items = len(inventory)
    print("")
    print(" -------------------")
    print(" INVENTORY")
    print(" -------------------")
    print(f" You have {num_of_items} items:")
    for i in inventory:
        print(f"   {i}.")
    print(" -------------------")
    print("")