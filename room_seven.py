import msvcrt, os, time, retry
from read_text import read_letters
from inventory import get_items
from inventory import add_item
from inventory import remove_item
from inventory import inv
from inventory import inventory
import motel_navigation

first7 = 0
TV_count = 0
ward_count = 0
bath_count = 0
sink_count = 0
umb_count = 0

def door_7():
    global TV_count
    global first7
    global ward_count
    global bath_count
    global held_item
    global umb_count
    if TV_count != 0 and ward_count != 0 and bath_count != 0:
        read_letters("    It appears you've done everything you can in room 7.")
        motel_navigation.enter_corridor()
    if first7 == 0:
        first7 += 1
        read_letters(f"""\033[1;31;40m\n\n    You attempt to enter room No. 7, but it appears to be locked.\n    The lock seems brittle, maybe I could break it with something""")



        a = False
        while a == False:
          if inventory.count("Umbrella") == 0:
              read_letters("\033[1;31;40m\n    It seems that there's no way in this room right now\n")
              
              



              print("\n\n\n       (Press spacebar to continue)")
              c = False
              while c == False:
                space = msvcrt.getch().decode().lower()
                if space == " ":
                  motel_navigation.enter_corridor()
                  c = True
                  a = True
          elif inventory.count("Umbrella") > 0 :
              read_letters("\033[1;31;40m\n    You could use the Umbrella to open the door,\n    But it looks like it might break,\033[1;37;40m\n    Would you like to use the unbrella? (Y)es or (N)o\n")
              answer = msvcrt.getch().decode().lower()
              if answer == "y":
                  read_letters("\033[1;31;40m\n    You break the lock and Umbrella snaps in half.\n")
                  held_item = "Fists"
                  remove_item("Umbrella")
                  umb_count += 1
                  a = True
                  in_room7()
              elif answer == "n":
                a = True
                motel_navigation.enter_corridor()
              else:
                read_letters("Invalid answer, please try retry")
                continue
    elif first7 == 1:
        b = False
        while b == False:
          if umb_count == 0:
            if inventory.count("Umbrella") > 0 :
                read_letters("\033[1;31;40m    You could use the Umbrella to open the door,\n    But it looks like it might break,\033[1;37;40m\n    Would you like to continue?\n")
                answer = msvcrt.getch().decode().lower()
                if answer == "y":
                    read_letters("\033[1;37;40m\n    You break the lock and Umbrella snaps in half.\n")
                    held_item = "Fists"
                    remove_item("Umbrella")
                    umb_count += 1
                    b = True
                    in_room7()
                elif answer == "n":
                  b = True
                  motel_navigation.enter_corridor()
                #else:
                #  read_letters("Invalid answer, please try retry")
                #  continue
          elif umb_count > 0:
            in_room7()
            
def in_room7():
    global TV_count
    global ward_count
    print("""\033[1;31;40m\n o(=(=(=(=)=)=)=)o
  !!!!!!}!{!!!!!!                                    __________
  !!!!!} | {!!!!!                                   |  __  __  |   ___________
  !!!!}  |  {!!!!     _!_                           | |  ||  | |  |     |     |
  !!!'   |   '!!!    |~@~|     ________________     | |  ||  | |  |     |     |
  ~@~----+----~@~    |___|    |                |    | |__||__| |  |    o|o    |
  !!!    |    !!!      |      |                |    |  __  __()|  |     |     |
  !!!    |    !!!     ( )     |_______  _______|    | |  ||  | |  |_____|_____|
  !!!____|____!!!  __(___)__  {__~@~__}{__~@~__}    | |  ||  | |  |_____-_____|
  !!!=========!!!   |__-__|   |%%%%%%%%%%%%%%%%|    | |__||__| |  |_____-_____|
 _!!!_________!!!___|_____|___|%%%%%%%%%%%%%%%%|____|__________|__|_____-_____|_
                    |     |   |%%%%%%%%%%%%%%%%|                  |/         \|
    
    You enter room 7 and are immediately greeted by an overwhelming acidic smell
    It's making your nose burn.""")
    d = False
    while d == False:
      read_letters("""\033[1;37;40m\n    When you inspect the room, you notice:
      A (T)V
      A (W)ardrobe
      A (B)athroom
     (C) to return to corridor
      
    What would you like to inspect?\n""")
      answer = msvcrt.getch().decode().lower()
      if answer == "t":
          if TV_count == 0:
              read_letters("""\033[1;31;40m\n\n   
    You inspect the TV, and turn it on.... Static                                             
    But you swear you're hearing things.
\033[1;37;40m\n    (W)ait around or (B)ack?\n""")
              answer = msvcrt.getch().decode().lower()
              if answer == "w":
                  TV_count +=1
                  read_letters("\033[1;31;40m\n\n#̷͍̝͔͚̩̻̰̮͇̪̝̃̓̐̄̏͗̔̆͂̈́́̾̓͜͜͝ͅ#̷̰̘̠̩̖̱̟̜̅̈́̉͆͂̉̾̕#̶̭̼̘̥͉̙̖̝̭̖̄̏#̵̢̂̊̓͐̌͂̊͋͂͘͠͝   #̸̳͚̲͇̅̌̈́͛̈́̓͠#̶̘̤͓͈̓̌̆̄̈́̋́̈́̾̕̕͝#̷͍̝͔͚̩̻̰̮͇̪̝̃̓̐̄̏͗̔̆͂̈́́̾̓͜͜͝ͅ#̷̰̘̠̩̖̱̟̜̅̈́̉͆͂̉̾̕#̶̭̼̘̥͉̙̖̝̭̖̄̏#̵̢̂̊̓͐̌͂̊͋͂͘͠͝#̷̤̦̟̼̭̳͗͋̈́̊͊̒͝#̷̡̼̪̱̫̱̻̣̾͆͑ͅ#̷̡̦̼̰̥͈̱̣̼͉͎͚̖̌̈́̂͜#̸̳̜̤͉͈̅͆̂̾͛͛́͌̕͝.  #̷̢̘̱̳͖̺̞͖͂̆̋̀͋̍̇́̑̄̍̅̿̽̃́̇̓̉͆̋̄͂̂̇̈̓͊͆͘͝#̷̡̛̦̯̻̬̥̟̹͉̲͈̘͋̓̈͌̾̅̊͂̔̆̂̓͂̏̈́͒̀̾̈̿͗́́̈̑̑͘͠#̷̢͍̺̻̻̩̘͇͍͎̪̲͈̰̝̦͍̱̹͙̠̥̹͒͊͐͐̍̈̏̀͒͌̔̄̀̉̄̾̅̎̉͂̕͝ͅ#̸̡̡̨̡̛̮̦̞̟̝͍͉̰͓͕̯͇̜̖̖̥͎̯̜͙̪͇̼̦̮̮͙̝͍́̋͂͒̽̅̎̅͑͆͗̍́̆̓͗̽̐̋̉͒̂͛̀̃̂͂̆͌͛̽̆͘ͅͅ#̸̡̢̙͔̥͙͚͇͓̙̠̍͑̇͒͜͝#̷̧̨̧̪̟̦͙̳̬̼̻͚̹̻͔̤̩͚̳̽́͜͜#̵̖̬̝̖͚͉̫̥̖̹̪̭̳̻̜̤̪͍͈̞̏̿̀̂̃͒̊͝   #̶̖͍̦̟̲͙̖͍̔͌͗̌̍̎̒ͅ#̷͈̦͇̬̌̂̋̊́̽̎͒͠#̴̢̛̝̠̩̯̮̝͗͋̓̑̕#̴̡̱̤͍͙̪͎̽̈́̾̇̚͜͝͠\n#̶͚̅̈́͗̾͝#̶̠̰̠͔̯̱̌#̷̛̜̠̐̀̌̅͘̚͘͝ͅ#̸̠̜̒͌̿̽#̷̭͓̪͊   #̷̡̛̦̯̻̬̥̟̹͉̲͈̘͋̓̈͌̾̅̊͂̔̆̂̓͂̏̈́͒̀̾̈̿͗́́̈̑̑͘͠#̷̢͍̺̻̻̩̘͇͍͎̪̲͈̰̝̦͍̱̹͙̠̥̹͒͊͐͐̍̈̏̀͒͌̔̄̀̉̄̾̅̎̉͂̕͝ͅ#̸̡̡̨̡̛̮̦̞̟̝͍͉̰͓͕̯͇̜̖̖̥͎̯̜͙̪͇̼̦̮̮͙̝͍̘́̋͂͒̽̅̎̅͑͆͗̍́̆̓͗̽̐̋̉͒̂͛̀̃̂͂̆͌͛̽̆͘ͅͅ")



                  read_letters("\n\n\033[1;37;40m\n    Seem there's nothing but static on tv...\n")
              elif answer == "b":
                  read_letters("\n    You leave the TV alone, god knows what they're showing here.\n")
          else:
              read_letters("\n    You seem to have done everything you can with the TV.\n")
      elif answer == "w":
          if ward_count == 0:
              read_letters("\n    You walk over to the wardrobe, it can be opened.\n    Would you like to open the Wardrobe? Y/N\n")        
              answer = msvcrt.getch().decode().lower()
              if answer == "i":
                get_items()
              elif answer == "y":
                 read_letters("""\033[1;31;40m\n    You inspect the wardrobe and a-\n\n\n\n\n\n BODY FALLS OUT?!?!?\n
    Do you want to inspect the body?...   (Y/N)""")
                 answer = msvcrt.getch().decode().lower()
                 if answer == "i":
                     get_items()
                 elif answer == "y":
                     read_letters("""\033[1;37;40m\n\n    Checking the body, you see it seems to have been horrificly morphed by time,
    With mold and maggots, but you notice something sticking out of it's chest...""")
                     print("""
\033[1;37;40m      .---.
      |---|
      |---|
      |---|
      |^ - \--.
      |________:
\033[1;30;40m      |  |//|
      |  |//|
      |  |//|
      |  |//|
      |  |\033[1;31;40m//|
      |  |//|
__\033[1;30;40m    |  |.-|
  \033[1;31;40m\___|  \033[1;31;40m|**|______________""")
                     read_letters("\n\n\033[1;31;40m\n    'A knife? Poor fella' You mutter to yourself\n\033[1;37;40m    Do you want to retreive the rusty knife? (Y/N)\n")
                     answer = msvcrt.getch().decode().lower()
                     if answer == "i":
                         get_items()
                     elif answer == "y":
                         read_letters("\033[1;37;40m\n    You decide to take the knife, with it taking a bit more tug that you'd have liked...\n")
                         add_item("Rusty Knife")
                         ward_count += 1
                     elif answer == "n":
                         read_letters("    It's probably best to leave the knife in it's 'pedestal'...")
                 elif answer == "n":
                     read_letters("\n    You leave the body alone, respecting the dead\n")
              elif answer == "n":
                  read_letters("\n    You leave the wardrobe alone.\n")
          else:
              read_letters("\n    You seem to have done everything you can with the wardrobe.\n")
      elif answer == "b":
          if bath_count == 0:
              read_letters("\033[1;31;40m\n    You enter the bathroom, where the acidic smell gets worse.")
              d = True
              bath_7()
          else:
              read_letters("    It appears you've done everything you can in the bathroom.")
      elif answer == "c":
        d = True
        motel_navigation.enter_corridor()
      elif answer == "i":
        get_items()
      # else:
      #   read_letters("\nInvalid answer, please try retry\n")



def bath_7():
  global bath_count
  global sink_count
  e = False
  while e == False:
    read_letters("""\n\033[1;37;40m\n    There is
    A (B)ath filled with a murky dark acidic smelling liquid
    A (S)ink cabinet.
    (L)eave
    What would you like to do?\n\n""")
    answer = msvcrt.getch().decode().lower()
    if answer == "i":
      get_items()
    elif answer == "b":
      if bath_count == 0:
        invent = inv()
        if invent.count("Plastic Gloves") > 0:
          read_letters("    You can stick your hand in the acidic bath wearing the Plastic Gloves, continue? (Y/N)\n")
          answer = msvcrt.getch().decode().lower()
          if answer == "i":
            get_items()
          elif answer == "y":
            read_letters("""\033[1;31;40m    You put your hand in the bath and feel around the liquid...
    You can't tell what's in there, but you don't want to know either.
    Eventually you feel something and pull your hand out as quickly as you can""")
            read_letters("""\n    A bone?... You run out of the bathroom immediately""")
            time.sleep(3)
            bath_count += 1
            e = True
            in_room7()
          elif answer == "n":
            read_letters("    It's probably of the right idea that you don't put you hand in there at all.")
        else:
          read_letters("    You can risk putting your arm in the bath, but it might not be the best idea. Proceed? (Y/N)")
          answer = msvcrt.getch().decode().lower()
          if answer == "i":
            get_items()
          elif answer == "y":
            read_letters("""\033[1;31;40m\n    You put your arm down into the bath's liquid and start to slowly feel pain.
    and the pain scales incredibly quickly- you jerk your arm out of the bath to see""")
            print("""
\033[1;37;40m        _     .-.
       ( `. .'   )
        `. `   /'
          |   |
\033[1;31;40m       ,. |   |,.,
\033[1;33;40m      |  \033[1;31;40m`**^^*`  \033[1;33;40m|
      |           |
      |           |""")
            read_letters("\033[1;31;40mOh... My... God...\n")
            read_letters("""    The sudden realisation that your arm is missing overwhelms you with pain
    To the point your screaming in agony, writhing in pain bleeding down your missing arm
    Until you eventually pass out and bleed out on the floor...\n""")
            retry.retry()
          elif answer == "n":
            read_letters("\n    Not putting your hand in that? Yeah that's definitely for the better\n")
          else:
            read_letters("    Invalid answer, please try retry\n")
      else:
        read_letters("    It appears you've done everything you can in the bathroom.\n")
        e = True
        in_room7()
    elif answer == "s":
      if sink_count == 0:
        sink_count += 1
        read_letters("""    You inspect the sink cabinet and find a pair of
    Latex plastic gloves. Maybe you could stick your hand in the bath without fearing anything now""")
        add_item("Plastic Gloves")
      else:
        read_letters("    It appears you've done everything you can with the sink.\n")
    elif answer == "l":
      e = True
      in_room7()


