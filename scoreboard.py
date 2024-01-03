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


    def prep_scoreboard(self):
        # Convert the current score into a string
        score_string = str(self.stats.score)

        # Render the image of the string
        self.score_image = self.font.render(score_string, True, self.text_color, self.settings.bg_color)

        # Display the score at the top-right of the screen window with a small offset of 20x20 to get off the edge of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        # Draw the scoreboard rect
        self.screen.blit(self.score_image, self.score_rect)
