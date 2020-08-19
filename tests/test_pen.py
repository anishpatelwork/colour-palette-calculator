from colour_palette.pen import Pen
from colour_palette.colour import Colour


def test_initialise_pen():
    colour = Colour(41, 165, 155)
    brand = "Tombow"
    name = "Sea Blue - 373"
    tombow_373 = Pen(brand, name, colour)
    assert isinstance(tombow_373, Pen)

    rgb_colour = "41,165,155"
    tombow_rgb_initialised = Pen(brand, name, rgb=rgb_colour)
    assert isinstance(tombow_rgb_initialised, Pen)
    assert tombow_373 == tombow_rgb_initialised
