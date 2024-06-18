### Mechanics Master Sheet ###
# This doc will contain all the basic game/dice mechanics for conflict resolution

import math
import random

def diceroll():
    roll = random.randint(0,99)
    double = False
    if roll % 11 == 0:
        double = True
    # print('Roll: ' + str(roll))
    # print('Crit: ' + str(double))
    result = {
        'roll' : roll,
        'dub' : double
    }
    # print(result['roll'])
    return (result)

# diceroll()

def ability_check(player='', threshold=50):
    print('ability check test: ' + player)
    if player == '':
        player = diceroll()
        print(player)
    # print(player['roll'])
    print('Roll: ' + str(player['roll']) + ' vs. Threshold: ' + str(threshold))
    if player['roll'] < threshold :
        print('Success!')
    else:
        print('Fail...')

def opposed_check(player='', opponent=''):
    print('ability check test: ' + player)
    if player == '':
        player = diceroll()
        print(player)
    if opponent == '':
        opponent = diceroll()
        print(opponent)
    # print(player['roll'])
    print('Roll: ' + str(player['roll']) + ' vs. Opponent: ' + str(opponent['roll']))
    if player['roll'] < opponent['roll'] :
        print('Success!')
    else:
        print('Fail...')


### Test ###
# diceroll()
# ability_check()
opposed_check()