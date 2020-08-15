import colorsys


class Colour:

    MIN_RGB_VALUE = 0
    MAX_RGB_VALUE = 255

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, o):
        if isinstance(o, Colour):
            return self.r == o.r and self.g == o.g and self.b == o.b
        return False

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
            colours.append(Colour(int(round(r*255)), int(round(g*255)), int(round(b*255))))
        return colours
