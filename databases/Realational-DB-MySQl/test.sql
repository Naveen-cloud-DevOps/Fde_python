show DATABASES;
CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);

SHOW TABLES;
INSERT INTO students (name, age, course)
VALUES
('Naveen', 25, 'Python'),
('Veera', 26, 'DevOps'),
('Rahul', 24, 'AWS'),
('Kumar', 27, 'Cloud Computing');

SELECT * FROM students;