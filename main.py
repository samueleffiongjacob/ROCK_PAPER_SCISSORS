from FINAL_QUSTIONS.main import askYesNoQuestion
from START_END.main import start_end
import os
import sys
sys.path.append("..")


# To clear the enviroment of the game after playing


def clear():
    os.system("cls")
    # NOTE: please change the "cls" to "clear" if u are on a MAC OR LINUX OS to aviod error. leave the "cls"
    # if u are using windoms


# The main function
if __name__ == '__main__':

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors"}

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
            continue

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
                "Wrong choice. Read instructions Below carefully.")
            print('---------------------------------------------------------')


answer = askYesNoQuestion(
    "Are you sure u want to leave? (click any key to leave e.g yes, no): \n")
if answer == "YES":
    print("bye which to see u again.")
elif answer == "NO":
    print("bye which to see u again.")
