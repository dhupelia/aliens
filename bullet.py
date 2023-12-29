import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ### Define a bullet and its behaviors
    def __init__(self, game):
        # Create a bullet at the ship's current position
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then update it right away to the correct position at the mid-top of the game's ship object
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's position as a float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # Move the bullet up the screen each tick (remember up and down are flipped due to 0,0 start at the top-left
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
