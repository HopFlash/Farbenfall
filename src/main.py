""" This is the main module for the game Farbenfall.
It's development started in the GameJam "My First Game Jam: Winter 2021".
https://itch.io/jam/my-first-game-jam-winter-2021

"""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from intro import Intro
from playscene import Playscene
from fps import Fps


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
        self.screen = pygame.display.set_mode((1280, 720), flags=displayFlags)
        # window program title (perhaps later something for version management?)
        pygame.display.set_caption('Farbenfall v0.1')
        # initializing pygames clock system
        self.clock = pygame.time.Clock()
        # an dictionary of userevents to communicate between different classes and scenes
        self.eventDict = initUserEvents()

        # saving position when mouse button is down
        self.mouseClickStartPos = None
        # every scene has an own event loop
        self.sceneEventloop = None

        # TODO: react on window resizing
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.fps = Fps(self)
        self.intro = Intro(self)
        self.playfield = Playscene(self)

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
                elif event.type == self.eventDict['INTRO_CLICKED']:
                    if event.action == 'PLAY':
                        self.showGame()
                    elif event.action == 'ABOUT':
                        self.showAbout()
                if self.sceneEventloop:
                    self.sceneEventloop(event)

            self.screen.blit(self.background, (0, 0))
            self.allActiveSprites.add(self.fps)
            self.allActiveSprites.update()
            self.allActiveSprites.draw(self.screen)
            pygame.display.flip()

            # showing FPS
            self.fps.setFps(self.clock.get_fps())
            self.clock.tick(600)

    def resetScene(self):
        self.sceneEventloop = None
        self.allActiveSprites.empty()

    def showIntro(self):
        self.resetScene()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.allActiveSprites.add(self.intro)
        self.sceneEventloop = self.intro.eventloop

    def showGame(self):
        self.resetScene()
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        self.allActiveSprites.add(self.playfield)
        self.sceneEventloop = self.playfield.eventloop

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
