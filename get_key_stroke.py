import msvcrt, time
 
def get_response(option_list):
    valid_key_press = False
    while valid_key_press == False:
        key_pressed = msvcrt.getch().decode().lower() # gets the key pressed
        if key_pressed == "i" or key_pressed == "s" or key_pressed == "q":
            valid_key_press = True
            continue
        for key in option_list:
            if key_pressed == key:
                valid_key_press = True
                continue
    return key_pressed

    

