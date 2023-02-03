import random
import sys

from creatures.player import Player, character_folder, characters
from functions import *
from game import Game


class Main():
    def __init__(self):
        self.player_loaded = None
        self.current_player = None

    # Menu Functions
    def preview_character(self):
        """Preview the character information from the 'self.current_player' variable."""

        title1("Your Current Player")
        print(self.current_player)
        hold()

    def load_character(self):
        """Display info about the characters in the 'character' folder and allow the user to Load the character they select. This method will then:
         - fill the 'self.current_character' var with data from the file they chose.
         - set the player_loaded var to True.
         """

        title2("load")
        characters = os.listdir(character_folder)
        i = 0
        for char in characters:
            i += 1
            print(f"    {i} | {char}")
        character = prompt(
            "What character do you want to load?\n      - Name or Number Only   - Case Sensitive")
        if character.isnumeric():
            character = characters[int(character) - 1].split(".")[0]
        try:
            self.current_player = load(
                character_folder, "", character, ".char", None)
            self.player_loaded = True
        except:
            print("[!] Failed to load Character")

    def create_character(self):
        """"""
        self.current_player = Player()
        self.current_player.create_player()
        self.preview_character()
        commit = decision("Are you happy with this character?", "Save", "Change Somthing...")
        if commit == "y":
            # Saving
            self.player_loaded = True
            try:
                save(character_folder, "", self.current_player,
                     self.current_player.name, ".char")
            except:
                print("[!] failed to save Character.")
            clear_screen()
        else:
            changeToMake = promptOptions("What do you want to change?", [
                                         "Name", "Race", "Gender"], ">").lower()
            if changeToMake == "name":
                self.current_player.name = ''
                self.current_player.create_player()
            elif changeToMake == "race":
                self.current_player.race = ''
                self.current_player.create_player()
            elif changeToMake == "gender":
                self.current_player.gender = ''
                self.current_player.create_player()

    def menu(self):
        while True:
            tabTitle("TA", "Main Menu")

            # NOT PERMANANT | Quick character loading
            if characters:
                index = random.randint(0, len(characters) - 1)
                character = characters[index].split(".")[0]
                self.current_player = load(
                    character_folder, "", character, ".char", None)

            if not self.current_player:
                self.player_loaded = False
            else:
                self.player_loaded = True

            # Title
            clear_screen()
            title1("text adventure\n")
            if self.player_loaded:
                print(f'    [@] Player: {self.current_player.name}')

            # Input Loop
            while True:
                # Menu Options
                if not self.player_loaded:
                    dimmedText("    [>] Start")
                else:
                    print("    [>] Start")
                if not os.listdir(character_folder):
                    dimmedText("    [^] Load")
                else:
                    print("    [^] Load")
                print("    [+] Create a new Character")
                print("    [X] Exit")

                # Input
                user_input = input("\n    [?] ").lower()

                # Input to Actions | 
                if self.player_loaded == True and (user_input == "player" or user_input == "preview" or user_input == "@"):
                    self.preview_character()
                    break
                elif self.player_loaded == True and (user_input == "start" or user_input == ">"):
                    game.setup(self.current_player)  # Setup game
                    # game.run()#In Game
                    break  # after game, break to reset
                elif os.listdir(character_folder) and (user_input == "load" or user_input == "^" or user_input == "2"):
                    self.load_character()
                    break
                elif user_input == "create character" or user_input == "cc" or user_input == "3" or user_input == "+":
                    self.create_character()
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
