"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaam63hp8u791gv5q10-a.oregon-postgres.render.com",
        database="todo_rb5a",
        user="root",
        password="A8T9t6bMLt3chdUJhWsz9Hw01GhnopYY")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
