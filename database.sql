CREATE DATABASE human_friends;
USE human_friends;
CREATE TABLE home_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);

CREATE TABLE pack_animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    type VARCHAR(50),
    commands TEXT,
    birth_date DATE
);
