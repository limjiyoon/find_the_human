"""Game status contains the current state of the game.

Game status is created when the game phase is changed.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GameStatus:
    """The game status."""

    n_rounds: int
    players: tuple[PlayerStatus, ...]

    def is_game_end(self) -> bool:
        """Check if the game is ended.

        The game end condition: human or robot players are all eliminated.
        """
        return True


@dataclass(frozen=True)
class PlayerStatus:
    """The status of a player."""

    name: str
    role: str
    is_alive: bool
