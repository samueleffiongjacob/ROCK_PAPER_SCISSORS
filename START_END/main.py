import os
from TRADITIONAL_WAY.main import rps_instructions
from TRADITIONAL_WAY.main import rps
from NEW_WAY.main import rpsls_instructions
from NEW_WAY.main import rpsls


def clear():
    os.system("cls")
    # NOTE: please change the "cls" to "clear" if u are on a MAC OR LINUX OS to aviod error. leave the "cls"
    # if u are using windoms
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
            print("Wrong choice. Read instructions Below carefully.")
