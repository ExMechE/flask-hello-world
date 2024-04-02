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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab_10_sql_user:HzOhwqZJynf1mEUTvbcPbKLHvnxGm5Gj@dpg-co62cg63e1ms73behhlg-a/lab_10_sql")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
