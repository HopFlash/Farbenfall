import pygame
import ffImageSprites


class Block(ffImageSprites.FFImageSprites):
    def __init__(self, gameobj, filename):
        super().__init__(gameobj, filename)
        self.attached = False

    def changecolor(self, newcolor):
        pxarray = pygame.PixelArray(self.image)
        pxarray.replace((255, 255, 255), newcolor, distance=0)
        self.image = pxarray.make_surface()

    def update(self):
        super().update()
        if self.attached:
            if pygame.mouse.get_focused():
                newX, newY = pygame.mouse.get_pos()
                self.rect.center = newX, newY

    def attachToMouse(self, attach=True):
        self.attached = attach
