import pygame
from pygame.locals import *
import random


# Dog class
class Dog:
    """
    Represents an image of a dog. Keeps track of window to be drawn in,
    image width/height/speed/direction/position in window. Included methods:
    update() and draw().
    """

    def __init__(self, window: object, window_width: int, window_height: int,
                 image: object) -> None:
        # Initialize window so dogs can be drawn into window later
        self._window = window
        self._window_width = window_width
        self._window_height = window_height

        # Load image of this dog
        self._image = image

        # Get rect of image. rect = (x, y, width, height)
        dog_rect = self._image.get_rect()
        self._width = dog_rect.width
        self._height = dog_rect.height

        # Verifies that rect will always be fully visible in window
        self._max_width = self._window_width - self._width
        self._max_height = self._window_height - self._height

        # Represents position of rect. Starts with random pos
        self._x = random.randrange(0, self._max_width)
        self._y = random.randrange(0, self._max_height)

        # Sets a random speed between -4 (up/left) and 4 (down/right),
        # excluding 0, in both the x and y directions
        speed_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self._x_speed = random.choice(speed_list)
        self._y_speed = random.choice(speed_list)

    def update(self) -> None:
        """
        Checks if dog rect is hitting an edge of window. If so, reverses
        direction of dog rect to opposite. Updates dog rect's new position
        in window.
        @:return None
        """
        # Checks if hitting right/left edge of window. If so, changes direct
        if (self._x < 0) or (self._x > self._max_width):
            self._x_speed = -self._x_speed

        # Checks if hitting top/bottom edge of window. If so, changes direct
        if (self._y < 0) or (self._y > self._max_height):
            self._y_speed = -self._y_speed

        # Update dog's position, using the speed in both directions
        self._x += self._x_speed
        self._y += self._y_speed

    def draw(self) -> None:
        """
        Displays dog rect/image in window.
        :return: None.
        """
        self._window.blit(self._image, (self._x, self._y))
