from colour_palette.pen_collection import PenCollection
from colour_palette.colour import Colour
from colour_palette.pen import Pen


def test_initialise_pen_collection():
    pen_collection = PenCollection(_get_test_pen_collection())
    assert len(pen_collection.pens) > 10


def test_find_closest_pen_to_colour():
    pen_collection = PenCollection(_get_test_pen_collection())
    test_colour = Colour(255, 255, 0)
    closest_pen = pen_collection.closest_pen_to_colour(test_colour)
    assert closest_pen.name == "Process Yellow - 055"


def test_find_complementary_pen():
    pen_collection = PenCollection(_get_test_pen_collection())
    chinese_red = Pen(856, "Tombow", "Chinese Red - 856", Colour(235, 40, 49))
    complementary_pen = pen_collection.find_complementary_pen(pen=chinese_red)
    turquoise = Pen(443, "Tombow", "Turquoise - 443", Colour(0, 175, 219))
    assert complementary_pen == turquoise

    lamp_black = Pen(25, "Tombow", "Lamp Black - N25", Colour(0, 1, 24))
    peach = Pen(20, "Tombow", "Peach - 020", Colour(248, 243, 185))
    lamp_black_complementary = pen_collection.find_complementary_pen(
        pen=lamp_black)
    assert lamp_black_complementary == peach


def test_find_analogous_pens():
    pen_collection = PenCollection(_get_test_pen_collection())
    peach = Pen(20, "Tombow", "Peach - 020", Colour(248, 243, 185))
    analogous_pens = pen_collection.find_analogous_pens(peach)
    assert len(analogous_pens) == 3


def test_find_split_complementary_pens():
    pen_collection = PenCollection(_get_test_pen_collection())
    scarlet = Pen(933, "Tombow", "Scarlet - 933", Colour(246, 115, 37))
    split_complementary_pens = pen_collection.find_split_complementary_pens(scarlet)
    assert len(split_complementary_pens) == 3


def test_find_pen_by_pen_number():
    pen_collection = PenCollection(_get_test_pen_collection())
    found_pen = pen_collection.find_pen_by_pen_number("062")
    pale_yellow = Pen(62, "Tombow", "Pale Yellow - 062", Colour(254, 245, 108))
    assert found_pen == pale_yellow


def test_get_pen_by_id():
    pen_collection = PenCollection(_get_test_pen_collection())
    found_pen = pen_collection.get_pen_by_id(1)
    peach = Pen(1, "Tombow", "Peach - 020", Colour(248, 243, 185))
    assert found_pen == peach


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
        {"brand": "Tombow", "name": "Asparagus - 192", "rgb": "109,171,154"},
        {"brand": "Tombow", "name": "Light Green - 195", "rgb": "58,180,73"},
        {"brand": "Tombow", "name": "Gray Green - 228", "rgb": "60,105,99"},
        {"brand": "Tombow", "name": "Mint - 243", "rgb": "162,215,195"},
        {"brand": "Tombow", "name": "Sap Green - 245", "rgb": "0,126,67"},
        {"brand": "Tombow", "name": "Hunter Green - 249", "rgb": "13,103,81"},
        {"brand": "Tombow", "name": "Dark Green - 277", "rgb": "1,131,99"},

        {"brand": "Tombow", "name": "Green - 296", "rgb": "0,164,138"},
        {"brand": "Tombow", "name": "Holly Green - 312", "rgb": "98,140,133"},
        {"brand": "Tombow", "name": "Sea Green - 346", "rgb": "0,102,79"},
        {"brand": "Tombow", "name": "Sea Blue - 373", "rgb": "0,171,170"},
        {"brand": "Tombow", "name": "Turquoise - 443", "rgb": "0,175,219"},
        {"brand": "Tombow", "name": "Sky Blue - 451", "rgb": "161,219,236"},
        {"brand": "Tombow", "name": "Process Blue - 452", "rgb": "0,62,98"},
        {"brand": "Tombow", "name": "Cyan - 476", "rgb": "1,124,196"},
        {"brand": "Tombow", "name": "Glacier Blue - 491", "rgb": "155,218,236"},
        {"brand": "Tombow", "name": "Reflex Blue - 493", "rgb": "0,167,210"},
        {"brand": "Tombow", "name": "Light Blue - 515", "rgb": "1,171,232"},
        {"brand": "Tombow", "name": "True Blue - 526", "rgb": "0,62,98"},
        {"brand": "Tombow", "name": "Navy Blue - 528", "rgb": "0,70,129"},
        {"brand": "Tombow", "name": "Peacock Blue - 533", "rgb": "95,176,226"},
        {"brand": "Tombow", "name": "Cobalt Blue - 535", "rgb": "0,100,160"},
        {"brand": "Tombow", "name": "Mist purple - 553", "rgb": "138,190,232"},
        {"brand": "Tombow", "name": "Ultramarine - 555", "rgb": "0,87,167"},
        {"brand": "Tombow", "name": "Deep Blue - 565", "rgb": "6,65,137"},
        {"brand": "Tombow", "name": "Periwinkle - 603", "rgb": "118,133,194"},
        {"brand": "Tombow", "name": "Violet - 606", "rgb": "60,41,134"},
        {"brand": "Tombow", "name": "Lilac - 620", "rgb": "155,166,212"},

        {"brand": "Tombow", "name": "Purple Sage - 623", "rgb": "138,145,199"},
        {"brand": "Tombow", "name": "Imperial Purple - 636", "rgb": "92,57,151"},
        {"brand": "Tombow", "name": "Purple - 665", "rgb": "156,64,152"},
        {"brand": "Tombow", "name": "Orchid - 673", "rgb": "208,162,203"},
        {"brand": "Tombow", "name": "Royal Purple - 676", "rgb": "110,40,139"},
        {"brand": "Tombow", "name": "Dark Plum - 679", "rgb": "79,10,86"},
        {"brand": "Tombow", "name": "Deep Magenta - 685", "rgb": "152,60,150"},
        {"brand": "Tombow", "name": "Pink Rose - 703", "rgb": "236,137,184"},
        {"brand": "Tombow", "name": "Pink - 723", "rgb": "243,154,193"},
        {"brand": "Tombow", "name": "Rhodamine Red - 725", "rgb": "219,69,154"},
        {"brand": "Tombow", "name": "Hot Pink - 743", "rgb": "240,96,156"},
        {"brand": "Tombow", "name": "Rubine Red - 755", "rgb": "273,47,127"},
        {"brand": "Tombow", "name": "Port Red - 757", "rgb": "139,0,86"},
        {"brand": "Tombow", "name": "Carnation - 761", "rgb": "249,190,204"},
        {"brand": "Tombow", "name": "Blush - 772", "rgb": "246,161,181"},
        {"brand": "Tombow", "name": "Baby Pink - 800", "rgb": "249,206,216"},
        {"brand": "Tombow", "name": "Cherry - 815", "rgb": "239,35,83"},
        {"brand": "Tombow", "name": "Persimmon - 835", "rgb": "230,23,63"},
        {"brand": "Tombow", "name": "Wine Red - 837", "rgb": "140,11,66"},
        {"brand": "Tombow", "name": "Carmine - 845", "rgb": "230,67,61"},
        {"brand": "Tombow", "name": "Crimson - 847", "rgb": "163,10,54"},

        {"brand": "Tombow", "name": "Flesh - 850", "rgb": "251,207,195"},
        {"brand": "Tombow", "name": "Chinese Red - 856", "rgb": "235,40,49"},
        {"brand": "Tombow", "name": "Coral - 873", "rgb": "249,170,137"},
        {"brand": "Tombow", "name": "Brown - 879", "rgb": "63,27,21"},
        {"brand": "Tombow", "name": "Warm Red - 885", "rgb": "241,107,50"},
        {"brand": "Tombow", "name": "Redwood - 899", "rgb": "67,20,0"},
        {"brand": "Tombow", "name": "Red - 905", "rgb": "241,107,50"},
        {"brand": "Tombow", "name": "Pale Cherry - 912", "rgb": "248,162,91"},
        {"brand": "Tombow", "name": "Scarlet - 925", "rgb": "246,115,37"},
        {"brand": "Tombow", "name": "Orange - 933", "rgb": "246,141,30"},
        {"brand": "Tombow", "name": "Tan - 942", "rgb": "237,202,179"},
        {"brand": "Tombow", "name": "Gold Ochre - 946", "rgb": "229,126,31"},
        {"brand": "Tombow", "name": "Burnt Sienna - 947", "rgb": "168,77,19"},
        {"brand": "Tombow", "name": "Chocolate - 969", "rgb": "86,38,7"},
        {"brand": "Tombow", "name": "Saddle Brown - 977", "rgb": "147,92,60"},
        {"brand": "Tombow", "name": "Chrome Yellow - 985", "rgb": "253,170,36"},
        {"brand": "Tombow", "name": "Light Sand - 990", "rgb": "238,224,185"},
        {"brand": "Tombow", "name": "Light Ochre - 991", "rgb": "255,225,135"},
        {"brand": "Tombow", "name": "Sand - 992", "rgb": "186,170,118"},
        {"brand": "Tombow", "name": "Chrome Orange - 993", "rgb": "252,180,64"},


        {"brand": "Tombow", "name": "Black - N15", "rgb": "36,31,33"},
        {"brand": "Tombow", "name": "Lamp Black - N25", "rgb": "0,1,24"},
        {"brand": "Tombow", "name": "Cool Gray 10- N45", "rgb": "64,69,80"},
        {"brand": "Tombow", "name": "Cool Gray 7 - N55", "rgb": "104,107,115"},
        {"brand": "Tombow", "name": "Cool Gray 6 - N60", "rgb": "156,178,209"},
        {"brand": "Tombow", "name": "Cool Gray 5 - N65", "rgb": "128,132,140"},
        {"brand": "Tombow", "name": "Warm Gray 2 - N79", "rgb": "123,112,108"},
        {"brand": "Tombow", "name": "Warm Gray 1 - N89", "rgb": "208,224,239"},
    ]
