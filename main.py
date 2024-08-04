# main gaim loop logic

import sys
import os
# os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from tcod import libtcodpy # <- For refactor, sys warnings

from engine import Engine
from entity import Entity
# from actions import EscapeAction, MovementAction
from input_handlers import EventHandler# handle_keys


DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")
#
def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(FONT_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height/2), "@", (255,255,255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height/2), "@", (255,255,0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width, 
        screen_height, 
        tileset=tileset, 
        title="IO engine project", 
        vsync=True
    ) as context :
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True: 
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)

if __name__ == "__main__" :
    main()

