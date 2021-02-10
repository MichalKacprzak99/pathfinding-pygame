from typing import List

import pygame as pg
import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from settings import Colors
from point import Point


class PathFinder:
    def __init__(self, window: pg.Surface, matrix: np.ndarray):
        self.start_point = None
        self.end_point = None
        self.window = window
        self.matrix = matrix
        self.path_able_to_find = False

    def set_point(self, clicked_point: Point):
        if self.start_point is None:
            self.start_point = clicked_point
        elif self.end_point is None:
            self.end_point = clicked_point
            self.path_able_to_find = True

    def reset(self):
        self.start_point = self.end_point = None

    def draw_points(self):
        if self.start_point is not None:
            self.start_point.draw(self.window, Colors.GREEN.value)

        if self.end_point is not None:
            self.end_point.draw(self.window, Colors.RED.value)

    def find_path(self):

        grid = Grid(matrix=self.matrix)
        start = grid.node(*self.start_point.get_squared_coordinates())
        end = grid.node(*self.end_point.get_squared_coordinates())
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        self.path_able_to_find = False
        path_points = [Point(*path_point) for path_point in path[1:-1]]
        self.draw_path(path_points)

    def draw_path(self, path_points: List[Point]):
        for path_point in path_points:
            path_point.draw(self.window, Colors.GRAY.value)
            pg.time.delay(100)


