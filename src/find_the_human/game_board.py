from dataclasses import dataclass
import datetime


@dataclass
class Message:
    """A message sent by a player."""
    player: str
    msg: str
    timestamp: datetime.datetime

    def __repr__(self) -> str:
        return f"Message(player={self.player}, msg={self.msg}, timestamp={self.timestamp.time()})"

    def __str__(self) -> str:
        return f"[{self.timestamp}] {self.player}: {self.msg}"

class GameBoard:
    """The game board that keeps track of the user chatting messages."""

    def __init__(self):
        self._messages: list[Message] = []

    def add_message(self, player: str, msg: str) -> None:
        """Add a message to the game board."""
        self._messages.append(Message(player, msg, datetime.datetime.now(datetime.UTC)))

    def get_messages(self, n_limit: int = 0) -> list[str]:
        """Get the last n_limit messages.

        Notes:
            There are some reasons that we return string of messages.
            1. Prevent modification of the original messages by users.
            2. User does not need to know the internal structure of the Message class.
            3. Easier to display messages in the UI.
        """
        assert n_limit >= 0, f"n_limit must be non-negative, but got {n_limit}"

        # Check limit is valid
        if n_limit > len(self._messages):
            n_limit = len(self._messages)

        return [str(msg) for msg in self._messages[-n_limit:]]
