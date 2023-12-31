import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ### Define an alien object and its behaviors and state

    def __init__(self, game):
        # Load the alien and set its starting position

        # Initialize the Sprite
        super().__init__()
        self.screen = game.screen

        # Load the image and define its rect based upon the image's dimensions
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.rect = self.image.get_rect()

        # Set the alien start position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position in a float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

