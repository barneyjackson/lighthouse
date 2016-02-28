from flask import Flask
from flask import request, send_from_directory
from flask import render_template
from flask.ext import shelve
from menu import Menu

import json
import ast

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)


@app.route('/menu', methods=["GET", "PUT"])
def hello_world():
  db = shelve.get_shelve()

  if request.method == "GET":
    menu = db['1']
    print menu.content
    return json.dumps(menu.content)
  elif request.method == "PUT":
    # todo(parth): validation
    print type(request.data)
    print type(request.json)
    db['1'] = Menu(request.json)
    return "success"

@app.route('/', methods=["GET"])
def serve_index():
    '''
    db = shelve.get_shelve()
    db['1'] = Menu({
        "description": "Some Meta Text",
        "children": [
            {"description": "Get info about food.", "children": [{"description": "More Food Info"}]},
            {"description": "Get info about housing.", "children": []},
            {"description": "What's the name of this camp.", "answer": "Zaatari"}
        ]
    })
    '''
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
  app.run(debug=True)
