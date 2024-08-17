# main gaim loop logic

import sys
import os
# os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob
import copy

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from tcod import libtcodpy # <- For refactor, sys warnings

import color
from engine import Engine
# from entity import Entity
import gameobjects
# from game_map import GameMap
# from actions import EscapeAction, MovementAction
from procgen import generate_dungeon


DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")

def main() -> None:
    screen_width = 80
    screen_height = 55

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(FONT_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD)

    # player = Entity(int(screen_width / 2), int(screen_height/2), "@", (255,255,255))
    player = copy.deepcopy(gameobjects.player)
    engine = Engine(player=player)
    
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )

    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventuruer, to yet another dungeon!", color.welcome_text
    )

    with tcod.context.new_terminal(
        screen_width, 
        screen_height, 
        tileset=tileset, 
        title="IO engine project", 
        vsync=True
    ) as context :
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True: 
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            engine.event_handler.handle_events(context)

if __name__ == "__main__" :
    main()

