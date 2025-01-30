-- schema.sql

-- Table for students
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    student_name TEXT,
    house_id INTEGER,
    head_id INTEGER,
    FOREIGN KEY (house_id) REFERENCES houses(id),
    FOREIGN KEY (head_id) REFERENCES heads(id)
);

-- Table for houses
CREATE TABLE houses (
    id INTEGER PRIMARY KEY,
    house_name TEXT
);

-- Table for heads
CREATE TABLE heads (
    head_id INTEGER PRIMARY KEY,
    head_name TEXT
);

-- Table for house assignments
CREATE TABLE house_assignments (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (house_id) REFERENCES houses(id),
    PRIMARY KEY (student_id, house_id)
);
