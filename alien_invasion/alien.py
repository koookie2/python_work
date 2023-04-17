import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and get its starting position."""
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
        """Update the ships's position based on movement flags."""
        # The temporary attribute "x" stores where the ship should actually be,
        # since the ship will only take the integer part.
        
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: # can be replaced with "self.screen_rect.left"
            self.x -= self.settings.ship_speed
        
        # Update rect object from self x.
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)