import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/testflask')
def test_flask():
	return {"hello": "there"}


def dict_factory(cursor, row):
	d = {}
	for i, col in enumerate(cursor.description):
		d[col[0]] = row[i]
	return d

@app.route('/analyses')
def get_analyses():
	conn = sqlite3.connect("../../data.sqlite")
	conn.row_factory = dict_factory
	c = conn.cursor()


	c.execute("SELECT * FROM Analyses;")
	analyses = c.fetchall()

	return {"analyses": analyses}