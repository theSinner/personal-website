from jinja2 import Environment, FileSystemLoader
import json
from utils import normalize_data
import shutil

with open('data.json') as json_file:
    data = normalize_data(json.load(json_file))

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')
result = template.render(data=data)

with open("dist/index.html", "w") as fh:
    fh.write(result)

shutil.copytree('./static', './dist/static')
