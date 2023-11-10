from flask import Flask, render_template, jsonify,request
from data import data

app = Flask(__name__)
@app.route("/")
def hello():
    return jsonify({"data":data,"success":"success"})
@app.route("/star_details")
def pde():
    name = request.args.get('name')
    star_data = next(item for item in data if item["star_names"] == name)
    return jsonify({"data":star_data,"success":"success"})

app.run(debug = True)