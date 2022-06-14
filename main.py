import random
import os
from telnetlib import PRAGMA_HEARTBEAT
import time
from traceback import print_tb

# To clear the enviroment of the game after playing


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


# def CHOOSE():
#     print('ARE U SURE U WANT TO LEAVE ENTER "y" to exit or "n" to "stay"')
#     inp = str(input("Enter your Answer : "))
#     while True:
#         # Try block to handle the player choice
#         try:
#             choice = inp
#         except ValueError:
#             clear()
#             print("Wrong Choice")
#             continue
#         if inp.lower() == "n":
#             print('CONTINUE your game')
#             rps()

#         elif inp.lower() == "y":
#             break


# def CHOOSE1():

#     inp = str(input("Enter your Answer : "))
#     while True:
#         # Try block to handle the player choice
#         try:
#             choice = inp
#         except ValueError:
#             clear()
#             print("Wrong Choice")
#             continue
#         if inp.lower() == "y":
#             break


def rps():

    global rps_table
    global game_map
    global name

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

        if inp.upper() == "H":
            clear()
            rps_instructions()
            continue
        elif inp.upper() == "E":

            print(
                "YOU HAVE EXITED SELF  from Rock-Paper-Scissors Game you plAY IN the traditional Way of Gaming wait for 3 seconds to continue ")
            time.sleep(3)
            clear()
            break
        elif inp.upper() == "R":
            player_move = 0
        elif inp.upper() == "P":
            player_move = 1
        elif inp.upper() == "S":
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
            print(name, "WINS!!!")
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


def rpsls():

    global rpsls_table
    global game_map
    global name

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

        if inp.upper() == "H":
            clear()
            rpsls_instructions()
            continue
        elif inp.upper() == "E":
            print(
                "YOU HAVE EXITED SELF  from Rock-Paper-Scissors Game you plAY IN the new version way of Gaming wait for 3 seconds to continue ")
            time.sleep(3)
            clear()
            break
        elif inp.upper() == "R":
            player_move = 0
        elif inp.upper() == "P":
            player_move = 1
        elif inp.upper() == "S":
            player_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()
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
            print(name, "WINS!!!")
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

# START AND END


def start_end():
    while True:
        print("Let's Play!!!")
        print("Which version of Rock-Paper-Scissors?")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to play Rock-Paper-Scissors IN the new version way of Gaming")
        print("Enter 3 to End the Game")

        # Try block to handle the player choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")
            continue
        # Play the traditional version of the game
        if choice == 1:
            rps()

        # Play the new version of the game
        elif choice == 2:

            rpsls()

        # Quit the STARTING LOOP
        elif choice == 3:
            print('-----------------------------------------')
            print(' WELCOME BACK TO The main function PLEASE SELECT AN OPTION BELOW')
            print('--------------------------------------------------------')
            break

        else:
            clear()
            print("Wrong choice. Read instructions carefully.")


# The main function
if __name__ == '__main__':

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors"}

    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    # Win-lose matrix for new version of the game
    rpsls_table = [[-1, 1, 0, 0, -2], [1, -1, 2, 0, 1],
                   [0, 2, -1, 2, -2], [0, 1, 2, -1, 2], [-2, 1, 2, 0, -1]]

    print('---------------------------------------------')
    name = input("Enter your name: ")
    print('---------------------------------------------')
    print(name + " WELCOME TO Rock-Paper-Scissors GAME ")
    print('---------------------------------------------')
    # The GAME LOOP
    while True:

        # The Game Menu
        print()
        print('SELECT AN OPTION BELOW')
        print("Type 'start' to Start")
        print("Type 'end' to quit")
        print()

        # Try block to handle the player choice
        try:
            choice = str(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")
            continue

        # Play the traditional version of the game
        if choice == "start":
            print('-----------------------------------------------------')
            print(
                'CHOOSE THE TYPE OF GAME U WANT TO PLAY  OR TYPE "3" TO RETURN To The main function')
            print('-------------------------------------------')
            start_end()

        # Quit the GAME LOOP
        elif choice == "end":
            print('-----------------------------------------------')
            print(
                'THANK YOU FOR PLAYING THE Rock-Paper-Scissors GAME. Which to see u next Time. Bye !!!!!!!')
            print('---------------------------------------------')
            break

        # Other wrong input
        else:
            clear()
            print(
                "Wrong choice. Read instructions carefully.")
            print('---------------------------------------------------------')

    def askYesNoQuestion(question):
        YesNoAnswer = input(question).upper()
        if YesNoAnswer == "YES" or YesNoAnswer == "NO":
            return YesNoAnswer
        else:
            return askYesNoQuestion(question)


answer = askYesNoQuestion("Are you sure u want to leave? (Yes): \n")
if answer == "YES":
    print("bye which to see u again.")
elif answer == "NO":
    print("continue.")
