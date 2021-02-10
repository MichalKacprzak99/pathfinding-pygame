from enum import Enum, unique


class Dimension(Enum):
    """
    Enum for storing dimensions of screen/board and squares.
    """
    SQUARE_WIDTH = 80
    SQUARE_HEIGHT = 80
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800


@unique
class Colors(Enum):
    """
    Enum for storing colors in RGB format.
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



