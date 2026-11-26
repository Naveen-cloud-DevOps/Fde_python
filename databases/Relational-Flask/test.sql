
-- =========================================
-- CREATE DATABASE
-- =========================================

CREATE DATABASE IF NOT EXISTS dev;

-- Select database
USE dev;

-- =========================================
-- CREATE USERS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    age INT,
    city VARCHAR(100)
);

-- =========================================
-- INSERT SAMPLE DATA
-- =========================================

INSERT IGNORE INTO users (name, email, age, city)
VALUES
('Naveen', 'naveen@gmail.com', 33, 'Hyderabad'),
('Rahul', 'rahul@gmail.com', 28, 'Bangalore'),
('Kiran', 'kiran@gmail.com', 30, 'Vizianagaram'),
('Suresh', 'suresh@gmail.com', 26, 'Chennai'),
('Vamsi', 'vamsi@gmail.com', 29, 'Vijayawada'),
('Ramesh', 'ramesh@gmail.com', 32, 'Hyderabad'),
('Prasad', 'prasad@gmail.com', 27, 'Bangalore'),
('Arun', 'arun@gmail.com', 31, 'Chennai'),
('Mahesh', 'mahesh@gmail.com', 25, 'Vizag'),
('Sai', 'sai@gmail.com', 24, 'Hyderabad');

-- =========================================
-- VERIFY DATA
-- =========================================

SELECT * FROM users;

SELECT COUNT(*) AS total_users FROM users;
