import random
from functions import *

worlds = "worlds\\"
saved_worlds = os.listdir(worlds)

class World():
    def __init__(self):
        self.world_name = None
        self.world_data = []
        self.start = (0,0)

    def load_world(self, world = str):
        """Loads the tile data from a world file, into a instatiated "World" class"""
        name = world.split(".")[0]
        self.world_name = name.split("\\\\")[1]
        world_data = []
        with open(f"{world}","r") as w:
            tile_rows = w.readlines()
        for y in range(len(tile_rows)):
            tile_columns = tile_rows[y].split(".")
            tile_columns[-1] = tile_columns[-1].replace("\n","") #remove the new line
            world_data.append(tile_columns)
        self.world_data = world_data

    def create_blank_world(self, name = str, size = [int, int]):
        """Creates a world file of a chosen size, with blank tiles. Returns the world file name."""
        width = size[0]
        height = size[1]
        i = 1
        if saved_worlds:
            for saved_world in saved_worlds:
                if name == saved_world.split(".")[0]: 
                    new_world = f"{worlds}\{name}{(len(saved_worlds) - 1) + 1}.txt"
                    break
                elif i == len(saved_worlds): 
                    new_world = f"{worlds}\{name}.txt"
                i += 1
        else: new_world = f"{worlds}\{name}.txt"
        self.world_name = new_world
        with open(f"{new_world}","x") as w:
            for y in range(height):
                for x in range(width):
                    if x + 1 == width: w.write("[]")
                    else: w.write("[].")
                if y + 1 == height:pass
                else: w.write("\n")
        return new_world

    def generate(self, name, size):
        """Generate a new world, filled with random tiles."""
        new_world = self.create_blank_world(name, size)
        self.load_world(new_world)

if __name__ == "__main__":
    map = World()
    map.generate([11,11])
    input()