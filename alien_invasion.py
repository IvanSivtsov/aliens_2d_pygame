import sys
import pygame

class AlienInvasion:
    """Class for managing of game bahavior and resources"""

    def __init__(self):
        """Init of game and game`s resources"""
        pygame.init()
        self.bg_color = (15, 14, 48) #cosmos BG color
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Launch of game loop"""
        while True:
            #Track events from keyboard & mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)

            #Display of last draw screen
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == '__main__':
    #Create instance of class and run game
    ai = AlienInvasion()
    ai.run_game()
