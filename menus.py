import sys

gamestate = {
    'playerzone' : None,
    'playerpos' : {
        'x' : None,
        'y' : None,
        'z' : None
    }
}

def print_location():
    print('\n' + 'PlayerPOS: ' + str(gamestate['playerpos']))

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    # main_character.location = destination
    print_location()

def move(option):
    UP = ['up', 'north', 'w']
    DOWN = ['down', 'south', 's']
    LEFT = ['left', 'west', 'a']
    RIGHT = ['right', 'east', 'd']
    print('Test: Move')
    print('Write the move function to update gamestate with room info')
    print('Current Location: ' + str(gamestate['playerpos']))
    direction = input('> ')
    if direction.lower() in UP :
        print('UP input: ' + direction)
        gamestate['playerpos']['y'] += 1
        print_location()
    elif direction.lower() in DOWN :
        gamestate['playerpos']['y'] -= 1
        print('DOWN input: ' + direction)
        print_location()
    elif direction.lower() in LEFT :
        gamestate['playerpos']['x'] -= 1
        print('LEFT input: ' + direction)
        print_location()
    elif direction.lower() in RIGHT :
        gamestate['playerpos']['x'] += 1
        print('RIGHT input: ' + direction)
        print_location()
    else :
        print('Erroneous Input: ' + direction)
    action_menu()

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    # main_character.location = destination
    print_location()

def inspect():
    print('Test: Inspect')
    print('Fill rooms with inspectible stuff')
    action_menu()

def interact():
    print('Test: Interact')
    print('Make rooms with interactable stuff')
    action_menu()

def action_menu() :
    print('Test: Action Menu')
    print('Select action\n')
    action_menu_selections()

def action_menu_selections():
    option = input("> ")
    MOVE = ['move', 'm',] # 'a', 's', 'd', 'w'] <- if shortcutting movement, will need to reword how the move functino is called
    INSPECT = ['inspect', 'i']
    INTERACT = ['interact', 'j']
    QUIT = ['quit', 'q']
    HELP = ['help', '?']
    if option.lower() in MOVE :
        move(option) #writing this soon
    elif option.lower() in INSPECT:
        inspect()
    elif option.lower() in INTERACT:
        interact()
    elif option.lower() in HELP:
        print('Action menu options:')
        print('Move [M]')
        print('Inspect [I]')
        print('Interact [J]')
        print('Quit [Q]')
        action_menu_selections()
    elif option.lower() in QUIT:
        sys.exit()
    else :
        print("Please enter a valid command. (Enter Help [?] for a list of commands and shortcuts)")
        action_menu_selections()

def testmovefunctions() :
    print('Test: ACTION MENU START')
    action_menu_selections()

gamestate['playerpos'] = {
        'x' : 1,
        'y' : 1,
        'z' : 1
    }
# testmovefunctions()
# print(gamestate['playerpos']['x'])

# Export

