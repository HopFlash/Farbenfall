import pygame
from pygame.sprite import AbstractGroup


class Fps(pygame.sprite.Sprite):
    def __init__(self, gameobj, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj

        self.font = pygame.font.Font(None, 32)

        self.fpsValueStr = "-1"
        self.update()

    def update(self):
        self.image = self.font.render(self.fpsValueStr, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 10)

    def setFps(self, value: float):
        self.fpsValueStr = str(round(value))
