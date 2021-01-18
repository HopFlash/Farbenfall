import pygame
from pygame.constants import SRCALPHA
from pygame.sprite import AbstractGroup


class Intro(pygame.sprite.Sprite):
    def __init__(self, gameobj, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj

        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup = pygame.sprite.RenderPlain()

        self.introTitle = IntroTitle(gameobj, self, self.myGroup)
        self.introButtons = [
            IntroPlayButton(self.gameobj, self, 'Play', self.myGroup),
            IntroAboutButton(self.gameobj, self, 'About', self.myGroup),
            IntroQuitButton(self.gameobj, self, 'Quit', self.myGroup)
        ]
        for i, iButton in enumerate(self.introButtons):
            iButton.rect.top = 500
            iButton.rect.left = 400 + i * 150

    def update(self, *args, **kwargs) -> None:
        self.image = pygame.Surface(self.gameobj.screen.get_size())
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.myGroup.update()
        self.myGroup.draw(self.image)

    def checkMouseClick(self, event):
        mouseClickPos = pygame.mouse.get_pos()
        for iButton in self.introButtons:
            if iButton.rect.collidepoint(mouseClickPos):
                iButton.clicked(event)


class IntroTitle(pygame.sprite.Sprite):
    """
    docstring
    """
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

    def __init__(self, gameobj, parent, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj
        self.parent = parent
        self.font = pygame.font.Font('./data/BRLNSB.TTF', 128)

        introTextImages = []
        textOffset = 0
        introTextHeight = 0
        for i, c in enumerate('Farbenfall'):
            charColor = self.colorList[i]
            charImage = self.font.render(c, True, charColor)
            introTextImages.append((textOffset, charImage))
            textOffset = textOffset + charImage.get_width() + 3
            if charImage.get_height() > introTextHeight:
                introTextHeight = charImage.get_height()
        introTextWidth = textOffset

        self.image = pygame.Surface((introTextWidth, introTextHeight), flags=SRCALPHA)
        self.rect = self.image.get_rect()
        for charOffsetX, textImage in introTextImages:
            self.image.blit(textImage, (charOffsetX, 0))
        self.rect.centerx = round(self.parent.rect.centerx)
        self.rect.centery = round(self.parent.rect.centery)

    def update(self):
        self.rect.centerx = round(self.parent.rect.centerx)
        self.rect.centery = round(self.parent.rect.centery)


class IntroButton(pygame.sprite.Sprite):
    def __init__(self, gameobj, parent, text, *groups: AbstractGroup):
        super().__init__(*groups)
        self.gameobj = gameobj
        self.parent = parent
        self.text = text

        self.font = pygame.font.Font(None, 40)

        self.image = pygame.Surface((100, 50), flags=SRCALPHA)
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        textImage = self.font.render(self.text, True, (255, 255, 0))
        textRect = textImage.get_rect()
        textRect.center = self.rect.center
        self.image.blit(textImage, textRect)


class IntroPlayButton(IntroButton):
    def clicked(self, event):
        playEvent = pygame.event.Event(self.gameobj.eventDict['INTRO_CLICKED'], action='PLAY')
        pygame.event.post(playEvent)


class IntroAboutButton(IntroButton):
    def clicked(self, event):
        playEvent = pygame.event.Event(self.gameobj.eventDict['INTRO_CLICKED'], action='ABOUT')
        pygame.event.post(playEvent)


class IntroQuitButton(IntroButton):
    def clicked(self, event):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
