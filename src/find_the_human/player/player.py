from abc import ABC, abstractmethod

from find_the_human.game_board import GameBoard
from find_the_human.player.role import Role


class Player(ABC):
    """Player plays the game.

    Responsibilities:
    - Chat with other players.
    - Vote for players.
    - Take actions based on their role.
    """
    def __init__(self, name: str, role: Role, board: GameBoard):
        self._name = name
        self._board = board
        self._role = role

    @abstractmethod
    def chat(self, message: str) -> bool:
        """Generate a response to a chat message."""
        pass

    @abstractmethod
    def vote(self, player: str) -> bool:
        """Vote for a player.

        Separate it with `action` method, since it would have different restriction.
        """
        pass

    @abstractmethod
    def action(self, player: str) -> bool:
        """Take an action against a player."""
        pass

    @abstractmethod
    def get_game_status(self) -> dict[str, str]:
        """Get the current game status."""
        pass

    def get_history_messages(self, n_limit: int = 0) -> list[str]:
        """Get the last n_limit messages from the game board.

        Notes:
            If n_limit is 0 or bigger than history size, return all messages.
        """
        assert n_limit >= 0, f"n_limit must be non-negative, but got {n_limit}"
        return self._board.get_messages(n_limit)

    @property
    def name(self) -> str:
        """Get the name of the player."""
        return self._name

    @property
    def role(self) -> str:
        """Get the role of the player.

        Notes:
            User cannot change its role directly, it must be assigned by the GameMaster.
        """
        return self._role.value

    @property
    def action_description(self) -> list[str]:
        """Get the action_description of the role."""
        return self._role.available_actions()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Player(name={self.name}, role={self._role})"