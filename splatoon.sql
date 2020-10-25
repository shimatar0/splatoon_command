CREATE DATABASE IF NOT EXISTS splatoon;

CREATE TABLE splatoon.weapon (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    category VARCHAR(50),
    full_name VARCHAR(50),
    short_name VARCHAR(50),
    sub_weapon VARCHAR(50),
    special VARCHAR(50),
    main_performance_up VARCHAR(50)
);