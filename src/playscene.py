import pygame
from pygame.sprite import AbstractGroup

import block
import utils
import waterfall


class Playscene(pygame.sprite.Sprite):
    def __init__(self, gameobj, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj

        # loading background
        self.image, self.rect = utils.load_image('background.png')
        self.backgroundImg = self.image.copy()

        self.myGroup = pygame.sprite.RenderPlain()

        self.spritesDict = {}

        colorBlock = block.Block(self, 'block.png', self.myGroup)
        colorBlock.resizeProp(0.15)
        colorBlock.moveTo(500, 500)
        self.spritesDict['block'] = colorBlock

        # the waterfall that is actual coloring the block
        self.coloringWaterfall = None

        waterfallGroup = pygame.sprite.RenderPlain()
        w_blue = waterfall.Waterfall(self, (0, 0, 255), 'waterfall_blue.png', self.myGroup, waterfallGroup)
        w_blue.moveTo(65, 100)
        w_green = waterfall.Waterfall(self, (0, 255, 0), 'waterfall_green.png', self.myGroup, waterfallGroup)
        w_green.moveTo(320, 100)
        w_red = waterfall.Waterfall(self, (255, 0, 0), 'waterfall_red.png', self.myGroup, waterfallGroup)
        w_red.moveTo(570, 100)

        self.spritesDict['waterfalls'] = [w_blue, w_green, w_red]
        self.spritesDict['waterfallGroup'] = waterfallGroup

    def update(self, *args, **kwargs) -> None:
        self.myGroup.update()
        # background
        self.myGroup.clear(self.image, self.backgroundImg)
        # all sprites
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
        colorblock = self.spritesDict['block']
        if self.coloringWaterfall:
            # calculate new color
            # take waterfall color and the color step depending on intensity
            # add this color to the old with additive (?) method
            colorblock.changecolor(self.coloringWaterfall.color)
        else:
            colorblock.waterfallTime = 0
