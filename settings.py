class GameSettings:
    def __init__(self):
        ### Store hardcoded settings here

        # Flag if the game will be in fullscreen or not
        self.full_screen = False

        # Set the background color of the game window
        self.bg_color = (36, 36, 36)

        # Set the window height and width
        self.window_height = 800
        self.window_width = 1200

        # Set the ship movement speed
        self.ship_speed = 5.1

        # Bullet Settings
        self.bullet_speed = 9.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.max_bullets = 8

        # Alien fleet settings
        self.max_aliens_per_row = 6
        self.max_aliens_rows = 4

        # Alien movement settings
        self.alien_move_speed = 2.5
        self.alien_drop_speed = 20

        # Create a flag to track whether the fleet should be moving right or left
        self.aliens_moving_right = True