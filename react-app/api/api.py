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
	# connect to database
	conn = sqlite3.connect("../../data.sqlite")
	# change the output format to a dictionary
	conn.row_factory = dict_factory
	# get the cursor for queries
	c = conn.cursor()

	c.execute("SELECT * FROM Analyses;")
	analyses = c.fetchall()
	return {"analyses": analyses}