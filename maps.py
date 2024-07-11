import gameobjects

# Game Zones
demo_zone = gameobjects.zone()
demo_zone.size = {
    'x' : 5, #width
    'y' : 5, #height
    'z' : 1  #floors
}
demo_zone.description = 'A strange gaol. The dust seems to hang in the air.'

# print(demo_zone.size['z'])

def create_zone_rooms(zone):
    # print('Test: ' + zone.description)
    id_counter = 0
    for z in range (zone.size['z']):
        for y in range (zone.size['y']):
            for x in range (zone.size['x']):
                new_room = gameobjects.room()
                new_room.id = id_counter
                new_room.xyz = {
                    'x' : x,
                    'y' : y,
                    'z' : z
                }
                zone.rooms.append(new_room)
                id_counter += 1
                # print(new_room.xyz)
    

create_zone_rooms(demo_zone)

demo_zone.rooms[0].events.append('Testin this shit')

def check_da_rooms(zone):
    for room in zone.rooms :
        print(room.event)

check_da_rooms(demo_zone) 