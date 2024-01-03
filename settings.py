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

        # Set the maximum number of lives
        self.ship_limit = 3

        # Set the scale at which the speed of aliens (our difficulty) increases each wave
        self.scale_speed = 1.1

        # Set the scale at which our points should scale up per-wave
        self.alien_points_multiplier = 2

        # Set how many points each killed alien is worth in the first wave
        self.alien_points = 10

        # Initialize dynamic settings that will need to be reset each replay
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self, reset_scale = True, reset_speed = True):
        if reset_scale == True:
            # Set the scale at which the point values increase each wave for this game
            self.alien_points_scale = 1

        if reset_speed == True:
            # Alien movement settings
            self.alien_move_speed = 11.5
            self.alien_drop_speed = 25

        # Create a flag to track whether the fleet should be moving right or left
        self.aliens_moving_right = True


    def increase_speed(self):
        #self.ship_speed *= self.scale_speed
        self.alien_move_speed = self.alien_move_speed * self.scale_speed
