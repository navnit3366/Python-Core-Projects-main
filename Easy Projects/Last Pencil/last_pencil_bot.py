# Last pencil with two players John and Jack but Jak is a bot
# Jack (the bot) will follow a win strategy if possible otherwise will go random

import random

def bot_turn(number_of_pencils):
    while True:
        if number_of_pencils in [1, 2]:
            pencils = 1
            break
        elif number_of_pencils == 3:
            pencils = 2
            break
        elif number_of_pencils == 4:
            pencils = 3
            break
        elif number_of_pencils == 5:
            pencils = random.randint(1, 3)
            break
        else:
            number_of_pencils -= 4
    
    print(pencils)
    return pencils
    
def john_turn(pencils, number_of_pencils):
    while pencils not in choosen_pencils:
        print(f"Possible values: {choosen_pencils}")
        print(f"Please try again {current_player}:")
        try:
            pencils = int(input())
        except ValueError:
            print(f"The number of pencils should be numeric, try again {current_player}")
            continue
    while pencils > number_of_pencils:
        print("Too many pencils were taken")
        print(f"Please try again {current_player}:")
        try:
            pencils = int(input())
        except ValueError:
            print(f"The number of pencils should be numeric, try again {current_player}")
            continue
    
    return pencils

print("How many pencils would you like to use:")
while True:
    try:
        number_of_pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        print("Try again: how many pencils would you like to use:")
    else:
        if number_of_pencils <= 0:
            print("The number of pencils should be positive")
            print("Try again: how many pencils would you like to use:")
        else:
            break

players = ["John", "Jack"]
bot = "Jack"
print(f"Who will be the first ({players[0]}, {players[1]}):")

starting_player = input().title()
while starting_player not in players:
    print(f"Incorrect player name, choose between {players[0]} and {players[1]}")
    starting_player = input().title()

print(f"{starting_player} is going first!")
current_player = starting_player
print("|" * number_of_pencils)
choosen_pencils = [1, 2, 3]

while True:
    if current_player == players[0]:
        next_player = players[1]
    else:
        next_player = players[0]
    print(f"{current_player}'s turn:")
    
    if current_player == bot:
        pencils = bot_turn(number_of_pencils)
    else:
        try:
            pencils = int(input())
        except ValueError:
            print(f"The number of pencils should be numeric, try again {current_player}")
            continue
        else:
            pencils = john_turn(pencils, number_of_pencils)
        
        
    number_of_pencils -= pencils
    if number_of_pencils == 0:
        print(f"{next_player} won!")
        break
    else:
        print("|" * number_of_pencils)
        current_player = next_player
