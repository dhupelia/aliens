import pygame

class Ship:
    ### Manage the ship object and behaviors

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        # Load the ship image and get its rect
        #self.image = pygame.image.load('DurrrSpaceShip.png')
        self.image = pygame.image.load('cat.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Create variables to track the current x and y position of this ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Set flags for tracking whether a key is held down for continuous motion
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        ### Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if (self.moving_right == True) and (self.rect.right < self.screen_rect.right):
            self.rect.x += self.settings.ship_speed
        elif (self.moving_left == True) and (self.rect.left > self.screen_rect.left):
            self.rect.x -= self.settings.ship_speed
        elif (self.moving_up == True) and (self.rect.top > self.screen_rect.top):
            self.rect.y -= self.settings.ship_speed
        elif (self.moving_down == True) and (self.rect.bottom < self.screen_rect.bottom):
            self.rect.y += self.settings.ship_speed