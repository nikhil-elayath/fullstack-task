drop database if exists university;
create database university;

\c university;

CREATE TABLE university_details
(
    id SERIAL,
    alpha_two_code VARCHAR(500),
    country VARCHAR(500),
    domain VARCHAR(50),
    university_name VARCHAR(500),
    web_page VARCHAR(500),
    university_description VARCHAR(500),
    university_image VARCHAR(500),
    PRIMARY KEY(id)

);
