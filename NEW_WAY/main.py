import random
import os
import time


def clear():
    os.system("cls")
    # NOTE: please change the "cls" to "clear" if u are on a MAC OR LINUX OS to aviod error. leave the "cls"
    # if u are using windoms

# Set of instructions for Rock-Paper-Scissors-Lizard-Spock IN the new version way of Gaming


def rpsls_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors IN the new version way of Gaming : ")
    print()
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print("Scissors decapitates Papper")
    print("Rock hit Paper")
    print("Paper disproves Cut from Scissors")
    print("Paper move from  Rock")
    print("Rock crushes Scissors")
    print()


def rpsls():

    global rpsls_table
    global game_map
    global name

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors"}

    # Win-lose matrix for new version of the game
    rpsls_table = [[-1, 1, 0, 0, -2], [1, -1, 2, 0, 1],
                   [0, 2, -1, 2, -2], [0, 1, 2, -1, 2], [-2, 1, 2, 0, -1]]

    # Game Loop for each game of Rock-Paper-Scissors IN the new version way of Gaming
    while True:
        # Note the "\t" is use to give space in between lines
        print("--------------------------------------")
        print(
            'YOU HAVE CHOOSE to play Rock-Paper-Scissors IN the new version way of Gaming')
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"H for help\" for instructions")
        print("Enter \"R for Rock\" \"P for Paper\" \"S for Scissors\"  to play")
        print("Enter \"E for exit\" to quit")
        print("--------------------------------------")

        print()

        # Player Input
        inp = input("Enter your move : ")

        if inp.lower() == "h":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower() == "e":
            print(
                "YOU HAVE EXITED SELF  from Rock-Paper-Scissors Game you plAY IN the new version way of Gaming wait for 3 seconds to continue ")
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
            rpsls_instructions()
            continue

        print("Computer making a move....")

        comp_move = random.randint(0, 2)
        print()
        time.sleep(2)

        print("Computer chooses ", game_map[comp_move].upper())

        winner = rpsls_table[player_move][comp_move]
        print()
        if winner == player_move:
            print('---------------------------------------------------------')
            print("YOU WINS!!!")
            print('---------------------------------------------------------')
            print('PLEASE wait FOR 5 seconds')
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
            print('---------------------------------------------------------')
            print('PLEASE wait FOR 5 seconds')
        else:
            print("TIE GAME")
            print('---------------------------------------------------------')
            print('PLEASE wait FOR 5 seconds')
        print()
        time.sleep(5)
        clear()
