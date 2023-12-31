from settings import GameSettings

class GameStats:
    ### Track game statistics

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_remaining = self.settings.ship_limit