import pygame
from pygame.sprite import AbstractGroup

import block
import waterfall


class Playscene(pygame.sprite.Sprite):
    def __init__(self, gameobj, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj

        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup = pygame.sprite.RenderPlain()

        self.spritesDict = {}

        colorBlock = block.Block(self, 'block.png', self.myGroup)
#        colorBlock.changecolor((10, 210, 10))
        colorBlock.resizeProp(0.15)
        self.spritesDict['block'] = colorBlock

        w_blue = waterfall.Waterfall(self, 'waterfall_blue.png', self.myGroup)
        w_blue.moveTo(20, 20)
        w_blue.resizeProp(0.5)
        w_green = waterfall.Waterfall(self, 'waterfall_green.png', self.myGroup)
        w_green.moveTo(170, 20)
        w_green.resizeProp(0.5)
        w_red = waterfall.Waterfall(self, 'waterfall_red.png', self.myGroup)
        w_red.moveTo(320, 20)
        w_red.resizeProp(0.5)

    def update(self, *args, **kwargs) -> None:
        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup.update()
        self.myGroup.draw(self.image)

    def eventloop(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.checkMouseClick(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.spritesDict['block'].attached = False

    def checkMouseClick(self, event):
        mouseClickPos = pygame.mouse.get_pos()
        colorblock = self.spritesDict['block']
        if colorblock.rect.collidepoint(mouseClickPos):
            colorblock.attached = True

