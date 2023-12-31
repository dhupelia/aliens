import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from settings import GameSettings
from ship import Ship
from enemy import Alien
from bullet import Bullet

class Aliens:
    ## Class to manage the game assets and behaviors

    def __init__(self):
        ## Init the game
        pygame.init()

        self.settings = GameSettings()

        # Set a clock for fps
        self.clock = pygame.time.Clock()

        # Create the window at fullscreen or a set resolution based upon the settings file boolean
        if self.settings.full_screen == True:
            # Run in fullscreen and grab the fullscreen width and height sizes for future use
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))

        # Set the background color of the game window
        self.bg_color = self.settings.bg_color

        # Caption the game window
        pygame.display.set_caption("--- Cat vs Aliens ---")

        # Create the ship instance
        self.ship = Ship(self)

        # Create a container for a group of enemies and spawn the enemies
        self.enemies = pygame.sprite.Group()
        self._create_fleet()

        # Create a container for a group of bullets
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        ## Main Game Loop
        while True:
            # Poll for kb/m events
            self._check_events()

            # Update the ship each frame
            self.ship.update()

            # Update the bullets each frame
            self._update_bullets()

            # Draw the screen
            self._update_screen()

            # Tick the frame counter to try and remain a constant 60
            self.clock.tick(60)


    def _update_bullets(self):
        # Update the bullets each frame
        self.bullets.update()

        # Delete any bullets that left the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_events(self):
        # Poll and handle kb/m events
        for event in pygame.event.get():
            # Quit gracefully if the user enters 'q' or any other exit command
            if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_q)):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Disable up/down movement by ignoring the keydown event of up/down arrows, thereby never setting the up or down flags to True
        # elif event.key == pygame.K_UP:
        #    self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #    self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.max_bullets:
                self._fire_bullet()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _create_fleet(self):
        # Make an alien
        alien = Alien(self)
        self.enemies.add(alien)

        # Determine the width and height of each alien to space them out
        self.alien_width = alien.rect.width
        self.alien_height = alien.rect.width

        # Determine the size of the Sprite for spacing out purposes
        alien_width, alien_height = alien.rect.size

        # Setup tracking variables for the position of each alien we need to create
        current_x = alien_width
        current_y = alien_height

        # Setup counters for how many rows and columns of aliens we need
        row_counter = 0

        # Used nested while loops to create multiple rows of aliens
        while row_counter < self.settings.max_aliens_rows:
            # Increment the row counter
            row_counter += 1

            # Setup a counter to track how many ships were created per row
            ship_counter = 0

            # Create a row of spaced out aliens (hahaha)
            while ship_counter < self.settings.max_aliens_per_row:
                # Increment the ship counter
                ship_counter += 1

                # Create the next alien
                self._create_alien(current_x, current_y)

                # Set the next alien's starting X position to 2 times the width of one alien (so they're evenly spaced)
                # NOTE: this spacing is arbitrary (could be whatever)
                current_x += 2 * self.alien_width
            
            # Set the next row of aliens starting Y position to 2 times the width of one alien (so they're evenly spaced)
            # NOTE: this spacing is arbitrary (could be whatever)
            current_y += 2 * self.alien_height


    def _create_alien(self, x_position, y_position):
        ### Create an alien and place it at the specified position

        # Instantiate a new alien
        new_alien = Alien(self)

        # Set the new alien's x position
        new_alien.x = x_position
        new_alien.rect.x = x_position

        # Set the new alien's y position
        new_alien.y = y_position
        new_alien.rect.y = y_position

        # Add the alien to the alien sprite group
        self.enemies.add(new_alien)


    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        # Draw the screen
        self.screen.fill(self.bg_color)

        # Draw the ship each frame
        self.ship.blitme()

        # Draw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draw the enemies
        self.enemies.draw(self.screen)

        # Flip the screen buffer
        pygame.display.flip()
 
if __name__ == '__main__':
    # Make a game instance and run the game
    game = Aliens()
    game.run_game()
