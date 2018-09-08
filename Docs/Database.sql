CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "User" (
    "UUID" uuid PRIMARY KEY DEFAULT uuid_in((md5(((random())::text || (now())::text)))::cstring)
);

CREATE TABLE "Discord" (
    "UUID" uuid REFERENCES "User"("UUID") NOT NULL,
    discord_id VARCHAR(18) NOT NULL,
    username VARCHAR(30) NOT NULL
);

CREATE TABLE "Points" (
    receipt_id SERIAL PRIMARY KEY,
    "UUID" uuid REFERENCES "User"("UUID") NOT NULL,
    reward_type VARCHAR(5) NOT NULL,
    point INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE "Attendance_box" (
    box_id SERIAL NOT NULL PRIMARY KEY,
    class CHARACTER(1) NOT NULL,
    receipt_id INTEGER REFERENCES "Points"(receipt_id)
);

CREATE TABLE "Attendance" (
    "UUID" uuid REFERENCES "User"("UUID") NOT NULL,
    box_id INTEGER REFERENCES "Attendance_box"(box_id) NOT NULL,
    date DATE NOT NULL DEFAULT now()
);
