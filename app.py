import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Thomas Chavez in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab_10_sql_user:HzOhwqZJynf1mEUTvbcPbKLHvnxGm5Gj@dpg-co62cg63e1ms73behhlg-a/lab_10_sql")
    conn.close()
    return "Database Connection Successful"
