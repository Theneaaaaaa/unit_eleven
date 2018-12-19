import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        # Create a surface with the correct height and width
        # Get the rect coordinates
        # Fill the surface with the correct color
