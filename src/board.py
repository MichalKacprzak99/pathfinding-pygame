import random
import numpy as np
import pygame as pg


from settings import Dimension, Colors


class Board:
    """
    A class representing a chess-like board but with different size: 10x10, instead of classic 8x8.

    ...

    Attributes
    ----------

    window: pygame.Surface
        Pygame object for representing images.
    matrix: numpy.ndarray
        array 10x10 representing state of board .
        1 represents empty square and 0 represent obstacle

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
        self.matrix = np.full((10, 10), 1)

    def draw_board(self):
        """
        All elements of board are drawn.

        :return: None
        """
        self.window.fill(Colors.WHITE.value)
        self.draw_lines()
        self.draw_obstacles()
        pg.display.update()

    def draw_lines(self):
        """
        Draws lines on the board, the first and last lines are not drawn because these lines are the ends of the screen

        :return: None
        """
        for x_cord in range(0, Dimension.SCREEN_WIDTH.value, Dimension.SQUARE_WIDTH.value):
            pg.draw.line(self.window, Colors.BLACK.value, (x_cord, 0), (x_cord, Dimension.SCREEN_HEIGHT.value))

        for y_cord in range(0, Dimension.SCREEN_HEIGHT.value, Dimension.SQUARE_HEIGHT.value):
            pg.draw.line(self.window, Colors.BLACK.value, (0, y_cord), (Dimension.SCREEN_WIDTH.value, y_cord))

    def draw_obstacles(self):
        """
        Obstacles created by self.create_obstacles are drawn on self.windows as a black rectangles.

        :return: None
        """
        obstacles = self.create_obstacles()

        for obstacle in obstacles:
            obstacle_x_cord, obstacle_y_cord = obstacle
            obstacle_x_cord *= Dimension.SQUARE_WIDTH.value
            obstacle_y_cord *= Dimension.SQUARE_HEIGHT.value
            rect = (obstacle_x_cord, obstacle_y_cord, Dimension.SQUARE_WIDTH.value, Dimension.SQUARE_HEIGHT.value)
            pg.draw.rect(self.window, Colors.BLACK.value, rect)

    def create_obstacles(self):
        """
        Function creates from 1 to 10 obstacles with random coordinates.
        The self.matrix is modified to reflect the changes to on the board

        :return: list of obstacles coordinates
        :rtype: list
        """
        obstacle_number = random.randint(1, 10)
        obstacles = list()

        for _ in range(obstacle_number):
            obstacle_x_cord = random.randint(0, 9)
            obstacle_y_cord = random.randint(0, 9)
            self.matrix[obstacle_y_cord][obstacle_x_cord] = 0
            obstacles.append((obstacle_x_cord, obstacle_y_cord))

        return obstacles

    def redraw_board(self):
        pass


