from .pen import Pen


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
