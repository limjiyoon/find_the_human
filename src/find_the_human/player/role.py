from enum import Enum


class Role(Enum):
    """The role of a player in the game.

    The role defines the actions that a player can take.
    """
    UNASSIGNED = "unassigned"
    HUMAN = "human"
    ROBOT = "robot"

    def available_actions(self) -> list[str]:
        """Get the available actions for the role."""
        return ACTIONS_DESCRIPTIONS[self]


ACTIONS_DESCRIPTIONS = {
    Role.UNASSIGNED: [],
    Role.HUMAN: ["Turn Off Robot", "Do Nothing"],
    Role.ROBOT: {"Do Nothing"},
}