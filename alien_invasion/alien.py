import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and get its starting position."""
        self.settings = ai_game.settings
        
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
        # print(self.rect)

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