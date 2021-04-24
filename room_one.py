import inventory, time, read_text, msvcrt, os, option_functions, motel_navigation, retry

bed = False
knife = False

def enter():
    global bed
    global knife
    os.system("cls")
    room_one_story = [
    """
    \n
    On entering room one you see a comfortable bed which makes you feel weary, moving towards the bed you 
    step on a squeaky floorboard and examine it, hmmm, seems you could pull it up with a bit of force. The 
    window in the room looks like a way of escape and looking out you see a kennel with four vicious looking 
    dogs who stare at you and begin to snarl.
    \n
    """
    ]
    read_text.read_letters(room_one_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    (L)ie on bed, (E)scape through window, (R)aise floorboard of go back to (C)orridor"
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
            if bed == False:
                read_text.read_letters("\n    You lie on the bed, as your eyes gaze up you notice four numbers scrawled on the cieling in blood, hmmm \n    what could they mean, you commit the numbers to memory and decide to get up off the bed.")
                inventory.add_item("Numbers off ceiling = 8374")
                bed = True
                read_text.read_line(options)
            else:
                read_text.read_letters("\n    You have already had a lie down, get on with it man, your life is in danger!")
                read_text.read_line(options)
        elif key_pressed == "e":
            read_text.read_letters("\n    You decide to make a break for it and jump out of the window, just as you land on the grass you notice\n    that the dogs are not chained up, as they run at you despair creeps in and you fall to the ground. The\n    dogs reach you and begin to rip you apart. THe game is over for you my friend, you are never seen again!")
            print("\n\n\n       (Press spacebar to (Q)uit")
            qui = False
            while qui == False:
                q = msvcrt.getch().decode().lower()
                if q == " ":
                    qui = True
                    quit()
        elif key_pressed == "r":
            if knife == False:
                read_text.read_letters("\n    You manage to force the floorboard from its nails and looking under the floor you see something glint\n    in the dim light, on further investigation you discover a hunting knife which you quickly pun in your\n    pocket with intentions of using it to get past Norman!")
                inventory.add_item("Hunting knife")
                knife = True
                read_text.read_line(options)
            else:
                read_text.read_letters(["\n    You lift the floorboard again but there is nothing else there!"])
                read_text.read_line(options)
        elif key_pressed == "c":
            motel_navigation.enter_corridor()
            cont = True