from colour_palette.pen_collection import PenCollection
from colour_palette.colour import Colour


def test_initialise_pen_collection():
    pen_collection = PenCollection(_get_test_pen_collection())
    assert len(pen_collection.pens) > 10


def test_find_closest_pen_to_colour():
    pen_collection = PenCollection(_get_test_pen_collection())
    test_colour = Colour(255, 255, 0)
    closest_pen = pen_collection.closest_pen_to_colour(test_colour)
    assert closest_pen.name == "Process Yellow - 055"

    raksha_test = Colour(255, 0, 0)
    closest_raksha = pen_collection.closest_pen_to_colour(raksha_test)
    print(closest_raksha)


def _get_test_pen_collection():
    return [
        {"brand": "Tombow", "name": "Peach - 020", "rgb": "248,243,185"},
        {"brand": "Tombow", "name": "Light Orange - 025", "rgb": "253,201,56"},
        {"brand": "Tombow", "name": "Yellow Gold - 026", "rgb": "198,150,24"},
        {"brand": "Tombow", "name": "Dark Ochre - 027", "rgb": "93,75,13"},
        {"brand": "Tombow", "name": "Process Yellow - 055", "rgb": "255,242,23"},
        {"brand": "Tombow", "name": "Pale Yellow - 062", "rgb": "254,245,108"},
        {"brand": "Tombow", "name": "Green Ochre - 076", "rgb": "157,148,19"},
        {"brand": "Tombow", "name": "Baby Yellow - 090", "rgb": "255,245,137"},
        {"brand": "Tombow", "name": "Avocado - 098", "rgb": "125,122,15"},
        {"brand": "Tombow", "name": "Light Olive - 126", "rgb": "170,183,52"},
        {"brand": "Tombow", "name": "Chartreuse - 133", "rgb": "194,217,65"},
        {"brand": "Tombow", "name": "Dark Olive - 158", "rgb": "103,150,80"},
        {"brand": "Tombow", "name": "Willow Green - 173", "rgb": "149,201,74"},
        {"brand": "Tombow", "name": "Dark Jade - 177", "rgb": "69,96,38"},
    ]
