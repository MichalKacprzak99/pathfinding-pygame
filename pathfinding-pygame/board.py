import random
from typing import List

import numpy as np
import pygame as pg

from utils import Dimension, Colors
from square import Square


class Board:
    """
    A class representing a chess-like board but with different size: 10x10, instead of classic 8x8.

    ...

    Attributes
    ----------

    window: pygame.Surface
        Pygame object for representing images.
    board_matrix: numpy.ndarray
        array 10x10 representing state of board .
        1 represents empty square and 0 represent obstacle.

    """
    def __init__(self, window: pg.Surface):
        """
         Creates a new ``Board`` instance.

        Parameters
        ----------
            window : pygame.Surface
                Pygame object for representing images.
        """
        self.window = window
        self.board_matrix = np.full(Dimension.board_size(), 1)
        self.maximum_obstacles_on_board = 10
        self.obstacles = self.create_obstacles()

    def draw_board(self):
        """
        All elements of board are drawn.

        :return: None
        """
        self.window.fill(Colors.WHITE.value)
        self.draw_lines()
        self.draw_obstacles()

    def draw_lines(self):
        """
        Draws lines on the board, the first and last lines are not drawn because these lines are the ends of the screen

        :return: None
        """
        for x_cord in range(0, Dimension.SCREEN_WIDTH.value, Dimension.SQUARE_WIDTH.value):
            pg.draw.line(self.window, Colors.BLACK.value, (x_cord, 0), (x_cord, Dimension.SCREEN_HEIGHT.value))

        for y_cord in range(0, Dimension.SCREEN_HEIGHT.value, Dimension.SQUARE_HEIGHT.value):
            pg.draw.line(self.window, Colors.BLACK.value, (0, y_cord), (Dimension.SCREEN_WIDTH.value, y_cord))

        pg.display.update()

    def draw_obstacles(self):
        """
        Obstacles created by self.create_obstacles are drawn on self.windows as a black rectangles.

        :return: None
        """
        for obstacle in self.obstacles:
            obstacle.draw(self.window, Colors.BLACK.value)

    def create_obstacles(self) -> List[Square]:
        """
        Function creates from 1 to 10 obstacles with random coordinates.
        The self.matrix is modified to reflect the changes to on the board

        :return: list of obstacles coordinates
        :rtype: list
        """
        obstacles_number = random.randint(1, self.maximum_obstacles_on_board)
        obstacles = list()

        while len(obstacles) < obstacles_number:

            obstacle_x_pos = random.randint(0, Dimension.board_width() - 1)
            obstacle_y_pos = random.randint(0, Dimension.board_height() - 1)
            obstacle = Square(obstacle_x_pos, obstacle_y_pos)
            if obstacle not in obstacles:
                self.board_matrix[obstacle_y_pos][obstacle_x_pos] = 0
                obstacles.append(obstacle)

        return obstacles

    def is_square_empty(self, clicked_square: Square) -> bool:
        """
        Checks if clicked square is not obstacle and it's possible to start/end path here.

        :param clicked_square: A square of board which user clicked.
        :return: true if square is not obstacle, otherwise false
        """
        return clicked_square not in self.obstacles

    def recreate_obstacles(self):
        """
        Creates new state of board with different number of obstacles and their positions.

        :return: None
        """
        self.board_matrix = np.full(Dimension.board_size(), 1)
        self.obstacles = self.create_obstacles()

