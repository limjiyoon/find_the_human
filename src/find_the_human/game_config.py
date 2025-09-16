"""Game config contains the initial condition or rule of the game.

It doesn't change during the game.
"""

from collections import Counter
from dataclasses import dataclass

from find_the_human.player.role import Role


@dataclass(frozen=True)
class GameConfig:
    """The game configuration."""

    player_names: list[str]
    roles: Counter[Role]  # the number of players assigned to the role
    phase_time_limit: dict[str, int]
