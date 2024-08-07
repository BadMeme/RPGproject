from __future__ import annotations

from typing import Optional, Tuple, TypeVar, TYPE_CHECKING
import copy

if TYPE_CHECKING:
    from game_map import GameMap
T = TypeVar('T', bound='Entity')



class Entity:
    # Generic object class encompassing player, enemy, item, etc.
    gamemap: GameMap

    def __init__(
            self, 
            gamemap: Optional[GameMap] = None,
            x: int = 0, 
            y: int = 0, 
            char: str = '?', # = '?'
            color: Tuple[int, int, int]= (255, 255, 255),
            name: str = "<Unnamed>",
            blocks_movement: bool=False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap :
            # if gamemap isnt provided now then it will be set later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x:int, y:int) -> T:
        """Spawn a copy of this instance at the given lcoation."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. handles moving across gamemaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"): #possibly uninitialized.
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        # move the entity by a given amount
        self.x += dx
        self.y += dy
