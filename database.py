from sqlalchemy import create_engine
from sqlalchemy import text

con_str = "mysql+pymysql://root:heet@0.tcp.in.ngrok.io:17171/assignment"
engine = create_engine(con_str)

with engine.connect() as conn:
  result = conn.execute(text("select * from movies"))
  print(result.all())
