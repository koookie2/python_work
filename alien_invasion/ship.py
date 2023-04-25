import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and get its starting position."""
        self.settings = ai_game.settings
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien_invasion/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
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
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

# Example 12-2
class Mario:
    """A class to manage mario."""
    
    def __init__(self, ai_game):
        """Initialize mario and his starting position"""
        self.ai_screen = ai_game.screen
        self.ai_screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('alien_invasion/mario.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.center = self.ai_screen_rect.center

    def blitme(self):
        """Draw mario at his current location"""
        self.ai_screen.blit(self.image, self.rect)

# Example 12-4
class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initialize the rocket and its starting position"""
        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('alien_invasion/mario.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False        

    def update(self):
        """Update the rocket's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self x.
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)

# Example 12-6
class SidewaysShip:
    """A class to manage the sideways ship."""

    def __init__(self, ai_game):
        """Initialize the ship and get its starting position."""
        self.settings = ai_game.settings
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('alien_invasion/sideways_ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ships's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)