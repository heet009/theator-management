from flask import Flask, render_template, jsonify

app = Flask(__name__)

movies = [
  {
    'id':1,'title':'xyz','img':'static/header.jpg','link':'moviepic.html'
  },
  {
    'id':2,'title':'abc','img':'static/eg.jpg','link':'moviepic.html'
  },
  {
    'id':3,'title':'pqr','img':'static/header.jpg','link':'moviepic.html'
  }
]

@app.route("/")
def theator_manage():
  return render_template('home.html',movie=movies)

@app.route("/api/movies")
def list_movies():
  return jsonify(movies)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

