class Colour:

    MIN_RGB_VALUE = 0
    MAX_RGB_VALUE = 255

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


    def __eq__(self, other):
        if isinstance(other, Colour):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return False
    
    def complementary_colour(self):
        r = self.MAX_RGB_VALUE - self.r
        g = self.MAX_RGB_VALUE - self.g
        b = self.MAX_RGB_VALUE - self.b
        return Colour(r, g, b)