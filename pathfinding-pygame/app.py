import pygame as pg

from utils import Dimension, Buttons
from board import Board
from pathfinder import PathFinder
from square import Square


class Application:
    """
    Main class of application

    ...

    Attributes
    ----------

    caption: str
        title of window

    window: pygame.Surface
        Pygame object for representing images.

    board: board.Board
        Instance of ```Board```
    """
    def __init__(self):
        """
         Creates a new ``Application`` instance.
        """

        self.caption = "Basic Pathfinding"
        self.window = pg.display.set_mode((Dimension.SCREEN_WIDTH.value, Dimension.SCREEN_HEIGHT.value))
        self.board = Board(self.window)
        self.path_finder = PathFinder(self.window)

    def run(self):
        """
        run program and handle all pygame.events

        :return: None
        """

        pg.display.set_caption(self.caption)
        self.board.draw_board()
        running = True
        while running:

            self.path_finder.draw_squares()
            if self.path_finder.path_able_to_find:
                path = self.path_finder.find_path(self.board.board_matrix)
                self.path_finder.draw_path(path)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONUP and event.button == Buttons.MOUSE_LEFT.value:
                    self.choose_square()

                if event.type == pg.MOUSEBUTTONUP and event.button == Buttons.MOUSE_RIGHT.value:
                    self.clear_board()

                if event.type == pg.KEYDOWN and event.key == Buttons.R_KEYBOARD.value:
                    self.new_board()

        pg.quit()

    def new_board(self):
        """
        Create new obstacles and redrawn board.
        :return:
        """
        self.board.recreate_obstacles()
        self.clear_board()

    def choose_square(self):
        clicked_square_pos = Square.convert_to_board_coordinates(pg.mouse.get_pos())
        clicked_square = Square(*clicked_square_pos)
        if self.board.is_square_empty(clicked_square):
            self.path_finder.set_point(clicked_square)

    def clear_board(self):
        """
        Removes the found path and selected squares from the board.
        Board is redrawn

        :return: None
        """
        self.path_finder.reset()
        self.board.draw_board()
