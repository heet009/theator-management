from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


movies = []

def load_movies():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies"))
    column_names = result.keys()

    for row in result.all():
      movies.append(dict(zip(column_names,row)))
    return movies


@app.route("/")
def home_page():
  movies = load_movies()
  return render_template('login.html', movie=movies)


@app.route("/home")
def movies_manage():
  movies = load_movies()
  return render_template('home.html', movie=movies)


@app.route("/api/movies")
def list_movies():
  return jsonify(movies)


@app.route("/login")
def events_manage():
  return render_template('login.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
