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

    # default moveTo moves to new topleft position
    def moveTo(self, newX, newY):
        self.moveToTopLeft(newX, newY)

    # move to new topleft position
    def moveToTopLeft(self, newX, newY):
        # calculate the difference to move it
        moveX = newX - self.rect.x
        moveY = newY - self.rect.y
        self.rect.move_ip(moveX, moveY)

    # move to new center position
    def moveToCenter(self, newX, newY):
        # calculate the difference to move it
        moveX = newX - self.rect.centerx
        moveY = newY - self.rect.centery
        self.rect.move_ip(moveX, moveY)
