import pygame

from ffImageSprites import FFImageSprites


class Block(FFImageSprites):
    def __init__(self, gameobj, filename, *groups):
        super().__init__(gameobj, filename, *groups)
        self.attached = False
        self.referencePxarray = pygame.PixelArray(self.image)

    def changecolor(self, newcolor):
        pxarray = pygame.PixelArray(self.referencePxarray.make_surface())
        pxarray.replace((255, 255, 255), newcolor, distance=0)
        width, height = self.image.get_size()
        self.image = pxarray.surface
        self.resize(width, height)

    def update(self):
        super().update()
        if self.attached:
            if pygame.mouse.get_focused():
                newX, newY = pygame.mouse.get_pos()
                self.rect.center = newX, newY

    def attachToMouse(self, attach=True):
        self.attached = attach
