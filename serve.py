from flask import Flask, render_template
import json
from utils import normalize_data

app = Flask(__name__)


@app.route("/")
def index():
    with open('data.json') as json_file:
        data = normalize_data(json.load(json_file))
        return render_template("./index.html", data=data)

app.run(debug=True, port=4000)