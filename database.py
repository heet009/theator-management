from sqlalchemy import create_engine
from sqlalchemy import text

con_str = "mysql+pymysql://root:heet@0.tcp.in.ngrok.io:17248/assignment"
engine = create_engine(con_str)


def load_movies():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies"))
    column_names = result.keys()
    movies = []

    for row in result.all():
      movies.append(dict(zip(column_names, row)))
    return movies


def load_movies_id(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies where id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      col = result.keys()
      return dict(zip(col, rows[0]))
