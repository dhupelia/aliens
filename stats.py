from settings import GameSettings

class GameStats:
    ### Track game statistics

    def __init__(self, game):
        self.settings = game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_remaining = self.settings.ship_limit
        self.score = 0
        self.enemy_wave = 1
