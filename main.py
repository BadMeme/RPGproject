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

gamestate = {
    'player_pos' : None,
    'player_room' : None,
    'player_zone' : None,
}

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
        self.id = 0
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

def create_zone(zone=demo_zone):
    # print('Test: ' + zone.description)
    id_counter = 0
    for z in range (zone.size['z']):
        for y in range (zone.size['y']):
            for x in range (zone.size['x']):
                new_room = room()
                new_room.id = id_counter
                new_room.xyz = {
                    'x' : x,
                    'y' : y,
                    'z' : z
                }
                zone.rooms.append(new_room)
                id_counter += 1

create_zone(demo_zone)

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
    print('                            ')
    print('                            ')
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
    print('                            ')
    print('                            ')
    print('                            ')
    print('                            ') #lol is this even right
    title_screen_selections()

# Gameplay Screen 

def move():
    print('Write the move function to update gamestate with room info')
    # if direction.lower == 'move' :
    #     print('Which direction?')
    #     print('[W] Up')
    #     print('[S] Down')
    #     print('[A] Left')
    #     print('[D] Right')
    #     choice = input('> ')
    #     move(choice)
    action_menu()

def inspect():
    print('Fill rooms with inspectible stuff')
    action_menu()

def interact():
    print('Make rooms with interactable stuff')
    action_menu()


def action_menu_selections():
    option = input("> ")
    if option.lower() == ('move') or ('m') or ('a') or ('s') or ('d') or ('w') :
        move(option) #writing this soon
    elif option.lower() == ('inspect') or ('i'):
        inspect()
    elif option.lower() == ('interact') or ('j'):
        interact()
    elif option.lower() == ('quit'):
        sys.exit()
    else :
        print("Please enter a valid command.")
        action_menu_selections()

def action_menu():
    os.system('clear')
    print('############################')
    print('##    Input your action   ##')
    print('############################')
    action_menu_selections()

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
            'vitality' : 13,
            'agility' : 11,
            'mind' : 10,
            'will' : 8,
            'charisma' : 5
        }
    elif main_character.origin == 'thief':
        main_character.stats = {
            'strength' : 11,
            'vitality' : 10,
            'agility' : 15,
            'mind' : 8,
            'will' : 5,
            'charisma' : 13
        }
    elif main_character.origin == 'mage':
        main_character.stats = {
            'strength' : 5,
            'vitality' : 10,
            'agility' : 8,
            'mind' : 15,
            'will' : 13,
            'charisma' : 11
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

    # gamestate.player_pos = 0
    # gamestate.player_zone = 0

    action_menu()


title_screen()