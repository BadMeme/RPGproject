from __future__ import annotations
from typing import Optional, TYPE_CHECKING
import tcod.event
# from tcod import libtcodpy
from actions import Action, EscapeAction, BumpAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]) :
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov() # Update the FOV before the players next actions

    def ev_quit (self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key == tcod.event.KeySym.UP:
            # action = MovementAction(dx=0, dy=-1)
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.KeySym.DOWN:
            # action = MovementAction(dx=0, dy=1)
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.KeySym.LEFT:
            # action = MovementAction(dx=-1, dy=0)
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.KeySym.RIGHT:
            # action = MovementAction(dx=1, dy=0)
            action = BumpAction(player, dx=1, dy=0)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction(player)

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