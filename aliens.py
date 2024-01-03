import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from time import sleep

from settings import GameSettings
from ship import Ship
from enemy import Alien
from bullet import Bullet
from stats import GameStats
from button import Button
from scoreboard import Scoreboard

class Aliens:
    ## Class to manage the game assets and behaviors

    def __init__(self):
        ## Init the game
        pygame.init()

        # Grab the game settings
        self.settings = GameSettings()

        # Setup the game stats
        self.stats = GameStats(self)

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

        # Create the play button (doing this in init since we only need the one button)
        self.play_button = Button(self, "Play")

        # Create the scoreboard
        self.board = Scoreboard(self)

    def run_game(self):
        ## Main Game Loop
        while True:
            # Poll for kb/m events
            self._check_events()

            # Check if we're still in an active game loop and only update ships/bullets/aliens if so
            if self.stats.game_active == True:
                # Update the ship each frame
                self.ship.update()

                # Update the bullets each frame
                self._update_bullets()

                # Update the aliens each frame
                self._update_aliens()

            # Draw the screen
            self._update_screen()

            # Tick the frame counter to try and remain a constant 60
            self.clock.tick(60)


    def _update_aliens(self):
        # Update the aliens each frame
        self._check_fleet_edges()
        self._check_fleet_bottom()
        self.enemies.update()

        # Check for collision between the aliens and the player ship
        if (pygame.sprite.spritecollideany(self.ship, self.enemies)):
            self._ship_hit()

        # Check if we ran out of aliens and start the next wave
        if len(self.enemies) < 1:
             # Clear out the bullets
            self.bullets.empty()

            # Make the game harder for the next wave by speeding up the ships each round
            self.settings.increase_speed()

            # Increase the point value for the next round
            self.settings.alien_points_scale = self.settings.alien_points_scale * self.settings.alien_points_multiplier
            print(self.settings.alien_points_scale)
            print(self.settings.alien_points_multiplier)

            # Reset the game dynamic stats and settings
            self.settings.initialize_dynamic_settings(False)
   
            # Setup a new fleet
            self._create_fleet()

            # Move the ship back to center
            self.ship.center_ship()
            
            # Pause the game for a moment to let the player gather their thoughts
            sleep(0.5)

    def _ship_hit(self):
        # Handle a ship being hit

        # Decrement the ships remaining
        self.stats.ships_remaining -= 1

        # Clear out the bullets
        self.bullets.empty()

        # Check if we're out of lives else reset the fleet and ship
        if self.stats.ships_remaining <= 0:
            # Out of lives!  Disable the game
            self.stats.game_active = False

            # Bring back the mouse cursor so the player can interact with UI again
            pygame.mouse.set_visible(True)

            # Reset the game dynamic stats and settings
            self.settings.initialize_dynamic_settings()
        else:
            # Clear out the aliens
            self.enemies.empty()

            # Setup a new fleet
            self._create_fleet()

            # Move the ship back to center
            self.ship.center_ship()

            # Pause the game for a moment to let the player gather their thoughts
            sleep(0.5)


    def _check_fleet_bottom(self):
        # Get the window/screen width and height
        width, height = pygame.display.get_surface().get_size()

        # Loop through all of the alien objects
        for alien in self.enemies.sprites():
            # If the alien's rect has reached the bottom edge call it the same as a hit ship
            if alien.rect.bottom >= height:
                self._ship_hit()
                break


    def _check_fleet_edges(self):
        # Set a flag to track whether we should switch directions
        switch_direction = False

        # Check if the fleet needs to be dropped and switched direciton
        for x in self.enemies.sprites():
            if x.check_edges() == True:
                switch_direction = True

        # If we decided to switch directions, move forward and reset the toggle
        if switch_direction == True:
            self._change_fleet_direction()
            switch_direction = False


    def _change_fleet_direction(self):
        # Toggle the right/left movement boolean
        game.settings.aliens_moving_right = not game.settings.aliens_moving_right

        # Loop through all of the ships
        for x in self.enemies.sprites():
            # Drop each ship's y position by the settings drop speed
            x.rect.y += self.settings.alien_drop_speed



    def _update_bullets(self):
        # Update the bullets each frame
        self.bullets.update()

        # Delete any bullets that left the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullet hits on aliens and delete any that did
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        # Add points for any killed aliens this tick
        if collisions:
            self.stats.score += (self.settings.alien_points * self.settings.alien_points_scale)
            print(self.stats.score)


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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.stats.game_active == False:
                    position = pygame.mouse.get_pos()
                    self._check_play_button(position)


    def _check_play_button(self, position):
        # Check if the mouse position was on the play button when clicked
        if self.play_button.rect.collidepoint(position):
            # Set the game active now
            self.stats.game_active = True

            # Reset the stats
            self.stats.reset_stats()

            # Reset the fleet and bullets
            self.bullets.empty()
            self.enemies.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor since the game is starting
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        if self.stats.game_active == True:
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
        if self.stats.game_active == True:
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
        self.alien_height = alien.rect.height

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
            
            # Reset the x position for the next row to start back at the left again
            current_x = alien_width

            # Set the next row of aliens starting Y position to 2 times the width of one alien (so they're evenly spaced)
            # NOTE: this spacing is arbitrary (could be whatever)
            current_y += 2 * self.alien_height

            # Reset the ship counter for the next row of aliens
            ship_counter = 0


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

        # Debug statement to record each alien being created
        # print(f"Alien # {len(self.enemies)}:   {x_position}, {y_position}")

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

        # Draw the play button if the game isn't currently active
        if self.stats.game_active == False:
            self.play_button.draw_button()

        # Draw the scoreboard
        self.board.show_score()

        # Flip the screen buffer
        pygame.display.flip()
 
if __name__ == '__main__':
    # Make a game instance and run the game
    game = Aliens()
    game.run_game()
