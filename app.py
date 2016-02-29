from flask import Flask, request, redirect, send_from_directory, render_template
from flask.ext import shelve
import twilio.twiml
from menu import Menu
import json

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

users = {}
script = {
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

@app.route("/", methods=['GET', 'POST'])
def twilio_route():
  db = shelve.get_shelve()
  from_number = request.values.get('From', None)[1:]
  from_message = request.values.get('Body', None)

  if(from_number in users):
    try:
      int(from_message)
    except:
      resp = twilio.twiml.Response()
      resp.message("You must enter a valid option or 0 to start again!")
      return str(resp)
    else:
      if int(from_message) == 0:
        del users[from_number]
        compressed_path = ""
        users[from_number] = compressed_path
      else:
        compressed_path = users[from_number]
        path_message = int(from_message) - 1
        compressed_path = str(compressed_path) + str(path_message)
        users[from_number] = compressed_path
  else:
    compressed_path = ""
    users[from_number] = compressed_path

  uncompressed_path = list(compressed_path)

  menu = db['1'].content
  node = menu["children"]
  for index in uncompressed_path:
    node = node[int(index)]["children"]

  if len(node) == 1 and not node[0]['children']:
    message = node[0]['description']
    del users[from_number]
  else:
    message = "Please select an option.\n"
    for index, child in enumerate(node):
      message = message + str(index + 1) + " - " + child["description"] + "\n"
    message = message + '\n0 - Start Again'

  resp = twilio.twiml.Response()
  resp.message(message)

  return str(resp)

@app.route('/menu', methods=["GET", "PUT"])
def menu_route():
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

@app.route('/admin', methods=["GET"])
def admin_route():
  db = shelve.get_shelve()
  return send_from_directory('.', 'index.html')

@app.route('/init', methods=["GET"])
def init_route():
  db = shelve.get_shelve()
  db['1'] = Menu(script)
  return "success"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)