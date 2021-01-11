""" This is the main module for the game Farbenfall.
It's development started in the GameJam "My First Game Jam: Winter 2021".
https://itch.io/jam/my-first-game-jam-winter-2021

"""

import pygame
from pygame.locals import QUIT


class Intro(object):
    """
    docstring
    """

    def __init__(self, gameobj):
        self.show = True
        self.gameobj = gameobj

    def render(self):
        background = pygame.Surface(self.gameobj.screen.get_size())
        background = background.convert()
        background.fill((150, 250, 250))
        self.gameobj.screen.blit(background, (0, 0))


class Game(object):
    """
    docstring
    """

    def __init__(self):
        pygame.init()
#        displayFlags = pygame.FULLSCREEN | pygame.RESIZABLE
        displayFlags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((800, 600), flags=displayFlags)
        pygame.display.set_caption('Farbenfall v0.1')
        self.clock = pygame.time.Clock()

        self.intro = Intro(self)

    def run(self):

        while 1:
            self.intro.render()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    myGame = Game()
    myGame.run()
