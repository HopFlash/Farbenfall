""" This is the main module for the game Farbenfall.
It's development started in the GameJam "My First Game Jam: Winter 2021".
https://itch.io/jam/my-first-game-jam-winter-2021

"""
import os
import pygame
from pygame.locals import QUIT, RLEACCEL, KEYDOWN, K_ESCAPE


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image, image.get_rect()

def load_image_Colorkey(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Intro(object):
    """
    docstring
    """

    def __init__(self, gameobj):
        self.show = True
        self.gameobj = gameobj
        self.font = pygame.font.Font(None, 128)
        self.text = self.font.render('Farbenfall',  True, (200, 50, 0))
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
            self.introTextImages.append( (textOffset, charImage) )
            textOffset = textOffset + charImage.get_width() + 3
        self.introTextLength = textOffset


    def render(self):
        background = pygame.Surface(self.gameobj.screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        
        for charOffsetX, textImage in self.introTextImages:
            textpos = textImage.get_rect(x=background.get_width()/2 - self.introTextLength/2 + charOffsetX, centery=background.get_height()/2)
            background.blit(textImage, textpos)

        self.gameobj.screen.blit(background, (0, 0))

class ffSprites(pygame.sprite.Sprite):
    def __init__(self, gameobj, filename='waterfall.png'):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.gameobj = gameobj
        self.image, self.rect = load_image(filename)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10

    def changecolor(self, newcolor):
        pxarray = pygame.PixelArray(self.image)
        pxarray.replace((76, 69, 207), newcolor, distance=0)
        self.image = pxarray.make_surface()

    def resize(self, newX, newY):
        self.image = pygame.transform.scale(self.image, (newX, newY))

    def resizeProp(self, newScale):
        x = self.image.get_width()
        y = self.image.get_height()
        self.resize(round(x*newScale), round(y*newScale))


class Waterfall(ffSprites):
    pass


class Sponge(ffSprites):
    pass


class Game(object):
    """
    docstring
    """

    def __init__(self):
        pygame.init()
#        displayFlags = pygame.FULLSCREEN | pygame.RESIZABLE
        displayFlags = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((800, 600), flags=displayFlags)
        pygame.display.set_caption('Farbenfall v0.1')
        self.clock = pygame.time.Clock()

        self.intro = Intro(self)

        sponge = Sponge(self, 'sponge.png')
        sponge.resizeProp(0.25)
#        w_generic = Waterfall(self)
        w_blue = Waterfall(self, 'waterfall_blue.png')
        w_blue.rect.topleft = 20, 20
        w_blue.resizeProp(0.5)
        w_green = Waterfall(self, 'waterfall_green.png')
        w_green.rect.topleft = 170, 20
        w_green.resizeProp(0.5)
        w_red = Waterfall(self, 'waterfall_red.png')
        w_red.rect.topleft = 320, 20
        w_red.resizeProp(0.5)
        sponge.changecolor((10, 210, 10))

        self.allSprites = pygame.sprite.RenderPlain((sponge, w_blue, w_green, w_red))

    def run(self):

        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

        while 1:
            self.intro.render()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    myGame = Game()
    myGame.run()
