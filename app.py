from flask import Flask, render_template, jsonify,request
from database import load_movies, load_movies_id

app = Flask(__name__)


@app.route("/")
def home_page():
  movies = load_movies()
  return render_template('login.html',movie=movies)
  

@app.route("/logindata",methods=['post'])
def login_page():
  data = request.form
  return jsonify(data)
  

#@app.route("/login")
#def events_manage():
#  return render_template('login.html')


@app.route("/home",methods=['post'])
def movies_manage():
  data = request.form
  movies = load_movies()
  return render_template('home.html', movie=movies,login=data)


@app.route("/api/movies")
def list_movies():
  movies = load_movies()
  return jsonify(movies)


@app.route("/moviepic/<id>")
def show_mov(id):
  mov = load_movies_id(id)
  
  return render_template('moviepic.html', mov=mov)


@app.route("/booking")
def book():
  return render_template('booking.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
