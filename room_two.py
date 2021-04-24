import inventory, time, read_text, msvcrt, os, option_functions, motel_navigation

safe = False
crowbar = False
gun = False


def enter():
    global safe
    global crowbar
    global gun 
    os.system("cls")
    room_one_story = [
    """
    \n
    On entering room two there is a picture on the wall, a quick glance shows it is on a hinge, in\n    the corner there are a bunch of crowbars stood against the wall and in the middle\n    of the room is a table with a drawer partly open.
    \n
    """
    ]
    read_text.read_letters(room_one_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    (L)ook at picture, (P)ick up crowbar, (E)xamine table or go back to (C)orridor?"
    ]
    read_text.read_line(options)
    cont = False
    while cont == False:
        key_pressed = msvcrt.getch().decode().lower() # gets the key pressed
        if key_pressed == "i" or key_pressed == "q":
            os.system("cls")
            option_functions.other_options(key_pressed)
            read_text.read_line(options)
        elif key_pressed == "s":
            os.system("cls")
            cont = True
            enter()
        elif key_pressed == "l":
            if safe == False:
                read_text.read_letters("\n    Looking a little closer at the picture you discover that it pulls sideways to reveal a safe.\n    Looks like you need a code to open the safe!")
                if "Numbers off ceiling = 8374" in inventory.inventory:
                    read_text.read_letters("\n    Ah... you remember the numbers from the cieling in room one, trying the numbers with\n    the safe you find the safe opens to reveal some money! £2000, what a lucky day!")
                    inventory.add_item("£2000")
                    safe = True
                else:
                    read_text.read_letters("\n    You try different numbers but you cant open the safe!")
            else:
                read_text.read_letters("\n    Now you are being greedy! You already have the money from the safe!")
            read_text.read_line(options)
        elif key_pressed == "p":
            if crowbar == False:         
                read_text.read_letters("\n    You go over to the crowbars and pick one up")
                crowbar = True
                inventory.add_item("Crowbar")
            else:
                read_text.read_letters("\n    You have already got a crowbar")
            read_text.read_line(options)
        elif key_pressed == "e":
            if gun == False:
                read_text.read_letters("\n    You go over to the table, on opening the drawer fully you discover a gun inside, you add it\n    to your weapons to fight Norman!")
                inventory.add_item("Gun")
                gun = True  
            else:
                 read_text.read_letters("\n    You check the drawer again but it is empty!")
            read_text.read_line(options)
        elif key_pressed == "c":
            motel_navigation.enter_corridor()
            cont = True


    













