import random
from functions import *

# X          | Y
#    ----------------------
#    W = LEFT-  | N = UP+
#    E = RIGHT+ | S = DOWN-

class Room():
    def __init__(self):
        self.coordinate = None

        self.id = None
        self.starting_room = False
        self.exit_room = False

        #Room Doors
        self.N = None
        self.S = None
        self.W = None
        self.E = None

    def __str__(self):
        return(f"""
----------------------------------------------
    Start?: {self.starting_room}
    Exit?: {self.exit_room}

    ID: {self.id}
    Coords: {self.coordinate}
    N Door: {self.N}
    S Door: {self.S}
    W Door: {self.W}
    E Door: {self.E}
----------------------------------------------
""")

class Map():
    def __init__(self):
        self.rooms = []

    def create_rooms(self, roomsToCreate, existingRoomIDs):
        for x in range(roomsToCreate):
            room = Room() #Create New Room
            while True:
                id = random.randint(1, roomsToCreate)
                if not id in existingRoomIDs:
                    existingRoomIDs.append(id)
                    room.id = id
                    break
            self.rooms.append(room) #Add room to list

    def generate_map(self, roomsToCreate = int):
        DIRECTIONS = ["N","S","W","E"]

        existingRooms = []
        existingRoomIDs = []
        directions = []

        #Set amount of rooms then create rooms
        if not roomsToCreate: roomsToCreate = random.randint(5,9)
        self.create_rooms(roomsToCreate, existingRoomIDs)

        #Find Room ID 1 and make it the starting room
        for room in self.rooms:
            if room.id == 1:
                room.starting_room = True
                room.coordinate = [0,0]
                break

        #Bring Starting Room to front of list so we can start there when assigning rooms to doors in a for loop
        for room in self.rooms:
            if room.starting_room == True:
                self.rooms.pop(self.rooms.index(room))
                self.rooms.insert(0, room)
                break

        #PATHING / CONNECT ROOMS-----
        currentCoord = [0,0]
        for room in self.rooms:
            turned = False
            roomIndex = self.rooms.index(room)

            #Next Room ID | If we reach the end of rooms list, we make a door an EXIT
            if roomIndex == len(self.rooms) - 1: 
                nextRoomsID = "EXIT"
                room.exit_room = True
            else: 
                nextRoomsID = self.rooms[roomIndex + 1].id

            #Choose a direction
            direction = random.choice(DIRECTIONS)

            #Corrections
            if len(directions) > 1:
                #I want to turn if weve gone the same way twice
                if directions[-1] == direction:
                    match direction:
                        case "N": 
                            direction = random.choice(["W","E"])
                        case "S": 
                            direction = random.choice(["W","E"])
                        case "W": 
                            direction = random.choice(["N","S"])
                        case "E": 
                            direction = random.choice(["N","S"])
                    turned = True

            if (len(directions) > 1) and turned == False:
                #We dont want rooms going directly back onto themselfs
                match directions[-1]:
                    case "N": 
                        direction = random.choice(["N","W","E"]) 
                    case "S": 
                        direction = random.choice(["S","W","E"])
                    case "W": 
                        direction = random.choice(["N","W","S"])
                    case "E": 
                        direction = random.choice(["N","S","E"])

            #Assign | Coords
            if room.starting_room == False:
                room.coordinate = currentCoord
                x = room.coordinate[0]
                y = room.coordinate[1]
                if directions[-1] == "N":  y += 1
                elif directions[-1] == "S": y -= 1
                elif directions[-1] == "W": x -= 1
                elif directions[-1] == "E": x += 1
                room.coordinate = [x,y]
                currentCoord = room.coordinate

            #No Overlap
            if len(existingRooms) > 1 and room.starting_room == False: #need more than one room to compare
                for existingRoom in existingRooms: #looping here so we can look at each rooms coordinates
                    if existingRoom.coordinate == room.coordinate: #<_ Coords still match, loops when it shouldnt really
                        #Back Up in Coords
                        x = room.coordinate[0]
                        y = room.coordinate[1]
                        if directions[-1] == "N":  y -= 1
                        elif directions[-1] == "S": y += 1
                        elif directions[-1] == "W": x += 1
                        elif directions[-1] == "E": x -= 1
                        room.coordinate = [x,y]

                        #Choose a differnt Direction
                        if directions[-1] == "N": 
                            direction = random.choice(["S","W","E"])
                        elif directions[-1] == "S":
                            direction = random.choice(["N","W","E"])
                        elif directions[-1] == "W":
                            direction = random.choice(["S","N","E"])
                        elif directions[-1] == "E":
                            direction = random.choice(["S","N","W"])
                        
                        #Re Assign Coord
                        x = room.coordinate[0]
                        y = room.coordinate[1]
                        if directions[-1] == "N":  y += 1
                        elif directions[-1] == "S": y -= 1
                        elif directions[-1] == "W": x -= 1
                        elif directions[-1] == "E": x += 1
                        room.coordinate = [x,y]
                        currentCoord = room.coordinate

                        #break the for loop
                        break

            #Assign | Room IDS & Add to directions
            if direction == "N":
                room.N = nextRoomsID
                directions.append("N")
            elif direction == "S":
                room.S = nextRoomsID
                directions.append("S")
            elif direction == "W":
                room.W = nextRoomsID
                directions.append("W")
            elif direction == "E":
                room.E = nextRoomsID
                directions.append("E")
            existingRooms.append(room)


        #Dubuging
        print("\n-- ROOMS -----\n")
        for room in self.rooms:
            print(f"Rooms Index: {self.rooms.index(room)}:{room}")
        print(f"\nRooms to Make (var): {roomsToCreate}")
        print(f"Blank Rooms Created (objs in list): {len(self.rooms)}")
        print(f"Directions: {directions}")
        hold()
