import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and get its starting position."""        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion/alien.bmp')
        self.rect = self.image.get_rect()

        # idk to add this
        # # Store a float for the ship's exact horizontal position.
        # self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        return (self.rect.right >= self.screen.get_rect().right) or (self.rect.left <= 0) # can be replaced with "self.screen_rect.left"

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

# Example 13-1
class Star(Sprite):
    """A class to manage a single star."""

    def __init__(self, ai_game):
        """Initialize the star and get its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

# Example 13-3
class Raindrop(Sprite):
    """A class to manage a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and get its starting position."""
        self.settings = ai_game.settings
        
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the ship's exact horizontal position.
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        return (self.rect.right >= self.screen.get_rect().right) or (self.rect.left <= 0) # can be replaced with "self.screen_rect.left"

    def update(self):
        """Move the alien right or left."""
        # self.y += 1
        self.rect.y += 1