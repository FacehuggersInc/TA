import random
from functions import *

class Room():
    def __init__(self):
        self.coordinate = None

        self.id = None
        self.start = False
        self.exit = False

        #Room Doors
        self.N = None
        self.S = None
        self.W = None
        self.E = None

    def __str__(self):
        return(f"""
    Start?: {self.start}
    Exit?: {self.exit}
    ID: {self.id}
    Coords: {self.coordinate}
    N Door:{self.N} | S Door:{self.S} | W Door:{self.W} | E Door:{self.E}
""")

class Map():
    def __init__(self):
        self.rooms = []
        self.coordinates = []
        self.creationData = []

    def start_room(self):
        starting_room = Room()
        starting_room.start = True
        starting_room.coordinate = [0,0]
        starting_room.id = 1
        return starting_room

    def increment_coord(self, current_coord, direction = str):
        x = current_coord[0]
        y = current_coord[1]
        match direction:
            case "N": y += 1
            case "S": y -= 1
            case "W": x -= 1
            case "E": x += 1
        next_coord = [x,y]
        return next_coord

    def create_path(self, path_distance = int):
        DIRECTIONS = ["N","S","W","E"]
        UP_CLKWSE_CRCL = ["N","E","S","W"]
        UP_CNTR_CLKWSE_CRCL = ["N","W","S","E"]
        DWN_CLKWSE_CRCL = ["S","E","N","W"]
        DWN_CNTR_CLKWSE_CRCL = ["S","W","N","E"]
        
        path = []
        while not len(path) == (path_distance - 1):
            dir = random.choice(DIRECTIONS)

            #No Circles
            if len(path) >= 4:
                path_slice = [path[-4],path[-3],path[-2],path[-1]]
                if path_slice == UP_CLKWSE_CRCL:
                    for p in range(4):
                        del path[-1]
                elif path_slice == UP_CNTR_CLKWSE_CRCL:
                    for p in range(4):
                        del path[-1]
                elif path_slice == DWN_CLKWSE_CRCL:
                    for p in range(4):
                        del path[-1]
                elif path_slice == DWN_CNTR_CLKWSE_CRCL:
                    for p in range(4):
                        del path[-1]

            #Cant go back
            if len(path) > 1:
                if path[-1] == "N" and dir == "S":dir = random.choice(["N","W","E"])
                elif path[-1] == "S" and dir == "N":dir = random.choice(["S","W","E"])
                elif path[-1] == "W" and dir == "E":dir = random.choice(["S","N","W"])
                elif path[-1] == "E" and dir == "W":dir = random.choice(["S","N","E"])

            path.append(dir)
        return path



    def generate(self, roomsToCreate = int):
        #Comparison Varibles
        existingRooms = []
        existingRoomIDs = []

        #Create the Starting Room
        start_room = self.start_room()
        self.rooms.append(start_room)

        #Add start_room to generation varibles
        existingRooms.append(start_room)
        existingRoomIDs.append(start_room.id)
        self.coordinates.append(start_room.coordinate)
        current_coord = start_room.coordinate

        #Generate Blank Rooms
        for x in range(roomsToCreate - 1):
            room = Room()
            self.rooms.append(room)

        #Assign Ids
        for room in self.rooms:
            if room.start == True: 
                continue
            while True:
                id = random.randint(1,roomsToCreate)
                if not id in existingRoomIDs:
                    room.id = id
                    existingRoomIDs.append(id)
                    break

        #Create Main Path
        path = self.create_path(roomsToCreate)

        #Connect Rooms According to Path & Assign Coordinates



        #Debugging
        for room in self.rooms:
            print(room)
        print(path)
        hold()


