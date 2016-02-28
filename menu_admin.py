from flask import Flask
from flask import request, send_from_directory
from flask import render_template
from flask.ext import shelve
from menu import Menu

import json

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

initial_script = {
  "description": "",
  "children": [
    {
      "description": "0 - Food",
      "children": [
        {
          "description": "0 - Merchants Accepting Food Vouchers",
          "children": [
            {
              "description": 'This is the answer for Merchants Accepting Food Vouchers!',
              "children": []
            }
          ]
        },
        {
          "description": "1 - Food Voucher Eligibility and Process",
          "children": [
            {
              "description": 'This is the answer for Food Voucher Eligibility and Process!',
              "children": []
            }
          ]
        },
        {
          "description": "2 - Employment in Food Industry",
          "children": [
            {
              "description": 'This is the answer for Employment in Food Industry!',
              "children": []
            }
          ]
        }
      ]
    },
    {
      "description": "1 - Shelter",
      "children": [
        {
          "description": 'This is the answer for Shelter!',
          "children": []
        }
      ]
    },
    {
      "description": "2 - Transportation",
      "children": [
        {
          "description": 'This is the answer for Transportation!',
          "children": []
        }
      ]
    },
    {
      "description": "3 - Border",
      "children": [
        {
          "description": 'This is the answer for Border!',
          "children": []
        }
      ]
    },
    {
      "description": "4 - Registration & Legal Documents",
      "children": [
        {
          "description": 'These are the Registration & Legal Documents!',
          "children": []
        }
      ]
    }
  ]
}

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
  db = shelve.get_shelve()
  #db['1'] = Menu(initial_script)
  return send_from_directory('.', 'index.html')

if __name__ == '__main__':
  app.run(debug=True)
