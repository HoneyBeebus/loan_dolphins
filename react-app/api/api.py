import datetime
import sqlite3
import runAnalysis
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

	# run the FAIR analysis
	analysis_data = runAnalysis.FAIR(analysis_data)
	
	# # and commit to database?
	# conn = sqlite3.connect("../../data.sqlite")
	# c = conn.cursor()

	# # get a new ID for the analysis
	# c.execute("SELECT max(AID) FROM Analyses;")
	# max_aid = c.fetchone()[0]
	# if max_aid == None:
	# 	aid = 0
	# else:
	# 	aid = max_aid + 1
	
	# c.execute(
	# 	"INSERT INTO Analyses "
	# 	"(AID, UID, lossScenario, runDate, overallResidualRisk, potentialLossMagnitude, "
	# 	"resistanceStrengthVulnerabilityInherent, resistanceStrengthVulnerabilityControls, "
	# 	"probabilityOfActionDeterrenceInherent, probabilityOfActionDeterrenceControls, "
	# 	"contactFrequencyAvoidanceInherent, contactFrequencyAvoidanceControls, "
	# 	"threatCapability, secondaryLossProbability, "
	# 	"primaryLossMagnitudeResponsiveInherent, primaryLossMagnitudeResponsiveControls, "
	# 	"secondaryLossMagnitudeResponsiveInherent, secondaryLossMagnitudeResponsiveControls, "
	# 	"notes) "
	# 	"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
	# 	(
	# 		aid, 1, "temporary scenario", datetime.datetime.now(), 'VL', 1,
	# 		analysis_data["resistanceStrengthVulnerabilityInherent"],
	# 		analysis_data["resistanceStrengthVulnerabilityControls"],
	# 		analysis_data["probabilityOfActionDeterrenceInherent"],
	# 		analysis_data["probabilityOfActionDeterrenceControls"],
	# 		analysis_data["contactFrequencyAvoidanceInherent"],
	# 		analysis_data["contactFrequencyAvoidanceControls"],
	# 		analysis_data["threatCapability"],
	# 		analysis_data["secondaryLossProbability"],
	# 		analysis_data["primaryLossMagnitudeResponsiveInherent"],
	# 		analysis_data["primaryLossMagnitudeResponsiveControls"],
	# 		analysis_data["secondaryLossMagnitudeResponsiveInherent"],
	# 		analysis_data["secondaryLossMagnitudeResponsiveControls"],
	# 		"temporary notes"
	# 	)
	# )
	# conn.commit()


	# respond back to the client with something here
	return analysis_data