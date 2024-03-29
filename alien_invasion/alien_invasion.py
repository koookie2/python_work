import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from score_board import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Start Alien Invasion in an inactive state.
        self.game_active = False

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Full-screen display
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Make the Play button.
        self.play_button = Button(self, "Play")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.score_board = Scoreboard(self)

        # Create the game objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.current_drop = 0

        self.difficulty = None
    
    def _create_fleet(self):
        """Create the fleet of alien."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien_width, alien_height = Alien(self).rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
        
            # Reset x value and increment y_value
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.rect.move_ip(x_position, y_position)
        new_alien.x = x_position
        self.aliens.add(new_alien)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(self.play_button.rect.collidepoint(pygame.mouse.get_pos()))

            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pressed=False, key_pressed=False):
        """Start a new game when the player clicks "Play.\""""
        if (mouse_pressed or key_pressed) and not self.game_active and self.difficulty:
                # Reset the game statistics.
                self.settings.initialize_dynamic_settings(self.difficulty)
                self.difficulty = None

                self.stats.reset_stat()
                self.score_board.prep_score()
                self.score_board.prep_level()
                self.score_board.prep_ships()

                self.game_active = True

                # Get rid of any remaining bullets and aliens.
                self.bullets.empty()
                self.aliens.empty()

                # Create a new fleet and center the ship.
                self._create_fleet()
                self.ship.center_ship()

                # Hide the mouse curseor.
                pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()
        
        if event.key == pygame.K_e:
            self.difficulty = 1
        if event.key == pygame.K_m:
            self.difficulty = 2
        if event.key == pygame.K_h:
            self.difficulty = 4

        if event.key == pygame.K_p:
            self._check_play_button(key_pressed=True)

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the "Bullets Group.\""""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
        self._delete_bullets()
        self._check_bullet_alien_collision()

    def _delete_bullets(self):
        """Get rid of bullets that have disappeared."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self._delete_aliens(collisions.values())
            self.score_board.prep_score()
            self.score_board.check_high_score()
        
        self._check_alien_amount()

    def _delete_aliens(self, collisions):
        """Get rid of aliens that have been shot."""
        for alien in collisions.values():
            self.stats.score += self.settings.alien_points * len(alien)

    def _check_alien_amount(self):
        """If there are no aliens, rebuild the fleet and increment the level."""
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.score_board.prep_level()
    
    def _update_aliens(self):
        """Check if fleet is at an edge, then update positions."""
        on_edge = False
        if self._check_fleet_edges():
            if self.current_drop < self.settings.fleet_drop:
                self._drop_fleet()
                on_edge = True
            else:
                self._change_fleet_direction()
                on_edge = False
        if not on_edge:
            self.aliens.update()
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                return True
                        
    def _drop_fleet(self):
        """Drop the entire fleet."""
        for alien in self.aliens.sprites():
            alien.rect.y += 1
        self.current_drop += 1
    
    def _change_fleet_direction(self):
        """Change the entire fleet's direction"""
        self.current_drop = 0
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 1:
            # Decrement "ship_left", and update scoreboard.
            self.stats.ships_left -= 1
            self.score_board.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self.ship.center_ship()
            self._create_fleet()
            self.current_drop = 0
            self.settings.fleet_direction = 1

            # Pause
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip them to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.score_board.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    AlienInvasion().run_game()