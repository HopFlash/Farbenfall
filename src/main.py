""" This is the main module for the game Farbenfall.
It's development started in the GameJam "My First Game Jam: Winter 2021".
https://itch.io/jam/my-first-game-jam-winter-2021

"""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

import intro
import block
import waterfall


def initUserEvents():
    eventDict = {
        'INTRO_CLICKED': pygame.event.custom_type(),
    }
    return eventDict


class Game(object):
    """
    docstring
    """

    def __init__(self):
        # initializing the pygame engine
        pygame.init()
        #        displayFlags = pygame.FULLSCREEN | pygame.RESIZABLE
        # game in window mode and resizeable (later fullscreen mode too)
        displayFlags = pygame.RESIZABLE
        # the resolution of 800x600 will only be the base and reference window size (perhaps a 16:9 would be better?)
        # when resizing the window or using fullscreen in monitor's native mode the sprite sizes and positioning need
        # to be automatically adjusted
        self.screen = pygame.display.set_mode((800, 600), flags=displayFlags)
        # window program title (perhaps later something for version management?)
        pygame.display.set_caption('Farbenfall v0.1')
        # initializing pygames clock system
        self.clock = pygame.time.Clock()
        # an dictionary of userevents to communicate between different classes and scenes
        self.eventDict = initUserEvents()

        # scenes can have a function to check for mouse clicks like button clicks (see event loop)
        self.checkMouseClick = None
        # saving position when mouse button is down
        self.mouseClickStartPos = None

        # TODO: react on window resizing
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.intro = intro.Intro(self)

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

        self.allGameSprites = pygame.sprite.RenderPlain((colorBlock, w_blue, w_green, w_red))

        self.allActiveSprites = pygame.sprite.RenderPlain()

    def run(self):
        self.showIntro()

        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseClickStartPos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.checkMouseClick:
                        self.checkMouseClick(event)
                elif event.type == self.eventDict['INTRO_CLICKED']:
                    if event.action == 'PLAY':
                        self.showGame()
                    elif event.action == 'ABOUT':
                        self.showAbout()

            self.screen.blit(self.background, (0, 0))
            self.allActiveSprites.update()
            self.allActiveSprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def resetScene(self):
        self.checkMouseClick = None
        self.allActiveSprites.empty()

    def showIntro(self):
        self.resetScene()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.allActiveSprites.add(self.intro)
        self.checkMouseClick = self.intro.checkMouseClick

    def showGame(self):
        self.resetScene()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        self.allActiveSprites = self.allGameSprites

    def showAbout(self):
        self.resetScene()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # self.allActiveSprites = self.allGameSprites

    def quitGame(self):
        self.resetScene()
        exit()


if __name__ == "__main__":
    myGame = Game()
    myGame.run()
