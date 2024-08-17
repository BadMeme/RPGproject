from __future__ import annotations
from typing import Optional, TYPE_CHECKING
import tcod.event
from tcod import libtcodpy
from actions import Action, EscapeAction, BumpAction, WaitAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]) :
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        raise NotImplementedError()
    
    def handle_events(self, context: tcod.context.Context) -> None:
        for event in tcod.event.wait():
            context.convert_event(event)
            self.dispatch(event)
    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
            self.engine.mouse_location = event.tile.x, event.tile.y

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def on_render(self,console:tcod.Console) -> Optional[Action]:
        self.engine.render(console)

class MainGameEventHandler(EventHandler):
    def handle_events(self, context: tcod.context.Context) -> None:
        for event in tcod.event.wait():
            context.convert_event(event)

            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov() # Update the FOV before the players next actions

    # def ev_quit (self, event: tcod.event.Quit) -> Optional[Action]:
    #     raise SystemExit()
    
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
        elif key == tcod.event.KeySym.v:
            self.engine.event_handler = HistoryViewer(self.engine)

        return action
    
class GameOverEventHandler(EventHandler):
    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.ESCAPE: #TODO this makes an error, suggests ESCAPE but doesnt work
            action = EscapeAction(self.engine.player)

        #no valid key was pressed
        return action

CURSOR_Y_KEYS = {
    tcod.event.KeySym.UP: -1, 
    tcod.event.KeySym.DOWN: 1,
    tcod.event.KeySym.PAGEUP: -10,
    tcod.event.KeySym.PAGEDOWN: 10,
}

class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console) #Draw the main state as bkgd

        log_console = tcod.console.Console(console.width - 6, console.height - 6)

        # Draw a frame with a custom banner title
        log_console.draw_frame(0, 0, log_console.width, log_console.height)
        log_console.print_box(
            0, 0, log_console.width, 1, '-|Message History|-', alignment = libtcodpy.CENTER
        )

        #render the message log using the curser parameter.

        self.engine.message_log.render_messages(
            log_console,
            1,
            1, 
            log_console.width - 2,
            log_console.height - 2,
            self.engine.message_log.messages[: self.cursor +1],
        )
        log_console.blit(console, 3, 3)

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        # Fancy conditional movement to make it feel right.
        if event.sym in CURSOR_Y_KEYS:
            adjust = CURSOR_Y_KEYS[event.sym]
            if adjust < 0 and self.cursor == 0:
                # Only move from the top to the bottom when youre on the edge.
                self.cursor = self.log_length -1
            elif adjust > 0 and self.cursor == self.log_length - 1:
                #same with bottom to top movement.
                self.cursor = 0
            else:
                # Otherwise move while staying clamped to the bounds of the history
                self.cursor = max(0, min(self.cursor + adjust, self.log_length -1))
        elif event.sym == tcod.event.KeySym.HOME:
            self.cursor = 0 # move directly to the top message
        elif event.sym == tcod.event.KeySym.END:
            self.cursor = self.log_length - 1 #move directly to the last message
        else: # any other key moves back to the main game state
            self.engine.event_handler = MainGameEventHandler(self.engine)
