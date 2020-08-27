import flask
from flask import jsonify
from flask import request
import json
from colour_palette.pen_collection import PenCollection
from pathlib import Path


app = flask.Flask(__name__)
app.config["DEBUG"] = True

path = Path(__file__).parent / "../colour_palette/data/tombow.json"
with path.open() as json_file:
    print(json_file)
    data = json.load(json_file)
    pens = PenCollection(data)


@app.route('/pens', methods=['GET'])
def pen_collection():
    pen_number = request.args.get('number')
    if pen_number is not None:
        pen = pens.find_pen_by_pen_number(pen_number)
        return jsonify(pen.serialize())
    return jsonify([{p: pens.pens[p].serialize()} for p in pens.pens])


@app.route('/pens/<id>/complementary')
def complementary_pen(id):
    pen = pens.pens[int(id)]
    complementary_pen = pens.find_complementary_pen(pen)
    return jsonify(complementary_pen.serialize())


@app.route('/pens/<id>')
def pen_details(id):
    pen = pens.pens[int(id)]
    return jsonify(pen.serialize())


@app.route('/pens/<id>/split-complementary')
def split_complementary(id):
    pen = pens.pens[int(id)]
    return jsonify([p.serialize() for p in pens.find_split_complementary_pens(pen)])


@app.route('/pens/<id>/analogous')
def analogous_pens(id):
    pen = pens.pens[int(id)]
    analogous = pens.find_analogous_pens(pen)
    return jsonify([p.serialize() for p in analogous])


app.run(host='0.0.0.0')
