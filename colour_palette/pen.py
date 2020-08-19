from .colour import Colour


class Pen:

    def __init__(self, id, brand, name, colour=None, rgb=None):
        self.id = id
        self.brand = brand
        self.name = name
        if colour is not None:
            self.colour = colour
        elif rgb is not None:
            rgb_split = rgb.split(',')
            self.colour = Colour(rgb_split[0], rgb_split[1], rgb_split[2])

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'name': self.name,
            'colour': self.colour.serialize()
        }

    def __eq__(self, o):
        if isinstance(o, Pen):
            return self.brand == o.brand and self.name == o.name and self.colour == o.colour
        return False

    def __str__(self):
        return f'{self.brand}, {self.name}'
