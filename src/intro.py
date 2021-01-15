import pygame


class Intro(object):
    """
    docstring
    """

    def __init__(self, gameobj):
        self.show = True
        self.gameobj = gameobj
        self.font = pygame.font.Font(None, 128)
        self.text = self.font.render('Farbenfall', True, (200, 50, 0))
        self.textStr = 'Farbenfall'
        colorList = [
            (148, 0, 211),
            (148, 0, 211),
            (75, 0, 130),
            (0, 0, 255),
            (0, 255, 0),
            (0, 255, 0),
            (255, 255, 0),
            (255, 127, 0),
            (255, 0, 0),
            (255, 0, 0)
        ]
        self.introTextImages = []
        textOffset = 0
        for i, c in enumerate(self.textStr):
            charColor = colorList[i]
            charImage = self.font.render(c, True, charColor)
            self.introTextImages.append((textOffset, charImage))
            textOffset = textOffset + charImage.get_width() + 3
        self.introTextLength = textOffset

    def render(self):
        background = pygame.Surface(self.gameobj.screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))

        for charOffsetX, textImage in self.introTextImages:
            textpos = textImage.get_rect(x=background.get_width() / 2 - self.introTextLength / 2 + charOffsetX,
                                         centery=background.get_height() / 2)
            background.blit(textImage, textpos)

        self.gameobj.screen.blit(background, (0, 0))
