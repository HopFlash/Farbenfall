import pygame
from pygame.sprite import AbstractGroup

import block
import waterfall


class Playscene(pygame.sprite.Sprite):
    def __init__(self, gameobj, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj

        # background
        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup = pygame.sprite.RenderPlain()

        self.spritesDict = {}

        colorBlock = block.Block(self, 'block.png', self.myGroup)
        colorBlock.resizeProp(0.15)
        colorBlock.moveTo(300, 300)
        self.spritesDict['block'] = colorBlock

        # the waterfall that is actual coloring the block
        self.coloringWaterfall = None

        waterfallGroup = pygame.sprite.RenderPlain()
        w_blue = waterfall.Waterfall(self, (0, 0, 255), 'waterfall_blue.png', self.myGroup, waterfallGroup)
        w_blue.resizeProp(0.5)
        w_blue.moveTo(20, 0)
        w_green = waterfall.Waterfall(self, (0, 255, 0), 'waterfall_green.png', self.myGroup, waterfallGroup)
        w_green.resizeProp(0.5)
        w_green.moveTo(170, 0)
        w_red = waterfall.Waterfall(self, (255, 0, 0), 'waterfall_red.png', self.myGroup, waterfallGroup)
        w_red.resizeProp(0.5)
        w_red.moveTo(320, 0)

        self.spritesDict['waterfalls'] = [w_blue, w_green, w_red]
        self.spritesDict['waterfallGroup'] = waterfallGroup

    def update(self, *args, **kwargs) -> None:
        # background
        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup.update()
        self.myGroup.draw(self.image)

        self.checkBlockWaterfallCollisions()
        self.updateBlockColoring()

    def eventloop(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.checkMouseClick()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.spritesDict['block'].attached = False

    def checkMouseClick(self):
        mouseClickPos = pygame.mouse.get_pos()
        colorblock = self.spritesDict['block']
        if colorblock.rect.collidepoint(mouseClickPos):
            colorblock.attached = True

    def checkBlockWaterfallCollisions(self):
        colorblock = self.spritesDict['block']
        waterfallGroup = self.spritesDict['waterfallGroup']
        collidedWaterfall = pygame.sprite.spritecollideany(colorblock, waterfallGroup, collided=pygame.sprite.collide_mask)
        self.coloringWaterfall = collidedWaterfall

    def updateBlockColoring(self):
        if self.coloringWaterfall:
            colorblock = self.spritesDict['block']
            colorblock.changecolor(self.coloringWaterfall.color)
