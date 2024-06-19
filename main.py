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
        self.mp = 0
        self.conditions = []
        self.wounds = []
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
            'strength' : 8,
            'vitality' : 8,
            'agility' : 8,
            'mind' : 8,
            'will' : 8,
            'charisma' : 8
        }

    print(main_character.stats)