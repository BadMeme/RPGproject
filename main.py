# IO text RPG main engine file 

# imports

import cmd
import textwrap
import sys
import os
import time
import random

# settings
screen_width = 100

# Game State
class player:
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
        self.xyz = {
            'x' : '',
            'y' : '',
            'z' : '',
        }
        self.tiles = []
        self.doors = []
        self.event = []
        self.contains = []
        self.description = ''

class tile:
    def __init__(self):
        self.xyz = {
            'x' : '',
            'y' : '',
            'z' : '',
        }
        self.event = []
        self.contains = []
        self.description = ''

main_character = player()

# Game Zones
demo_zone = zone()
demo_zone.size = {
    'x' : 5, #width
    'y' : 5, #height
    'z' : 1  #floors
}
demo_zone.description = 'A strange gaol. The dust seems to hang in the air.'

def create_zone(zone):
    for z in zone.size[z]:
        for y in zone.size[y]:
            for x in zone.size[x]:
                new_room = room()
                new_room.xyz = {
                    'x' : x,
                    'y' : y,
                    'z' : z
                }
                zone.rooms.append(new_room)

    


    #Will make game state tracker for time and ambient mana, as well as rng shit. lots of stuff later

### Title Screen 

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #writing this soon
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() #writing this soon
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('###          I|O         ###')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('   Copyright 2024 badMeme   ') #lol is this even right
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('############################')
    print('###          I|O         ###')
    print('############################')
    print(' - Use up, down, Left, right to move')
    print(' - Type command names to perform actions')
    print(' - "Look" to inspect something       ')
    print('     Copyright 2024 badMeme ') #lol is this even right
    title_screen_selections()


### Game Loops ###

# Blocking out New Game -> Character Creation -> Map movement #

def script_text(script):
    for character in script:
        sys.stdout.write(character)
        sys.stdout.flush() ###Look this up
        time.sleep(0.03)

def start_game():
    # Create character
    # Ask character customization questions
    # assign stats + skills
    os.system('clear')

    question1 = 'Hello, what is your name?\n'
    script_text(question1)
    main_character.name = input('> ')

    question2 = 'Hello, ' + main_character.name + '. What is your origin?\n'
    script_text(question2)
    main_character.origin = input('> ')

    if main_character.origin == 'debug':
        main_character.stats = {
            'strength' : 10,
            'vitality' : 10,
            'agility' : 10,
            'mind' : 10,
            'will' : 10,
            'charisma' : 10
        }
    elif main_character.origin == 'warrior':
        main_character.stats = {
            'strength' : 15,
            'vitality' : 12,
            'agility' : 12,
            'mind' : 10,
            'will' : 8,
            'charisma' : 5
        }
    elif main_character.origin == 'thief':
        main_character.stats = {
            'strength' : 10,
            'vitality' : 10,
            'agility' : 15,
            'mind' : 12,
            'will' : 5,
            'charisma' : 12
        }
    elif main_character.origin == 'mage':
        main_character.stats = {
            'strength' : 5,
            'vitality' : 10,
            'agility' : 8,
            'mind' : 15,
            'will' : 12,
            'charisma' : 12
        }
    else :
        main_character.stats = {
            'strength' : 10,
            'vitality' : 10,
            'agility' : 10,
            'mind' : 10,
            'will' : 10,
            'charisma' : 10
        }
        for skill in main_character.skills :
            main_character.skills[skill] = 3
    
    introtext = main_character.name + ' the ' + main_character.origin + '...\n'
    introtext_2 = 'To be adventuring here, you must be seeking the manafont.\n'
    introtext_3 = 'That from which all things emerge\n.'
    introtext_4 = '...and to which all things return.\n'
    # introtext_5 = 'Many fearsome things seek to master the manafont. Not the least of which, Man\n'
    introtext_6 = 'There is danger, but do not fear.\n'
    introtext_7 = 'Remember, all things remain in flux.'
    script_text(introtext)
    script_text(introtext_2)
    script_text(introtext_3)
    script_text(introtext_4)
    # script_text(introtext_5)
    script_text(introtext_6)
    script_text(introtext_7)


# title_screen()