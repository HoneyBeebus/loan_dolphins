#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/testflask')
def test_flask():
	return {"hello": "there"}