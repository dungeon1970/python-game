import inventory, time, read_text, msvcrt, os, option_functions, motel_navigation

umbrella = False

def enter():
    global umbrella
    os.system("cls")
    room_three_story = [
    """
    \n
    You enter room three, there is a bed in the room, a table and chairs. You search\n    under the bed but there is nothing there. There looks to be something\n    behind the door. 
    """
    ]
    read_text.read_letters(room_three_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    (L)ook behind door, Look under (B)ed or go back to (C)orridor"
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
            if umbrella == False:
                print("""
                You find an umbrella and pick it up.
                """
                )
                umbrella = True
                inventory.add_item("Umbrella")
            else:
                print("""
                You already have the umbrella.
                """
                )
            read_text.read_line(options)
        elif key_pressed == "b":
            print("""
                There is nothing under the bed.
                """
                )
            read_text.read_line(options)
        elif key_pressed == "c":
            motel_navigation.enter_corridor()
            cont = True









