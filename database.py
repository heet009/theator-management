from sqlalchemy import create_engine
from sqlalchemy import text

con_str = "mysql+pymysql://root:heet@0.tcp.in.ngrok.io:10584/assignment"
engine = create_engine(con_str)


def load_movies():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies"))
    column_names = result.keys()
    movies = []

    for row in result.all():
      movies.append(dict(zip(column_names, row)))
    return movies


def load_seats():
  with engine.connect() as conn:
    result = conn.execute(text("select * from theater"))
    column_names = result.keys()
    seats = []

    for row in result.all():
      seats.append(dict(zip(column_names, row)))
    return seats


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


def show_time(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from shows where movie_id = :val"),
                          {'val': id})
    column_names = result.keys()
    show = []

    for row in result.all():
      show.append(dict(zip(column_names, row)))
    return show


def seat_select(check, thea):
  with engine.connect() as conn:
    for ch in check:
      if thea == 't1':
        query = text("UPDATE theater SET t1 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't2':
        query = text("UPDATE theater SET t2 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't3':
        query = text("UPDATE theater SET t3 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't4':
        query = text("UPDATE theater SET t4 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't5':
        query = text("UPDATE theater SET t5 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't6':
        query = text("UPDATE theater SET t6 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})
      if thea == 't7':
        query = text("UPDATE theater SET t7 = 'disabled' WHERE seat = :c1")
        conn.execute(query, {"c1": ch})

      conn.commit()


      #conn.close()
def get_showid(mov_id, room_t, time):
  with engine.connect() as conn:
    result = conn.execute(
      text(
        "select show_id from shows where movie_id = :val1 AND room = :val2 AND timing = :val3"
      ), {
        'val1': mov_id,
        'val2': room_t,
        'val3': time
      })

    #show = []
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      col = result.keys()
      return dict(zip(col, rows[0]))


def add_login_db(name, email, id1, seat_book, sea):
  with engine.connect() as conn:
    conn.execute(
      text(
        "insert into customer (name1,email,show_id,Seats_Booked,seats) values(:name,:email,:sh_id,:seats_book,:seat)"
      ), {
        'name': name,
        'email': email,
        'sh_id': id1,
        'seats_book': seat_book,
        'seat': sea
      })
    conn.commit()
    conn.close()
