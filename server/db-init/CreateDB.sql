drop database if exists university;
create database university;

\c university;

CREATE TABLE university_details
(
    id SERIAL,
    alpha_two_code VARCHAR(255),
    country VARCHAR(255),
    domain VARCHAR(50),
    university_name VARCHAR(255),
    web_page VARCHAR(255),
    university_description VARCHAR(255),
    university_image VARCHAR(255),
    PRIMARY KEY(id)

);
