import pygame as pg
import math

from typing import Tuple

from settings import Dimension


class Square:
    """
    Class for representing square on the board
    """
    def __init__(self, x: int, y: int):
        """
         Creates a new ``Square`` instance.
        """
        self.x, self.y = x, y

    @property
    def window_coordinates(self) -> Tuple[int, int]:
        """
        Transform board coordinates of square to window coordinates

        :return: coordinates of top left corner of square
        """
        return self.x * Dimension.SQUARE_WIDTH.value + 1, self.y * Dimension.SQUARE_HEIGHT.value + 1

    @staticmethod
    def convert_to_board_coordinates(clicked_position: Tuple[int, int]) -> Tuple[int, int]:
        x, y = clicked_position
        x = math.floor(x / Dimension.SQUARE_WIDTH.value)
        y = math.floor(y / Dimension.SQUARE_HEIGHT.value)
        return x, y

    @property
    def board_coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def draw(self, window: pg.Surface, color: Tuple[int, int, int]):
        """
        Full fill square with given color.

        :param window: window created by pygame
        :param color: color in RGB format
        :return: None
        """
        rect = (self.window_coordinates, (Dimension.SQUARE_WIDTH.value - 1, Dimension.SQUARE_HEIGHT.value - 1))
        pg.draw.rect(window, color, rect)

        pg.display.update(rect)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))
