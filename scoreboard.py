import pygame.font

class Scoreboard:
    """ Class to track and display a scoreboard on screen """

    def __init__(self, game):
        """ Init the scorekeeping attributes """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Setup the font, color and size for the scoreboard
        self.text_color = (200, 100, 100)
        self.font = pygame.font.SysFont(None, 48)

        # Prep the initial score image
        self.prep_scoreboard()

        # Prep the enemy wave / level image
        self.prep_enemy_wave()


    def prep_enemy_wave(self):
        # Convert the current enemy wave into a string
        string = f"Level = {self.stats.enemy_wave}"
        wave_string = str(string)

        # Render the image of the string
        self.wave_image = self.font.render(wave_string, True, self.text_color, self.settings.bg_color)

        # Display the score at the top-right of the screen window with a small offset of 20x20 to get off the edge of the screen
        self.wave_rect = self.wave_image.get_rect()
        self.wave_rect.right = self.screen_rect.right - 20
        self.wave_rect.top = 20
        

    def prep_scoreboard(self):
        # Convert the current score into a string
        string = f"Score = {self.stats.score}"
        #score_string = str(self.stats.score)
        score_string = str(string)

        # Render the image of the string
        self.score_image = self.font.render(score_string, True, self.text_color, self.settings.bg_color)

        # Display the score at the top-left of the screen window with a small offset of 20x20 to get off the edge of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20


    def show_score(self):
        # Draw the scoreboard rect
        self.screen.blit(self.score_image, self.score_rect)


    def show_enemy_wave(self):
        # Draw the wave
        self.screen.blit(self.wave_image, self.wave_rect)