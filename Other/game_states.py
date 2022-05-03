import enum


class GameStates(enum.Enum):
    DEFAULT = None
    CHOOSE_CHARACTER = 100
    CHOOSE_NAME = 101
    PLAY = 200
