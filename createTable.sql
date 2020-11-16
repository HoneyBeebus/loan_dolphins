CREATE TABLE Analyses (
    AID INTEGER PRIMARY KEY,
    UID INTEGER,
	lossScenario VARCHAR(15),
	runDate DATE,
	overallResidualRisk CHAR(2),
	potentialLossMagnitude INTEGER,
	resistanceStrengthVulnerabilityInherent INTEGER,
	resistanceStrengthVulnerabilityControls INTEGER,
	probabilityOfActionDeterrenceInherent INTEGER,
	probabilityOfActionDeterrenceControls INTEGER,
	contactFrequencyAvoidanceInherent INTEGER,
	contactFrequencyAvoidanceControls INTEGER,
	threatCapability INTEGER,
	secondaryLossProbability INTEGER,
	primaryLossMagnitudeResponsiveInherent INTEGER,
	primaryLossMagnitudeResponsiveControls INTEGER,
	secondaryLossMagnitudeResponsiveInherent INTEGER,
	secondaryLossMagnitudeResponsiveControls INTEGER,
	notes VARCHAR(1000)
);

CREATE TABLE Users (
	UID INTEGER PRIMARY KEY,
	username VARCHAR(20),
	password VARCHAR(20),
	role CHAR(1)
);