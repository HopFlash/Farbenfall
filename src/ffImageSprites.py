import pygame
import utils


class FFImageSprites(pygame.sprite.Sprite):
    def __init__(self, gameobj, filename):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.gameobj = gameobj
        self.image, self.rect = utils.load_image(filename)
        self.x = self.rect.x
        self.y = self.rect.y
        self.moved = True

    def update(self):
        super().update()
        if self.moved:
            self.rect.topleft = self.x, self.y
            self.moved = False

    def resize(self, newX, newY):
        self.image = pygame.transform.scale(self.image, (newX, newY))
        self.rect = self.image.get_rect()

    def resizeProp(self, newScale):
        x = self.image.get_width()
        y = self.image.get_height()
        self.resize(round(x * newScale), round(y * newScale))

    def moveTo(self, newX, newY):
        self.x = newX
        self.y = newY
        self.moved = True
