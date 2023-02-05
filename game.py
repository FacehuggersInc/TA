from functions import *
from world_gen import World

class Game():
    def __init__(self):
        self.running = False
        self.player = None

    #Before Game Start
    def setup(self, current_player):
        self.player = current_player
        w = World()
        w.generate()
        clear_screen()
    def stop(self):
        self.running = False


    #Game Loop
    def run(self):
        self.running = True
        while self.running:
            tabTitle("TA","In Game")
            print("IN GAME CURRENT PLAYER")
            print(self.player)
            hold()
            self.stop()








































