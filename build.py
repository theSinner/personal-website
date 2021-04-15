from jinja2 import Environment, FileSystemLoader
import json
from utils import normalize_data
import shutil
import os

with open('data.json') as json_file:
    data = normalize_data(json.load(json_file))

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')
result = template.render(data=data)

with open("dist/index.html", "w") as fh:
    fh.write(result)

try:
    os.rmdir('./dist/static')
except OSError:
    pass


shutil.copytree('./static', './dist/static')
