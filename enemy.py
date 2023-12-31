import pygame
from pygame.sprite import Sprite
from settings import GameSettings

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

        # Retrieve the game settings
        self.settings = game.settings
    
    def update(self):
        # Update the aliens each tick

        # Move the alien to the right or left depending upon the current fleet direciton
        if self.settings.aliens_moving_right == True:
            self.x += self.settings.alien_move_speed
            self.rect.x = self.x
        else:
            self.x -= self.settings.alien_move_speed
            self.rect.x = self.x

    def check_edges(self):
        # Track whether the aliens have reached the edge of the screen

        # Get the screen rect dimensions
        screen_rect = self.screen.get_rect()

        # Check if this alien instance's x position has gone past the edge of the screen on either side
        if (self.rect.right >= screen_rect.right) or (self.rect.left <= 0):
            return True
