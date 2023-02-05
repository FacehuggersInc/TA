import random
from functions import *

worlds = "worlds//"
saved_worlds = os.listdir(worlds)

class World():
    def __init__(self):
        world = []
        start = (0,0)

    def __str__(self):
        return(f"""{self.world}""")

    def create_blank_world(self, width, height):
        with open(f"{worlds}\world{(len(saved_worlds) - 1) + 1}.txt","x") as w:
            for y in range(height):
                for x in range(width):
                    w.write("X")
                w.write("\n")

    def generate(self):
        self.create_blank_world(20,20)


if __name__ == "__main__":
    map = World()
    map.generate()
