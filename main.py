import random
import sys

from functions import *
from game import Game, saved_worlds, characters

class Main():
    def __init__(self):
        pass

    #Main Menu Function/Loop
    def menu(self):
        while True:
            tabTitle("TA", "Main Menu")

            # Title
            clear_screen()
            title1("text adventure\n")
            if game.world_loaded:
                print(f'    [#] World: {game.world.world_name}')
            if game.player_loaded:
                print(f'    [@] Player: {game.player.name}')

            # Input Loop
            while True:
                # Menu Options
                if not game.player_loaded or not game.world_loaded:
                    dimmedText("    [>] Start")
                else:
                    print("    [>] Start")
                if not characters or not saved_worlds:
                    dimmedText("    [^] Load")
                else:
                    print("    [^] Load")
                print("    [+] Create")
                print("    [X] Exit")

                # Input
                user_input = input("\n    [?] ").lower()

                # Input to Actions | 
                if game.player_loaded == True and (user_input == "player" or user_input == "preview" or user_input == "@"):
                        game.preview_character()
                        break
                elif game.player_loaded == True and game.world_loaded and (user_input == "start" or user_input == ">"):
                    game.setup()  # Setup game
                    break  # after game, break to reset
                elif (characters or saved_worlds) and (user_input == "load" or user_input == "^" or user_input == "2"):
                    game.load()
                    break
                elif user_input == "create" or user_input == "c" or user_input == "3" or user_input == "+":
                    game.create()
                    break
                elif user_input == "exit" or user_input == "e" or user_input == "4":
                    commit_exit = decision(
                        "Are you sure you want to exit?", "Exit!", "Stay")
                    if commit_exit == "y":
                        clear_screen()
                        sys.exit()
                    else:
                        break
                else:
                    print("\n    [Err] Option Unavailable")
                    hold()
                    break

if __name__ == "__main__":
    # Initialize and Run
    main = Main()
    game = Game()
    main.menu()
