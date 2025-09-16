"""Game phase defines what to do in the game.

The game flows like below:
Setup -> Discussion -> Vote -> Action -> End
            ↑ ___________________|
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from find_the_human.game_config import GameConfig
from find_the_human.game_status import GameStatus


class GamePhase(ABC):
    """Game Phase is a state machine for the game.

    It has two behaviors:
    1. play: Player plays according to the game
    2. next_phase: Go next phase
    """

    def __init__(self, config: GameConfig):
        self._config = config

    @abstractmethod
    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step next phase."""
        pass

    @abstractmethod
    def play(self, game_status: GameStatus) -> GameStatus:
        """Play the game according to the phase."""
        pass


class SetupPhase(GamePhase):
    """Assign the roles before the playing the game."""

    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step next phase."""
        _ = game_status
        return DiscussionPhase(self._config)

    def play(self, game_status: GameStatus) -> GameStatus:
        """Make players play the game in the phase."""
        _ = game_status
        return GameStatus(1, ())


class DiscussionPhase(GamePhase):
    """Players discuss and try to identify the human player."""

    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step next phase.

        Transition Rule:
            goto VotingPhase
        """
        _ = game_status
        return VotingPhase(self._config)

    def play(self, game_status: GameStatus) -> GameStatus:
        """Discuss and try to identify the human player.

        Steps:
        1. GM announce the phase
        2. GM announce the result of the action phase
        3. Player reasoning and chat on the board
        4. GM announce the remain time periodically
        5. GM announce the last 5 seconds
        """
        _ = game_status
        return GameStatus(1, ())


class VotingPhase(GamePhase):
    """Players vote to eliminate a player they suspect is the robot."""

    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step next phase.

        Transition Rule:
            If every human or robot players are elimianated, goto EndPhase
            Otherwise, goto ActionPhase
        """
        if game_status.is_game_end():
            return EndPhase(self._config)
        else:
            return ActionPhase(self._config)

    def play(self, game_status: GameStatus) -> GameStatus:
        """Eliminate one player with voting."""
        _ = game_status
        # Pick player to eliminate

        # Vote to save or eliminate
        return GameStatus(1, ())


class ActionPhase(GamePhase):
    """The robot player takes an action based on its role."""

    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step next phase.

        Transition Rule:
            If every robot players are elimianated: goto EndPhase
            Otherwise: goto DiscussionPhase
        """
        if game_status.is_game_end():
            return EndPhase(self._config)
        else:
            return DiscussionPhase(self._config)

    def play(self, game_status: GameStatus) -> GameStatus:
        """Make every player to decide and take action."""
        _ = game_status
        return GameStatus(1, ())


class EndPhase(GamePhase):
    """Final phase that ends the game."""

    def next_phase(self, game_status: GameStatus) -> GamePhase:
        """Step to end game.

        Transition Rule:
            EndPhase

        It returns itself for idempotency.
        """
        _ = game_status  # don't use game status
        return self

    def play(self, game_status: GameStatus) -> GameStatus:
        """Announce the winner, game history and end the game."""
        _ = game_status
        # print winner
        return GameStatus(1, ())
