import sqlite3
from flask import Flask
from flask import request

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

@app.route('/runAnalysis',methods=["POST"])
def run_analysis():
	# get the data sent by the request
	analysis_data = request.get_json()

	# access properties like so
	test_prop = analysis_data["contactFrequencyAvoidanceInherent"]
	print(f"Testing reading from analysis data: {test_prop}")
	
	# List of properties is:
	# contactFrequencyAvoidanceInherent
	# contactFrequencyAvoidanceControls
	# probabilityOfActionDeterrenceInherent
	# probabilityOfActionDeterrenceControls
	# threatCapability
	# resistanceStrengthVulnerabilityInherent
	# resistanceStrengthVulnerabilityControls
	# primaryLossMagnitudeInherent
	# primaryLossMagnitudeControls
	# secondaryLossMagnitudeInherent
	# secondaryLossMagnitudeControls
	# secondaryLossProbabilty

	# analysis logic can be called here.
	
	# and commit to database?

	# respond back to the client with something here
	return {}