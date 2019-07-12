import logging
from enum import Enum

class Color(Enum):
    YELLOW = 1
    GREEN = 2

class State:
    """A point-in-time representation of total game state"""

    def __init__(self, firstPlayer):
        self.logger = logging.getLogger(__name__)
        self.turn = firstPlayer

    def dump(self):
        """Put the game state in a human-understandable form on STDOUT"""
        print(f"It is {self.turn}'s turn")


class GameBoard:
    """Tracks the movement of player tokens"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Track who's where
        self.greenPosition = 0
        self.yellowPosition = 0

        # Track events during turns
        self.buttonIndexes = []
        self.patchIndexes = []
