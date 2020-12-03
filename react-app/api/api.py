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

@app.route('/login', methods=["POST"])
def basic_login():
	# this is a very basic login check
	# eventually should be replaced with real authentication

	login_data = request.get_json()

	conn = sqlite3.connect("../../data.sqlite")
	c = conn.cursor()

	c.execute(
		"SELECT uid, role FROM Users WHERE username=? AND password=?;",
		(login_data["username"], login_data["password"])
	)
	user = c.fetchone()
	if user != None:
		return {"success": True, "uid": user[0], "role": user[1]}
	else:
		return {"success": False}

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

	# respond back to the client with something here
	return analysis_data

@app.route("/commit", methods=["POST"])
def commit_results():
	# get the request data
	analysis_data = request.get_json()

	# connect to database
	conn = sqlite3.connect("../../data.sqlite")
	c = conn.cursor()

	# get a new ID for the analysis
	c.execute("SELECT max(AID) FROM Analyses;")
	max_aid = c.fetchone()[0]
	if max_aid == None:
		aid = 0
	else:
		aid = max_aid + 1

	# insert into the database
	c.execute(
		"INSERT INTO Analyses "
		"(AID, UID, lossScenario, runDate, "
		"overallRiskInherent, "
		"overallRiskResidual, "
		"primaryRiskInherent, "
		"primaryRiskResidual, "
		"primaryLossEventFrequencyInherent, "
		"primaryLossEventFrequencyResidual, "
		"secondaryRiskInherent, "
		"secondaryRiskResidual, "
		"secondaryLossEventFrequencyInherent, "
		"secondaryLossEventFrequencyResidual, "
		"vulnerabilityInherent, "
		"vulnerabilityResidual, "
		"threatEventFrequencyInherent, "
		"threatEventFrequencyResidual, "
		"potentialLossMagnitude, "
		"resistanceStrengthVulnerabilityInherent, "
		"resistanceStrengthVulnerabilityControls, "
		"resistanceStrengthVulnerabilityResidual, "
		"probabilityOfActionDeterrenceInherent, "
		"probabilityOfActionDeterrenceControls, "
		"probabilityOfActionDeterrenceResidual, "
		"contactFrequencyAvoidanceInherent, "
		"contactFrequencyAvoidanceControls, "
		"contactFrequencyAvoidanceResidual, "
		"threatCapability, "
		"secondaryLossProbability, "
		"primaryLossMagnitudeResponsiveInherent, "
		"primaryLossMagnitudeResponsiveControls, "
		"primaryLossMagnitudeResponsiveResidual, "
		"secondaryLossMagnitudeResponsiveInherent, "
		"secondaryLossMagnitudeResponsiveControls, "
		"secondaryLossMagnitudeResponsiveResidual, "
		"notes) "
		"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
		(
			aid, analysis_data["uid"], "temporary scenario", datetime.datetime.now(),
			analysis_data["overallRiskInherent"],
			analysis_data["overallRiskResidual"],
			analysis_data["primaryRiskInherent"],
			analysis_data["primaryRiskResidual"],
			analysis_data["primaryLossEventFrequencyInherent"],
			analysis_data["primaryLossEventFrequencyResidual"],
			analysis_data["secondaryRiskInherent"],
			analysis_data["secondaryRiskResidual"],
			analysis_data["secondaryLossEventFrequencyInherent"],
			analysis_data["secondaryLossEventFrequencyResidual"],
			analysis_data["vulnerabilityInherent"],
			analysis_data["vulnerabilityResidual"],
			analysis_data["threatEventFrequencyInherent"],
			analysis_data["threatEventFrequencyResidual"],
			# analysis_data["potentialLossMagnitude"],
			None,
			analysis_data["resistanceStrengthVulnerabilityInherent"],
			analysis_data["resistanceStrengthVulnerabilityControls"],
			analysis_data["resistanceStrengthVulnerabilityResidual"],
			analysis_data["probabilityOfActionDeterrenceInherent"],
			analysis_data["probabilityOfActionDeterrenceControls"],
			analysis_data["probabilityOfActionDeterrenceResidual"],
			analysis_data["contactFrequencyAvoidanceInherent"],
			analysis_data["contactFrequencyAvoidanceControls"],
			analysis_data["contactFrequencyAvoidanceResidual"],
			analysis_data["threatCapability"],
			analysis_data["secondaryLossProbability"],
			analysis_data["primaryLossMagnitudeResponsiveInherent"],
			analysis_data["primaryLossMagnitudeResponsiveControls"],
			analysis_data["primaryLossMagnitudeResponsiveResidual"],
			analysis_data["secondaryLossMagnitudeResponsiveInherent"],
			analysis_data["secondaryLossMagnitudeResponsiveControls"],
			analysis_data["secondaryLossMagnitudeResponsiveResidual"],
			"temporary notes"
		)
	)
	conn.commit()

	return {"success": True}