# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from dog import *

# 2 - Define constants
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 650
FRAMES_PER_SECOND = 30

# 3 - Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: images, sounds, etc.
images = [pygame.image.load('images/dog1.png'),
          pygame.image.load('images/dog2.png'),
          pygame.image.load('images/dog3.png'),
          pygame.image.load('images/dog4.png'),
          pygame.image.load('images/dog5.png'),
          pygame.image.load('images/dog6.png')]
background = pygame.image.load('images/bones.jpeg')

# 5 - Initialize variables
dog_list = []
for image in images:
    o_dog = Dog(window, WINDOW_WIDTH, WINDOW_HEIGHT, image)
    dog_list.append(o_dog)

# 6 - Main loop
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    for dog in dog_list:
        dog.update()

    # 9 - Clear the window before drawing it again
    window.blit(background, (0, 0))

    # 10 - Draw the window elements
    for dog in dog_list:
        dog.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
