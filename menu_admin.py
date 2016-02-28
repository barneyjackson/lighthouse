from flask import Flask
from flask import request, send_from_directory
from flask import render_template
from menu import Menu

import json

app = Flask(__name__)

menu = Menu({
    "description": "Some Meta Text",
    "children": [
        {"description": "Get info about food.", "children": [{"description": "More Food Info"}]},
        {"description": "Get info about housing.", "children": []},
        {"description": "What's the name of this camp.", "answer": "Zaatari"}
    ]
})

@app.route('/menu', methods=["GET", "PUT"])
def hello_world():

  if request.method == "GET":
    #return render_template('menu_admin.html', menu=menu.content)
    return json.dumps(menu.content)
  elif request.method == "PUT":
    global menu
    # todo(parth): validation
    menu = Menu(request.data)
    return "success"

@app.route('/', methods=["GET"])
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
  app.run(debug=True)
