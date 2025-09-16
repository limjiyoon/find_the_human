"""Role definition and for the game.

The role definition contains the available action for each role.
"""

from enum import Enum


class Role(Enum):
    """The role of a player in the game.

    The role defines the actions that a player can take.
    """

    UNASSIGNED = "unassigned"
    HUMAN = "human"
    ROBOT = "robot"

    def action_description(self) -> str:
        """Get the available actions for the role."""
        return ACTIONS_DESCRIPTIONS[self]


ACTIONS_DESCRIPTIONS = {
    Role.UNASSIGNED: [],
    Role.HUMAN: "Turn Off Robot",
    Role.ROBOT: "Do Nothing",
}
