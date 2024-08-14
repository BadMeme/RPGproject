from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor


### Sample objects, temporary
player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5)
)

orc = Actor(
    char="o", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense = 0, power = 3)
)

troll = Actor(
    char="o", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense = 1, power = 4)
)




### Old structs, will refactor into new schema
class character:
    def __init__(self):
        self.name = ''
        self.hp = 5
        self.mp = 5
        self.conditions = []
        self.wounds = []
        self.inventory = []
        self.stats = {
            'strength' : 2,
            'vitality' : 2,
            'agility' : 2,
            'mind' : 2,
            'will' : 2,
            'charisma' : 2
        }
        self.skills = {
            'blade' : 0,
            'polearm' : 0,
            'mace' : 0,
            'perception' : 0,
            'athletics' : 0,
            'influence' : 0,
            'decieve' : 0,
            'arcane' : 0,
            'stealth' : 0,
            'insight' : 0
        }
        self.location = ''
        self.origin = ''
        self.gameover = False
        #leaving room to expand past tutorial. might store stats in a dictionary or as individual properties of player
# player = character()

class zone:
    def __init__(self):
        self.size = {
            'x' : '', #width
            'y' : '', #height
            'z' : ''  #floors
        }
        self.rooms = []
        self.contains = []
        self.description = ''

class room:
    def __init__(self):
        self.id = 0
        self.xyz = {
            'x' : '',
            'y' : '',
            'z' : '',
        }
        self.tiles = []
        self.doors = []
        self.events = []
        self.contains = []
        self.description = ''

class tile:
    def __init__(self):
        self.xyz = {
            'x' : '',
            'y' : '',
            'z' : '',
        }
        self.events = []
        self.contains = []
        self.description = ''
    # for future when movement and combat is tile based with frontend 

class item:
    def __init__(self):
        self.name = '',
        self.type = '',
        self.descrption = ''

class weapon(item):
    def __init__(self):
        self.category = '',
        self.damage = '',
        self.keywords =''

class event:
    def __init__(self):
        self.text = ''
        self.flag = False
        self.trigger = None