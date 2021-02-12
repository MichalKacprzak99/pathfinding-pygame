import unittest
import pygame as pg
import numpy as np

from board import Board
from square import Square
from settings import Dimension


class BoardTest(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(pg.display.set_mode((0, 0)))

    def test_is_square_empty_true(self):
        clicked_square_test = Square(0, 0)

        self.board.board_matrix = np.full(Dimension.board_size(), 1)

        result = self.board.is_square_empty(clicked_square_test)
        self.assertTrue(result)

    def test_is_square_empty_false(self):
        clicked_square_test = Square(0, 0)

        self.board.board_matrix = np.full(Dimension.board_size(), 1)

        self.board.board_matrix[0][0] = 0
        result = self.board.is_square_empty(clicked_square_test)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
