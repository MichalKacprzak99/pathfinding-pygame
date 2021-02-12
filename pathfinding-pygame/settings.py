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
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BROWN = (106, 55, 5)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)
    BUMBLEBEE = (255, 226, 5)
    ORANGE = (229, 83, 0)


@unique
class Buttons(Enum):
    """
    Class for storing keys for mouse and keyboard buttons
    """
    MOUSE_LEFT = 1
    MOUSE_RIGHT = 3



