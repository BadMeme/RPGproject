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