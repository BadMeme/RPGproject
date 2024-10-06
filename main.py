# main gaim loop logic

import sys
import os
# os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob
import traceback

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from tcod import libtcodpy # <- For refactor, sys warnings

import color
# from engine import Engine
# from entity import Entity
# import gameobjects
import exceptions
import input_handlers
# from game_map import GameMap
# from actions import EscapeAction, MovementAction
# from procgen import generate_dungeon
import setup_game

DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")

def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine, then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game Saved")

def main() -> None:
    screen_width = 80
    screen_height = 55

    tileset = tcod.tileset.load_tilesheet(FONT_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD)

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
        screen_width, 
        screen_height, 
        tileset=tileset, 
        title="IO engine project", 
        vsync=True
    ) as context :
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        try:
            while True: 
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try: 
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception: #handle exceptions in game.
                    traceback.print_exc() #print error to stderr.
                    #then print error to message log
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )

        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit: #Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException: # save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise

if __name__ == "__main__" :
    main()

