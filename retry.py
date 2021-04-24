import sys, msvcrt, motel_navigation
from read_text import read_letters
def retry():
  read_letters("Would you like to try again? Y/N\n")
  reset = msvcrt.getch().decode().lower()
  if reset == "y":
    motel_navigation.enter_corridor()
  elif reset == "n":
    read_letters("Thank you for playing!")
    sys.exit()
  else:
    read_letters("Please enter Y/N\n")
    retry()

def end():
    read_letters("""\n\n    Norman falls to his knees, a shiny key with a skull on the end
    falls out of his pocket as he hits the ground, this is your chance to leave!
    You rush to grab the key as fast as you put it in the door.
    You turn the lock to here a click. You open the door and leave.
    Goodbye Bates Hotel, you're free from this nightmare that once was.....

                                              """)
    read_letters("         Right?...   \n")
    sys.exit()