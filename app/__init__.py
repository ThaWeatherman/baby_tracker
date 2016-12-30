from flask import Flask
from flask import g
import pymongo


app = Flask(__name__)
app.config.from_object('config')


def get_db():
    # TODO: try except
    conn = getattr(g, '_connection', None)
    if conn is None:
        conn = g._connection = pymongo.MongoClient(app.config['MONGO_URL'])
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = g._connection[app.config['MONGO_NAME']]
    return db


@app.teardown_appcontext
def close_connection(e):
    conn = getattr(g, '_connection', None)
    if conn is not None:
        conn.close()

from app import views
from app import api
