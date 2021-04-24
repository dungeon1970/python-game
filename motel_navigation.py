from get_key_stroke import get_response
import option_functions, read_text, inventory, os, time, room_one, room_two, room_three, room_five, room_seven, msvcrt
import fight


def story_begin():
    os.system("cls")
    print("""
    \033[1;36;40m ____        _   
    |  _ \      | |  
    | |_) | __ _| |_   ___  ___ 
    |  _ < / _` | __| / _ \/ __|
    | |_) | (_| | |_ |  __/\__ \ 
    |____/_\__,_|\__|_\___||___/.  
    \033[1;31;40m|  ____________________  |  |
    \033[1;31;40m| | \033[1;30;40m[|]\033[1;33;40m[|]\033[1;30;40m[|]\033[1;33;40m[|][|][|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;33;40m[|][|]\033[1;30;40m[|]\033[1;33;40m[|]\033[1;30;40m[|][|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;33;40m[|]\033[1;30;40m[|][|][|]\033[1;33;40m[|]\033[1;30;40m[|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;33;40m[|][|][|]\033[1;30;40m[|][|]\033[1;33;40m[|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;33;40m[|]\033[1;30;40m[|]\033[1;33;40m[|][|]\033[1;30;40m[|][|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;30;40m[|][|]\033[1;33;40m[|]\033[1;30;40m[|][|]\033[1;33;40m[|] \033[1;31;40m| |  |
    \033[1;31;40m| | \033[1;33;40m[|]\033[1;30;40m[|]\033[1;33;40m[|]\033[1;30;40m[|]\033[1;33;40m[|][|] \033[1;31;40m| |  |
    \033[1;31;40m| |____________________\033[1;31;40m| |  |
    \033[1;31;40m|___________________________|
    \033[1;31;40m|\033[1;33;40m[][][][][][][][][][][] \033[1;31;40m|   |
    \033[1;31;40m|\033[1;33;40m[][][][][][][][][][][] \033[1;31;40m|   |
    \033[1;31;40m|\033[1;33;40m[][][][][][][][][][][] \033[1;31;40m|   |
    \033[1;31;40m|__________\033[1;37;40m||\033[1;31;40m___________\033[1;31;40m|___|""")
    time.sleep(2)
    os.system("cls")

    print("""
            _______                        
           |       |              
       ____|_______|____       
          // ~~ ~~ \\               
         /\  O| |O  /\            
         \_   (_)   _/         ___________________         ________________________
           \  ___  /          |___________________|       |________________________|
            \_____/             |\ ___________ /|         |        /             / |
       _____|_____|_____        | |  /|,| |   | |         |       /         /   /  |
      /    /\    /\     \       | | |,x,| |   | |         |      /         /   /   |
     |     \ \  / /      |      | | |,x,' |   | |         |     /   /     /   /    |
     |   |  \ \/ /   |   |      | | |,x   ,   | |         |        //    /         |
     |   |   \ \/    |   |      | | |/    |   | |         |       //           /   |
     |   |    \o\    |   |      | |    /] ,   | |         |  /    /           /    |
     |   |    | |    |   |      | |   [/ ()   | |         | /    /     /     /     |
     |   |    |o|    |   |      | |       |   | |         |/          /     /      |
     |   |    | |    |   |      | |       |   | |         |========================|
     |   |    |o|    |   |      | |       |   | |
     |___|    | |\   |___|      | |      ,'   | |
     /   \___/_/\_\__/   \      | |   ,'      | |
     \\\\_\         /_////______|_|,'_________|_|______________________________________
      \\\)     |     (///         
        | ___  | ___  |         
        |      |      |   

\033[1;37;40m
         This game was created by
        Colin, Deano, John and Wayi   

        Press Space to continue......       
    """)
    c = False
    while c == False:
        key_pressed = msvcrt.getch().decode().lower()
        if key_pressed == " ":
            c = True
    os.system("cls")

    beginning_story = [
    """

    

          'Hello and welcome to Bates Motel', said the strange looking man
    outside the entrance of a seedy looking, run down motel.
            
        He walks through the creaking front entrance and beckons you inside.
    You follow him in, and on entering the reception hall you see a corridor with eight rooms to
    to your left. The strange man walks over to the back door at the other end of the reception room
    as the entrance door slams shut behind you. A fear falls over you, deciding to leave, you
    try to open the front door you find it is jammed tight with no way of escaping.
            
        Asking the strange man that you wish to go he replies 'I am Norman Bates
    and you will never leave here alive!'. He stands blocking the only way out... the door
    at the other side of reception, panic sets in and the only options you have are to fight
    Norman or enter the corridor and try to find something in one of the motel rooms to help you.


    Pressing (i) at anytime will show your inventory
             (s) at any time will show where in the story you are
         and (q) at any time will quit
    
    """
    ]
    read_text.read_letters(beginning_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    (F)ight Norman or enter the (C)orridor\n"
    ]
    option_list = ["f", "c"]
    read_text.read_line(options)
    cont = False
    while cont == False:
        answer = get_response(option_list)
        if answer == "i" or answer == "q":
            os.system("cls")
            option_functions.other_options(answer)
            read_text.read_line(options)
        elif answer == "s":
            cont = True
            story_begin()
        elif answer == "f":
            fight.fight_norman()
            cont = True
        elif answer == "c":
            enter_corridor()
            cont = True


def enter_reception():      
    os.system("cls")
    reception_story = [
    """
    \n
    You enter the reception of the motel, Norman looks at you menacingly next to the rear exit,
    you can see eight rooms along the corridor to your left.
    \n
    """
    ]
    read_text.read_letters(reception_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    Go to (C)orridor or (F)ight Norman"
    ]
    option_list = ["c", "f"]
    read_text.read_line(options)
    cont = False
    while cont == False:
        answer = get_response(option_list)
        if answer == "i" or answer == "q":
            os.system("cls")
            option_functions.other_options(answer)
            read_text.read_line(options)
        elif answer == "s":
            os.system("cls")
            cont = True
            enter_reception()
        elif answer == "c":
            enter_corridor()
            cont = True
        elif answer == "f":
            fight.fight_norman()
       


def enter_corridor():
    os.system("cls")
    corridor_story = [
    """\033[1;37;40m
    \n
    You enter the corridor of the motel, it is very dark and musty with spiders webs
    and dirt everywhere, along the corridor there are eight doors numbered one to eight.
    What to do.... You decide to try looking in each room to find something to defeat 
    Norman and escape to freedom!
    \n
    """
    ]
    read_text.read_letters(corridor_story)
    options =[
        "\n",
        "    What would you like to do?",
        "    Go back to (R)eception or enter a room (1-8)"
    ]
    option_list = ["r", "1", "2", "3", "4", "5", "6", "7", "8"]
    read_text.read_line(options)
    cont = False
    while cont == False:
        answer = get_response(option_list)
        if answer == "i" or answer == "q":
            os.system("cls")
            option_functions.other_options(answer)
            read_text.read_line(options)
        elif answer == "s":
            os.system("cls")
            cont = True
            enter_corridor()
        elif answer == "r":
            enter_reception()
            cont = True
        elif answer == "1":
            # define function for room one
            room_one.enter()
            enter_corridor()
            cont = True
        elif answer == "2":
            # define function for room two
            room_two.enter()
            print("2")
            cont = True
        elif answer == "3":
            # define function for room three
            room_three.enter()
            cont = True
        elif answer == "4":
            # define function for room four
            print("    The door is locked")
            read_text.read_line(options)
        elif answer == "5":
            # define function for room five
            room_five.enter()
            cont = True
        elif answer == "6":
            # define function for room six
            print("    The door is locked")
            read_text.read_line(options)
        elif answer == "7":
            # define function for room seven
            room_seven.door_7()
            cont = True
        elif answer == "8":
            # define function for room eight
            print("    The door is locked")
            read_text.read_line(options)