from .colour import Colour


class Pen:

    def __init__(self, brand, name, colour=None, rgb=None):
        self.brand = brand
        self.name = name
        if colour is not None:
            self.colour = colour
        elif rgb is not None:
            rgb_split = rgb.split(',')
            self.colour = Colour(rgb_split[0], rgb_split[1], rgb_split[2])

    def __eq__(self, o):
        if isinstance(o, Pen):
            return self.brand == o.brand and self.name == o.name and self.colour == o.colour
        return False
