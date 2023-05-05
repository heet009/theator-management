from flask import Flask, render_template, jsonify, request
from database import load_movies, load_movies_id, add_login_db, load_seats, show_time, seat_select, get_showid
import json

app = Flask(__name__)


@app.route("/")
def home_page():
  movies = load_movies()
  print(movies)
  return render_template('login.html', mov=movies)


@app.route("/logindata", methods=['post'])
def login_page():
  data = request.form
  return jsonify(data)


#@app.route("/login")
#def events_manage():
#  return render_template('login.html')
email = ""
name = ""
id1 = 0  #movie_id
theator = ""  #room
time_m = ""  #timing
seats = ""  #all seats
show_id = 0  #show id
no_s = 0  #no of seats
total = 0


@app.route("/home", methods=['post'])
def movies_manage():
  data = request.form
  global email
  email = request.form['Email']
  global name
  name = request.form['Name']
  movies = load_movies()
  return render_template('home.html', movie=movies, login=data)


@app.route("/moviepic/<id>")
def show_mov(id):
  mov = load_movies_id(id)
  show = show_time(id)
  global id1
  id1 = id

  print(show)
  print(mov)
  return render_template('moviepic.html', mov=mov, sh=show)


@app.route("/booking/<th>/<time>")
def book(th, time):
  seats = load_seats()
  global theator
  theator = th
  global time_m
  time_m = time
  mov = load_movies_id(id1)
  return render_template('booking.html', seat=seats, thea=th, t=time, mov=mov)


@app.route("/final")
def fi():
  checkedIDs = request.args.get('checkedIDs')
  checkedIDs = json.loads(checkedIDs)
  global time_m
  print(time_m)
  global id1
  print(id1)
  global theator
  print(theator)
  show = get_showid(id1, theator, time_m)
  global show_id
  sho_id = [int(value) for value in show.values()]
  show_id = sho_id[0]
  print(sho_id[0])
  global seats
  seats = ','.join(checkedIDs)
  global no_s
  for c in checkedIDs:
    no_s = no_s + 1
  print(no_s)
  global total
  total = no_s * 35
  seat_select(checkedIDs, theator)
  mov = load_movies_id(id1)
  add_login_db(name, email, show_id, no_s, seats)
  return render_template('final.html',
                         seatbook=checkedIDs,
                         name=name,
                         email=email,
                         mov=mov,
                         theator=theator,
                         time_m=time_m,
                         seats=seats,
                         no_s=no_s,
                         total=total)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
