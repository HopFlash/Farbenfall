from ffImageSprites import FFImageSprites


class Waterfall(FFImageSprites):
    def __init__(self, gameobj, color, filename, *groups):
        super().__init__(gameobj, filename, *groups)
        self.color = color
