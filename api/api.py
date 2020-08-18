import flask
from flask import jsonify
import json
from colour_palette.pen_collection import PenCollection
import jsonpickle


app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open(r'C:\code\colour-palette-calculator\colour_palette\data\tombow.json') as json_file:
    print(json_file)
    data = json.load(json_file)
    pens = PenCollection(data)


@app.route('/pens', methods=['GET'])
def pen_collection():
    return pens.toJSON()


@app.route('/pen/<pen_number>/complementary')
def complementary_pen(pen_number):
    pen = pens.find_pen_by_pen_number(pen_number)
    complementary_pen = pens.find_complementary_pen(pen)
    return jsonify(penname=complementary_pen.name, brand=complementary_pen.brand)


# @app.route('/pen/<pen_number>/split-complementary')
# def split_complementary(pen_number):
#     pen = pens.find_pen_by_pen_number(pen_number)
#     return jsonify(pens.find_split_complementary_pens(pen))


app.run()
