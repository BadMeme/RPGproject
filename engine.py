from __future__ import annotations
from typing import TYPE_CHECKING

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

import lzma
import pickle

# from entity import Entity
# from game_map import GameMap
import exceptions
from message_log import MessageLog
# from input_handlers import MainGameEventHandler
import render_functions

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap, GameWorld
    # from input_handlers import EventHandler

class Engine:
    game_map: GameMap
    game_world: GameWorld

    def __init__(self, player: Actor):
        # self.event_handler : EventHandler = MainGameEventHandler(self)
        self.message_log = MessageLog()
        self.mouse_location =(0,0)
        self.player = player

    def handle_enemy_turns(self) -> None :
        for entity in set(self.game_map.actors) - {self.player}:
            # print(f'The {entity.name} wonders when it will get to take a real turn.')
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass # ignore impossible action exceptions from AI

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles['transparent'],
            (self.player.x, self.player.y), 
            radius = 8,
        ) 
        #if a tile is visible, add to explored
        self.game_map.explored |= self.game_map.visible   

    def render(self, console: Console) -> None:
        self.game_map.render(console)
        self.message_log.render(
            console=console, x=21, y=45, width=40, height=5
        )
        render_functions.render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        render_functions.render_dungeon_level(
            console=console,
            dungeon_level=self.game_world.current_floor,
            location=(0, 47)
        )

        render_functions.render_names_at_mouse_location(
            console=console, x=21, y=44, engine=self
        )
    
    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)