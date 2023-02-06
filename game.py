from functions import *
from world_gen import World, saved_worlds
from creatures.player import Player, character_folder, characters

class Game():
    def __init__(self):
        self.running = False
        self.world_loaded = False
        self.player_loaded = False

        self.world = None
        self.player = None

    def stop(self):
        """Stop the game loop."""
        self.running = False

    def preview_character(self):
        """Preview the character information from the 'self.current_player' variable."""
        title2("Your Current Player")
        print(self.player)
        hold()

    def load_character(self):
        """Display info about the characters in the 'character' folder and allow the user to Load the character they select. This method will then:
         - fill the 'self.current_character' var with data from the file they chose.
         - set the player_loaded var to True.
         """
        title1("load")
        characters = os.listdir(character_folder)
        character = numSelectOptions(
            "What character do you want to load?", 
            characters
        )
        character = character.split(".")[0]
        self.current_player = load(
            character_folder, "", character, ".char", None)
        self.player_loaded = True

    def load_world(self):
        clear_screen()
        title1("Game Setup | Load World ...")
        world = numSelectOptions(
            "What world do you want to load?",
            saved_worlds
        )
        self.world.load_world(f"{world}")

    def load(self):
        pass

    def create_new_character(self):
        """"""
        self.player = Player()
        self.player.create_player()
        self.preview_character()
        commit = decision("Are you happy with this character?", "Save", "Change Somthing...")
        if commit == "y":
            # Saving
            self.player_loaded = True
            try:
                save(character_folder, "", self.player,
                     self.player.name, ".char")
            except:
                print("[!] failed to save Character.")
            clear_screen()
        else:
            changeToMake = promptOptions("What do you want to change?", [
                                         "Name", "Race", "Gender"], ">").lower()
            if changeToMake == "name":
                self.player.name = ''
                self.player.create_player()
            elif changeToMake == "race":
                self.player.race = ''
                self.player.create_player()
            elif changeToMake == "gender":
                self.player.gender = ''
                self.player.create_player()

    def create_new_world(self):
        self.world = World()
        clear_screen()
        title1("text adventure | Game Setup | Create World ...")
        world_name = prompt("What do you want the name of your world to be?", False)
        world_width = prompt("What should the width of the world be?", True)
        world_height = prompt("What should the height of the world be?", True)
        self.world.generate(world_name, [world_width,world_height])

    def create(self):
        while True:
            tabTitle("TA", "Create Menu")

            clear_screen()
            title1("TEXT ADVENTURE | CREATE ...")
            if self.world_loaded or self.player_loaded:
                title2("Whats Loaded Currently")
            if self.world_loaded:
                print(f'    [#] World: {self.world.world_name}')
            if self.player_loaded:
                print(f'    [@] Player: {self.player.name}')

            #Create Options
            print("\n    [1] World")
            print("    [2] Character")
            print("\n    [<] Go Back")

            #Create Input Loop
            while True:
                create_input = input("\n    [?] ").lower()
                if create_input == "world" or create_input == "1":
                    self.create_new_world()
                    if self.world:
                        self.world_loaded = True
                    break
                elif create_input == "character" or create_input == "2":
                    self.create_new_character()
                    if self.player:
                        self.player_loaded = True
                    break
                elif create_input == "back" or create_input == "done" or create_input == "3":
                    return

    #Before Game Start
    def setup(self):
        pass

    #Game Loop
    def run(self):
        self.running = True
        while self.running:
            pass

