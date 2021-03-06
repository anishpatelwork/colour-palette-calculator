from colour_palette.colour import Colour


def test_complementary_colour():
    black = Colour(0, 0, 0)
    white = Colour(255, 255, 255)
    complementary_to_black = black.complementary_colour()
    complementary_to_white = white.complementary_colour()
    assert black == complementary_to_white
    assert white == complementary_to_black

    red = Colour(255, 0, 0)
    cyan = Colour(0, 255, 255)
    complementary_to_red = red.complementary_colour()
    assert cyan == complementary_to_red

    green = Colour(0, 255, 0)
    magenta = Colour(255, 0, 255)
    complementary_to_green = green.complementary_colour()
    assert magenta == complementary_to_green

    blue = Colour(0, 0, 255)
    yellow = Colour(255, 255, 0)
    complementary_to_blue = blue.complementary_colour()
    assert yellow == complementary_to_blue


def test_triadic_colours():
    red = Colour(255, 0, 0)
    blue = Colour(0, 0, 255)
    green = Colour(0, 255, 0)
    red_triadic_colours = red.triadic_colours()
    assert red in red_triadic_colours
    assert blue in red_triadic_colours
    assert green in red_triadic_colours
    test_colour = Colour(49, 206, 143)
    test_colour_triadic_colours = test_colour.triadic_colours()
    expected_result_1 = Colour(206, 143, 49)
    expected_result_2 = Colour(143, 49, 206)
    assert test_colour in test_colour_triadic_colours
    assert expected_result_1 in test_colour_triadic_colours
    assert expected_result_2 in test_colour_triadic_colours


def test_analogous_colours():
    test_colour = Colour(33, 66, 222)
    expected_result_1 = Colour(94, 33, 222)
    # Ever so slightly different to some other calculators out there
    # assuming that this is using a differnt number of degrees of rotation
    expected_result_2 = Colour(33, 160, 222)
    analogous_colours = test_colour.analogous_colours()
    assert test_colour in analogous_colours
    assert expected_result_1 in analogous_colours
    assert expected_result_2 in analogous_colours


def test_split_complementary_colours():
    test_colour = Colour(0, 0, 255)
    expected_result_1 = Colour(255, 128, 0)
    expected_result_2 = Colour(128, 255, 0)
    test_split_complementary_colours = test_colour.split_complementary()
    assert len(test_split_complementary_colours) == 3
    assert test_colour in test_split_complementary_colours
    assert expected_result_1 in test_split_complementary_colours
    assert expected_result_2 in test_split_complementary_colours


def test_rgb_to_hex():
    black = Colour(0, 0, 0)
    assert black.hex() == '#000000'
    white = Colour(255, 255, 255)
    assert white.hex().lower() == '#FFFFFF'.lower()
    red = Colour(255, 0, 0)
    assert red.hex().lower() == '#FF0000'.lower()
    blue = Colour(0, 255, 0)
    assert blue.hex().lower() == '#00FF00'.lower()
    green = Colour(0, 0, 255)
    assert green.hex().lower() == '#0000FF'.lower()
    silver = Colour(192, 192, 192)
    assert silver.hex().lower() == '#C0C0C0'.lower()
