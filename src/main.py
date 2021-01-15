""" This is the main module for the game Farbenfall.
It's development started in the GameJam "My First Game Jam: Winter 2021".
https://itch.io/jam/my-first-game-jam-winter-2021

"""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

import intro
import block
import waterfall


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

        self.intro = intro(self)

        self.spritesDict = {}

        colorBlock = block.Block(self, 'sponge.png')
        colorBlock.changecolor((10, 210, 10))
        colorBlock.resizeProp(0.15)
        self.spritesDict['sponge'] = colorBlock

        w_blue = waterfall.Waterfall(self, 'waterfall_blue.png')
        w_blue.moveTo(20, 20)
        w_blue.resizeProp(0.5)
        w_green = waterfall.Waterfall(self, 'waterfall_green.png')
        w_green.moveTo(170, 20)
        w_green.resizeProp(0.5)
        w_red = waterfall.Waterfall(self, 'waterfall_red.png')
        w_red.moveTo(320, 20)
        w_red.resizeProp(0.5)

        self.allSprites = pygame.sprite.RenderPlain((colorBlock, w_blue, w_green, w_red))

    def run(self):

        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

        while 1:
            self.intro.render()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    myGame = Game()
    myGame.run()
