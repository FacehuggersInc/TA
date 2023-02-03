from functions import *
character_folder = "A:\PY\Projects\TA\characters"
characters = os.listdir(character_folder)

races = [
    "Human",
    "Elf",
    "Halfling",
    "Dwarf",
    "Goblin",
    "Orc"
]
genderExamples = ["Male","Female","Etc."]

class Player():
    def __init__(self):
        #Identity
        self.name = ''
        self.race = ''
        self.gender = ''

        #? Race Stats ?

        #Stats
        self.maxHealth = 100
        self.health = 100
        self.defense = 10
        self.attack = 2

        #Inventory
        self.carry_weight_limit = 50
        self.carry_weight = self.carry_weight_limit
        self.inv_slots_hor = 5
        self.inv_slots_ver = 5
        self.inventory_slots = self.inv_slots_hor * self.inv_slots_ver
        self.inventory = [
            ['Sword','5'],
            ['Leather Pants','5'],
            ['Apple','3']
        ]
    
    def __str__(self):
        return(f"""
    Player: {self.name}
    Race: {self.race}
    Gender: {self.gender}

    Health: {self.health}/{self.maxHealth}
    Defense: {self.defense}
    Atk: {self.attack}

    Carry Weight: {self.carry_weight}/{self.carry_weight_limit}
    Inv Slots: {self.inventory_slots}
    Inventory {self.inventory}
    """)
    
    def create_player(self):
        clear_screen()
        title1("create your character | Indentity")

        #Name Input Loop
        while not self.name:
            name = prompt("What do you want your Name to be?")
            self.name = name

        #Race Input Loop
        while not self.race:
            race = promptOptions(
                "What do you want your Race to be?",
                races,
                "*"
            )
            self.race = race
        
        #Gender Input Loop
        while not self.gender:
            gender = promptOptions(
                "What gender is your character?",
                genderExamples,
                "*"
            )
            self.gender = gender
        













