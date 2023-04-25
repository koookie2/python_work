class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_status()
    
    def reset_status(self):
        """Initialize statistics that can change during a game"""
        self.ships_left = self.settings.ship_limit