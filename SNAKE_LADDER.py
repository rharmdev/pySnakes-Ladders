
import time 
import os
import sys 
import random 
os.system('ladder.png')
print("Welcome to snakes and ladders.")
position = 0
pick = int(input("Number 1-6 "))
if pick > 6:
    print("Pick the right number.")
    os.execl(sys.executable, sys.executable, *sys.argv)
position = pick + int(position)
print("Your position is", position)

while position < 64:
    time.sleep(1)
    print("Next turn.")
    babatunde = input("You wanna roll? Y/N ")
    if babatunde == "Y":
        pick = random.randint(1,6)
        position = pick + int(position)
        print("You rolled", pick)
        print("Your position is", position)
    else:
        break
    if position == 8:
         position = 15
         print("You went up a ladder, Nice! Your position is now", position)
    if position == 13:
         position += 16
         print("You went up a ladder, Nice! Your position is now", position)
    if position == 31:
         position += 20
         print("You went up a ladder, Nice! Your position is now", position)
    if position == 40:
         position += 19
         print("You went up a ladder, Nice! Your position is now", position)
    if position == 27:
         position -= 23
         print("You went down a snake, Damn! Your position is now", position)
    if position == 33:
         position -= 14
         print("You went down a snake, Damn! Your position is now", position)
    if position == 41:
         position -= 30
         print("You went down a snake, Damn! Your position is now", position)
    if position == 64:
        print("You legend, you won the game")
    if position > 64:
        position -= pick
        print('You missed the end, your position has been reverted.')
        print(position)

        




