import unittest
import pygame as pg
import numpy as np

from square import Square
from pathfinder import PathFinder
from utils import Dimension


class PathFinderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.path_finder = PathFinder(pg.display.set_mode((0, 0)))

    def test_set_point_both_points_set(self):
        start_square_test = Square(0, 0)
        end_square_test = Square(1, 1)

        self.path_finder.set_point(start_square_test)
        self.path_finder.set_point(end_square_test)

        self.assertEqual(self.path_finder.start_square, start_square_test)
        self.assertEqual(self.path_finder.end_square, end_square_test)

    def test_set_point_failed_to_set_end_point(self):
        clicked_square_test = Square(0, 0)

        self.path_finder.set_point(clicked_square_test)
        self.path_finder.set_point(clicked_square_test)
        self.assertIsNone(self.path_finder.end_square)

    def test_find_path_found(self):
        start_square_test = Square(0, 0)
        end_square_test = Square(2, 0)

        self.path_finder.set_point(start_square_test)
        self.path_finder.set_point(end_square_test)

        matrix_test = np.full(Dimension.board_size(), 1)

        path_test = self.path_finder.find_path(matrix_test)

        self.assertEqual(path_test, [Square(1, 0)])

    def test_find_path_not_found(self):

        start_square_test = Square(0, 0)
        end_square_test = Square(2, 0)

        self.path_finder.set_point(start_square_test)
        self.path_finder.set_point(end_square_test)

        matrix_test = np.full(Dimension.board_size(), 1)
        matrix_test[0][1] = matrix_test[1][1] = matrix_test[1][0] = 0
        path_test = self.path_finder.find_path(matrix_test)

        self.assertEqual(path_test, [])


if __name__ == "__main__":
    unittest.main()