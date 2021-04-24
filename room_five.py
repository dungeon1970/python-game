import inventory, time, read_text, msvcrt, os, option_functions, motel_navigation

starting_pistol = False
bow_and_arrow = False

def enter():
    global starting_pistol
    global bow_and_arrow

    os.system("cls")
    room_three_story = [
    """
    \n
    You enter room five and you see two items in the room, one is a starting\n    pistol under the table, a bow and arrows hanging off a picture\n    on the wall and a door leading to who knows where. 
    """
    ]
    read_text.read_letters(room_three_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    (P)ick up the starting pistol, (T)ake the bow and arrows from the picture, (O)pen\n    the door or go back to (C)orridor "
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
        elif key_pressed == "p":
            if starting_pistol == False:
                print("""
                You pick up the starting pistol!
                """
                )
                starting_pistol = True
                inventory.add_item("Starting Pistol")
            else:
                print("""
                You already have the starting pistol.
                """
                )
            read_text.read_line(options)
        elif key_pressed == "t":
            if bow_and_arrow == False:
                print("""
                You take the bow and arrow from the picture!
                """
                )
                bow_and_arrow = True
                inventory.add_item("Bow and arrow")
            else:
                print("""
                You already have bow and arrow.
                """
                )
            read_text.read_line(options)
        elif key_pressed == "o":
            read_text.read_letters("""\n    Behind the door is a corridor, you follow it and go through a hatch at the end\n    and you end up ????""")
            print("\n\n\n       (Press spacebar to continue")
            c = False
            while c == False:
                space = msvcrt.getch().decode().lower()
                if space == " ":
                    motel_navigation.enter_corridor()
                    c = True
        elif key_pressed == "c":
            motel_navigation.enter_corridor()
            cont = True