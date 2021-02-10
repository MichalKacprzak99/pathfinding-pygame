import pygame as pg
import math

from typing import Tuple

from settings import Dimension


class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def get_screen_coordinates(self) -> Tuple[int, int]:
        return self.x * Dimension.SQUARE_WIDTH.value + 1, self.y * Dimension.SQUARE_HEIGHT.value + 1

    def convert_to_square_coordinates(self):
        self.x = math.floor(self.x / Dimension.SQUARE_WIDTH.value)
        self.y = math.floor(self.y / Dimension.SQUARE_HEIGHT.value)

    def get_squared_coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def draw(self, window: pg.Surface, color: Tuple[int, int, int]):
        rect = (self.get_screen_coordinates(),
                (Dimension.SQUARE_WIDTH.value - 1, Dimension.SQUARE_HEIGHT.value - 1))
        pg.draw.rect(window, color, rect)

        pg.display.update()
