CREATE DATABASE vehicle_service_db;
USE vehicle_service_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin','admin123');

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(200)
);

CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_no VARCHAR(20),
    model VARCHAR(50)
);

CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT,
    service_charge FLOAT,
    parts_cost FLOAT,
    total_amount FLOAT
);