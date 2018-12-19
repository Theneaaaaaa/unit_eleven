# Thenea Sun
# Dec. 18th
# A project about breakout game

import pygame, sys
from pygame.locals import *
import block
import random

pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
X_SPEED = 3
Y_SPEED = 4
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32, 0)
pygame.display.set_caption("Break out game")

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.width = width

        # Create a surface with the correct height and width
        self.image =

        # Get the rect coordinates
        self.rect =

def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
