CREATE TABLE "Users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    "name" TEXT,
    "email" TEXT
);

SELECT * FROM Users;

INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');
INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');

SELECT * FROM Users;

DELETE FROM Users WHERE email='ted@umich.edu';

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu';

SELECT * FROM Users WHERE email='csev@umich.edu';

SELECT * FROM Users ORDER BY email DESC;

SELECT * FROM Users ORDER BY name DESC;



