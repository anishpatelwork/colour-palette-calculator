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
    print(f'Chosen Pen {pen}')
    choice = int(input("Enter Find Complementary Pen (1), Find Analogous Pens (2), Find Split Complementary Pens(3)"))
    if choice == 1:
        complementary_pen = pens.find_complementary_pen(pen)
        print(f'Chosen pen {pen}, Complementary Pen {complementary_pen}')
    elif choice == 2:
        analogous_pens = pens.find_analogous_pens(pen)
        for analogous_pen in analogous_pens:
            print(f'Chosen pen {pen}, Analogous Pen {analogous_pen}')
    elif choice == 3:
        split_complementary_pens = pens.find_split_complementary_pens(pen)
        for split_complementary_pen in split_complementary_pens:
            print(f'Chosen pen {pen}, Split complementary Pen {split_complementary_pen}')