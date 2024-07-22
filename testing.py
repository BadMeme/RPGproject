
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


print 