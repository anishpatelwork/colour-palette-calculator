from .pen import Pen
import json


class PenCollection:

    def __init__(self, initialisation_collection):
        self.pens = []
        for p in initialisation_collection:
            self.pens.append(Pen(p["brand"], p["name"], rgb=p["rgb"]))

    def closest_pen_to_colour(self, colour):
        closest_distance = self.pens[0].colour.distance_to_colour(colour)
        closest_pen = self.pens[0]
        for pen in self.pens:
            distance = pen.colour.distance_to_colour(colour)
            if distance < closest_distance:
                closest_distance = distance
                closest_pen = pen
        return closest_pen

    def find_complementary_pen(self, pen=None, colour=None):
        if pen is not None:
            complementary_colour = pen.colour.complementary_colour()
            return self.closest_pen_to_colour(complementary_colour)
        elif colour is not None:
            return self.closest_pen_to_colour(colour)
        else:
            raise ValueError("Must pass in either a colour or pen")

    def find_analogous_pens(self, pen):
        analogous_pens = []
        analogous_colours = pen.colour.analogous_colours()
        for colour in analogous_colours:
            closest_pen = self.closest_pen_to_colour(colour)
            analogous_pens.append(closest_pen)
        return analogous_pens

    def find_split_complementary_pens(self, pen):
        split_complementary_pens = []
        split_complementary_colours = pen.colour.split_complementary()
        for colour in split_complementary_colours:
            closest_pen = self.closest_pen_to_colour(colour)
            split_complementary_pens.append(closest_pen)
        return split_complementary_pens

    def find_pen_by_pen_number(self, pen_number):
        for pen in self.pens:
            if pen_number in pen.name:
                return pen
        raise ValueError("Pen does not exist in collection")

    def toJSON(self):
        return json.dumps(self.pens, default=lambda o: o.__dict__, sort_keys=True,
                          indent=4)
