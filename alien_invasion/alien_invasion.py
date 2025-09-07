import sys
import pygame

class AlienInvasion:
    """Overall class to manage all game assets and behaviour"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Main loop to run the game"""
        while True:
            # watch for keyboard and mouse actions.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the geme.
    ai = AlienInvasion()
    ai.run_game()