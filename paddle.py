import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        # Create a surface with the correct height and width
        # Get the rect coordinates
        # Fill the surface with the correct color

    def move(self):
        paddle_x = pygame.mouse.get_pos()
        self.rect.x = paddle_x[0]
