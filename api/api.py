import flask
from flask import jsonify
from flask import request
import json
from colour_palette.pen_collection import PenCollection


app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open(r'C:\code\colour-palette-calculator\colour_palette\data\tombow.json') as json_file:
    print(json_file)
    data = json.load(json_file)
    pens = PenCollection(data)


@app.route('/pens', methods=['GET'])
def pen_collection():
    pen_number = request.args.get('number')
    if pen_number is not None:
        pen = pens.find_pen_by_pen_number(pen_number)
        return jsonify(pen.serialize())
    return jsonify([p.serialize() for p in pens.pens])


@app.route('/pens/<id>/complementary')
def complementary_pen(id):    
    pen = pens.get_pen_by_id(int(id))
    complementary_pen = pens.find_complementary_pen(pen)
    return jsonify(complementary_pen.serialize())


@app.route('/pens/<id>')
def pen_details(id):
    pen = pens.get_pen_by_id(int(id))
    return jsonify(pen.serialize())


@app.route('/pens/<id>/split-complementary')
def split_complementary(id):
    pen = pens.get_pen_by_id(int(id))
    return jsonify([p.serialize() for p in pens.find_split_complementary_pens(pen)])


@app.route('/pens/<id>/analogous')
def analogous_pens(id):
    pen = pens.get_pen_by_id(int(id))
    analogous = pens.find_analogous_pens(pen)
    return jsonify([p.serialize() for p in analogous])


app.run()
