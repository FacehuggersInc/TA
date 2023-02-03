from functions import *
from world import Map

class Game():
    def __init__(self):
        self.running = False
        self.player = None

    #Before Game Start
    def setup(self, current_player):
        self.player = current_player
        w = Map()
        w.generate_map(20)
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








































