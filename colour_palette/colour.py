import colorsys
import math


class Colour:

    MIN_RGB_VALUE = 0
    MAX_RGB_VALUE = 255

    def __init__(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def __eq__(self, o):
        if isinstance(o, Colour):
            return self.r == o.r and self.g == o.g and self.b == o.b
        return False

    def distance_to_colour(self, other_colour):
        r_distance = self.r - other_colour.r
        g_distance = self.g - other_colour.g
        b_distance = self.b - other_colour.b
        return math.sqrt(math.pow(r_distance, 2) + math.pow(g_distance, 2) + math.pow(b_distance, 2))

    def complementary_colour(self):
        r = self.MAX_RGB_VALUE - self.r
        g = self.MAX_RGB_VALUE - self.g
        b = self.MAX_RGB_VALUE - self.b
        return Colour(r, g, b)

    def triadic_colours(self):
        colours = []
        traidic_colour_1 = Colour(self.g, self.b, self.r)
        traidic_colour_2 = Colour(self.b, self.r, self.g)
        colours.append(self)
        colours.append(traidic_colour_1)
        colours.append(traidic_colour_2)
        return colours

    def analogous_colours(self):
        colours = []
        colours.append(self)
        d = 30/360
        r, g, b = map(lambda x: x/255., [self.r, self.g, self.b])
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        hues = [(h+d) % 1 for d in (-d, d)]
        for hue in hues:
            r, g, b = colorsys.hls_to_rgb(hue, l, s)
            colour = Colour(int(round(r*255)),
                            int(round(g*255)),
                            int(round(b*255)))
            colours.append(colour)
        return colours

    def split_complementary(self):
        colours = []
        colours.append(self)
        complementary = self.complementary_colour()
        complementary_analogous = complementary.analogous_colours()
        complementary_analogous = [
            colour for colour in complementary_analogous
            if not colour == complementary]
        colours.extend(complementary_analogous)
        return colours
