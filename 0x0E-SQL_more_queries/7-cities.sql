-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- swtich to the database
USE hbtn_0d_usa;
--create table
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INT NOT NULL,
    name NOT NULL VARCHAR(256),
    PRIMARY KEY(id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
