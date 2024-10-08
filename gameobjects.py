from components.ai import HostileEnemy
from components.fighter import Fighter
from components import consumable, equippable
from components.equipment import Equipment
from components.inventory import Inventory
from entity import Actor, Item
from components.character_progression import Level


### Sample objects, temporary
player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, base_defense=2, base_power=5),
    equipment=Equipment(),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)
)

orc = Actor(
    char="o", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, base_defense = 0, base_power = 3),
    equipment=Equipment(),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35)
)

troll = Actor(
    char="o", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, base_defense = 1, base_power = 4),
    equipment=Equipment(),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100)
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4)
)

magebolt_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Magebolt scroll",
    consumable=consumable.MagicDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="~", 
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

mageburst_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Mageburst scroll",
    consumable=consumable.MagicAreaDamageConsumable(damage=12, radius = 3)
)

dagger = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Dagger", 
    equippable=equippable.Dagger()
)

sword = Item(
    char="[",
    color=(139, 69, 19),
    name="Swordr",
    equippable=equippable.Sword(),
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", 
    color=(139, 69, 19), 
    name="Chain Mail", 
    equippable=equippable.ChainMail()
)


###
###
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