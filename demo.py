# demo tutorial resource

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
        self.mp = 0
        self.conditions = []
        self.stats = []
        self.location = 'b2'
        self.job = ''
        self.gameover = False
        #leaving room to expand past tutorial. might store stats in a dictionary or as individual properties of player

main_character = player()

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



### Interactivity ###

def print_location():
    print('\n' + ('#' * (4 + len(main_character.location))))
    print('#' + main_character.location.upper() + '#')
    print('#' + zonemap[main_character.location][DESCRIPTION])
    print('\n' + ('#' * (4 + len(main_character.location))))

def player_prompt():
    print('\n' + '============================')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ') # "> "
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[main_character.location][UP]
        movement_handler()
    elif dest in ['left', 'west']:
        destination = zonemap[main_character.location][LEFT]
        movement_handler()
    elif dest in ['right', 'east']:
        destination = zonemap[main_character.location][RIGHT]
        movement_handler()
    elif dest in ['down', 'south']:
        destination = zonemap[main_character.location][DOWN]
        movement_handler()

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    main_character.location = destination
    print_location()

def player_examine(action):
    if zonemap[main_character.location][SOLVED]:
        print('Youve already exhausted this zone.')
    else:
        print('You can trigger a puzzle here.')

### Maps ###

#Test Grid
# a |_|_|_|_|
# b |_|_|_|_|
# c |_|_|_|_|
# d |_|_|_|_|
#    1 2 3 4
#

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1': {
        ZONENAME : 'Town Market',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b1',
        LEFT : '',
        RIGHT : 'a2'
    },
    'a2': {
        ZONENAME : 'Town Entrance',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a2'
    },
    'a3': {
        ZONENAME : 'Town Square',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'c3'
    },
    'a4': {
        ZONENAME : 'Town Residence',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : ''
    },
    'b1': {
        ZONENAME : 'Fields',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : '',
        RIGHT : 'b2'
    },
    'b2': {
        ZONENAME : 'Home',
        DESCRIPTION : 'This is your home',
        EXAMINATION : 'Your home looks the same - nothing has changed',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3'
    },
    'b3': {
        ZONENAME : 'Forest',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4'
    },
    'b4': {
        ZONENAME : 'Deep Forest',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : ''
    }
}
    
### Game Loops ###

def start_game(): 
    setup_game()

def main_game_loop():
    while main_character.gameover is False:
        player_prompt()

def setup_game(): 
    os.system('clear')

    question1 = "Hello, what's your name?\n"
    for character in question1:
            sys.stdout.write(character)
            sys.stdout.flush() ###Look this up
            time.sleep(0.05)
    main_character.name = input('> ')

    question2 = 'Hello, ' + main_character.name + ', what role do you want ot play?\n'
    # question2added = '(You can play as a warrior, priest or mage)\n'
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    # for character in question2added:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    player_job = input('> ')
    valid_jobs = ('warrior', 'mage', 'priest')
    if player_job.lower() in valid_jobs:
        main_character.job = player_job 
        print('You are now a '+ player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        main_character.job = input('> ')
        if player_job.lower() in valid_jobs:
            main_character.job = player_job 
            print('You are now a '+ player_job + '!\n')

    ### Player Stats
    if main_character.job == 'warrior':
        main_character.hp = 120 # was self?
        main_character.mp = 20
    elif main_character.job == 'mage':
        main_character.hp = 40  # was self?
        main_character.mp = 120
    elif main_character.job == 'priest':
        main_character.hp = 60  # was self?
        main_character.mp = 60

    ### Introduction

    question3 = 'Welcome, ' + main_character.name + ' the ' + main_character.job + '.\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = 'Welcome to this fantasy World!\n'
    speech2 = 'I hope it greets you well!\n'
    speech3 = 'Just make sure you dont get too lost...\n'
    speech4 = 'Heheheheh...\n'

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print('####################')
    print('# Lets start now!  #')
    print('####################')

    main_game_loop()

title_screen()