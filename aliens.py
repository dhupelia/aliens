import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from settings import GameSettings
from ship import Ship

class Aliens:
    ## Class to manage the game assets and behaviors

    def __init__(self):
        ## Init the game
        pygame.init()

        self.settings = GameSettings()

        # Set a clock for fps
        self.clock = pygame.time.Clock()

        # Create the window at a set resolution
        self.screen = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))

        # Set the background color of the game window
        self.bg_color = self.settings.bg_color

        # Caption the game window
        pygame.display.set_caption("Aliens!")

        # Create the ship instance
        self.ship = Ship(self)


    def run_game(self):
        ## Main Game Loop
        while True:
            # Poll for kb/m events
            self._check_events()

            # Update the ship each frame
            self.ship.update()

            # Draw the screen
            self._update_screen()

            # Tick the frame counter to try and remain a constant 60
            self.clock.tick(60)


    def _check_events(self):
        # Poll and handle kb/m events
        for event in pygame.event.get():
            # Quit gracefully if the user enters 'q' or any other exit command
            if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and event.key == pygame.K_q):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        # Draw the screen
        self.screen.fill(self.bg_color)

        # Draw the ship each frame
        self.ship.blitme()
        
        # Flip the screen buffer
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    game = Aliens()
    game.run_game()
