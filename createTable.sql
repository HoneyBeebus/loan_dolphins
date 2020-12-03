CREATE TABLE Analyses (
    AID INTEGER PRIMARY KEY,
    UID INTEGER,
	lossScenario VARCHAR(15),
	runDate DATE,

	overallRiskInherent INTEGER,
	overallRiskResidual INTEGER,
	primaryRiskInherent INTEGER,
	primaryRiskResidual INTEGER,
	primaryLossEventFrequencyInherent INTEGER,
	primaryLossEventFrequencyResidual INTEGER,
	secondaryRiskInherent INTEGER,
	secondaryRiskResidual INTEGER,
	secondaryLossEventFrequencyInherent INTEGER,
	secondaryLossEventFrequencyResidual INTEGER,
	vulnerabilityInherent INTEGER,
	vulnerabilityResidual INTEGER,
	threatEventFrequencyInherent INTEGER,
	threatEventFrequencyResidual INTEGER,

	potentialLossMagnitude INTEGER,
	resistanceStrengthVulnerabilityInherent INTEGER,
	resistanceStrengthVulnerabilityControls INTEGER,
	resistanceStrengthVulnerabilityResidual INTEGER,
	probabilityOfActionDeterrenceInherent INTEGER,
	probabilityOfActionDeterrenceControls INTEGER,
	probabilityOfActionDeterrenceResidual INTEGER,
	contactFrequencyAvoidanceInherent INTEGER,
	contactFrequencyAvoidanceControls INTEGER,
	contactFrequencyAvoidanceResidual INTEGER,
	threatCapability INTEGER,
	secondaryLossProbability INTEGER,
	primaryLossMagnitudeResponsiveInherent INTEGER,
	primaryLossMagnitudeResponsiveControls INTEGER,
	primaryLossMagnitudeResponsiveResidual INTEGER,
	secondaryLossMagnitudeResponsiveInherent INTEGER,
	secondaryLossMagnitudeResponsiveControls INTEGER,
	secondaryLossMagnitudeResponsiveResidual INTEGER,

	notes VARCHAR(1000)
);

CREATE TABLE Users (
	UID INTEGER PRIMARY KEY,
	username VARCHAR(20),
	password VARCHAR(20),
	role CHAR(1)
);