-- Task 7
-- MySQL script to create a database of cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY (id),
       state_id INT NOT NULL FOREIGN KEY (id),
       name VARCHAR(256) NOT NULL
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id)
);
