class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop = 1000

        # How quickly the game speeds up
        self.speed_up_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
    
    def initialize_dynamic_settings(self, difficulty_level):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5 * difficulty_level
        self.bullet_speed = 2.5 * difficulty_level
        self.alien_speed = 1.0 * difficulty_level
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Initialize speed settings."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points *= int(self.alien_points * self.score_scale)