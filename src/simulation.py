import sys
import pygame as pg

from settings import Dimension, Buttons
from board import Board
from pathfinder import PathFinder
from square import Square


class Simulation:
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
         Creates a new ``Simulation`` instance.
        """
        pg.init()
        pg.font.init()
        self.caption = "Basic Pathfinding"
        self.window = pg.display.set_mode((Dimension.SCREEN_WIDTH.value, Dimension.SCREEN_HEIGHT.value))
        self.board = Board(self.window)
        self.path_finder = PathFinder(self.window, self.board.matrix)

    def run(self):
        """
        run program and handle all pygame.events

        :return: None
        """
        pg.display.set_caption(self.caption)
        self.board.draw_board()
        while True:

            self.path_finder.draw_squares()
            if self.path_finder.path_able_to_find:
                self.path_finder.find_path()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONUP and event.button == Buttons.MOUSE_LEFT.value:
                    self.choose_square()

                if event.type == pg.MOUSEBUTTONUP and event.button == Buttons.MOUSE_RIGHT.value:
                    self.clear_board()

                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    self.new_board()

    def new_board(self):
        self.path_finder.reset()
        self.board.recreate_obstacles()
        self.board.draw_board()

    def choose_square(self):
        clicked_square = Square(*pg.mouse.get_pos())
        clicked_square.convert_to_square_coordinates()
        if self.board.is_square_free(clicked_square):
            self.path_finder.set_point(clicked_square)

    def clear_board(self):
        self.path_finder.reset()
        self.board.draw_board()