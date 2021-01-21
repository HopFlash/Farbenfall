import pygame
from pygame.sprite import AbstractGroup

import utils


class FFImageSprites(pygame.sprite.Sprite):
    def __init__(self, gameobj, filename, *groups: AbstractGroup):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, *groups)
        self.gameobj = gameobj
        self.image, self.rect = utils.load_image(filename)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = self.rect.x
        self.y = self.rect.y
        self.moved = True

    def update(self):
        super().update()
        if self.moved:
            self.rect.topleft = self.x, self.y
            self.moved = False

    def resize(self, newX, newY):
        # remember the position
        x, y = self.rect.center
        self.image = pygame.transform.scale(self.image, (newX, newY))
        # get new scaled rectangle at the same center position
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def resizeProp(self, newScale):
        x, y = self.image.get_size()
        self.resize(round(x * newScale), round(y * newScale))

    def moveTo(self, newX, newY):
        self.x = newX
        self.y = newY
        self.moved = True
