from typing import Optional
import tcod.event
from tcod import libtcodpy

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]) :
    def ev_quit (self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        return action
#  Old Key handler. Leaving as notes for future refactor.
#  Refactor notes that this version handles the information being passed
#  As dictionaries, so that these functions can be called without explicit
#  Key presses. (Simultaneous info, AI input? etc)


# def handle_keys(key):
#     # movement keys
#     if key.vk == libtcodpy.KEY_UP:
#         return {"move":(0,-1)}
#     elif key.vk == libtcodpy.KEY_DOWN:
#         return {"move":(0,1)}
#     elif key.vk == libtcodpy.KEY_LEFT:
#         return {"move":(-1,0)}
#     elif key.vk == libtcodpy.KEY_RIGHT:
#         return {"move":(1,0)}            
#     # may add z variable here later for tile height etc

#     if key.vk == libtcodpy.KEY_ENTER and key.lalt:
#         # ALT+Enter: toggle full screen
#         return {"fullscreen": True}
    
#     elif key.vk == libtcodpy.KEY_ESCAPE:
#         # Exit the game
#         return {'exit': True}
    
#     return {}