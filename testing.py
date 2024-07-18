# main gaim loop logic

import sys
import os
# os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob

import tcod as libtcod


DATA_FOLDER = 'data'
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10_gs_tc.png")
#
def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libtcod.console_set_custom_font(FONT_FILE, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, "IO engine project", False)

    key=libtcod.Key()
    mouse=libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()
    
        escape_key = libtcod.console_check_for_keypress()
        if key.vk == libtcod.KEY_ESCAPE :
            return True


# if __name__ == "__main__" :
#     main()

main ()
