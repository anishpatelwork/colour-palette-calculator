from colour_palette.pen_collection import PenCollection
import json


if __name__ == "__main__":
    with open(r'C:\code\colour-palette-calculator\colour_palette\data\tombow.json') as json_file:
        data = json.load(json_file)
        pens = PenCollection(data)
        # for pen in pens.pens:
        #     print(pen)
    print('Enter your chosen pen number')
    pen_number = input()
    print(f'Looking for {pen_number}')
    pen = pens.find_pen_by_pen_number(pen_number)
    complementary_pen = pens.find_complementary_pen(pen)
    print(f'Chosen pen {pen}, Complementary Pen {complementary_pen}')