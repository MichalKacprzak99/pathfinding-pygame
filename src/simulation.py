import sys
import pygame as pg


from settings import Dimension
from board import Board


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
        self.caption = "Testing"
        self.window = pg.display.set_mode((Dimension.SCREEN_WIDTH.value, Dimension.SCREEN_HEIGHT.value))
        self.board = Board(self.window)

    def run(self):
        """
        run program and handle all pygame.events

        :return: None
        """
        pg.display.set_caption(self.caption)

        self.board.draw_board()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
