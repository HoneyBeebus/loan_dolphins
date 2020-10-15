CREATE TABLE Classes (
    class CHAR(15) PRIMARY KEY,
    type CHAR(2) NOT NULL,
    country CHAR(15),
    numGuns INTEGER,
    bore INTEGER,
    displacement INTEGER
);

INSERT INTO Classes VALUES("Bismarck", "bb", "Germany", 8, 15, 42000);