import time, sys

# function to read a line of text with a delay beforehand, the parameter text should be a 'list
def read_line(text):
    time.sleep(.5)
    for line in text:
        print(line)
        time.sleep(.8)

# function to read a line of text one letter at a time, the parameter text should be a 'list'
def read_letters(text):
    for line in text:
        for letter in line:
            time.sleep(.01)
            sys.stdout.write(letter)
            sys.stdout.flush()
    time.sleep(.5)
