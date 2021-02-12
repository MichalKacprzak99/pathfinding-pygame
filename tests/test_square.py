import unittest
import random

from square import Square
from settings import Dimension


class SquareTest(unittest.TestCase):

    def test_convert_to_board_coordinates(self):

        clicked_positions_test_seq = list()
        board_coordinates_seq = list()

        for x in range(Dimension.board_height()):
            for y in range(Dimension.board_height()):
                random_clicked_x_pos = x * Dimension.SQUARE_WIDTH.value + \
                                       random.randint(1, Dimension.SQUARE_WIDTH.value-1)
                random_clicked_y_pos = y * Dimension.SQUARE_HEIGHT.value + \
                                       random.randint(0, Dimension.SQUARE_HEIGHT.value-1)
                clicked_positions_test_seq.append((random_clicked_x_pos, random_clicked_y_pos))
                board_coordinates_seq.append((x, y))

        converted_clicked_positions_test = [Square.convert_to_board_coordinates(clicked_position_test)
                                            for clicked_position_test in clicked_positions_test_seq]

        self.assertListEqual(converted_clicked_positions_test, board_coordinates_seq)


if __name__ == "__main__":
    unittest.main()