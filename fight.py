import inventory
import room_seven
import motel_navigation
import retry
import random
import read_text
import msvcrt

firsttime = 0

def fight_norman():
  global firsttime
  global your_hp
  global norm_health
  if firsttime == 0:
    firsttime += 1
    your_hp = 15
    norm_health = 20
  inventory.get_inventory()
  if inventory.held_item == "Fists":
    your_atk = random.randint(1,2)
  elif inventory.held_item == "Gun":
    your_atk = random.randint(10, 15)
  elif inventory.held_item == "Crowbar":
    your_atk = random.randint(2,4)
  elif inventory.held_item == "Starting pistol":
    your_atk = random.randrange(1, 9, 2)
  elif inventory.held_item == "Rusty Knife":
    your_atk = 0
  elif inventory.held_item == "Bow and arrow":
    your_atk = random.randrange(1, 8)
  elif inventory.held_item == "Manual Revolver":
    your_atk = random.randrange(1, 10 , 3)
  elif inventory.held_item == "Umbrella":
    your_atk = random.randint(1,3)
  elif inventory.held_item == "Hunting knife":
    your_atk = random.randint(3,6)
  else:
    your_atk = 0
  f = False
  while f == False:
    if your_hp <= 0:
      read_text.read_letters("""\033[1;31;40m\n    Norman triumphs over you, resulting in the end of your life.
    Unfortunately Norman Bates was the last face you ever saw
    And his reign of terror will proceed to rage on.\n""")
      your_hp = 15
      norm_health =20
      firsttime -= 1
      f = True
      retry.retry()
    read_text.read_letters(f"\033[1;37;40m\n    What would you like to do?:\n")
    print(f"\033[1;37;40m    (A)ttack Norman with {inventory.held_item}\n(D)istract Norman\n(R)eturn to reception\n")
    answer = msvcrt.getch().decode().lower()
    if answer == "a":
      norm_health -= your_atk
      if your_atk == 0:
        read_text.read_letters(f"\033[1;31;40m    Norman chuckles. You honestly thought your {inventory.held_item} would do something to me? FOOL\n     Norman took no damage from that attack and launches you back into the reception\n")
        f = True
        motel_navigation.enter_reception()
      elif norm_health > 16:
        read_text.read_letters(f"\033[1;31;40m    You hit Norman for {your_atk} damage\n    'I appreciate the effort but you've barely wounded me!'\n")
        read_text.read_letters(f"\033[1;31;40m    Norman has {norm_health} hp left\n")
        norm_atk = random.randint(1,4)
        your_hp -= norm_atk
        read_text.read_letters(f"\033[1;37;40m    Norman hits you for {norm_atk} hp,\n    Watch out, you only have {your_hp} hp left\n")
      elif norm_health <= 16 and norm_health > 12:
        read_text.read_letters(f"\033[1;31;40m\n    You hit Norman for {your_atk} damage\n    'You really think this is hurting me?' Norman exclaims\n")
        read_text.read_letters(f"\033[1;31;40m    Norman has {norm_health} hp left\n")
        norm_atk = random.randint(2,5)
        your_hp -= norm_atk
        read_text.read_letters(f"\033[1;37;40m    Norman hits you for {norm_atk} hp,\n    Watch out, you only have {your_hp} hp left\n")
      elif norm_health <= 12 and norm_health > 6:
        read_text.read_letters(f"\033[1;31;40m    You hit Norman for {your_atk} damage\n    'You're not doing a great job!' Normal stumbles as he proclaims\n")
        read_text.read_letters(f"\033[1;31;40m    Norman has {norm_health} hp left\n")
        norm_atk = random.randint(1,5)
        your_hp -= norm_atk
        read_text.read_letters(f"\033[1;37;40m    Norman hits you for {norm_atk} hp,\n    Watch out, you only have {your_hp} hp left\n")
      elif norm_health <= 6 and norm_health >= 1:
        read_text.read_letters(f"\033[1;31;40m    You hit Norman for {your_atk} damage\n    'I told you I'm not letting you leave here alive!' Normal shouts with murderous intent\n")
        read_text.read_letters(f"\033[1;31;40m    Norman has {norm_health} hp left\n")
        norm_atk = random.randint(2,6)
        your_hp -= norm_atk
        read_text.read_letters(f"\033[1;37;40m    Norman hits you for {norm_atk} hp,\n    Watch out, you only have {your_hp} hp left\n")
      elif norm_health <1:
        read_text.read_letters("\033[1;31;40\n    You hit Norman for the remainder of his health.")
        read_text.read_letters("\033[1;31;40m\n    'Impossible, you...    Can't...             L e a v e......'")
        firsttime -= 1
        f = True
        retry.end()
    elif answer == "d":
      read_text.read_letters("    Norman doesn't fall for your pitiful attempt to point and distract him,\n    He proceeds to launch you back into the reception.\n")
      f = True
      motel_navigation.enter_reception()
    elif answer == "r":
      read_text.read_letters("    You decide to return to the reception. Probably for the better...")
      f = True
      motel_navigation.enter_reception()
