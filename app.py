from flask import request, Flask, jsonify, Response

import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='cruduser user='Andrew' host='localhost'")
cursor = conn.cursor()

@app.route("/user/add", methods=["POST"])
def add_user():
  form = request.form
  first_name = form.get('first_name')
  if first_name == '':
    return jsonify('first name is a required field'), 400
  last_name = form.get('last_name')
  if last_name == '':
    return jsonify('last name is a required field'), 400
  email = form.get('email')
  if email == '':
    return jsonify('email is a required field'), 400
  password = form.get('password')
  if password == '':
    return jsonify('password is a required field'), 400
  city = form.get('city')
  state = form.get('state')
  active = form.get('active')

  cursor.execute("INSERT INTO users (first_name, last_name, email, password, city, state, active) Values (%s, %s, %s, %s, %s, %s, %s", (first_name, last_name, email, password, state, city, active))
  conn.commit()

  return jsonify("user added successfully"), 200

@app.route("/user/edit/<user_id>", methods=["POST"])
def edit_user(user_id):
  form = request.form
  first_name = form.get('first_name')
  if first_name == '':
    return jsonify('first name is a required field'), 400
  last_name = form.get('last_name')
  if last_name == '':
    return jsonify('last name is a required field'), 400
  email = form.get('email')
  if email == '':
    return jsonify('email is a required field'), 400
  password = form.get('password')
  if password == '':
    return jsonify('password is a required field'), 400
  city = form.get('city')
  state = form.get('state')
  active = form.get('active')

  cursor.execute("UPDATE ")
  return

@app.route("/user/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
  return

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
  cursor.execute("SELECT first_name, last_name, email, password, city, state, active FROM users Where (user_id == %s)", [f'{user_id}'])
  results = cursor.fetchone()

  result_dictionary = {
    "first_name": results[0],
    "last_name": results[1],
    "email": results[2],
    "password": results[3],
    "state": results[4],
    "city": results[5],
    "active": results[6],
  }
  return jsonify(result_dictionary), 200

@app.route("/user/list", methods=["GET"])
def get_all():
  cursor.execute("SELECT id, name, mascot, city, state, championshipsWon FROM nflteams")
   results = cursor.fetchall()
   list_of_teams = []
   
   for team in results:
      list_of_teams.append( {
         'id' : team[0],
         'name' : team[1],
         'mascot' : team[2],
         'city' : team[3],
         'state' : team[4],
         'championshipsWon' : team[5]
      } )

   output_dictionary = {
      "teams" : list_of_teams
   }
   return jsonify(output_dictionary), 200
  return

if __name__ == "__main__":
  app.run()





# CREATE TABLE IF NOT EXISTS Users (
#    user_id serial PRIMARY KEY,
#    first_name VARCHAR NOT NULL,
#    last_name VARCHAR,
#    email VARCHAR NOT NULL,
#    password VARCHAR NOT NULL,
#    city VARCHAR,
#    state VARCHAR,
#    active BOOLEAN DEFAULT true
# );