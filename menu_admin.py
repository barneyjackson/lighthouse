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
  "id": "b3db002c",
  "description": "",
  "children": [
    {
      "id": "0d832351",
      "description": "Food",
      "children": [
        {
          "id": "8c1cb0b3",
          "description": "Merchants Accepting Food Vouchers",
          "children": [
            {
              "id": "19a90842",
              "description": 'This is the answer for Merchants Accepting Food Vouchers!',
              "children": []
            }
          ]
        },
        {
          "id": "ac6cc8df",
          "description": "Food Voucher Eligibility and Process",
          "children": [
            {
              "id": "601c1784",
              "description": 'This is the answer for Food Voucher Eligibility and Process!',
              "children": []
            }
          ]
        },
        {
          "id": "16f22006",
          "description": "Employment in Food Industry",
          "children": [
            {
              "id": "bb1743c5",
              "description": 'This is the answer for Employment in Food Industry!',
              "children": []
            }
          ]
        }
      ]
    },
    {
      "id": "3434d327",
      "description": "Shelter",
      "children": [
        {
          "id": "1f853337",
          "description": 'This is the answer for Shelter!',
          "children": []
        }
      ]
    },
    {
      "id": "417a9367",
      "description": "Transportation",
      "children": [
        {
          "id": "1967b7d4",
          "description": 'This is the answer for Transportation!',
          "children": []
        }
      ]
    },
    {
      "id": "27322478",
      "description": "Border",
      "children": [
        {
          "id": "68f2b6b4",
          "description": 'This is the answer for Border!',
          "children": []
        }
      ]
    },
    {
      "id": "ccb1e1ce",
      "description": "Registration & Legal Documents",
      "children": [
        {
          "id": "36fe07f2",
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
    return json.dumps(menu.content)
  elif request.method == "PUT":
    # todo(parth): validation
    menu = Menu(request.json)
    valid, errors = menu.validate()
    if valid:
        print 'VALID'
	db['1'] = menu
	resp = {"success": ":D"}
    else:
        print 'INVALID'
	resp = {"error": errors}
    return json.dumps(resp)

@app.route('/', methods=["GET"])
def serve_index():
  valid, errors = Menu(initial_script).validate()
  db = shelve.get_shelve()
  if valid:
      #db['1'] = Menu(initial_script)
      return send_from_directory('.', 'index.html')
  else:
    raise Exception("test data not valid")


if __name__ == '__main__':
  app.run(debug=True)
