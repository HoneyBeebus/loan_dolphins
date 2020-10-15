CREATE TABLE Analyses (
    UID INTEGER PRIMARY KEY,
	client VARCHAR(15),
	run_Date DATE,
	risk_Inherent CHAR(2),
	risk_Residual CHAR(2),
	notes VARCHAR(280)
);

CREATE TABLE Users (
	UID INTEGER PRIMARY KEY,
	username VARCHAR(20),
	role CHAR(1)
);