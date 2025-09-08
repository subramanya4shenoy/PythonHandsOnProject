""" A class to manage the ship """
import pygame

class Ship():
    def __init__(self, ai_game):
        """ Initialise the game variables """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship on the screen. """
        self.screen.blit(self.image, self.rect)

