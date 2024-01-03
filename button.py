import pygame.font

class Button:
    """ Define buttons and corresponding behaviors """

    def __init__(self, game, msg):
        # Initiatlize the button to draw within the game screen
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Set the button dimensions and properties
        self.width = 200
        self.height = 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Buld the button's rect (surface) and position it in the middle of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Add the requested message to the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Render the requested message in a font onto an image and draw it in the center of the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Color the button and draw it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
