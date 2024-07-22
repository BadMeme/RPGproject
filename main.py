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
from input_handlers import handle_keys


DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")
#
def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(FONT_FILE, 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    with tcod.context.new_terminal(
        screen_width, 
        screen_height, 
        tileset=tileset, 
        title="IO engine project", 
        vsync=True
    ) as context :
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True: 
            root_console.print(x=player_x, y=player_y, string="@")
            context.present(root_console)
            for event in tcod.event.wait():
                if event.type == 'QUIT' :
                    raise SystemExit()

    
    

    # libtcodpy.console_set_custom_font(FONT_FILE, libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_TCOD)
    # libtcodpy.console_init_root(screen_width, screen_height, "IO engine project", False)

    # console = tcod.console.Console(screen_width, screen_height)

    # key=libtcodpy.Key()
    # mouse=libtcodpy.Mouse()

    # while not libtcodpy.console_is_window_closed():
    #     libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS, key, mouse)
    #     libtcodpy.console_set_default_foreground(0, (255, 255, 255))
    #     libtcodpy.console_put_char(0, player_x, player_y, '@', libtcodpy.BKGND_NONE)
    #     # libtcodpy.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)
    #     libtcodpy.console_flush()

    #     libtcodpy.console_put_char(console, player_x, player_y, ' ', libtcodpy.BKGND_NONE)
    
    #     action = handle_keys(key)

    #     move = action.get('move')
    #     exit = action.get('exit')
    #     fullscreen = action.get('fullscreen')

    #     if move:
    #         dx, dy = move
    #         player_x += dx
    #         player_y += dy

    #     if exit:
    #         return True
        
    #     if fullscreen: 
    #         libtcodpy.console_set_fullscreen(not libtcodpy.console_is_fullscreen())

    #     if key.vk == libtcodpy.KEY_ESCAPE :
    #         return True


if __name__ == "__main__" :
    main()

