import random
import os
import time
from unicodedata import name


def clear():
    os.system("cls")
    # NOTE: please change the "cls" to "clear" if u are on a MAC OR LINUX OS to aviod error. leave the "cls"
    # if u are using windoms


# Set of instructions for Rock-Paper-Scissors


def rps_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print()


def rps():

    global rps_table
    global game_map
    global name

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors"}

    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
    # Game Loop for each game of Rock-Paper-Scissors
    while True:
        # Note the "\t" is use to give space in between lines
        print("--------------------------------------")
        print('YOU hvae choosen to play Rock-Paper-Scissors in the traditional Way')
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"H for help\" for instructions")
        print("Enter \"R for  Rock\",\"P for Paper\",\"S for Scissors\" to play")
        print("Enter \"E for exit\" to quit")
        print("--------------------------------------")

        print()

        # Player Input
        inp = input("Enter your move : ")

        if inp.lower() == "h":
            clear()
            rps_instructions()
            continue
        elif inp.lower() == "e":

            print(
                "YOU HAVE EXITED SELF  from Rock-Paper-Scissors Game you plAY IN the traditional Way of Gaming wait for 3 seconds to continue ")
            time.sleep(3)
            clear()
            break
        elif inp.lower() == "r":
            player_move = 0
        elif inp.lower() == "p":
            player_move = 1
        elif inp.lower() == "s":
            player_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()
            continue

        print("Computer making a move....")

        print()
        time.sleep(2)

        # Get the computer move randomly
        comp_move = random.randint(0, 2)

        # Print the computer move
        print("Computer chooses ", game_map[comp_move].upper())

        # Find the winner of the match
        winner = rps_table[player_move][comp_move]

        # Declare the winner
        if winner == player_move:
            print("YOU WINS!!!")
            print('---------------------------------------------')
            print('please wait for 5 seconds to continue')
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
            print('---------------------------------------------')
            print('please wait for 5 seconds to continue')
        else:
            print("TIE GAME")
            print('---------------------------------------------')
            print('please wait for 5 seconds to continue')

        print()
        time.sleep(5)
        clear()
