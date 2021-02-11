from typing import List

import pygame as pg
import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from settings import Colors
from square import Square


class PathFinder:
    def __init__(self, window: pg.Surface, matrix: np.ndarray):
        """
         Creates a new ``PathFinder`` instance.
        """
        self.start_square = None
        self.end_square = None
        self.window = window
        self.matrix = matrix
        self.path_able_to_find = False

    def set_point(self, clicked_square: Square):
        """
        Sets the starting or ending square of the path. The starting square will be set first, then the end square.

        :param clicked_square: clicked square by user
        :return: None
        """
        if self.start_square is None:
            self.start_square = clicked_square
        elif self.end_square is None:
            self.end_square = clicked_square
            self.path_able_to_find = True

    def reset(self):
        """
        Deletes chosen squares.

        :return: None
        """
        self.start_square = self.end_square = None

    def draw_squares(self):
        """
        if start or end square is not None, it is drawn.
        :return: None
        """
        if self.start_square is not None:
            self.start_square.draw(self.window, Colors.GREEN.value)

        if self.end_square is not None:
            self.end_square.draw(self.window, Colors.RED.value)

    def find_path(self):
        """
        Finds path between start and end square using A star algorithm.
        If path is founded, it is drawn.

        :return: None
        """
        grid = Grid(matrix=self.matrix)
        start = grid.node(*self.start_square.board_coordinates)
        end = grid.node(*self.end_square.board_coordinates)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        self.path_able_to_find = False
        path_squares = [Square(*path_point) for path_point in path[1:-1]]
        self.draw_path(path_squares)

    def draw_path(self, path_squares: List[Square]):
        for path_square in path_squares:
            path_square.draw(self.window, Colors.GRAY.value)
            pg.time.delay(100)
