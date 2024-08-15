from __future__ import annotations
from typing import TYPE_CHECKING

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

# from entity import Entity
# from game_map import GameMap
from input_handlers import MainGameEventHandler
from render_functions import render_bar

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap
    from input_handlers import EventHandler

class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.event_handler : EventHandler = MainGameEventHandler(self)
        self.player = player

    def handle_enemy_turns(self) -> None :
        for entity in set(self.game_map.actors) - {self.player}:
            # print(f'The {entity.name} wonders when it will get to take a real turn.')
            if entity.ai:
                entity.ai.perform()

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles['transparent'],
            (self.player.x, self.player.y), 
            radius = 8,
        ) 
        #if a tile is visible, add to explored
        self.game_map.explored |= self.game_map.visible   

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        # for entity in self.entities:
        #     console.print(entity.x, entity.y, entity.char, fg=entity.color)
        render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )
        context.present(console)
        console.clear()
