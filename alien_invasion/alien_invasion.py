import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage all game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Main loop to run the game"""
        while True:
            # watch for keyboard and mouse actions.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass of the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the geme.
    ai = AlienInvasion()
    ai.run_game()