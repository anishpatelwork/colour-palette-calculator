from colour_palette.colour import Colour

def test_complementary_colour():
    black = Colour(0,0,0)
    white = Colour(255, 255, 255)
    complementary_to_black = black.complementary_colour()
    complementary_to_white = white.complementary_colour()
    assert black == complementary_to_white
    assert white == complementary_to_black

    red = Colour(255,0,0)
    cyan = Colour(0,255,255)
    complementary_to_red = red.complementary_colour()
    assert cyan == complementary_to_red

    green = Colour(0,255,0)
    magenta = Colour(255,0,255)
    complementary_to_green = green.complementary_colour()
    assert magenta == complementary_to_green

    blue = Colour(0,0,255)
    yellow = Colour(255,255,0)
    complementary_to_blue = blue.complementary_colour()
    assert yellow == complementary_to_blue