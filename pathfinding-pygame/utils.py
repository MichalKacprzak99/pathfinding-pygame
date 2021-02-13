import pygame as pg

from enum import Enum, unique
from typing import Tuple


class Dimension(Enum):
    """
    Class for storing dimensions of screen/board and squares.
    """
    SQUARE_WIDTH = 80
    SQUARE_HEIGHT = 80
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    @classmethod
    def board_height(cls) -> int:
        return cls.SCREEN_HEIGHT.value // cls.SQUARE_HEIGHT.value

    @classmethod
    def board_width(cls) -> int:
        return cls.SCREEN_WIDTH.value // cls.SQUARE_WIDTH.value

    @classmethod
    def board_size(cls) -> Tuple[int, int]:
        return cls.board_width(), cls.board_height()


@unique
class Colors(Enum):
    """
    Class for storing colors in RGB format.
    """
    WHITE = pg.Color(255, 255, 255)
    BLACK = pg.Color(0, 0, 0)
    GREEN = pg.Color(0, 255, 0)
    RED = pg.Color(255, 0, 0)
    YELLOW = pg.Color(255, 255, 0)
    BROWN = pg.Color(106, 55, 5)
    BLUE = pg.Color(0, 0, 255)
    GRAY = pg.Color(128, 128, 128)
    BUMBLEBEE = pg.Color(255, 226, 5)
    ORANGE = pg.Color(229, 83, 0)


@unique
class Buttons(Enum):
    """
    Class for storing keys for mouse and keyboard buttons
    """
    MOUSE_LEFT = 1
    MOUSE_RIGHT = 3
    R_KEYBOARD = 114
