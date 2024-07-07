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

# Game Zones
demo_zone = zone()
demo_zone.size = {
    'x' : 5, #width
    'y' : 5, #height
    'z' : 1  #floors
}
demo_zone.description = 'A strange gaol. The dust seems to hang in the air.'

print(demo_zone.size['z'])

def create_zone(zone=demo_zone):
    print('Test: ' + zone.description)
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
                print(new_room.xyz)
    


create_zone(demo_zone)