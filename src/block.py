import pygame
import ffSprites


class Block(ffSprites.FFSprites):

    def changecolor(self, newcolor):
        pxarray = pygame.PixelArray(self.image)
        pxarray.replace((255, 255, 255), newcolor, distance=0)
        self.image = pxarray.make_surface()

    def update(self):
        super().update()
        if pygame.mouse.get_focused():
            newX, newY = pygame.mouse.get_pos()
            self.rect.center = newX, newY
